from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def helloWorld(request):
    return HttpResponse('Hello world!')

def taskList(request):
    return render(request, 'tasks/list.html')

def yourname(request, name):
    return render(request, 'tasks/yourname.html', {'name':name})
