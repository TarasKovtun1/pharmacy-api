from django.db import models

class Firm(models.Model):
    parent_id = models.IntegerField()
    parent_name = models.CharField(max_length=255)
    area_id = models.IntegerField()
    area_name = models.CharField(max_length=255)
    city_id = models.IntegerField()
    city_name = models.CharField(max_length=255)
    comdir_id = models.IntegerField()
    comdir_name = models.CharField(max_length=255)
    curator_id = models.IntegerField()
    curator_name = models.CharField(max_length=255)
    chiefaccountant_id = models.IntegerField()
    chiefaccountant_name = models.CharField(max_length=255)
    regionaldir_id = models.IntegerField()
    regionaldir_name = models.CharField(max_length=255)
    technicaldir_id = models.IntegerField(null=True, blank=True)
    technicaldir_name = models.CharField(max_length=255, null=True, blank=True)
    group_id = models.IntegerField()
    group_name = models.CharField(max_length=255)
    status_id = models.IntegerField()
    status_name = models.CharField(max_length=255)
    firm_id = models.IntegerField(unique=True)
    firm_name = models.TextField()
    path_base = models.CharField(max_length=255)

    def __str__(self):
        return self.firm_name
