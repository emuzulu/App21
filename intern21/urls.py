from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name='login'),
    path("logout", views.logout_view, name='logout'),
    path("applications", views.applications, name='applications'),
    path("<int:app_id>/delete", views.delete_view, name='delete'),
    path("add", views.add_view, name="add")



]