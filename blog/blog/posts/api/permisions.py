from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permition(self, request):
        if request.method == 'GET':
            return True
        else:
            return request.user_is_staff