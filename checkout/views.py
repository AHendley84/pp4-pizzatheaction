from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# Create your views here.
def checkout(request):
    basket = request.session.get('basket', {})
    if not basket:
        messages.error(request, "There are currently no items in your basket")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51OSbmLAeCiLG7FEMBt83SGPru1ltGlnqndcOngrNodbzkp9GOPOvmDCgyCMWwAVbgMhYQNqjPFoterTyAkAVOtSo007FVaUesL'
    }

    return render(request, template, context)
