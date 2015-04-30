.. _more-logging-reference-label:

More Logging
============

In this lesson, we learn how to customize logging by taking advantage of its modular design.

------------------
Logging Components
------------------

The Python logging facility separates its functionality into **four components**;
loggers, handlers, formatters and filters.

**Loggers** are instantiated from the *logging.getLogger()* method and are how we access logging functionality.

**Handlers** allow us to send log messages to different outputs.

**Formatters** allow us to format the output of our log messages.

**Filters** allow filtering beyond logging levels. We will not cover filters in this lesson.

-------
Example
-------

In this example we:

- instantiate a **logger** object,
- add two **handlers** to the logger--one which uses a **formatter**, and
- use the logger to write some simple **log statements**.

.. code-block:: python

    import logging

    # create our logger with level DEBUG
    logger = logging.getLogger('logging_example')
    logger.setLevel(logging.DEBUG)

    # create a console handler with level Info
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # add the console handler to our logger
    logger.addHandler(ch)


    # create a file handler with level Debug
    fh = logging.FileHandler('logging_example.log')
    fh.setLevel(logging.DEBUG)
    # create a formatter to use with our file handler
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # tell our file handler to use the formatter
    fh.setFormatter(formatter)
    # add the file handler to our logger
    logger.addHandler(fh)

    # some simple log statements
    logger.debug('Simple debug log statement.')
    logger.info('Simple info log statement.')
    logger.warning('Simple warning log statement.')
    logger.error('Simple error log statement.')
    logger.critical('Simple critical log statement.')


If we save this code to a file and run it, we get this output.

.. code-block:: bash

    $ python logging_example_4.py
    Simple info log statement.
    Simple warning log statement.
    Simple error log statement.
    Simple critical log statement.

But, we've also written to the file *logging_example.log*, where we see the DEBUG level message too.

.. code-block:: bash

    $ cat logging_example.log
    2015-04-28 11:43:41,254 - logging_example - DEBUG - Simple debug log statement.
    2015-04-28 11:43:41,254 - logging_example - INFO - Simple info log statement.
    2015-04-28 11:43:41,254 - logging_example - WARNING - Simple warning log statement.
    2015-04-28 11:43:41,255 - logging_example - ERROR - Simple error log statement.
    2015-04-28 11:43:41,255 - logging_example - CRITICAL - Simple critical log statement.

Notice the formatting from our formatter.


---------
Problem 3
---------

Add a logger of level INFO to TestTeach that:

- has a console handler of level ERROR,
- has a file handler of level INFO with a custom formatter,

and

- writes a log statement of level ERROR if there is no input,
- writes a log statement of level WARNING with the input if there is input but no response, and
- writes a log statement of level INFO with the input and response if there is both input and a response

Bunus Points
------------

Use a different formatter then the example.

Extra Credit
------------

- add a log statement of level CRITICAl when the response is 'Zoey', and
- add an SMTPHandler to your logger that sends you an email when there is a CRITICAL message


----
Help
----

At `docs.python.org <https://docs.python.org>`__ you can find more information about

- `handlers <https://docs.python.org/2/library/logging.handlers.html#module-logging.handlers>`__, and the
- `attributes available to logging.Formatter <https://docs.python.org/2/library/logging.html#logrecord-attributes>`__.

There is also a

- `logging reference <https://docs.python.org/2/library/logging.html>`__, and
-  `logging HOWTO <https://docs.python.org/2/howto/logging.html>`__.

