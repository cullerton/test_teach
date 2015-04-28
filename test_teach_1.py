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
