Title: Error Handling
Date: 2011-02-15 13:19
Author: markmc
Category: General
Slug: error-handling
Status: published

I came across a fairly typical error handling mistake today and thought
I'd share it.

The code was something like this:

    class Factory {
        static Foo getFoo() {
            try {
                // load a .properties file, read a key from it
                ...
                return new Foo(propValue);
            } catch (Exception ex) {
                log.error("Failed to find key in properties file: " + ex.toString());
                return null;
            }
        }
    }

and the caller did e.g.

        Factory.getFoo().doSomething();

The thing to note here is that the caller is assuming that `getFoo()`
method never returns `null`.

That's probably a good assumption on the part of the caller. The factory
method should always succeed unless there is a programmer error (e.g.
the key does not exist in the `.properties` file) or a system error
(e.g. an I/O error accessing the file). Neither of which the caller
should be expected to handle gracefully. That's what exceptions are for!

In the event of an error, we'd get a `NullPointerException` from the
caller site and an error printed to the logfile. If, for example, you
are running this code in a debugger, you'll be looking at a
`NullPointerException` with no clue as to what caused the exception.

The moral of the story here is to think clearly about when errors should
be handled gracefully and when you should just let exceptions be passed
back up the stack.

In the end, I added a new exception type:

    class FactoryException extends RuntimeException {
        
        private static final String ERROR_MSG = "Failed to lookup key {0} in file {1}";

        private String propsFile;
        private String propsKey;

        FactoryException(String propsFile, String key, Throwable cause) {
            super(MessageFormat.format(ERROR_MSG, propsFile, key), cause);
            this.propsFile = propsFile;
            this.propsKey = propsKey;
        }

        String getPropsFile() {
            return propsFile;
        }

        String getPropsKey() {
            return propsKey;
        }
    }

and then re-factored the original code:

    class Factory {
        static Foo getFoo() {
            try {
                // load a .properties file, read a key from it
                ...
                return new Foo(propValue);
            } catch (Exception ex) {
                throw new FactoryException(propsFile, propsKey, ex);
            }
        }
    }

so now if there is an error, rather than getting a fairly useless
`NullPointerException` you get:

    FactoryException: Failed to lookup key foo in file bar.properties
        ...
    Caused by: java.io.FileNotFoundException: ...
