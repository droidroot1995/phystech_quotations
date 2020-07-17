from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_GET, require_POST
from django.views.decorators.csrf import csrf_exempt

from django.apps import apps

from .forms import QuotationForm
# Create your views here.

@require_GET
def get_last_added_quotations(request):
    Quotation = apps.get_model('quotations.Quotation')
    quotations = Quotation.objects().all().values('id', 'author', 'quot_text')[-10:]
    result = []
    
    for quot in quotations:
        quotation = {'id': quot.id, 'author': quot.author, 'quot_text': quot.quot_text}
        result.append(quotation)
        
    result.reverse()
    
    return JsonResponse({'quotations': result})

@require_GET
def get_quot_by_id(request):
    Quotation = apps.get_model('quotations.Quotation')
    
    quotation = Quotation.objects().filter(id=request.GET['id']).values('id', 'author', 'quot_text', 'added_at', 'added_by').first()
    return JsonResponse({'quotation': quotation})

@csrf_exempt
@require_POST
def add_quotation(request):
    Quotation = apps.get_model('quotations.Quotation')
    User = apps.get_model('users.User')
    
    form = QuotationForm(request.POST)
    
    if form.is_valid():
        quotation = form.save()
        
        return JsonResponse({'quotation': quotation})
    
    return JsonResponse({'error': form.errors}, status=400)
