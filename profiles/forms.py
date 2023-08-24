from django import forms
from .models import UserProfile


# create your form objects below
# class ProfileForm(forms.Form):
#     user_image = forms.ImageField()

# using modelForm
class ProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = "__all__"
