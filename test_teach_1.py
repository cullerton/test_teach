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
