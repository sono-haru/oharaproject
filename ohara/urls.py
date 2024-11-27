from django.urls import path
from . import views
from . views import CountView
from .views import Keiziban_post_List
app_name = 'ohara'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('introduction/', views.IntroductionView.as_view(), name='introduction'),
    path('view_count/', CountView.as_view(), name='view_count'),
    # path('keiziban/', views.post_list, name='keiziban'),
    path('keiziban/new/', views.post_create, name='post_create'),
    path('keiziban/', Keiziban_post_List.as_view(), name='keiziban'),
    path('detail/<int:pk>',views.DetailView.as_view(),name='keiziban_detail'),
    path('ohara/<int:pk>/delete/',views.PostDeleteView.as_view(),name="post_delete"),
]