Title: There be divils here
Date: 2004-03-11 11:28
Author: markmc
Category: General
Slug: there-be-divils-here
Status: published

I reckon a lot of hackers don't realise how wary they need to  
be when using enums. Problems occur frequently because people  
(usually unwittingly) make assumptions about either the size,  
alignment or signedness of the integer representation for the  
enum which the compiler uses.

C99 says *Each enumerated type shall be compatible with  
an integer type. The choice of type is implementation-defined.  
An implementation may delay the choice of which integer type  
until all enumeration constants have been seen*. What  
this means is that once the compiler has seen all the constants  
you have defined for that enum, it will then decide what integer  
representation to use and that could be a signed or unsigned  
integer of any size.

So, GNOME hackers beware. *gconf\_enum\_to\_string()* is  
**nasty**. Have a look at the prototype:

    gboolean  gconf_string_to_enum (GConfEnumStringPair  lookup_table[],
                                    const gchar         *str,
                                    gint                *enum_value_retloc);
      

</p>
Bugs I've seen include:

    {
      enum { A, B } test_enum;

      gconf_enum_to_string (enum_to_str_table, str, (int *) &test_enum);
    }
      

This is guaranteed to cause crashes on some architectures since  
alignment of the *enum* is different from the expected  
alignment of an *int*. So it should be:

    {
      enum { A, B } test_enum;
      int test_int;

      if (gconf_enum_to_string (enum_to_str_table, str, &test_int))
        {
          test_enum = test_int;
        }
    }
      

Also, this breaks:

    {

      enum { A, B } test_enum;

      int test_int;
    test_enum = -1;

      gconf_enum_to_string (enum_to_str_table, str, &test_int);

      test_enum = test_int;
    if (test_enum

    The problem here is that you're assuming the enum has a signed

    representation when in fact the compiler may choose an unsigned

    representation. If the conversion fails, if (test_enum

    will not detect it.

    Alex also points out that when adding values to an enum in an API

    you need to be careful that you're not unwittingly changing the

    ABI because the compiler chooses to use a large integer representation

    for the enum than was previously used.
