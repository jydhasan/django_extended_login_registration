from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    father_name = forms.CharField(max_length=100, required=False, help_text='Optional.')
    mother_name = forms.CharField(max_length=100, required=False, help_text='Optional.')

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('father_name', 'mother_name')
