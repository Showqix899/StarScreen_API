from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        # Ensure the user is authenticated and their role is 'admin'
        return request.user and request.user.is_authenticated and request.user.role == 'admin'