from django.shortcuts import render
from django.views.generic.base import View
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .forms import ProfileForm
from .models import UserProfile


# Create your views here.
# class IndexView(View):
#     def get(self, request):
#         form = ProfileForm()
#         return render(
#             request,
#             "profiles/index.html",
#             {
#                 "form": form,
#             }
#         )

#     def post(self, request):
#         submitted_form = ProfileForm(request.POST, request.FILES)

#         if submitted_form.is_valid():
#             # print(f"\n{request.FILES['user_image']}\n")

#             uploaded_file = UserProfile(image=request.FILES["user_image"])
#             uploaded_file.save()
#             return HttpResponseRedirect("/profiles")

#         return render(
#             request,
#             "profiles/index.html",
#             {
#                 "form": submitted_form,
#             }
#         )

# using CreateView fpr rendering the index page
class IndexView(CreateView):
    template_name = "profiles/index.html"
    model = UserProfile
    form_class = ProfileForm
    success_url = "/profiles"


# route for the profile list view
class ProfileListView(ListView):
    template_name = "profiles/profile-list.html"
    model = UserProfile
    context_object_name = "profiles"
