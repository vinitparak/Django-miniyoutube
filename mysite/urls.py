"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from mysite.core import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
app_name = 'core'

urlpatterns = [
    path('',views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    url(r'^search/$', views.search, name='search'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.delete_book, name='delete_book'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    url(r'^edit_post/(?P<pk>\d+)/$', views.edit_post, name='edit_post')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
