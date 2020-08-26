from django import forms


class ContactUsForm(forms.Form):
    name = forms.CharField(max_length=25, required=True)
    subject = forms.CharField(max_length=50, required=True)
    sender = forms.EmailField()
    phone = forms.CharField(max_length=10, required=True)
    message = forms.CharField(required=False, widget=forms.Textarea)


# CAPACITY_CHOICES = [
#     ('0.5', '0.5 л'),
#     ('1', '1 л'),
#     ('1.5', '1.5 л'),
#     ('2', '2 л'),
#     ('1.5', '1.5 л'),
# ]
#
#
# class SimpleForm(forms.Form):
#     birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
#     favorite_colors = forms.MultipleChoiceField(
#         required=False,
#         widget=forms.CheckboxSelectMultiple,
#         choices=FAVORITE_COLORS_CHOICES,
#     )
