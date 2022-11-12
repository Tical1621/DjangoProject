from rest_framework import serializers
from parser_app.models import GroupsModel


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        id = serializers.IntegerField(primary_key=True)
        title = serializers.CharField(max_length=500)
        members_count = serializers.IntegerField()



