
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'pdf_reader_app'

urlpatterns = [
    path('main/', views.simple_upload, name='pdf_uploader'),
]
