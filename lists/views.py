from django.http import HttpResponse

def home_page(request):
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