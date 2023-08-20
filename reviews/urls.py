from django.urls import path
from . import views


# urls below
urlpatterns = [
    # path("", views.index),
    path("", views.IndexView.as_view()),  # for class based view
    path("thank-you", views.thank_you),
]
