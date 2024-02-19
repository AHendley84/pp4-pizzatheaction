from django import forms
from .models import BlogPost, BlogComment


class AddPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = [
            'title',
            'category',
            'product_name',
            'product_rating',
            'purchase_date',
            'content',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'created_by': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_rating'].label = 'Rating (1 to 5)'


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['comments']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
