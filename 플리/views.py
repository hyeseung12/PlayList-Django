from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import FormView, CreateView

from 플리.forms import EmailLoginForm, UserCreateForm, SignUpForm
from 플리.models import User, PlayList


def show_index(request):
    context = {}
    return render(request, '플리/index.html', context=context)

class EmailLoginView(FormView):
    form_class = EmailLoginForm
    template_name = '플리/login.html'

    def form_valid(self, form):
        email = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = User.objects.filter(email=email, password=password).first();
        user.last_login = timezone.now()
        if user is not None:
            login(self.request, user)
            return redirect('플리:show_index')
        return self.form_invalid(form)

class SignUpView(FormView):
    form_class = SignUpForm
    template_name = '플리/signup.html'

    def form_valid(self, form):
        email = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        if User.objects.filter(email=email).first() is None:
            print("user")
            user = User(email=email, password=password)
            user.save()
            return redirect('플리:show_login')

        return self.form_invalid(form)

def show_url(request):
    context = {}
    return render(request, '플리/url.html', context=context)

def show_mypage(request):
    context = {}
    return render(request, '플리/mypage.html', context=context)

class PlayListCreateView(CreateView):
    model = PlayList
    fields = ['title', 'image', 'author']

def show_create(request):
    context = {}
    return render(request, '플리/create.html', context=context)