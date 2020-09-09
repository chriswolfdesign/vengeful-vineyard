from django.db import models
from .models import Punishment, VineyardUser
from django.db.models import Prefetch, Sum, Case, When, F, Q, DecimalField, FilteredRelation
from django.db.models.query import QuerySet
class punishmentSystemService:
    @staticmethod
    def get_group_punishments(*,
                              group_name: str,
                              active_only: bool
                              ) -> QuerySet:

        punishments_in_group = Punishment.objects.filter((Q(active=True) | Q(active = active_only)), group__name=group_name)

        # remove not relevant punishments from the attribute (not field) "punishments"(punishments not in group)
        user_punishments_in_group = VineyardUser.objects.filter(vineyardgroup__name=group_name)\
            .prefetch_related(Prefetch("punishments", queryset=punishments_in_group))\
            .annotate(punishments_in_group_sum=Sum(                                                                                                                      #for each user, annotate the sum of punishments to the attribute "punishments_in_group_sum"
                Case(
                    When(Q(punishments__group__name=group_name) & (Q(punishments__active=True) | Q(punishments__active = active_only)), then=F('punishments__type__value')),   #for each relevant punishment, add its value to the sum
                    default=0,                                                                                                                                                 #for each irrelevant punishment, add 0 to the sum
                    output_field=DecimalField()))
        ).order_by("punishments_in_group_sum")

        #the "(Q(punishments__active=True) | Q(punishments__active = active_only))"-expression is disgusting, but it works:
        #if active_only is True then it becomes:  (Q(punishments__active=True) | (Q(punishments__active=True)))  == Q(punishments__active=True)
        #if active_only is False then it becomes: (Q(punishments__active=True) | (Q(punishments__active=False))) == Q(True)

        return user_punishments_in_group
