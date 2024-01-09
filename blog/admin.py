from django.contrib import admin
from .models import Post, Catagory


#For configration of Catagory admin
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('title','desc','urls')
    search_fields = ('title','desc')

#For configration of Post admin
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','content','urls','catagory')
    search_fields = ('title','content','catagory')
    list_filter = ('catagory',)
    # list_per_page = 10

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js','js/script.js',)

# Register your models here.
admin.site.register(Catagory,CatagoryAdmin)
admin.site.register(Post,PostAdmin)
