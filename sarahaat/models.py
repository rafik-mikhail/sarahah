from django.db import models
from sarahah_project import settings
from django.urls import reverse


class Sarahaat(models.Model):
    secret = models.TextField()
    forwhm = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sarahaat')

    def __str__(self):
        return self.secret[:25]

    def get_absolute_url(self):
        return reverse('sarahah_detail', args=[str(self.id)])
