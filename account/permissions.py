

from rest_framework import permissions
PERMISSION_MAP = {
	"1":"Staff",
	"2":"SP",
	"3":"PI",
	"4":"PSI",

}


class HasPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        
        return True
