from django.db import models


class GroupsModel(models.Model):  #@Entity @Table
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)
    members_count = models.IntegerField()

    def __getitem__(self, item):
        return self, item

    class Meta:
        db_table = 'groups'
