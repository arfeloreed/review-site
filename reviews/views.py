from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import ReviewForm
# from .models import Review


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
class IndexView(View):

    def get(self, request):
        form = ReviewForm()

        return render(
            request,
            "reviews/index.html",
            {
                "form": form,
            }
        )

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")

        return render(
            request,
            "reviews/index.html",
            {
                "form": form,
            }
        )

# view page for thank you route


def thank_you(request):
    return render(
        request,
        "reviews/thank-you.html",
    )
