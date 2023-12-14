from django import forms
from .models import Product


class ProductCreateForm(forms.ModelForm): # Model form
    title = forms.CharField(label='',
                    widget=forms.TextInput(attrs={"placeholder": "Your title" ,})),
    email = forms.EmailField()
    description = forms.CharField(
                    required=False,
                    widget=forms.Textarea(
                        attrs={
                            "class": "new-class-name two",
                            "placeholder": "Your description",
                            "id": "my-id-for-text-area",  # internal attr
                            "rows": 20,
                            "cols": 120,
                        }
                    ))
    price = forms.DecimalField(initial= 199.99)
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
        ]

        # Form
    # def clean_title(self, *args, **kwargs): # If you're not sure when you're overriding something, args and kwargs is good practice
    #     title = self.cleaned_data.get("title")
    #     if not "CEF" in title:
    #         raise forms.ValidationError("This is not a valid title")
    #     return title
    # def clean_email(self, *args, **kwargs): # If you're not sure when you're overriding something, args and kwargs is good practice
    #     email = self.cleaned_data.get("email")
    #     if not email.endswith("edu"):
    #         raise forms.ValidationError("This is not a valid email")
    #     else:
    #         return email

class RawProductForm(forms.Form): # Django form
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

