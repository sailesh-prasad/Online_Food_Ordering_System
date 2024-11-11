from django.shortcuts import render, get_object_or_404, redirect
from .models import DeliveryPerson, Feedback
from django.http import HttpResponse
from .forms import FeedbackForm  

def create_feedback(request, delivery_person_id):
    delivery_person = get_object_or_404(DeliveryPerson, id=delivery_person_id)
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.delivery_person = delivery_person
            feedback.save()
            return HttpResponse("Feedback submitted successfully.")
    else:
        form = FeedbackForm()
    return render(request, 'feedback_form.html', {'form': form, 'delivery_person': delivery_person})
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import AdminPrivilege


# def student_list(request):
#     students = Student.objects.all()
#     return render(request, 'home/student_list.html', {'students': students})

def feedback_list(request, delivery_person_id):
    delivery_person = get_object_or_404(DeliveryPerson, id=delivery_person_id)
    feedbacks = delivery_person.feedbacks.all()
    return render(request, 'feedback_list.html', {'feedbacks': feedbacks, 'delivery_person': delivery_person})
# def student_detail(request, student_id):
#     student = get_object_or_404(Student, id=student_id)
#     return render(request, 'home/student_detail.html', {'student': student})

# Check if the user is a superuser
def is_superuser(user):
    return user.is_superuser


def manage_admin_privileges(request):
    privileges = AdminPrivilege.objects.all()
    return render(request, 'home/manage_privileges.html', {'privileges': privileges})


def edit_admin_privilege(request, user_id):
    privilege = AdminPrivilege.objects.get(user_id=user_id)
    if request.method == 'POST':
        # Directly update privilege fields from POST data
        privilege.can_manage_orders = request.POST.get('can_manage_orders') == 'on'
        privilege.can_manage_inventory = request.POST.get('can_manage_inventory') == 'on'
        privilege.can_view_reports = request.POST.get('can_view_reports') == 'on'
        privilege.save()
        return redirect('manage_admin_privileges')
    return render(request, 'home/edit_privilege.html', {'privilege': privilege})

