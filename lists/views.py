from django.shortcuts import redirect, reverse
from products import models as product_models
from . import models


def save_fav_product(request, product_pk):
    action = request.GET.get("action", None)
    product = product_models.Product.objects.get_or_none(pk=product_pk)
    if product and action:
        the_list, _ = models.List.objects.get_or_create(
            user=request.user, name="Favorite"
        )
        if action == "add": the_list.products.add(product)
        elif action == "remove": the_list.products.remove(product)
    
    return redirect(reverse("products:detail", kwargs={"pk": product_pk}))