from django.shortcuts import render

def index(request):
    template = 'index.html'
    content = ''
    return render(request, template)