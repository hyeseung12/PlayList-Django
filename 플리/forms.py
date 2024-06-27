from django import forms
from django.contrib.auth.forms import AuthenticationForm

from 플리.models import User, UserManager


class UserCreateForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'nickname')

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email=email).exists():
            raise forms.ValidationError('존재하지 않는 이메일 주소입니다.')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8 or len(password) > 20:
            raise forms.ValidationError('비밀번호는 8자 이상 20자 이하이어야 합니다.')
        return password

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = UserManager.normalize_email(self.cleaned_data['email'])
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class EmailLoginForm(AuthenticationForm):
    username = forms.EmailField()

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if email and password:
            self.user_cache = User.objects.filter(email=email, password=password).first();
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data

class SignUpForm(AuthenticationForm):
    username = forms.EmailField()

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if email and password:
            self.user_cache = User.objects.filter(email=email).first();
            if self.user_cache is not None:
                raise forms.ValidationError(
                    self.error_messages['inactive'],
                    code='inactive',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                user = User(
                    email = email,
                    password = password
                )
                user.save()
                self.email = user.email
        return self.cleaned_data