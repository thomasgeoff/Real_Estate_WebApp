from django.contrib import admin

from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title','is_published','price','list_date','realtor')
    list_display_links = ('id','title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('id','title','description','price','list_date','realtor')
    list_per_page = 25
      

admin.site.register(Listing, ListingAdmin)

# Register your models here.
