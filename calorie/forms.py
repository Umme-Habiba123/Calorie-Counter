from django import forms
from django.contrib.auth.forms import UserCreationForm, User, AuthenticationForm
from .models import *




class RegisterForm(UserCreationForm):
    
    username=forms.CharField(label='Username', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter Login'
        }
    ))
    
    email=forms.CharField(label='Email', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Write Your Email'
        }
    ))
    
    password1=forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Password'
        }
    ))
    
    password2=forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Confirm Password'
        }
    ))
    
   
    class Meta:
        model=User
        fields=['username', 'email','password1', 'password2']
    
    
class LoginForm(AuthenticationForm):    
     username=forms.CharField(label='Username', widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'placeholder':'Enter Login'
        }
    ))
     
     email=forms.CharField(label='Email', widget=forms.TextInput(
         attrs={
             'class':'form-control',
             'placeholder':'Enter email'
         }
     ))
     
     password=forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Password'
        }
    ))
     
    
from .models import CalorieProfile


class CalorieProfileForm(forms.ModelForm):
    class Meta:
        model = CalorieProfile
        fields = ['name', 'age', 'gender', 'height', 'weight']
        

class FoodEntryForm(forms.ModelForm):
    class Meta:
        model = FoodEntry
        fields = ['item_name', 'calorie_consumed']      
