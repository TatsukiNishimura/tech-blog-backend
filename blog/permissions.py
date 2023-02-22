from rest_framework.permissions import BasePermission, IsAuthenticated


class BlogAuthentication(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        if view.action in ['create', 'destroy', 'update', 'partial_update']:
            return bool(request.user and request.user.is_authenticated)
        else:
            return True
