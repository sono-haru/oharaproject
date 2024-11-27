from django.contrib import admin
from .models import Keiziban_post
from .models import Keiziban_post, ViewCount

class User_post(admin.ModelAdmin):
    list_display=('id','title')
    list_display_links=('id','title')

admin.site.register(Keiziban_post,User_post)
class ViewCountAdmin(admin.ModelAdmin):
    list_display=('count',)
admin.site.register(ViewCount, ViewCountAdmin)