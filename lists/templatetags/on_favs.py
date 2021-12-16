from django import template
from lists import models as list_models
from products import models as product_models
from django.shortcuts import redirect, reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def on_favs(context, product):
    user = context.request.user
    the_list = list_models.List.objects.get_or_none(
        user=user, name="Favorite"
    )
    if the_list:
        try:
            the_list.products.get(name=product)
            return True
        except product_models.Product.DoesNotExist:
            return False
    else:
        return redirect(reverse("core:home"))



