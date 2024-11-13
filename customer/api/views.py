from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
#from .models import Student
from rest_framework import viewsets
from customer.models import Customer, Restaurant
from .serializers import CustomerSerializer, RestaurantSerializer



class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    
# def student_list(request):
#     students = Student.objects.all()
#     return render(request, 'home/student_list.html', {'students': students})

# def student_detail(request, student_id):
#     student = get_object_or_404(Student, id=student_id)
#     return render(request, 'home/student_detail.html', {'student': student})
