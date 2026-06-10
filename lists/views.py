from django.shortcuts import render, redirect, get_object_or_404
from lists.models import List, Item

def home_page(request):
    if request.method == 'POST':
        return new_list(request)
    return render(request, 'home.html')

def new_list(request):
    # 每次 POST 都只创建一个新列表和一个 Item
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

def view_list(request, list_id):
    list_ = get_object_or_404(List, id=list_id)
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'], list=list_)
        return redirect(f'/lists/{list_.id}/')
    items = list_.item_set.all()
    return render(request, 'list.html', {'list': list_, 'items': items})