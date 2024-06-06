from django.shortcuts import render

def show_index(request):
    context = {}
    return render(request, '플리/index.html', context=context)