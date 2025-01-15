from rest_framework.permissions import BasePermission

class IsVendor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_vendor()

class IsVenueOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_venue_owner()

class IsVenueManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_venue_manager()