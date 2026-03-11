# from django.shortcuts import render

# # Create your views here

# def basehtml(request):
#     return render (request, 'base.html')

from django.shortcuts import render

def basehtml(request):
    return render(request, 'base.html')
