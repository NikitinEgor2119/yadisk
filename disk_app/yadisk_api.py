import requests


def get_public_resource(public_key):
    url = f"https://cloud-api.yandex.net/v1/disk/public/resources?public_key={public_key}"
    all_items = []
    params = {"limit": 100}

    while url:
        response = requests.get(url, params=params)
        data = response.json()
        items = data.get("_embedded", {}).get("items", [])
        all_items.extend(items)
        url = data.get("_embedded", {}).get("next", None)

    return {"items": all_items}