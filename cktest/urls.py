from django.urls import path,include
from cktest import views
urlpatterns = [
    path('accueil/',views.index,name="index"),
]