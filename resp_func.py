import requests

def vk_api_resp(method, *arr):
    import user_data
    req = "https://api.vk.com/method/" + method + '?'
    if method == "friends.get":
        req += f'user_id={user_data.user_id}&'
    elif method == "users.get":
        pass
    req += f'access_token={user_data.ac_to}&'
    req += f'{user_data.version}&'
    for i in arr:
        req = req + i + '&'
    return requests.get(req)