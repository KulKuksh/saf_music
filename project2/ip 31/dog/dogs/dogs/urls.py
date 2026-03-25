
from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('breed/<int:id_breed>', views.breed),
    path('dog/<int:id_dog>', views.dog_info),
    path('breeds', views.breed_list),
    path('photos', views.photos),
    path('about', views.about),
    path('addbreed/', views.addBreed),
    path('addbreedform/', views.formAddBreed),
    path('adddogform/', views.formAddDog),
    path('adddog/', views.addDog),
    path('editbreedform/<int:id_breed>', views.formEditBreed),
    path('editbreed/', views.editBreed),
    path('deletebreed/<int:id_breed>', views.deleteBreed),
    path('editdogform/<int:id_dog>', views.formEditDog),
    path('editdog/', views.editDog),
    path('deletedog/<int:id_editDog>', views.deleteDog),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

