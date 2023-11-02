from django import forms
from .models import Contact,ServiceEnquiry

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your Name...", "class": "form-control"}),
            "address": forms.TextInput(attrs={"placeholder": "Your Address...", "class": "form-control"}),
            "email": forms.EmailInput(attrs={"placeholder": "Email...", "class": "form-control"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone Number...", "class": "form-control"}),
            "message": forms.Textarea(attrs={"placeholder": "Message..." , "class": "fullwidth"}),
        }



class ServiceEnquiryForm(forms.ModelForm):
    class Meta:
        model = ServiceEnquiry
        fields = ["name", "email", "phone"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your Name..."}),
            "email": forms.EmailInput(attrs={"placeholder": "Email..."}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone..."}),
        }