from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('tutoring/', include('noble_tutoring.urls')),
    path('admin/', admin.site.urls),
]
