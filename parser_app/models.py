from django.db import models


class GroupsModel(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)
    members_count = models.IntegerField()

    def __str__(self):
        return self.id

    class Meta:
        db_table = 'groups'

