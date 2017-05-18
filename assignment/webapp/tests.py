from django.test import TestCase
from webapp import views
# Create your tests here.

"""To test the webapp which displays the Hello World."""
class HelloWorldTestCase(TestCase):
    def test_request_status_hello_world(self):
        request = 'fake request'
        response = views.index(request)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Hello World.",status_code=200)
