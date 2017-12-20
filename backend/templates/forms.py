from django import forms

from .models import Section, Sectionright

class PostSection(forms.ModelForm):

    class Meta:
        model = Section
        fields = ('title', 'text',)

