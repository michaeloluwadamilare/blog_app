from django import forms
from .models import Post, Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'text']

    def __str__(self):
        return f'{self.comment_text} by {self.author}'