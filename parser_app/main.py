import requests
from auth_data import token
from db import insert_group



def get_groups(group_id):
    url = f"https://api.vk.com/method/groups.getById?group_id={group_id}&fields=name,members_count&access_token={token}&v" \
          f"=5.131"
    req = requests.get(url)
    src = req.json()
    data = src["response"][0]
    group = data['id']
    members = data['members_count']
    name = data['name']
    insert_group(group, members, name)


def main():
    group_id = input("id: ")
    get_groups(group_id)


if __name__ == '__main__':
    main()
