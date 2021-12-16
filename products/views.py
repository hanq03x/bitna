from django import http
from django.http.response import Http404
from django.views.generic import ListView, View
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models, forms
from reviews import models as review_models
from reviews import forms as review_forms


class HomeView(ListView):
    """ HomeView Definition """

    model = models.Product

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        rings = self.paginate_queryset(models.Ring.objects.all(), 10)
        earrings = self.paginate_queryset(models.Earring.objects.all(), 10)
        necklaces = self.paginate_queryset(models.Necklace.objects.all(), 10)
        bracelets = self.paginate_queryset(models.Bracelet.objects.all(), 10)
        context.update({
            'ring_list': rings[2],
            'ring_page': rings[1],
            'earring_list': earrings[2],
            'earring_page': earrings[1],
            'necklace_list': necklaces[2],
            'necklace_page': necklaces[1],
            'bracelet_list': bracelets[2],
            'bracelet_page': bracelets[1]
        })
        return context


class RingView(ListView):
    """ Ring List and Search View Definition """

    model = models.Ring
    paginate_by = 12
    paginate_orphans = 3
    ordering = "created"


class EarringView(ListView):
    """ EarringView Definition """

    model = models.Earring
    paginate_by = 12
    paginate_orphans = 3
    ordering = "created"


class NecklaceView(ListView):
    """ NecklaceView Definition """

    model = models.Necklace
    paginate_by = 12
    paginate_orphans = 3
    ordering = "created"


class BraceletView(ListView):
    """ BraceletView Definition """

    model = models.Bracelet
    paginate_by = 12
    paginate_orphans = 3
    ordering = "created"


def product_detail(request, pk):
    try:
        product = models.Ring.objects.get_or_none(pk=pk)
        if product: pass
        elif models.Earring.objects.get_or_none(pk=pk):
            product = models.Earring.objects.get(pk=pk)
        elif models.Bracelet.objects.get_or_none(pk=pk):
            product = models.Bracelet.objects.get(pk=pk)
        elif models.Necklace.objects.get_or_none(pk=pk):
            product = models.Necklace.objects.get(pk=pk)
        else:
            raise Http404
        review = review_models.Review.objects.filter(product=product)
        form = review_forms.CreateReviewForm()
        return render(request, "products/product_detail.html", {"product": product, "review": review, "form": form})
    except review_models.Review.DoesNotExist:
        return render(request, "products/product_detail.html", {"product": product, "form": form})


class SearchView(View):
    """ SearchView Definition """

    def get(self, request):
        form = forms.SearchForm(request.GET)
        if form.is_valid():
            type = form.cleaned_data.get("type")
            weight = form.cleaned_data.get("weight")
            material = form.cleaned_data.get("material")
            size = form.cleaned_data.get("size")
            stone = form.cleaned_data.get("stone")

            filter_args = {}
            if weight is not None:
                filter_args["weight__lte"] = weight
            for m in material:
                filter_args["material"] = m
            if type != "earring":
                if size is not None:
                    filter_args["size__gte"] = size
            if type != "bracelet":
                for s in stone:
                    filter_args["stone"] = s
            
            if type == "ring":
                qs = models.Ring.objects.filter(**filter_args).order_by("-created")
            elif type == "earring":
                qs = models.Earring.objects.filter(**filter_args).order_by("-created")
            elif type == "bracelet":
                qs = models.Bracelet.objects.filter(**filter_args).order_by("-created")
            elif type == "necklace":
                qs = models.Necklace.objects.filter(**filter_args).order_by("-created")
            
            paginator = Paginator(qs, 20, orphans=5)
            page = request.GET.get("page", 1)
            products = paginator.get_page(page)
            return render(
                request, "products/search.html", {"form": form, "products": products}
            )

        else:
            form = forms.SearchForm()

        return render(request, "products/search.html", {"form": form})
