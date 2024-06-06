from rest_framework import permissions
from .permissions import isTodoEditor

class TodoEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, isTodoEditor]