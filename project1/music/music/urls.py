
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('genres/', views.genres),
    path('deletegenre/<int:id_genre>', views.deletegenre),
    path('editgenre/<int:id_genre>', views.editgenre),
    path('add_genre/', views.add_genre),
    path('track/', views.track),
    path('addtrack/', views.addtrack),
    path('deletetrack/<int:id_track>', views.deletetrack),
    path('edittrack/<int:id_track>', views.edittrack),
    #коментарий
]
