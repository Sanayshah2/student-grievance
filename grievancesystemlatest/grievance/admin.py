from django.contrib import admin

# Register your models here.

from .models import Admin
from .models import Student
from .models import Complain
from .models import Like


admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(Complain)
admin.site.register(Like)