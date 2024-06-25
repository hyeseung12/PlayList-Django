from django.shortcuts import render

def show_index(request):
    context = {}
    return render(request, '플리/index.html', context=context)

def show_login(request):
    context = {}
    return render(request, '플리/login.html', context=context)

def show_signup(request):
    context = {}
    return render(request, '플리/signup.html', context=context)