from django.contrib import admin

# Register your models here.
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_mvp', 'email',
                    'phone', 'hire_date')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'phone', 'email')
    list_editable = ('is_mvp', 'phone', 'email')
    search_fields = ('phone', 'name', 'description',
                     'email')  # donot add any foreign key
    list_per_page = 20


admin.site.register(Realtor, RealtorAdmin)
