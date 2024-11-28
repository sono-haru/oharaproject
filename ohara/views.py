from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View, generic
from . import forms
from django.urls import reverse_lazy

# そら
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Keiziban_post
from django.shortcuts import render, redirect

# ねもと
from django.views.generic import DetailView
from django.views.generic import DeleteView
from .models import ViewCount
from django.utils import timezone
from django.core.mail import EmailMessage

#検索機能
from .models import Keiziban_post
from django.views.generic import ListView

class IndexView(TemplateView):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        page_view, created = ViewCount.objects.get_or_create(id=1)
        page_view.count += 1
        page_view.last_viewed = timezone.now()
        page_view.save()
        context = self.get_context_data(**kwargs)
        context['count'] = page_view.count
        context['last_viewed'] = page_view.last_viewed
        return self.render_to_response(context)



class ContactView(generic.FormView):
    template_name = 'contact.html'
    form_class = forms.OharaForm
    success_url = reverse_lazy('ohara:contact')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        inquiry = form.cleaned_data['inquiry']

        from_email = 'sonoharu032011@gmail.com'
        to_list = ['sonoharu032011@gmail.com']
        message = EmailMessage(
            subject=f"{name}からの問い合わせ",
            body=inquiry,
            from_email=from_email,
            to=to_list,
            cc=[email]
        )
        message.send()
        return super().form_valid(form)
    

class CountView(View):
    def get(self, request):
        return render(request, 'view_count.html', {
            'count': ViewCount.objects.first().count,'last_viewed':ViewCount.objects.first().last_viewed
        })

class IntroductionView(TemplateView):
    template_name='introduction.html'

class KeizibanView(TemplateView):
    template_name='keiziban.html'

# そらの
def post_list(request):
    posts = Keiziban_post.objects.all().order_by('-posted_at')  # 最新の投稿を上に表示
    return render(request, 'keiziban.html', {'posts': posts})

# 新規投稿を作成(そら)
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # ログインユーザーが投稿者
            post.save()
            return redirect('ohara:keiziban')  # 投稿後、掲示板一覧にリダイレクト
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})

# 閲覧数(ねもと)
class DetailView(DetailView):
    template_name="detail.html"
    model=Keiziban_post

class PostDeleteView(DeleteView):
    model=Keiziban_post
    template_name="post_delete.html"
    success_url=reverse_lazy("ohara:keiziban")

    def delete(self,request,*args,**kwargs):
        return super().delete(request,*args,**kwargs)
#検索機能
# __icontainsは小文字大文字の区別がない
class Keiziban_post_List(ListView):
    template_name = 'keiziban.html'
    context_object_name = 'posts'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            keiziban_post_list = Keiziban_post.objects.filter(
                title__icontains=query
            )
        else:
            keiziban_post_list = Keiziban_post.objects.all().order_by('-posted_at')
        return keiziban_post_list
    