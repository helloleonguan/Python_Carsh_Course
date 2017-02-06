class AnonymousSurvey():
    """Collect anonymous answers to a survey question."""
    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in responses:
            print('- ' + response)


# Testing
import unittest

# Test for a Class

class TestAnonmyousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""
    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)

unittest.main()

# The unittest.TestCase class has a setUp() method that allows you to 
# create these objects once and then use them in each of your test methods.
# Python runs the setUp() method before running
# each method starting with test_. Any objects created in the setUp() method
# are then available in each test method you write.

# def setUp(self):
#     """
#     Create a survey and a set of responses for use in all test methods.
#     """
#     question = "What language did you first learn to speak?"
#     self.my_survey = AnonymousSurvey(question)
#     self.responses = ['English', 'Spanish', 'Mandarin']
# ----- use self.<> to access attribute

# . = success, F = Assertion fail, E = error
# If a test case takes a long time to run because it contains many unit tests, you can
# watch these results to get a sense of how many tests are passing.