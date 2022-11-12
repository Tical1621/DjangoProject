from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from parser_app.main import get_groups_from_vk_api
from parser_app.models import GroupsModel
from parser_app.serializers import GroupsSerializer
from django.http import HttpResponseNotAllowed


@csrf_exempt
def get_groups(request, group_id):
    if request.method != 'GET':
        return HttpResponseNotAllowed()
    try:
        group = GroupsModel.objects.get(pk=group_id)  #query to db object.equals(ORM.Api)
        groups_serializer = GroupsSerializer(group)
        return JsonResponse(groups_serializer.data)
    except GroupsModel.DoesNotExist:
        group = None
    if group is None:
        group_json = get_groups_from_vk_api(group_id)
        print(group_json)
        grp = GroupsModel(pk=group_json['id'], name=group_json['name'], members_count=group_json['members_count'])
        grp.save()
        group_serializer = GroupsSerializer(grp)
        return JsonResponse(group_serializer.data)

