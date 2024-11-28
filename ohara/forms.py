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

# そらの
# ログイン時のみ実行
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        # フォームのデータを保存するが、まだデータベースにはコミットしない。
        if form.is_valid():
            post = form.save(commit=False)
            # 投稿のユーザーを現在のログインユーザーに設定。
            post.user = request.user  
            # 投稿をデータベースに保存
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'keiziban/post_form.html', {'form': form})

class PostForm(forms.ModelForm):
    class Meta:
      model = Keiziban_post
      fields = ['title', 'comment']