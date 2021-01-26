from django import forms


class Contact(forms.Form):
    message = forms.CharField(label=' ', widget=forms.TextInput(attrs={'placeholder': 'Message Here',
                                                                       'size': '100'}))
