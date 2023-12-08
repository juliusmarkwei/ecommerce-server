from rest_framework.permissions import BasePermission, SAFE_METHODS

# Custom Permission Classes
class AllowPostRequests(BasePermission):
    """
    Permission to allow anyone to make POST requests.
    """
    def has_permission(self, request, view):
        return request.method == "POST"

class IsOwnerOrAdmin(BasePermission):
    """
    Allows access only to admin users or the owner of the account for DELETE requests.
    """
    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return obj.username == request.user or request.user.is_superuser
        return False

class IsAdminUserOrReadOnly(BasePermission):
    """
    Allows access only to admin users for non-safe methods.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser
