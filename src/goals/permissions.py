from rest_framework import permissions

from goals.models import BoardParticipant, Role


class BoardPermissions(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        filters: dict = {'user': request.user, 'board': obj}
        if request.method not in permissions.SAFE_METHODS:
            filters['role'] = Role.owner

        return BoardParticipant.objects.filter(**filters).exists()


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_id == request.user.id


class GoalCategoryPermissions(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        filters: dict = {'user': request.user, 'board': obj.board}
        if request.method not in permissions.SAFE_METHODS:
            filters['role__in'] = [Role.owner, Role.writer]

        return BoardParticipant.objects.filter(**filters).exists()


class GoalPermissions(permissions.IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        filters: dict = {'user': request.user, 'board': obj.category.board}
        if request.method not in permissions.SAFE_METHODS:
            filters['role__in'] = [Role.owner, Role.writer]
        return BoardParticipant.objects.filter(**filters).exists()


class CommentsPermissions(permissions.IsAuthenticated):

    def has_object_permission(self, request, view, obj):
        return any((request.method in permissions.SAFE_METHODS, obj.user_id == request.user.id))
