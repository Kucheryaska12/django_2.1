from django.shortcuts import render, redirect, HttpResponse
from phones.management.commands.import_phones import Command
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    my_db = Command()
    my_db.handle()
    sortur = request.GET.get('sort')
    if sortur == 'name':
        phones_objects = Phone.objects.all().order_by('name')
    elif sortur == 'min_price':
        phones_objects = Phone.objects.all().order_by('price')
    elif sortur == 'max_price':
        phones_objects = Phone.objects.all().order_by('-price')
    else:
        phones_objects = Phone.objects.all()
    context = {'phones': phones_objects}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)



