from django.contrib import admin

from .models import Feed

# Register your models here.
@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):   # admin 페이지에서 바로 보여주는 정보
    list_display=['id', 'content', 'content_length', 'created_at', 'updated_at']  # id는 자동생성되어서 Feed class에 없어도 됨
    list_display_links=['content']   # content 클릭하면 새로운 페이지에서 상세 정보를 띄움