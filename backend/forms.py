from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Section, Sectionright, Algoleft, Algoright

class PostSection(forms.ModelForm):

    class Meta:
        model = Section
        fields = ('title', 'text',)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class PostSectionr(forms.ModelForm):

    class Meta:
        model = Sectionright
        fields = ('title', 'text',)

class PostAlgoLeft(forms.ModelForm):

    class Meta:
        model = Algoleft
        fields = ('title', 'text',)

class PostAlgoRight(forms.ModelForm):

    class Meta:
        model = Algoright
        fields = ('title', 'text',)

# backend forms to create (at least)
#BackHomeL, BackHomeR, BackAlgL, BackAlgR