from rest_framework.views import APIView
from apps.companies.models import Enterprise, Employee
from rest_framework.exceptions import APIException
from apps.accounts.models import GroupsPermissions, UserGroups
from apps.accounts.serializers import UserSerializer
from rest_framework.response import Response
from apps.accounts.auth import Authentication
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import User

class BaseView(APIView):
    def get_enterprise_user(self, user_id):
        enterprise = {
            "is_owner": False,
            "permissions": []
        }

        enterprise['is_owner'] = Enterprise.objects.filter(user_id=user_id).exists()

        if enterprise['is_owner']: return enterprise

        # Permissions, Get Employee
        employee = Employee.objects.filter(user_id=user_id).first()

        if not employee: raise APIException("Este usuário não é um funcionário")

        groups = UserGroups.objects.filter(user_id=user_id).all()

        for g in groups:
            group = g.group

            permissions = GroupsPermissions.objects.filter(group_id=group.id).all()

            for p in permissions:
                enterprise['permissions'].append({
                    "id": p.permission.id,
                    "label": p.permission.name,
                    "codename": p.permission.codename
                })

        return enterprise



        
        #Permissions, get employee

class SigninView(BaseView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = Authentication.signin(self, email=email, password=password)
        
        token = RefreshToken.for_user(user)

        enterprise = self.get_enterprise_user(user.id)

        serializer = UserSerializer(user)

        return Response({
            "user": serializer.data,
            "enterprise": enterprise,
            "refresh": str(token),
            "access": str(token.access_token)
        })
class SignupView(BaseView):
    def post(self, request):
        name = request.data.get('name')
        email = request.data.get('email')
        password = request.data.get('password')

        user = Authentication.signup(self, name=name, email=email, password=password)

        serializer = UserSerializer(user)

        return Response({"user": serializer.data})
    
class GetUserView(BaseView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = User.objects.filter(id=request.user.id).first()
        enterprise = self.get_enterprise_user(user)

        serializer = UserSerializer(user)

        return Response({
            "user": serializer.data,
            "enterprise": enterprise
        })