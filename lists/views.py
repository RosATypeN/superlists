from django.shortcuts import render, redirect, get_object_or_404

from .models import List, Item


def home_page(request):
    if request.method == 'POST':

        text = request.POST.get('item_text', '').strip()

        if text:
            new_list = List.objects.create()

            Item.objects.create(
                text=text,
                list=new_list
            )

            return redirect(
                'list_view',
                list_id=new_list.id
            )

    return render(request, 'home.html')


def list_page(request, list_id):

    list_ = get_object_or_404(
        List,
        id=list_id
    )

    if request.method == 'POST':

        text = request.POST.get(
            'item_text',
            ''
        ).strip()

        if text:
            Item.objects.create(
                text=text,
                list=list_
            )

        return redirect(
            'list_view',
            list_id=list_.id
        )

    return render(
        request,
        'list.html',
        {'list': list_}
    )