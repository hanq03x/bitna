from django.contrib import messages
from django.shortcuts import redirect, reverse, render
from django.views.generic import FormView
from products import models as product_models
from . import forms, models


def create_review(request, product):
    if request.method == "POST":
        form = forms.CreateReviewForm(request.POST)
        p = product_models.Product.objects.get_or_none(pk=product)
        if not p:
            return redirect(reverse("core:home"))
        if form.is_valid():
            review = form.save()
            review.product = p
            review.user = request.user
            review.save()
            messages.success(request, "Product reviewed")
            return redirect(reverse("products:detail", kwargs={"pk": p.pk}))


def delete_review(request, review):
    action = request.GET.get("action", None)
    review = models.Review.objects.get_or_none(pk=review)
    product = product_models.Product.objects.get_or_none(reviews=review)
    if review and action == "remove":
        review.delete()
    return redirect(reverse("products:detail", kwargs={"pk": product.pk}))
