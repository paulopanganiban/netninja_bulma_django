from django.urls import path
from . import views
app_name = "bulma"

urlpatterns = [
    path('', views.index, name='index')
]