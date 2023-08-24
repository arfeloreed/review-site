from django.urls import path
from . import views


# urls below
urlpatterns = [
    # path("", views.index),
    path("", views.IndexView.as_view()),  # for class based view
    # path("thank-you", views.thank_you),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.AllReviewsView.as_view()),
    # path("reviews/<int:id>", views.ReviewDetailView.as_view(), name="review-detail"),
    path("reviews/favorite", views.AddFavoriteView.as_view()),
    path("reviews/<int:pk>", views.ReviewDetailView.as_view(),
         name="review-detail"),  # using the DetailView
]
