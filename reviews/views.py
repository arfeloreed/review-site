from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from .forms import ReviewForm
from .models import Review


# Create your views here.
# view page for all reviews and home page
# def index(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)

#         if form.is_valid():
# print(f"\n{form.cleaned_data}\n")

# store the gathered data in the database
# review = Review(
#     username=form.cleaned_data["username"],
#     review_text=form.cleaned_data["review_text"],
#     rating=form.cleaned_data["rating"],
# )
# review.save()

# using the modelForm in storing the gathered data in the database
#         form.save()

#         return HttpResponseRedirect("/thank-you")
# else:
#     form = ReviewForm()

# return render(
#     request,
#     "reviews/index.html",
#     {
#         "form": form,
#     }
# )


# using a class based view
# class IndexView(View):

#     def get(self, request):
#         form = ReviewForm()

#         return render(
#             request,
#             "reviews/index.html",
#             {
#                 "form": form,
#             }
#         )

#     def post(self, request):
#         form = ReviewForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect("/thank-you")

#         return render(
#             request,
#             "reviews/index.html",
#             {
#                 "form": form,
#             }
#         )

# using the FormView to render our Form page
# class IndexView(FormView):
#     template_name = "reviews/index.html"
#     form_class = ReviewForm
#     success_url = "/thank-you"

#     def form_valid(self, form: Any) -> HttpResponse:
#         form.save()
#         return super().form_valid(form)

# using CreateView to render our form page
class IndexView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/index.html"
    success_url = "/thank-you"


# view page for thank you route
# def thank_you(request):
#     return render(
#         request,
#         "reviews/thank-you.html",
#     )


# class based view for thank you route
# class ThankYouView(View):
#     def get(self, request):
#         return render(
#             request,
#             "reviews/thank-you.html",
#         )


# using templateView
class ThankYouView(TemplateView):
    template_name = "reviews/thank-you.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["message"] = "This is a test message."
        return context


# view route for all reviews
# class AllReviewsView(TemplateView):
#     template_name = "reviews/all-reviews.html"

#     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context

# using the ListView for rendering all reviews
class AllReviewsView(ListView):
    template_name = "reviews/all-reviews.html"
    model = Review
    context_object_name = "reviews"

    # def get_queryset(self) -> QuerySet[Any]:
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__lt=3)
    #     return data


# view route for review detail page
# class ReviewDetailView(TemplateView):
#     template_name = "reviews/review-detail.html"

#     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
#         context = super().get_context_data(**kwargs)
    # retrieve the specific review from the url parameter
    # review_id = self.kwargs["id"]
    # review_post = Review.objects.get(pk=review_id)
    # context["review"] = review_post
    # return context

# using DetailView to render our review detail page
class ReviewDetailView(DetailView):
    template_name = "reviews/review-detail.html"
    model = Review
    # context_object_name = "review"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_review = self.object
        request = self.request
        favorite_id = request.session.get("favorite_review")
        context["is_favorite"] = favorite_id == str(loaded_review.id)
        return context


# route view for adding favorites with session
class AddFavoriteView(View):
    def post(self, request):
        favorite_id = request.POST["review_id"]
        request.session["favorite_review"] = favorite_id
        return HttpResponseRedirect("/reviews/" + favorite_id)
