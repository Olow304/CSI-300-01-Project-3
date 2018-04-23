from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.html import strip_tags
from twitter_app.models import Tweet


class UserForm(UserCreationForm):
    username = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput(attrs={'placeholder': 'Email'}))
    password1 = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(required=True, widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    def is_valid(self):
        form = super(UserForm, self).is_valid()
        for f, error in self.errors.items():
            if f != '__all_':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form

    class Meta:
        fields = ['email', 'username', 'password1', 'password2']
        model = User


class AuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))

    def is_valid(self):
        form = super(AuthForm, self).is_valid()
        for f, error in self.errors.items():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form


class TweetForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.widgets.Textarea())

    def is_valid(self):
        form = super(TweetForm, self).is_valid()
        for f in self.errors.items():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error'})
        return form

    class Meta:
        model = Tweet
        exclude = ('user',)
