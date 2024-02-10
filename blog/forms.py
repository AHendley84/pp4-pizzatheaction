from django import forms
from .models import BlogPost


class AddPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = (
            'title',
            'created_by',
            'content',
        )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'created_by': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }