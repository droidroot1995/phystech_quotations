from django.contrib import admin

class QuotationAdmin(admin.ModelAdmin):
    list_display = ('author', 'quotation')
    
admin.site.register(User, QuotationAdmin)
