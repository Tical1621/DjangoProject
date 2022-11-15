from django.http.response import JsonResponse
from parser_app.main import get_groups_from_vk_api
from parser_app.models import GroupsModel
from parser_app.serializers import GroupsSerializer
from django.http import HttpResponseNotAllowed, HttpResponseNotFound
from django.core.cache import cache
from asgiref.sync import sync_to_async


async def get_groups_async(request, group_id):  #cам по себе views equals(@Service/@Component)
    if request.method != 'GET':
        return HttpResponseNotAllowed(['GET'])
    resp = await cache.aget(f'group_{group_id}')
    if resp:
        return JsonResponse(resp)
    try:
        group = await GroupsModel.objects.aget(pk=group_id)  # query to db object.equals(ORM.Api) +async request to db
        groups_serializer = GroupsSerializer(group)
        await cache.aset(f'group_{group_id}', groups_serializer.data)
        return JsonResponse(await cache.aget(f'group_{group_id}'))
    except GroupsModel.DoesNotExist:
        group = None
    if group is None:
        try:
            group_json = (await sync_to_async(get_groups_from_vk_api)([group_id]))[0]
            grp = GroupsModel(pk=group_json['id'], name=group_json['name'], members_count=group_json['members_count'])
            await sync_to_async(grp.save)()
            group_serializer = GroupsSerializer(grp)
            await cache.aset(f'group_{group_id}', group_serializer.data)
            return JsonResponse(await cache.aget(f'group_{group_id}'))
        except (KeyError, AttributeError):
            return HttpResponseNotFound('group not found')
