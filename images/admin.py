from django.contrib import admin

from images.models import Image, Blog


class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ('uploaded_at', )
    list_display = ('__str__', 'uploaded_at')


admin.site.register(Image, ImageAdmin)


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'category', 'priority', 'date_added')
    list_filter = ('category', 'date_added')
    search_fields = ('title', 'keywords', 'heading', 'sub_heading')

admin.site.register(Blog, BlogAdmin)
