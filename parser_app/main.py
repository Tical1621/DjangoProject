import requests
from parser_app.auth_data import token


def get_groups_from_vk_api(groups_ids):
    groups_qp = ','.join([str(x) for x in groups_ids])  # list comprehension
    url = f"https://api.vk.com/method/groups.getById?group_ids={groups_qp}&fields=name,members_count&access_token={token}&v" \
          f"=5.131"
    req = requests.get(url)
    src = req.json()
    print(src)
    return src["response"]





