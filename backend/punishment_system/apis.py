from django.shortcuts import render
from rest_framework import viewsets
from .models import PunishmentType, Punishment, VineyardGroup, VineyardUser
from .serializers import PunishmentTypeSerializer, PunishmentSerializer, VineyardGroupSerializer, LeaderboardSerializer, VineyardUserSerializer
from django.contrib.auth import get_user_model
from .services import punishmentSystemService

# Create your views here.

class VineyardUserViewSet(viewsets.ModelViewSet): #Make service to create user from OW4 token
    queryset = VineyardUser.objects.all().order_by('-id')
    serializer_class = VineyardUserSerializer

class PunishmentTypeViewSet(viewsets.ModelViewSet):
    queryset = PunishmentType.objects.all().order_by('value')
    serializer_class = PunishmentTypeSerializer

class PunishmentViewSet(viewsets.ModelViewSet):
    queryset = Punishment.objects.all().order_by('-date')
    serializer_class = PunishmentSerializer
    #def preform_create(self, serializer):         authentication scheme needed for request.user
    #    serializer.save(giver=self.request.user)

class VineyardGroupViewSet(viewsets.ModelViewSet):
    queryset = VineyardGroup.objects.all()
    serializer_class = VineyardGroupSerializer
    lookup_field = 'name'

class LeaderboardViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = LeaderboardSerializer
    def get_queryset(self):
        active_only = self.request.query_params.get("active_only", "True").capitalize()
        group = self.kwargs['VineyardGroup']
        return punishmentSystemService.get_group_punishments(groupname=group, active_only=active_only)