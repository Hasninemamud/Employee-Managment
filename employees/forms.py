from django import forms
from .models import Employee
from PIL import Image

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'mobile', 'date_of_birth', 'photo']
    
    def save(self, *args, **kwargs):
        employee = super(EmployeeForm, self).save(*args, **kwargs)
        image = Image.open(employee.photo)
        image = image.resize((300, 300))
        image.save(employee.photo.path)
        return employee
