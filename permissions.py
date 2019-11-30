from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    """
        Object-level permission to only allow owners of an object to edit it.
    """
    # Default message
    # message = 'Permission Denied.'
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Instance must have an attribute named 'author' or 'user'.
        try:
            return obj.author == request.user
        except :
            return obj.user == request.user

        # return obj.author == request.user
