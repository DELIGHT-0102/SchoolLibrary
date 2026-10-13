from django import forms
from django.contrib.auth.models import User
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'author',
            'category',
            'description',
            'cover_image',
            'available'
        ]


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput
    )

    password_confirmation = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        confirmation = cleaned_data.get(
            'password_confirmation'
        )

        if password != confirmation:
            raise forms.ValidationError(
                'Passwords do not match.'
            )

        return cleaned_data