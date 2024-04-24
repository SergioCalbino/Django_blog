from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from users.models import User
from users.api.serializer import UserRegisterSerializer, UserSerializer, UserUpdateSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        
        # Si es valido entra al if
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(sefl, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    
    def put(self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user, data=request.data)
        
        if 'first_name' in request.data and not request.data['first_name']:
            return Response({'first_name': ['El nombre no puede estar vacío.']}, status=status.HTTP_400_BAD_REQUEST)
        
        if 'last_name' in request.data and not request.data['last_name']:
            return Response({'last_name': ['El apellido no puede estar vacío.']}, status=status.HTTP_400_BAD_REQUEST)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            