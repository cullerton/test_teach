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

We do **not** get both log statements because Python defauls to level Warning.

We can set the logging level with the *basicConfig* method.

.. code-block:: python
   :emphasize-lines: 2

    import logging
    logging.basicConfig(level=logging.INFO)

    logging.info('Simple info log statement.')
    logging.warning('Simple warning log statement.')

Then we can see both statements.

.. code-block:: bash

    $ python logging_example_2.py
    INFO:root:Simple info log statement.
    WARNING:root:Simple warning log statement.

---------
Problem 1
---------

Question 1
----------

How would you display messages of all levels?

Question 2
----------

How would you **only** display messages of levels Error and Critical?

Question 3
----------

How would you only display messages of levels Warning and Critical?

Problem
-------

Write code that produces the following output:

.. code-block:: bash

    $ python logging_example_3.py
    INFO:root:Simple info log statement.
    WARNING:root:Simple warning log statement.
    ERROR:root:Simple error log statement.
    CRITICAL:root:Simple critical log statement.


----------
Test Teach
----------

This is a simple application to use as an example for class.
It takes command-line input and returns an appropriate response.

Our Code
--------

.. code-block:: python

    import sys

    USAGE = "Usage: test_teach.py test_input"
    NO_RESPONSE = "We could not find a response for your input. Please try again."
    responses = {'one': 'two',
                 'abc': '123',
                 'blue': 'green',
                 'first': 'last',
                 'yes': 'no',
                 'dog': 'Zoey'}


    class TestTeach():

        def run(self):

            test_input = self.get_test_input()
            test_response = self.get_test_response(test_input)
            self.return_test_response(test_response)

        def get_test_input(self):

            # if they don't give us input, give them the USAGE message
            if not len(sys.argv) > 1:
                print USAGE
                sys.exit(1)

            return sys.argv[1]

        def get_test_response(self, test_input):

            test_response = responses[test_input.lower()] \
                if test_input.lower() in responses.keys() else None
            return test_response

        def return_test_response(self, test_response):

            if test_response:
                print test_response
            else:
                print NO_RESPONSE


    def main():

        test_teach = TestTeach()
        test_teach.run()

    if __name__ == '__main__':
        main()


If we run this code without passing any parameters, we get the USAGE message.

.. code-block:: bash

    $ python test_teach/test_teach_1.py
    Usage: test_teach.py test_input

If we run this code with a bad parameter, we get the NO_RESPONSE message.

.. code-block:: bash

    $ python test_teach/test_teach_1.py blah
    We could not find a response for your input. Please try again.

Finally, if we run this code with a good parameter, we get the response back.

.. code-block:: bash

    $ python test_teach/test_teach_1.py first
    last

Note that anything extra on the line is ignored.

.. code-block:: bash

    $ python test_teach/test_teach_1.py first second third
    last


Adding logging
--------------

First, we'll add logging that tells us when our application begins and ends running.

.. code-block:: python
   :emphasize-lines: 2,3,41,44

    import sys
    import logging
    logging.basicConfig(level=logging.INFO)

    USAGE = "Usage: test_teach.py test_input"
    NO_RESPONSE = "We could not find a response for your input. Please try again."


    class TestTeach():

        def run(self):

            test_input = self.get_test_input()
            test_response = self.get_test_response(test_input)
            self.return_test_response(test_response)

        def get_test_input(self):

            if not len(sys.argv) > 1:
                print USAGE
                sys.exit(1)

            return sys.argv[1]

        def get_test_response(self, test_input):

            test_response = responses[test_input.lower()] \
                if test_input.lower() in responses.keys() else None
            return test_response

        def return_test_response(self, test_response):

            if test_response:
                print test_response
            else:
                print NO_RESPONSE


    def main():

        logging.info("Begin")
        test_teach = TestTeach()
        test_teach.run()
        logging.info("End")

    if __name__ == '__main__':
        main()

Now, the output includes these log statements.

.. code-block:: bash

    $ python test_teach/test_teach_2.py first
    INFO:root:Begin
    last
    INFO:root:End

---------
Problem 2
---------

Add code to include log statements that contain the input and the response.

.. code-block:: bash

    $ python test_teach/test_teach_3.py first
    INFO:root:Begin
    INFO:root:input is first
    INFO:root:response is last
    last
    INFO:root:End
