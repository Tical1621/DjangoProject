from celery import shared_task
from celery.utils.log import get_task_logger
from models import GroupsModel


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
        # Do work with the current_page
        offset += page_size
