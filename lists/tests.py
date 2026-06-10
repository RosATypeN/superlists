from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
from lists.models import Item
from django.test import TestCase, Client

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

        home_page(request)

        self.assertEqual(Item.objects.count(), 1)

        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')
    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        request = HttpRequest()

        response = home_page(request)

        self.assertIn(b'itemey 1', response.content)
        self.assertIn(b'itemey 2', response.content)
    def test_can_save_a_POST_request_and_retrieve_it_later(self):
        client = Client()

        client.post('/', data={'item_text': 'A new list item'})

        response = client.get('/')

        self.assertContains(response, 'A new list item')
    def test_redirects_after_POST(self):
        response = self.client.post(
            '/',
            data={'item_text': 'A new list item'}
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')