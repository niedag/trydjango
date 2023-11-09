from django.shortcuts import render

from .models import Product
from .forms import ProductCreateForm, RawProductForm

def product_create_view_raw_django(request):
    my_form = RawProductForm() # Automatically a Get Method request.GET
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)
        if my_form.is_valid():
            # data is gud
            print(my_form.cleaned_data)
        else:
            print(my_form.errors)
    context = {
        "form": my_form,
    }
    return render(request, "products/product_detail_raw_django.html", context)

def product_create_view_raw_html(request):
    context = {}
    #print(request.GET)
    #print(request.POST)
    if(request.method == 'POST'):
        my_title = request.POST.get('title')
        print(my_title)
    return render(request, "products/product_detail_raw.html", context)

def product_create_view(request):
    form = ProductCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductCreateForm()

    context = {
        'form':form
    }
    return render(request, "products/product_create.html", context)

def product_detail_view(request):
    obj = Product.objects.get(id=2)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    # }
    context = {
        "object": obj
    }

    return render(request, "products/product_detail.html", context)