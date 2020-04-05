from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model

from rest_framework import viewsets
from apps.punishment_system.models import PunishmentType, Punishment
from vengeful_vineyard.serializers import UserSerializer, GroupSerializer

User = get_user_model()

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
