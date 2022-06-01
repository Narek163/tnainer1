from django.urls import path
from .import views
from .views import CategoryilstView, CatgoryDetalView
urlpatterns = [
    path('',CategoryilstView.as_view(),name='xanut'),
    path('xanut/<int:id>',CatgoryDetalView.as_view(),name='xanut_detal'),
]