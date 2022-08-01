from django.contrib import admin
from Pages.models import Service, Option, Discount
# Register your models here.

class TableAdmin(admin.ModelAdmin):
    readonly_fields = ('optionTitle','optionTitleAR')

admin.site.register(Option, TableAdmin)
admin.site.register(Service)
admin.site.register(Discount)
