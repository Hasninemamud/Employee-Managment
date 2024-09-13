from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('add/', views.add_employee, name='add_employee'),
    path('edit/<int:pk>/', views.edit_employee, name='edit_employee'),
    path('', views.employee_list, name='employee_list'),  # Assuming this is the employee list view
    path('delete/<int:pk>/', views.delete_employee, name='delete_employee'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
