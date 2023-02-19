from django.shortcuts import render, get_object_or_404 
import stripe 
from .models import Item

 # Get Stripe Session Id view 
def buy(request, item_id): 
    item = get_object_or_404(Item, pk=item_id) 

    # Create Stripe Session Id using Python Library Stripe  
    session = stripe.checkout.Session.create( 
        payment_method_types=['card'],   # Accept only card payments  
        line_items=[{               # Set item details  
            'name': item.name,   # Item name  
            'description': item.description, # Item description  
            'amount': int(item.price * 100), # Item price in cents (stripe requires integer value)  
            'currency': 'usd',     # Currency code (USD in this case)  
            'quantity': 1          # Quantity of items (1 in this case)   }],   )

    return JsonResponse({'sessionId': session['id']})
            

     # Get HTML page with information about selected item view
def item(request, item_id): 

    item = get_object_or_404(Item, pk=item_id) 

    context = {'item': item} 

    return render(request, 'index.html', context)
