import sys
import logging
logger = logging.getLogger("test_teach")
logger.setLevel(logging.INFO)

# create a console handler with level ERROR
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# add the console handler to our logger
logger.addHandler(ch)

# create a file handler with level INFO
fh = logging.FileHandler('test_teach.log')
fh.setLevel(logging.INFO)
# create a formatter to use with our file handler
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# tell our file handler to use the formatter
fh.setFormatter(formatter)
# add the file handler to our logger
logger.addHandler(fh)

USAGE = "Usage: %s test_input" % sys.argv[0]
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
            logger.error('No Input')
            print USAGE
            sys.exit(1)
        else:
            return test_input

    def get_test_response(self):

        if self.test_input.lower() in responses.keys():
            logger.info("input is %s and response is %s" % (
                self.test_input, self.test_response))
            return responses[self.test_input.lower()]
        else:
            logger.warning("no response: input is %s" % self.test_input)
            return None

    def return_test_response(self):

        print self.test_response if self.test_response else NO_RESPONSE


def main():

    test_teach = TestTeach()
    test_teach.run()

if __name__ == '__main__':
    main()
