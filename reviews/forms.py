from django import forms
from .models import Review


# create your form objects below
# review form
# class ReviewForm(forms.Form):
#     username = forms.CharField(max_length=70, error_messages={
#         "required": "Your name must not be empty",
#         "max_length": "Pleade enter a shorter name",
#     })
#     review_text = forms.CharField(
#         label="Your Feedback:", max_length=200, widget=forms.Textarea)
#     rating = forms.IntegerField(label="Your Rating:", min_value=1, max_value=5)

# cerating a form related to a model object for a database


class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Review
        # specifying wwhich fields from the model object are to be displayed
        # fields = ["username", "review_text", "rating"]
        # render all fields
        fields = "__all__"
        # using exclude to exempt a field that you don't want to be rendered
        # exclude = ["name_of_field"]
        labels = {
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }
        error_messages = {
            "username": {
                "required": "Your name must not be empty",
                "max_length": "Pleade enter a shorter name",
            }
        }
