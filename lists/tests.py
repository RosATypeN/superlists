from django.test import TestCase
from lists.models import List, Item

class HomePageTest(TestCase):

    def test_home_page_contains_input_box(self):
        response = self.client.get('/')
        self.assertContains(response, '<title>To-Do Lists</title>')
        self.assertContains(response, '<input')
        self.assertContains(response, 'name="item_text"')

class NewListTest(TestCase):

    def test_can_save_a_POST_request_and_redirect(self):
        # POST 到 /lists/new
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})

        self.assertEqual(List.objects.count(), 1)
        self.assertEqual(Item.objects.count(), 1)

        new_list_obj = List.objects.first()
        new_item = Item.objects.first()

        self.assertEqual(new_item.text, 'A new list item')
        self.assertEqual(new_item.list, new_list_obj)
        self.assertRedirects(response, f'/lists/{new_list_obj.id}/')

class ListViewTest(TestCase):

    def test_display_only_items_for_that_list(self):
        correct_list = List.objects.create()
        Item.objects.create(text='itemey 1', list=correct_list)
        Item.objects.create(text='itemey 2', list=correct_list)

        other_list = List.objects.create()
        Item.objects.create(text='other item 1', list=other_list)
        Item.objects.create(text='other item 2', list=other_list)

        response = self.client.get(f'/lists/{correct_list.id}/')
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
        self.assertNotContains(response, 'other item 1')
        self.assertNotContains(response, 'other item 2')

    def test_can_save_a_POST_request_to_existing_list(self):
        correct_list = List.objects.create()
        other_list = List.objects.create()

        response = self.client.post(
            f'/lists/{correct_list.id}/',
            data={'item_text': 'A new item for existing list'}
        )

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new item for existing list')
        self.assertEqual(new_item.list, correct_list)
        self.assertRedirects(response, f'/lists/{correct_list.id}/')