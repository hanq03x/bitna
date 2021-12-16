from django import forms
from . import models


class CreateReviewForm(forms.ModelForm):
    beauty = forms.IntegerField(max_value=5, min_value=1)
    size = forms.IntegerField(max_value=5, min_value=1)
    color = forms.IntegerField(max_value=5, min_value=1)
    finish = forms.IntegerField(max_value=5, min_value=1)

    class Meta:
        model = models.Review
        fields = (
            "beauty",
            "size",
            "color",
            "finish",
            "review",
        )
    
    def save(self):
        review = super().save(commit=False)
        return review