from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from restaurant.models import foodItems, restaurantUser
from django.db.models import Q
from django.http import request

User = get_user_model()

@login_required
def menu(request):
    user = request.user
    query = request.GET.get('q')
    foods = foodItems.objects.all()
    
    if query:
        foods = foods.filter(Q(name__icontains=query))
    
    cartEmpty = True
    if hasattr(user, 'customeruser'):
        name = user.customeruser.name
    else:
        name = "No name found"

    if 'cart' not in request.session:
        request.session['cart'] = {}

    if request.method == 'POST':
        id = request.POST.get("id")
        cart = request.session.get('cart', {})
        if id in cart:
            cart[id] += 1
            cartEmpty = False
        else:
            cart[id] = 1
            cartEmpty = False
        request.session['cart'] = cart

    list_restaurant = restaurantUser.objects.all()

    return render(request, 'index1.html', {
        'name': name,
        'foodItems': foods,
        'cart': request.session.get('cart', {}),
        'Empty': cartEmpty,
        'restaurant_list': list_restaurant
    
    })


@login_required
def restaurant_menu(request, restaurant_id):
    menu(request)
    restaurant = get_object_or_404(restaurantUser, id=restaurant_id)
    food_items = foodItems.objects.filter(restaurantName=restaurant)
    return render(request, 'restaurant_menu.html', {
        'restaurant': restaurant,
        'food_items': food_items
    })


def restaurantPage(request):
    rname = request.POST
    print(rname)

    return render(request,'restaurantPage.html')
