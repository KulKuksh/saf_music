
from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.glavnaya),
    path('about', views.second),
    path('Contacts', views.contacts),
    path('Photo', views.photo),
    path('Blog', views.blog),
    path('addBreed/', views.addBreed),
    path('addBreedform', views.formAddBreed),
    path('adddogform/', views.formAddDog),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
