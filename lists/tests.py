from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()

        response = home_page(request)

        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
    def test_home_page_contains_input_box(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertIn(b'<input', response.content)
        self.assertIn(b'name="item_text"', response.content)
    def test_can_save_a_POST_request(self):
         request = HttpRequest()
         request.method = 'POST'
         request.POST['item_text'] = 'A new list item'

         response = home_page(request)

         self.assertEqual(response.status_code, 302)
         self.assertEqual(response['location'], '/')