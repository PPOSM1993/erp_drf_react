# Description: Authentication class for signin and signup
from apps.companies.models import Enterprise, Employee
from .models import User
from rest_framework.exceptions import AuthenticationFailed, APIException
from rest_framework import status
from django.contrib.auth.hashers import check_password, make_password


# Create your views here.

class Authentication:
    def signin(self, email=None, password=None) -> User:
        exception_auth = AuthenticationFailed('Invalid credentials, try again')

        user_exists = User.objects.filter(email=email).exists()

        if not user_exists:
            raise exception_auth
        
        user = User.objects.filter(email=email).first()

        if not check_password(password, user.password):
            raise exception_auth
        
        return user
    
    def signup(self, name, email, password, type_account='owner', company_id=False):
        if not name or name == '':
            raise APIException('Name is required')
        
        if not email or email == '':
            raise APIException('Email is required')

        if type_account == 'employee' and not company_id:
            raise APIException('Company ID is required for employee account')

        user = User
        if user.objects.filter(email=email).exists():
            raise APIException('Email already exists')
        
        password_hashed = make_password(password)
        
        created_user = user.objects.create(
            name=name,
            email=email,
            password=password_hashed,
            is_owner=0 if type_account == 'employee' else 1
        )

        if type_account == 'owner':
            created_enterprise = Enterprise.objects.create(
                name='Nome da empresa',
                user_id=created_user.id
            )

        if type_account == 'employee':
            Employee.objects.create(
                enterprise_id=company_id or created_enterprise.id,
                user_id=created_user.id
        )