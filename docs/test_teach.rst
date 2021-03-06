.. _test_teach-reference-label:

Test Teach
==========

In this lesson, we apply logging to our own application.

--------
Our Code
--------

This is a simple application to use as an example for class.
It takes command-line input and returns an appropriate response.

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

        test_input = None
        test_response = None

        def run(self):

            self.test_input = self.get_test_input()
            self.test_response = self.get_test_response()
            self.return_test_response()

        def get_test_input(self):

            try:
                test_input = sys.argv[1]
            except IndexError:
                print USAGE
                sys.exit(1)
            else:
                return test_input

        def get_test_response(self):

            if self.test_input.lower() in responses.keys():
                return responses[self.test_input.lower()]
            else:
                return None

        def return_test_response(self):

            print self.test_response if self.test_response else NO_RESPONSE


    def main():

        test_teach = TestTeach()
        test_teach.run()

    if __name__ == '__main__':
        main()


If we run this code without passing any parameters, we get the USAGE message.

.. code-block:: bash

    $ python test_teach_1.py
    Usage: test_teach.py test_input

If we run this code with a bad parameter, we get the NO_RESPONSE message.

.. code-block:: bash

    $ python test_teach_1.py blah
    We could not find a response for your input. Please try again.

Finally, if we run this code with a good parameter, we get the response back.

.. code-block:: bash

    $ python test_teach_1.py first
    last

Note that anything extra on the line is ignored.

.. code-block:: bash

    $ python test_teach_1.py first second third
    last


----------------
Add Some Logging
----------------

We'll add two INFO level log statements to our application, telling us when it starts running and when it finishes.

First, we import the *logging* module, and use *baseConfig()* to set the logging level to *logging.INFO*.

Then, in *main()*, we add our two statements using *logging.info()*.

.. code-block:: python
   :emphasize-lines: 2,3,14,17

    import sys
    import logging
    logging.basicConfig(level=logging.INFO)

    USAGE = "Usage: test_teach.py test_input"
    NO_RESPONSE = "We could not find a response for your input. Please try again."


    ...


    def main():

        logging.info("Begin")
        test_teach = TestTeach()
        test_teach.run()
        logging.info("End")

    if __name__ == '__main__':
        main()

Now, the output of our application includes the log statements.

.. code-block:: bash

    $ python test_teach/test_teach_2.py first
    INFO:root:Begin
    last
    INFO:root:End

Question
--------

What happens if we don't pass any input now?

-----------------
Logging To A File
-----------------

When logging to the console, the output from your application can get lost in all the log messages.
Logging allows you to send those messages to a file using the *filename* parameter to the *basicConfig()* method.

If we change our basicConfig() call to include *filename*,

.. code-block:: python
   :emphasize-lines: 3

    import sys
    import logging
    logging.basicConfig(filename='test_teach.log', level=logging.INFO)

then the output of our application no longer contains the log messages,

.. code-block:: bash

    $ python test_teach/test_teach_3.py first
    last

but they are contained in the log file.

.. code-block:: bash

    $ cat test_teach.log
    INFO:root:Begin
    INFO:root:End


---------
Problem 2
---------

Add log statements displaying the input and the response, and move logging to a file.

.. code-block:: bash

    $ python test_teach/test_teach_4.py first
    last

.. code-block:: bash

    $ cat test_teach.log
    INFO:root:Begin
    INFO:root:input is first
    INFO:root:response is last
    INFO:root:End


