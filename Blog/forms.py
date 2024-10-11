from django import forms
from taggit.models import Tag
from .models import Contact
from .models import Book

class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email = forms.EmailField(label='Your Email')
    message = forms.CharField(widget=forms.Textarea, label='Your Message')

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', 'tags']  # Include tags in the form

class TagFilterForm(forms.Form):
    tag = forms.ModelChoiceField(
        queryset=Tag.objects.all(),  # Populates the dropdown with available tags
        required=False,  # Make this optional so users can view all books without filtering
        label="Filter by Tag"
    )
