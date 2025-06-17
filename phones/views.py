from django.shortcuts import render, redirect

from models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = {}
    # {'phones': Phone.objects.all()}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {'phone.name': Phone.objects.filter(slug=slug)['name'],
               'phone.price': Phone.objects.filter(slug=slug)['price'],
               'phone.image': Phone.objects.filter(slug=slug)['image'],
               'phone.release_date': Phone.objects.filter(slug=slug)['release_date'],
               'phone.lte_exists': Phone.objects.filter(slug=slug)['lte_exists'],
               }
    return render(request, template, context)
