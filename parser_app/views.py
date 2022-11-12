from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from main import get_groups_from_vk_api
from parser_app.models import GroupsModel
from parser_app.serializers import GroupsSerializer


@csrf_exempt
def get_groups(request):
    if request.method == 'GET':
        try:
            groups = GroupsModel.objects.all()
            groups_serializer = GroupsSerializer(groups, many=True)
            return JsonResponse(groups_serializer.data, safe=False)
        except GroupsModel.DoesNotExist:
            group = None
        if group is None:
            group_json = get_groups_from_vk_api()
            group_serializer = GroupsSerializer(data=group_json)
            grp = GroupsModel(pk=group_json['id'], title=group_json['name'], members_count=group_json['members_count'])
            grp.save()
            GroupsModel.objects.create(pk=group_json["id"], title=group_json["name"], users_count=group_json["members_count"])

