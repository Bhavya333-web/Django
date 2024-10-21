from django.db import models
from taggit.managers import TaggableManager  # Import TaggableManager



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


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
    from django.db import models
from taggit.managers import TaggableManager

class Blog(models.Model):
    title = models.CharField(max_length=200)  # Title of the blog post
    content = models.TextField()  # Content of the blog post
    author = models.CharField(max_length=100)  # Author of the blog post
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the date when created
    updated_at = models.DateTimeField(auto_now=True)  # Automatically set the date when updated
    tags = TaggableManager()  # Allows tags to be added to the blog post

    def __str__(self):
        return self.title  # Display the blog title in the admin panel

    
    
