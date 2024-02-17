from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Brand


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image',
        required=False,
        widget=CustomClearableFileInput
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_categories = [(
            c.id, c.get_friendly_name()) for c in categories]
        brands = Brand.objects.all()
        friendly_brands = [(b.id, b.get_friendly_name()) for b in brands]

        self.fields['category'].choices = friendly_categories
        self.fields['brand'].choices = friendly_brands
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-1'
