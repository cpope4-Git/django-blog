from django.contrib import admin
from blogging.models import Post, Category


class CategoryInline(admin.TabularInline):
    model = Post.categories.through
    extra = 0


class PostAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
