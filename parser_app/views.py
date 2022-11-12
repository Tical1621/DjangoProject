from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from parser_app.main import get_groups_from_vk_api
from parser_app.models import GroupsModel
from parser_app.serializers import GroupsSerializer
from django.http import HttpResponseNotAllowed
from django.core.cache import cache


@csrf_exempt
def get_groups(request, group_id):
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    try:
        #а вот тут бы ретёрнить из кэша до обращения к бд по id if possible
        group = GroupsModel.objects.get(pk=group_id)  #query to db object.equals(ORM.Api)
        groups_serializer = GroupsSerializer(group)
        cache.set(f'group_{group_id}', groups_serializer.data)
        return JsonResponse(cache.get(f'group_{group_id}'))
    except GroupsModel.DoesNotExist:
        group = None
    if group is None:
        group_json = get_groups_from_vk_api(group_id)
        grp = GroupsModel(pk=group_json['id'], name=group_json['name'], members_count=group_json['members_count'])
        grp.save()
        group_serializer = GroupsSerializer(grp)
        cache.set(f'group_{group_id}', group_serializer.data)
        return JsonResponse(cache.get(f'group_{group_id}'))

