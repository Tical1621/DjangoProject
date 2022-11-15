from rest_framework import serializers
from parser_app.models import GroupsModel


class GroupsSerializer(serializers.ModelSerializer):  #implements Serializable + @Data
    class Meta:
        model = GroupsModel
        fields = ('id', 'name', 'members_count')
