from django.shortcuts import render

def allblogs(request):
    return render(request, 'allblogs.html')
