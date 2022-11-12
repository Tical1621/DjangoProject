from rest_framework import serializers
from parser_app.models import GroupsModel


class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupsModel
        fields = ('id', 'name', 'members_count')
