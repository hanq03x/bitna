from django import forms
from . import models


class SearchForm(forms.Form):
    TYPE_CHOICES = (
        ("ring", "반지"),
        ("earring", "귀걸이"),
        ("necklace", "목걸이"),
        ("bracelet", "팔찌"),
    )
    type = forms.ChoiceField(
        choices=TYPE_CHOICES,
    )
    size = forms.IntegerField(required=False)
    weight = forms.IntegerField(required=False)
    material = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Material.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    stone = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Stone.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )