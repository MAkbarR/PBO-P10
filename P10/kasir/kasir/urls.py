from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path
from kasirmart.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('barang1/', Barang1),
    path('addbrg/', addbrg),
    path('Barang1/edit/<int:id_Barang1>', editbrg, name='editbrg'),
    path('Barang1/delete/<int:id_Barang1>', delbrg, name="delbrg"),
]
