from django.test import TestCase
from .models import Bug
from django.urls import reverse

class BugModelTestCase(TestCase):
    def setUp(self):
        self.bug = Bug.objects.create(
            description="Test Bug",
            bug_type="error",
            report_date="2023-01-01 12:00:00",
            status="to do"
        )

    def test_bug_description(self):
        """Test that bug description is properly stored."""
        self.assertEqual(self.bug.description, "Test Bug")

    def test_bug_type_choices(self):
        """Test that bug type is one of the valid choices."""
        bug = Bug(description="A valid bug type", bug_type="error", status="to do")
        self.assertEqual(self.bug.bug_type, "error")
        bug.save()

    def test_bug_status_choices(self):
        """Test that bug status is one of the valid choices."""
        bug = Bug(description="A valid bug Status", bug_type="error", status="to do")
        self.assertEqual(self.bug.status, "to do")
        bug.save()

    def test_bug_default_status(self):
        """Test that the default status is set to 'to do' if not provided."""
        bug = Bug(description="Bug with no status", bug_type="new feature")
        self.assertEqual(bug.status, "to do")


class BugViewTests(TestCase):
    def test_bug_submission_post(self):
        # Data for bug submission
        bug_data = {
            'description': 'This is a test bug',
            'bug_type': 'Feature Request',
            'report_date': '2023-10-17',
            'status': 'New',
        }

        # Submit a POST request to bug_submission view
        response = self.client.post(reverse('list_bugs'), bug_data)
        print("thee response", response)

        # Check if the bug was created
        self.assertEqual(response.status_code, 200) 

    def test_bug_submission_get(self):
        # Submit a GET request to bug_submission view
        response = self.client.get(reverse('list_bugs'))

        # Check if the response status code is 200 and the form is in the context
        self.assertEqual(response.status_code, 200)
        self.assertIn('bugs', response.context)

    def test_bug_list(self):
        # Create a test bug
        Bug.objects.create(
            description='Test Bug 1',
            bug_type='Bug',
            report_date='2023-10-16',
            status='New',
        )

        # Access the bug_list view
        response = self.client.get(reverse('list_bugs'))

        # Check if the response status code is 200 and the bug is in the context
        self.assertEqual(response.status_code, 200)
        self.assertIn('bugs', response.context)
        self.assertEqual(len(response.context['bugs']), 1)  # Only one bug created

    def test_bug_details(self):
        # Create a test bug
        test_bug = Bug.objects.create(
            description='Test Bug 2',
            bug_type='Bug',
            report_date='2023-10-17',
            status='New',
        )

        # Access the bug_details view for the created bug
        response = self.client.get(reverse('detail_view', args=[test_bug.pk]))

        # Check if the response status code is 200 and the bug is in the context
        self.assertEqual(response.status_code, 200)
        self.assertIn('bug', response.context)
        self.assertEqual(response.context['bug'], test_bug)

