from django.db import models


# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Type')

    def __str__(self):
        return f'{self.name}'


class Issue(models.Model):
    summary = models.CharField(max_length=300, null=False, blank=False, verbose_name='Summary')
    description = models.TextField(max_length=300, null=True, blank=True, verbose_name='Description')
    type = models.ManyToManyField('webapp.Type', related_name='issues', blank=True)
    status = models.ForeignKey('webapp.Status', on_delete=models.PROTECT, related_name='status', verbose_name='Status')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Update At')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')

    def __str__(self):
        return f'{self.pk}. {self.summary}'


class Status(models.Model):
    status_name = models.CharField(max_length=50, null=False, blank=False, verbose_name='Status')

    def __str__(self):
        return f'{self.status_name}'