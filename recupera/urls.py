from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Somente aqui!
    path('api/', include('api.urls')),
    path('livros/', include('livros.urls')),
]
