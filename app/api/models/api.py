from django.db import models
from django.utils import timezone

class Api(models.Model):
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    creator_id = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Api, self).save(*args, **kwargs)


    class Meta:
        abstract = True
