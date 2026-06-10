from django.test import TestCase
from lists.models import List, Item

class NewListTest(TestCase):

    def test_can_save_a_POST_request_and_redirect(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertEqual(List.objects.count(), 1)
        new_list = List.objects.first()
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')
        self.assertEqual(new_item.list, new_list)
        self.assertRedirects(response, f'/lists/{new_list.id}/')