from django.test import TestCase
from django.contrib.auth.models import User
from .models import BugTracker


class BugTrackerTestCase(TestCase):

    def setUp(self):
        """ Method setups the the Bug Tracker Object for testing """

        # Create test user for the bug object
        test_user = User.objects.create_user(
            username="kevin", email="kevin@gmail.com", password="password")
        # Create an instance of the bug for demo
        BugTracker.objects.create(bug_title="demo", project_name="demo",
                                  date_occured="2022-01-01", date="2022-01-01",
                                  bug_description="demo", bug_risk="Low",
                                  user=test_user)

    def test_bug_creation(self):
        """ Method tests that the bug object was created and saved to the database """

        # Call the bug object
        demo = BugTracker.objects.get(bug_title="demo")

        # Assert that it is a created object
        self.assertIsInstance(demo, BugTracker)
