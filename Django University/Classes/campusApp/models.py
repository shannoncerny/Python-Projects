from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, blank=True, null=False, default='')
    state = models.CharField(max_length=2, blank=True, null=False, default='')
    campus_id = models.IntegerField(default='', blank=True, null=False)

    # CREATES MODEL MANAGER
    object = models.Manager()

    # displays model as 'University Campus' in browser on admin page
    class Meta:
        verbose_name_plural = 'University Campus'
