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