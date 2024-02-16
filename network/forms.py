from django import forms


class NewPostForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(
        attrs={'rows': 3, 'placeholder': 'What\'s on your mind?'}))
