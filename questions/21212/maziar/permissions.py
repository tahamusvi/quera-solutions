from rest_framework import permissions

from rest_framework import permissions

class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of a comment or admins to edit or delete it.
    Read permissions are allowed to any request.
    """
    
    def has_permission(self, request, view):
        # Allow GET, HEAD, OPTIONS requests for any user
        if request.method in permissions.SAFE_METHODS:
            return True
        # For other requests (PUT, DELETE), the user must be authenticated
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Allow read-only access to any user (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Allow edit and delete only if the user is the owner or an admin
        return request.user.is_staff or obj.owner == request.user
