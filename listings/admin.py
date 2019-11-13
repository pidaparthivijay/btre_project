from django.contrib import admin

# Register your models here.
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor', 'price')
    list_editable = ('is_published', 'price', 'realtor')
    search_fields = ('price', 'title', 'zipcode',
                     'description', 'address', 'city')  # donot add any foreign key
    list_per_page = 20


admin.site.register(Listing, ListingAdmin)
