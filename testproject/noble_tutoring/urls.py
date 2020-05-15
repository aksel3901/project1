from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
<<<<<<< HEAD
#     path('courses/<int:course_id>/', views.detail, name='rooms')
# ]
=======
>>>>>>> 592fd72a14edeb1cfb8aec21ffc598a4d08cb154
    path('courses/<int:course_id>/', views.detail, name='rooms'),
    path('login_page', views.login_page),
    path('login_user', views.login_user),
    path('register_page', views.register_page),
    path('profile_page', views.profile_page)
<<<<<<< HEAD
]
=======
]
>>>>>>> 592fd72a14edeb1cfb8aec21ffc598a4d08cb154
