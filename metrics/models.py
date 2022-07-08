from django.db import models

from impact.models import TimeStampedModel


class Report(TimeStampedModel):
    uuid = models.UUIDField('model identifier', primary_key=True)
    url = models.CharField(max_length=255, null=False)
    score = models.PositiveIntegerField(null=True)
    
    metrics = models.JSONField()
