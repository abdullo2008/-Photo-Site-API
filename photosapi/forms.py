from django import forms
from .models import PhotoModel


class PhotoModelForm(forms.ModelForm):
    class Meta:
        model = PhotoModel
        fields = ['title', 'photo', 'caption']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'caption': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter caption'}),
        }