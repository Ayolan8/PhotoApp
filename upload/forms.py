from django import forms
from core.models import Photos

class AddForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ['title', 'description', 'created_by', 'photo',]


        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(),
            'created_by': forms.TextInput(attrs={
                'value': '',
                'type': 'hidden',
                'id': 'change'
            }),
            'photo': forms.FileInput(),
            }

class EditForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields = ['title', 'description', 'created_by', 'photo',]


        widgets = {
            'title': forms.TextInput(),
            'description': forms.Textarea(),
            'created_by': forms.TextInput(attrs={
                'value': '',
                'type': 'hidden',
                'id': 'change'
            }),
            'photo': forms.FileInput(),
            }
