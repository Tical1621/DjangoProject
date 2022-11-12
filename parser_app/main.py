import requests
from auth_data import token


def get_groups_from_vk_api(group_id):
    url = f"https://api.vk.com/method/groups.getById?group_id={group_id}&fields=name,members_count&access_token={token}&v" \
          f"=5.131"
    req = requests.get(url)
    src = req.json()
    data = src["response"][0]
    return data  #так можно написать?

