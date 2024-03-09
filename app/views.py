from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import generic
from .models import ObjectModel
from django.template.loader import get_template


templates = {
    "index": "app/index.html",
    "create": "app/create.html",
    "list": "app/list.html",
    "edit": "app/edit.html"
}


# Create your views here.
class IndexView( generic.TemplateView ):
    template_name = templates["index"]


class CreateView( generic.CreateView ):
    model = ObjectModel
    slug_field = "slug"
    slug_url_kwarg = "slug"
    template_name = templates["create"]
    fields = ( "title", "description" )


class ListView( generic.ListView ):
    model = ObjectModel
    slug_field = "slug"
    slug_url_kwarg = "slug"
    paginate_by = 10
    template_name = templates["list"]

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        queryset = queryset.order_by( "title" )
        return queryset


class EditView( generic.UpdateView ):
    model = ObjectModel
    slug_field = "slug"
    slug_url_kwarg = "slug"
    context_object_name = "context"
    template_name = templates["edit"]
    fields = ( "title", "description" )

