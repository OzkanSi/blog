from django.contrib import admin
from blog.models import Post, Category
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publish_date', 'slug']
    list_display_links = ['publish_date']
    list_filter = ['category']
    list_editable = ['title']

    class Meta:
        model = Post

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = (
        "pk",
        "title",
        "slug",
    ) 

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)