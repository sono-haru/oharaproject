from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=('username','email','password1','password2')
 
class ContactForm(forms.Form):
 
    name = forms.CharField(label='名前')
    email = forms.EmailField(label='鴨川アドレス')
    title = forms.CharField(label='件名')
    message = forms.CharField(label='かもけんに一言', widget=forms.Textarea)
 
    def __ini__(self, *args, **kwargs):
 
        super().__init__(*args, **kwargs)
 
        self.fields['name'].widget.attrs['placeholder'] = \
            '名前を入力してください'
 
        self.fields['name'].widget.attrs['class'] = 'form-control'
 
 
        self.fields['title'].widget.attrs['placeholder'] = \
            'かもけんを入力してください'
       
        self.fields['title'].widget.attrs['class'] = 'form-control'
 
 
        self.fields['message'].widget.attrs['placeholder'] = \
            'メッセージを鴨川してください'
       
        self.fields['message'].widget.attrs['class'] = 'form-control'
       
