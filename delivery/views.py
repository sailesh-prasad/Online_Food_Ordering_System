from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout, get_user_model
from delivery.models import deliveryUser
from customer.models import Order
from customer.models import State, City, Place
from django.core.mail import send_mail
from .models import Feedback

# Home view for logged-in users
@login_required
def home(request):
    delivery_user = deliveryUser.objects.get(username=request.user.username)
    orders = Order.objects.filter(delivery_person=delivery_user.name)  # Filter by delivery person's name

    if request.method == 'POST':
        order_id = request.POST.get('order_id')
        new_status = request.POST.get('status')
        try:
            order = Order.objects.get(id=order_id, delivery_person=delivery_user.name)
            order.status = new_status
            order.save()
            messages.success(request, f"Order status of {order.order_no} is {order.get_status_display()}")
        except Order.DoesNotExist:
            messages.error(request, 'Order not found or you are not authorized to update this order')

        return redirect('home')  # Redirect to avoid resubmission on refresh

    return render(request, 'Deliveryhome.html', {'orders': orders, 'messages': messages.get_messages(request), 'customer_address': delivery_user.address})

def loginDelivery(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Username or Password')
            return redirect('loginDelivery')
        elif user.is_delivery == False:
            messages.error(request, 'You are Registered as customer')
            return redirect('loginDelivery')
        elif user.is_restaurant == True:
            messages.error(request, 'You are Registered as restaurant')
            return redirect('loginDelivery')
        # Log the user in
        else:
            login(request, user)
            messages.success(request, 'Successfully Login')
            from_email = 'InFOODSys@gmail.com'  # Use the correct from_email
            user_name = deliveryUser.objects.get(email=username).name
            delivery_link = request.build_absolute_uri('/home/')
            send_mail(
                'Welcome Back, {}'.format(user_name),
                """Hello {},

Ready to deliver happiness today? 🚚💨
Check out your upcoming deliveries and get ready to hit the road!

👉 [View Upcoming Deliveries]({})

We're here to help you make someone's day better! 🌟

Drive safe and enjoy the ride,
Delivery Team 🚗💨""".format(user_name, delivery_link),
                from_email,
                [user.email],
                fail_silently=False,
                html_message="""Hello {},<br><br>

Ready to deliver happiness today? 🚚💨<br>
Check out your upcoming deliveries and get ready to hit the road!<br><br>

👉 <a href="{}">View Upcoming Deliveries</a><br><br>

We're here to help you make someone's day better! 🌟<br><br>

Drive safe and enjoy the ride,<br>
Delivery Team 🚗💨""".format(user_name, delivery_link)
            )
        return redirect('home')  # Redirect to a homepage or dashboard after login

    return render(request, 'loginDelivery.html')

def registerDelivery(request):
    states = State.objects.all()
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        state_id = request.POST.get('state')
        city_id = request.POST.get('city')
        place_id = request.POST.get('place')
        state = State.objects.get(id=state_id)
        city = City.objects.get(id=city_id)
        place = Place.objects.get(id=place_id)
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        delivery_data = deliveryUser(
            username=email,
            password=make_password(password),
            email=email,
            state=state, 
            city=city, 
            place=place,
            deliveryContact=phone,
            name=name,
            address=address,
            is_delivery=True
        )

        # Check if the user already exists
        if deliveryUser.objects.filter(username=email).exists() and deliveryUser.objects.filter(is_delivery=True):
            messages.error(request, 'User Already Exist in the System')
            return redirect('registerDelivery')
        elif deliveryUser.objects.filter(username=email).exists() and deliveryUser.objects.filter(is_delivery=False):
            messages.error(request, 'You have Customer Account Using This Email ID. Try Another Email ID')
            return redirect('loginDelivery')
        else:
            delivery_data.save()
            messages.success(request, "Successfully Registered")
            return redirect('loginDelivery')
    return render(request, 'registerDelivery.html', {'states': states})

def feedback_form(request):
    pass