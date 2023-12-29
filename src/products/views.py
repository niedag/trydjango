from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404

from .models import Product
from .forms import ProductCreateForm, RawProductForm


def product_list_view(request): #Dynamic linking Urls + Listing products ---- Check Product_list.html for more deets
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)

def product_delete_view(request, id):
    obj = get_object_or_404(Product, id= id)
    #obj.delete() -- using GET request to delete an entry-- NOT GOOD, USE POST REQUEST

    if request.method == "POST":
        obj.delete()
        return redirect('../../') # Go back a few pages
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)

def product_detail_view(request, id): # I want to be able to grab different data from the database
    #obj = Product.objects.get(id=my_id)
    obj = get_object_or_404(Product, id = id) # Handing DoesNotExist error most efficiently
    # try:
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #     raise Http404
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)

def product_update_view(request, id = id):
    obj = get_object_or_404(Product, id = id)
    form = RawProductForm(request.POST)
    context = {
        'form': form
    }
    return render (request, "products/product_create.html", context)

def product_create_view(request):
    form = ProductCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductCreateForm()
    context = {
        'form':form
    }
    return render(request, "products/product_create.html", context)

def render_initial_data(request): # Rendering objects from database, making initial values show, saving new values to objects
    initial_data = {
        'title': "My Awesome Title"
    }
    obj = Product.objects.get(id=1)
    form = ProductCreateForm(request.POST or None, initial = initial_data, instance = obj)
    if form.is_valid():
        form.save()
    context = {
        'form':form
    }
    return render(request, "products/product_create.html", context)

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

# def product_create_view(request):
#     form = ProductCreateForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form = ProductCreateForm()
#
#     context = {
#         'form':form
#     }
#     return render(request, "products/product_create.html", context)

#    return render(request, "products/product_detail.html", context)