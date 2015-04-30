.. _logging-reference-label:

Logging
=======

In this lesson, we introduce the mechanics of logging and write some simple log statements.

--------------
Simple Example
--------------

In this code, we import the logging facility, and add two logging statements.

.. code-block:: python

    import logging

    logging.info('Simple info log statement.')
    logging.warning('Simple warning log statement.')

The logging facility has methods for each of the logging levels.
Here, our first statement uses logging level **Info** and the second uses level **Warning**.

If we save this code to a file and run it, we get this output.

.. code-block:: bash

    $ python logging_example_1.py
    WARNING:root:Simple warning log statement.

We do **not** see the INFO log statement because Python defaults to only displaying statements of levels WARNING, ERROR and CRITICAL.

We can change the default behavior and set the logging level to INFO with the *basicConfig* method.

.. code-block:: python
   :emphasize-lines: 2

    import logging
    logging.basicConfig(level=logging.INFO)

    logging.info('Simple info log statement.')
    logging.warning('Simple warning log statement.')

Now we can see both statements.

.. code-block:: bash

    $ python logging_example_2.py
    INFO:root:Simple info log statement.
    WARNING:root:Simple warning log statement.

Notice that each of our log statements also display their logging level and the word *root*.

Root tells us that we are using the root logger. We'll discover what that means when we learn how to customize our log messages in :ref:`more-logging-reference-label`.

---------
Questions
---------

- How would you display messages of all levels?

- How would you **only** display messages of levels ERROR and CRITICAL?

- How would you only display messages of levels WARNING and CRITICAL?

---------
Problem 1
---------

Write code that produces the following output:

.. code-block:: bash

    $ python logging_example_3.py
    WARNING:root:Simple warning log statement.
    CRITICAL:root:Simple critical log statement.


