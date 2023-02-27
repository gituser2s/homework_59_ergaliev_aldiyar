from django.shortcuts import render, redirect, get_object_or_404
from django.core.handlers.wsgi import WSGIRequest
from webapp.models import Product, CategoryChoice
from webapp.forms import ProductForm


def add_view(request: WSGIRequest):
    if request.method == "GET":
        form = ProductForm()
        return render(request, 'product_create.html',
                      context={
                          'choices': CategoryChoice.choices,
                          'form': form
                        })

    form = ProductForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'product_create.html',
                      context={
                          'choices': CategoryChoice.choices,
                          'form': form
                      })
    else:
        product = Product.objects.create(**form.cleaned_data)
        return redirect('product_detail', pk=product.pk)


def detail_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product.html', context=context)


def update_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail', pk=product.pk)
        return render(request, 'product_update.html', context={'form': form, 'product': product})
    form = ProductForm(instance=product)
    return render(request, 'product_update.html', context={'form': form, 'product': product})


def delete_view(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_confirm_delete.html', context={'product': product})


def confirm_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('index')






