# forms.py

from django import forms
from allauth.account.forms import LoginForm, SignupForm, ResetPasswordForm, ResetPasswordKeyForm, AddEmailForm

class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['login'].widget.attrs.update({
            'class': 'w-full px-3 py-2 rounded-md bg-gray-700 text-gray-300 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Your Email'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'w-full px-3 py-2 rounded-md bg-gray-700 text-gray-300 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Your Password'
        })

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'w-full px-3 py-2 rounded-md bg-gray-700 text-gray-300 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Your Email'
        })
        self.fields['username'].widget.attrs.update({
            'class': 'w-full px-3 py-2 rounded-md bg-gray-700 text-gray-300 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Choose a Username'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'w-full px-3 py-2 rounded-md bg-gray-700 text-gray-300 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Create Password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'w-full px-3 py-2 rounded-md bg-gray-700 text-gray-300 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Confirm Password'
        })

class CustomPasswordResetForm(ResetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'w-full px-3 py-2 rounded-md bg-gray-700 text-gray-300 border border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500',
            'placeholder': 'Your Email'
        })



class CustomSetPasswordForm(ResetPasswordKeyForm):
    password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'New Password',
            'class': 'w-full bg-gray-700 text-white px-3 py-2 rounded-md'
        })
    )
    password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm New Password',
            'class': 'w-full bg-gray-700 text-white px-3 py-2 rounded-md'
        })
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'autofocus': 'true'
        })


class CustomAddEmailForm(AddEmailForm):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'input input-primary block w-full mt-1 text-lg rounded border-gray-300 focus:border-indigo-500 focus:ring-indigo-500',
                'placeholder': 'Your Email'
            }
        ),
        label='Email Address'
    )        