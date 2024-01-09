from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
from . import views

admin.site.site_header = "GolpoSolpo Admin"
admin.site.site_title = "GolpoSolpo"
# admin.site.index_header = "Index"

urlpatterns = [
    path('contact',views.Contact),
    path('post/<slug:url>/',views.firstpage),
    path('catagory/<slug:url>/',views.ViewCatagory),
    path('search',views.Search,name="search"),
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)