from django import forms


# Just creates a modifyable text box
class FacebookPostForm(forms.Form):
    text = forms.CharField(label = '', required = True,
                           widget = forms.Textarea(
                           attrs = {
                               "placeholder": "Your post",
                           }))