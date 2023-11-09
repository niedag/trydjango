from django import forms

from .models import Product


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]

class RawProductForm(forms.Form):
    title = forms.CharField(label = 'Product title',
                            widget = forms.TextInput(
                                attrs = {
                                    "placeholder": "Your product title",
                                }))
    description = forms.CharField(
                        required= False,
                        widget=forms.Textarea(
                            attrs = {
                                "class": "new-class-name two",
                                "placeholder": "Your description",
                                "id": "my-id-for-text-area", #internal attr
                                "rows": 15,
                                "cols": 40
                            }
                        ))
    price = forms.DecimalField(initial = 99.99)