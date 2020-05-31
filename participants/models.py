from django.db import models
from django.utils.translation import gettext_lazy as _


class EnvironmentExposures(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)


class GeneticMutations(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)


class Participants(models.Model):
    class Statuses(models.TextChoices):
        NOTREVIEWED = 'NOTREVIEWED', _('Not Reviewed')
        ACCEPTED = 'ACCEPTED', _('Reviewed - Accepted')
        NOTACCEPTED = 'NOTACCEPTED', _('Reviewed - Not Accepted')

    name = models.CharField(max_length=255)
    age = models.IntegerField()
    siblings = models.IntegerField()
    status = models.CharField(
        max_length=255, choices=Statuses.choices, default=Statuses.NOTREVIEWED)
    exposures = models.ManyToManyField(EnvironmentExposures)
    mutations = models.ManyToManyField(GeneticMutations)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    def get_exposures(self):
        return [e.name for e in self.exposures.all()]

    def get_mutations(self):
        return [m.name for m in self.mutations.all()]
