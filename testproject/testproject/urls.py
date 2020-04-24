from django.contrib import admin
from django.urls import include, path
from noble_tutoring.views import homepage_view

urlpatterns = [
    path('tutoring/', include('noble_tutoring.urls')),
    path('admin/', admin.site.urls),
    path('', homepage_view)
]
