from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import FormView

from 플리.forms import EmailLoginForm
from 플리.models import User


def show_index(request):
    context = {}
    return render(request, '플리/index.html', context=context)

class EmailLoginView(FormView):
    form_class = EmailLoginForm
    template_name = '플리/login.html'

    def form_valid(self, form, DoesNotExist=None):
        email = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = User.objects.filter(email=email, password=password).first();
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