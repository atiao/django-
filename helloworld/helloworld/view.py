from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
		print "_______________________", request
		context= {}
		context['hello'] = 'Hello World!'
		return render(request, 'hello.html', context)