from django.urls import path
from . import views


# url views below this
urlpatterns = [
    path("", views.IndexView.as_view()),
    path("list", views.ProfileListView.as_view()),
]
