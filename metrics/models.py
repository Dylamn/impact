from django.db import models

from accounts.models import User
from impact.models import TimeStampedModel
from metrics.utils import calculate_note


class Report(TimeStampedModel):
    uuid = models.UUIDField('model identifier', primary_key=True)
    url = models.CharField(max_length=255, null=False)
    score = models.PositiveIntegerField(null=True)
    metrics = models.JSONField()

    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    previous_report = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True
    )

    class Meta:
        ordering = ('uuid',)

    def get_note(self) -> str:
        return calculate_note(self.score)
