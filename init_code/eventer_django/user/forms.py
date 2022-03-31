from django import forms
from captcha.fields import CaptchaField

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={'invalid': 'Please fill in the correct email address'})
    
    password = forms.CharField(required=True, min_length=6, error_messages={'invalid': 'Password must not be less than 6 characters'})
    rePassword = forms.CharField(required=True, min_length=6, error_messages={'invalid': 'Password must not be less than 6 characters'})
    
    captcha = CaptchaField(required=True, error_messages={'invalid': 'Verification code error'})