from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from e_drugs.models import Medicine
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, medicine_id):
    cart = Cart(request)
    medicine = get_object_or_404(Medicine, id=medicine_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(medicine=medicine, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, medicine_id):
    cart = Cart(request)
    medicine = get_object_or_404(Medicine, id=medicine_id)
    cart.remove(medicine)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={
            'quantity': item['quantity'],
            'override': True
        })
    return render(request, 'detail.html', {'cart': cart})


