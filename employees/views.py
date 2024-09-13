from django.shortcuts import render,redirect, get_object_or_404

# Create your views here.

from django.core.paginator import Paginator
from .models import Employee
from .forms import EmployeeForm

def employee_list(request):
    search_query = request.GET.get('search', '')
    employees = Employee.objects.filter(first_name__icontains=search_query) | Employee.objects.filter(email__icontains=search_query)
    
    # Sorting
    sort_by = request.GET.get('sort_by', 'first_name')
    employees = employees.order_by(sort_by)

    # Pagination
    paginator = Paginator(employees, 10)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'employees/employee_list.html', {'page_obj': page_obj})




def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})

def edit_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_list')  
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/edit_employee.html', {'form': form})

def delete_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')
    return render(request, 'employees/confirm_delete.html', {'employee': employee})
