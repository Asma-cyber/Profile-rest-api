from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        # SAFE_METHODS is a tuple of HTTP methods that should be accepted as read-only
        # methods. See also: https://www.django-rest-framework.org/api-guide/permissions/#safe-methods
        if request.method in permissions.SAFE_METHODS:
            return True
        # obj is the object that the user is trying to access
        return obj.id == request.user.id
    
