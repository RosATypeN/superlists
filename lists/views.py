from django.shortcuts import render, redirect
from lists.models import Item, List


def home_page(request):
    if request.method == 'POST':

        list_ = List.objects.create()

        Item.objects.create(
            text=request.POST['item_text'],
            list=list_
        )

        return redirect('/')

    items = Item.objects.all()

    return render(
        request,
        'home.html',
        {'items': items}
    )