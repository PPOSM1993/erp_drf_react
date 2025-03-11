from .models import *
from rest_framework.views import APIView
from apps.accounts.models import *

from .exceptions import *
from .serializers import *

class BaseView(APIView):
    def get_enterprise_id(self, user_id):
        employee = Employee.objects.filter(user_id=user_id).first()
        owner = Enterprise.objects.filter(user_id=user_id).first()

        if employee:
            return employee.enterprise.id

        return owner.id

    def get_employee(self, employee_id, user_id):
        enterprise_id = self.get_enterprise_id(user_id)

        employee = Employee.objects.filter(id=employee_id, enterprise_id=enterprise_id).first()

        if not employee:
            raise EmployeeNotFound
        
        return employee
    
    def get_group(self, group_id, enterprise_id):
        group = Groups.objects.values('name').filter(id=group_id, enterprise_id=enterprise_id).first()

        if not group:
            raise GroupNotFound
        
        return group
    
    def get_status(self, status_id):
        status = TaskStatus.objects.filter(id=status_id).first()

        if not status:
            raise NotFoundTaskStatus
        
        return status
    
    def get_task(self, task_id, enterprise_id):
        task = Task.objects.filter(id=task_id, enterprise_id=enterprise_id).first()

        if not task:
            raise NotFoundTask
        
        return task

class EmployeeView(BaseView):
    pass