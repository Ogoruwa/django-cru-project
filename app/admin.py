from django.contrib import admin
from .models import ObjectModel


# Register your models here.
class ObjectModelAdmin( admin.ModelAdmin ):
    list_filter = ( "timestamp" )
    list_display = ( "title", "description", "timestamp" )
    autocomplete_fields = { "slug": ("title",) }
    readonly_fields = ( "slug", )

admin.site.register( ObjectModel )
