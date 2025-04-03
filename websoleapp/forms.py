

# class ContactForm(forms.Form):
#     complete_name = forms.CharField(max_length=100, required=True)
#     email_address = forms.EmailField(required=True)
#     phone_no = forms.CharField(max_length=15, required=True)
#     preferred_method = forms.ChoiceField(choices=[('Virtual', 'Virtual'), ('In-Office', 'In-Office')], widget=forms.RadioSelect)

from django import forms

class ContactForm(forms.Form):
    complete_name = forms.CharField(max_length=100, required=True)
    phone_no = forms.CharField(max_length=15, required=True)
    email_address = forms.EmailField(required=True)
    company_name = forms.CharField(max_length=100, required=True)
    requirements = forms.CharField(widget=forms.Textarea, required=True)
    file_upload = forms.FileField(required=False)  # Handle file upload
    image_upload = forms.ImageField(required=False)  # Handle image upload
