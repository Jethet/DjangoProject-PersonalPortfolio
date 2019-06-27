from django.urls import path

from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.detail, name='detail'),
]

# The second path makes it possible to go to the individual blogs: the path
# basically states 'look for an int after the /blog'
