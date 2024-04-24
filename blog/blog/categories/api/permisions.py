from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def  has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else: # any other method
            return request.user.is_staff