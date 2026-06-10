from django.test import TestCase
from lists.models import List, Item

class NewListTest(TestCase):

    def test_can_save_a_POST_request_and_redirect(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        # 验证新建 List
        self.assertEqual(List.objects.count(), 1)
        new_list = List.objects.first()
        # 验证新建 Item
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')
        self.assertEqual(new_item.list, new_list)
        # 验证重定向到列表页面
        self.assertRedirects(response, f'/lists/{new_list.id}/')

    def test_cannot_save_empty_list_items(self):
        list_ = List.objects.create()
        self.client.post(
            f'/lists/{list_.id}/',
            data={'item_text': ''}  # 空文本
        )
        # 验证空文本不会被保存
        self.assertEqual(Item.objects.filter(list=list_).count(), 0)

    def test_multiple_lists_have_separate_urls(self):
        self.client.post('/', data={'item_text': 'Buy peacock feathers'})
        first_list = List.objects.first()

        self.client.post('/', data={'item_text': 'Buy milk'})
        second_list = List.objects.last()

        self.assertNotEqual(first_list.id, second_list.id)

    def test_items_are_saved_to_correct_list(self):
        first_list = List.objects.create()
        second_list = List.objects.create()

        Item.objects.create(text='Item 1', list=first_list)
        Item.objects.create(text='Item 2', list=second_list)

        self.assertEqual(first_list.item_set.count(), 1)
        self.assertEqual(second_list.item_set.count(), 1)