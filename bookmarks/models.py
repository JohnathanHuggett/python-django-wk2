from django.db import models
from uuid import uuid4
from django.core.validators import URLValidator
from django.contrib.auth.models import User

# Create your models here.


# class Category(models.Model):
#     id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
#     name = models.CharField(max_length=50, blank=True)

#     # def __str__(self):
#     #    return self.name


class BookMark(models.Model):
    # TODO categories
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=200)
    notes = models.TextField(blank=True)
    web_address = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    category = models.CharField(max_length=20)


class PersonalBookMark(BookMark):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
