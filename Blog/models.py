from django.db import models

# Employee model
class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=50)
    emp_dob = models.DateTimeField()
    emp_address = models.CharField(max_length=200)

# Book model
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100)  # Adjusted max_length as per your needs
    
    class Meta:
        db_table = "MyBooks"
