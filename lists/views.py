from django.http import HttpResponse
from django.shortcuts import redirect
from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(
            text=request.POST['item_text']
        )
        return redirect('/')

    return HttpResponse(
        '<html>'
        '<title>To-Do lists</title>'
        '<body>'
        '<form method="POST">'
        '<input name="item_text">'
        '</form>'
        '</body>'
        '</html>'
    )