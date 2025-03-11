from rest_framework.exceptions import APIException

class EmployeeNotFound(APIException):
    status_code = 404
    default_detail = 'Employee not found.'
    default_code = 'not_found_employee'

class GroupNotFound(APIException):
    status_code = 404
    default_detail = 'Group not found.'
    default_code = 'not_found_group'

class RequiredField(APIException):
    status_code = 400
    default_detail = 'fields not correct.'
    default_code = 'error_required_field'

class NotFoundTaskStatus(APIException):
    status_code = 400
    default_detail = 'Task Status not found.'
    default_code = 'not_found_task_status'

class NotFoundTask(APIException):
    status_code = 404
    default_detail = 'Task not found.'
    default_code = 'not_found_task'