from django import forms
from django.core.mail import EmailMessage
from .models import Keiziban_post
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

class OharaForm(forms.Form):
 name = forms.CharField(label='名前', max_length=30)
 email = forms.EmailField(label='メール')
 inquiry = forms.CharField(label='問い合わせ内容',widget=forms.Textarea)
   
 def __init__(self, *args, **kwargs):
   super().__init__(*args, **kwargs)
 def send_email(self):
    name = self.cleaned_data['name']
    email = self.cleaned_data['email']
    inquiry = self.cleaned_data['inquiry']
   
    message = EmailMessage(subject=name + "からの問い合わせ",
                            body=inquiry,
                            from_email=email,
                            to=["admin@skilla.com"],
                            cc=[email])
    message.send()

# そらの
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # ログインしているユーザーを設定
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'keiziban/post_form.html', {'form': form})

class PostForm(forms.ModelForm):
    class Meta:
      model = Keiziban_post
      fields = ['title', 'comment']