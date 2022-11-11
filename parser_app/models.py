from django.db import models


class GetGroupsRequest(models.Model):
    group_id = models.AutoField(primary_key=True)


class GetGroupsResponse(models.Model):
    group_id = models.AutoField(primary_kye=True)
    title = models.CharField(max_length=200)
    users_count = models.AutoField()

    def __str__(self):
        return self.group_id  # это типо сеттеры?
