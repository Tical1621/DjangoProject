from celery import shared_task
from celery.utils.log import get_task_logger
from parser_app.models import GroupsModel
from parser_app.main import get_groups_from_vk_api

logger = get_task_logger(__name__)


@shared_task
def refresh_groups():
    groups_qs = GroupsModel.objects.all()
    groups_count = groups_qs.count()
    groups_qs_to_paginate = groups_qs.order_by('id')
    page_size = 500
    offset = 0
    while offset < groups_count:
        current_page = groups_qs_to_paginate[offset:offset + page_size]
        group_json = get_groups_from_vk_api(current_page.values_list('pk', flat=True))  #flat=true return array of ids
        for group in group_json:
            grp = GroupsModel(pk=group['id'], name=group['name'], members_count=group['members_count'])
            grp.save()
            print('succesfully updated data to id:', grp.pk)
        offset += page_size
