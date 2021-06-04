from django import forms
from .models import Data
class Student(forms.ModelForm):
    class Meta:
        model=Data
        fields=['name','email','password']
        error_messages={'name':{'required':'Naam likhna jaruri hy'},'email':{'required':'EMail likhna jaruri hy'},'password':{'required':'password likhna jaruri hy'}}
        widgets={
            "name":forms.TextInput(attrs={'class':'myclass','placeholder':"Enter your name"}),
            "email":forms.EmailInput(attrs={'class':'myclass1','placeholder':"Enter your email"}),
            'password':forms.PasswordInput(render_value=True,)
            }