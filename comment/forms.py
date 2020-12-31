from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    comment_message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Write a review'}),label="Review")
    rating = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),label="Rate")
    class Meta:
        model = Comment
        fields = ['rating','comment_message']