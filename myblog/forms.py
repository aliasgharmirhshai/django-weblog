from django import forms
from .models import Comments

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea, required=False)
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("name", "email", "body")


class SerachForm(forms.Form):
    query = forms.CharField()