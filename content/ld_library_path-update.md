Title: $LD_LIBRARY_PATH Update
Date: 2004-04-07 07:05
Author: markmc
Category: General
Slug: ld_library_path-update
Status: published

Of course, Ulrich did know. The [  
System V ABI specification's ELF
section](http://www.caldera.com/developers/gabi/latest/ch5.dynamic.html#shobj_dependencies)
contains the requirement  
that *\$LD\_LIBRARY\_PATH* have those semantics

       a string that holds a list of directories, separated by colons
       (:). For example, the string /home/dir/lib:/home/dir2/lib: tells the
       dynamic linker to search first the directory /home/dir/lib, then
       /home/dir2/lib, and then the current directory to find dependencies.
      

</p>
Moral of the story. Don't do

      export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/some/other/dir
      

Do this instead

      if [ -n $LD_LIBRARY_PATH ]; then
        export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/some/other/dir
      else
        export LD_LIBRARY_PATH=/some/other/dir
      fi
      

Or even

      export LD_LIBRARY_PATH=${LD_LIBRARY_PATH:+$LD_LIBRARY_PATH:}/some/other/dir
      

</p>

