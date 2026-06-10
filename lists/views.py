from django.http import HttpResponse
from django.shortcuts import redirect


def home_page(request):

    if request.method == 'POST':
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