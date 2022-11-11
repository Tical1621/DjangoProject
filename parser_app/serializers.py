from rest_framework import serializers
from parser_app.models import GetGroupsRequest, GetGroupsResponse


class GroupsRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = GetGroupsRequest
        fields = 'group_id'


class GroupsResponseSerilizer(serializers.ModelSerializer):
    class Meta:
        model = GetGroupsResponse
        fields = ('group_id', 'title', 'members_count')
