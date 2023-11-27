from django.urls import path
from .views import main,contact

urlpatterns = [
    path('',main),
    path('detaitl/<str:pk>',contact),
]