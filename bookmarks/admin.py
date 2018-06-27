from django.contrib import admin

from .models import BookMark, PersonalBookMark

# Register your models here.
admin.site.register(BookMark)
admin.site.register(PersonalBookMark)
