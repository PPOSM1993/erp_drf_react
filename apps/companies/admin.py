from django.contrib import admin
from .models import Enterprise, Employee, TaskStatus, Task
# Register your models here.

admin.site.register(Enterprise)
admin.site.register(Employee)
admin.site.register(TaskStatus)
admin.site.register(Task)