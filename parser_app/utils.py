from urllib.parse import urlparse, parse_qs


def parse_url(request):  #parsing groupId from request url
    url = request.get_full_path()
    group_id = parse_qs(urlparse(url).query)
    return group_id
