from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('webpage.urls')),
    # path('admin/', admin.site.urls),
]
