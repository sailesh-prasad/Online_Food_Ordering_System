from django.urls import path, include
from .api import urls as api_urls



urlpatterns = [
    path('api/', include(api_urls)),
]

# urlpatterns = [
#     path('student_list', views.student_list, name='student_list'),
#     path('studentr-detail/<int:student_id>/', views.student_detail, name='student_detail') 
# ]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('admin/manage-privileges/', views.manage_admin_privileges, name='manage_admin_privileges'),
#     path('admin/edit-privilege/<int:user_id>/', views.edit_admin_privilege, name='edit_admin_privilege'),
# ]
