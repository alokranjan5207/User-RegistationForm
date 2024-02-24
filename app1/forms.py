from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from typing import Any
class RegistationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email','password']
        # fields=['username','password','email']
    
    def save(self):
        s=super().save(commit=True) #      s=super().save(commit=False) me nhi store ho rha
        s.password=make_password(self.cleaned_data['password'])
        s.save()
        return s
    