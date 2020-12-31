from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),label="First Name")
    feedback = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Feedback'}),label="Feedback")

    class Meta:
        model = Feedback
        fields = ['first_name','feedback']