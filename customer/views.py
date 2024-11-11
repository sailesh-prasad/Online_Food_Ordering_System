from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import AdminPrivilege


# def student_list(request):
#     students = Student.objects.all()
#     return render(request, 'home/student_list.html', {'students': students})

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

