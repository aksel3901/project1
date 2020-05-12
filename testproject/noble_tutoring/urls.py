from django.urls import path

from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('courses/<int:course_id>/', views.detail, name='rooms'),
    path('login_page', views.login_page),
    path('login_user', views.login_user),
    path('register_page', views.register_page),
    path('profile_page', views.profile_page)
]
