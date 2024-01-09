"""GolpoSolpo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
from . import views

admin.site.site_header = "GolpoSolpo Admin"
admin.site.site_title = "GolpoSolpo"
# admin.site.index_header = "Index"

urlpatterns = [
    path('blogging/', include('blog.urls')),
    path('',views.firstpage),
    path('admin/', admin.site.urls),
    # path('tinymce/', include('tinymce.urls')),  #add tinymce text editor url.
]+static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
