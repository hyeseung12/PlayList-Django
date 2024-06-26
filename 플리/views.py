from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import FormView

from 플리.forms import EmailLoginForm


def show_index(request):
    context = {}
    return render(request, '플리/index.html', context=context)

class EmailLoginView(FormView):
    form_class = EmailLoginForm
    template_name = '플리/login.html'

    def form_valid(self, form):
        email = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('플리:show_index')  # 로그인 후 리디렉션할 URL
        return self.form_invalid(form)

def show_signup(request):
    context = {}
    return render(request, '플리/signup.html', context=context)

def show_url(request):
    context = {}
    return render(request, '플리/url.html', context=context)

def show_mypage(request):
    context = {}
    return render(request, '플리/mypage.html', context=context)