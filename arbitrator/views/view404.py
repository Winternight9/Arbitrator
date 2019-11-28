import sys

from django.shortcuts import render

def view404(request, exception, template_name='arbitrator/404.html'):
    res = render(request, template_name)
    res.status_code = 404
    return res


sys.modules[__name__] = view404