from django.contrib import admin
from quotations.models import Quotation

class QuotationAdmin(admin.ModelAdmin):
    list_display = ('author', 'quot_text')
    
admin.site.register(Quotation, QuotationAdmin)
