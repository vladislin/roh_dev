from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=25, required=True)
    subject = forms.CharField(max_length=50, required=True)
    sender = forms.EmailField()
    phone = forms.CharField(max_length=20, required=True)
    message = forms.CharField(required=False, widget=forms.Textarea)
