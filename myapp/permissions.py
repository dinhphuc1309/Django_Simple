from rest_framework import permissions


class IsUserOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        print(obj)
        print(request.user)

        if not request.user.is_anonymous:
            return request.user == obj

        return False


class IsSupperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        print(obj)
        print(request.user)
        return request.user and request.user.is_superuser
