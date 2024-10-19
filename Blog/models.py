from django.db import models
from taggit.managers import TaggableManager  # Import TaggableManager

# Employee model
class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=50)
    emp_dob = models.DateTimeField()
    emp_address = models.CharField(max_length=200)

# Book model with tagging functionality
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100)
    # Adding tags to the Book model
    tags = TaggableManager()  # This adds tagging functionality to the Book model

    class Meta:
        db_table = "MyBooks"

    def __str__(self):
        return self.book_name

# Contact model
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
    
