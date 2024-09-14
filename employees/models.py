from django.db import models
from PIL import Image

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to='employee_photos/')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # Save the instance first

        # Resize the photo
        img = Image.open(self.photo.path)
        
        # Set a maximum size (e.g., 300x300 pixels)
        max_size = (300, 300)
        if img.height > 300 or img.width > 300:
            img.thumbnail(max_size)
            img.save(self.photo.path)
