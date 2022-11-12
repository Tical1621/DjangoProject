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
        for group in current_page.iterator():
            group_json = get_groups_from_vk_api(group.__getattribute__('id'))
            grp = GroupsModel(pk=group_json['id'], name=group_json['name'], members_count=group_json['members_count'])
            grp.save()
            print('succesfully updated data to id:', group.__getattribute__('id'))
        offset += page_size
