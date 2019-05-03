from django import forms
from . models import Movie, User


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')



