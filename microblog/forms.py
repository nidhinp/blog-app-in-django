from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=32)
    password = forms.CharField(widget=forms.PasswordInput)
    
class NewblogpostsForm(forms.Form):
    title = forms.CharField(max_length=50)
    body = forms.CharField(widget=forms.Textarea, required=False)
    
class CommentForm(forms.Form):
    name = forms.CharField(max_length=32)
    comment = forms.CharField(widget=forms.Textarea(attrs={'cols': 30, 'rows': 4}))
    
