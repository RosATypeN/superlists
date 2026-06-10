# lists/views.py
from django.shortcuts import render, redirect, get_object_or_404
from lists.models import List, Item

def home_page(request):
    # 首页只显示输入框，不处理 POST
    return render(request, 'home.html')

def new_list(request):
    # 只通过 /lists/new POST 创建新的 List 和第一个 Item
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

def view_list(request, list_id):
    # 查看指定 List 的 Items
    list_ = get_object_or_404(List, id=list_id)
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'], list=list_)
        return redirect(f'/lists/{list_.id}/')
    items = list_.item_set.all()
    return render(request, 'list.html', {'list': list_, 'items': items})