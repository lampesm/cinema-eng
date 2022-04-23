from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, views):
        return bool(
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_staff
        )


class IsSuperUserOrStaffReadOnly(BasePermission):
    def has_permission(self, request, view):

        if request.method in SAFE_METHODS \
            and request.user.is_authenticated \
            and request.user.is_staff:
            return True

        return bool(request.user.is_superuser)