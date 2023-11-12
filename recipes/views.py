from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'recipes/home.html', context={'name':'Antonio'})


def contato(request):
    return HttpResponse('contato')


def my_view(request):
    return HttpResponse('ola')


def sobre(request):
    return HttpResponse('sobre')