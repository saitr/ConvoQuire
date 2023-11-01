from django import forms
from .models import *



class SignUpForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Enter Your UserName'}))  
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg','placeholder': 'Enter The Password'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg','placeholder': 'Enter Your Email'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already in use. Please use a different email.")
        return email

    class Meta:
        model = User
        fields = ('username','password', 'email')

class SignInForm(forms.Form):
    email= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg','placeholder': 'Password'}))
    class Meta:
        model = User
        fields = ('email', 'password')


class PostForm(forms.Form):
    heading= forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Please Type Your Question'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg', 'placeholder': 'Description', 'rows': 3}))
    class Meta:
        model = Post
        fields = ('heading', 'description')