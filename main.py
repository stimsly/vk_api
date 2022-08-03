import info
import resp_func

responce = resp_func.vk_api_resp(info.method_friends)

if responce.status_code != 200:
    print("Error 200!")
    exit()
if "response" not in responce.json():
    print(responce.json()["error"]["error_msg"])
    exit()


data = responce.json()['response']
print("Количество ваших друзей:", data['count'])


ids = data["items"]
res_ids = set()
was_banned = 0
private_users = 0
mystery_users = 0
progress = 0
print("Началась обработка!")
for i in ids:

    progress += 1
    cur_friend_req = resp_func.vk_api_resp(info.method_friends, f'user_id={i}')
    cur_friend_req = cur_friend_req.json()
    
    if 'response' in cur_friend_req:
        for j in cur_friend_req['response']['items']:
            res_ids.add(j)
    elif cur_friend_req['error']['error_code'] == 30:
        private_users += 1
    elif  cur_friend_req['error']['error_code'] == 18:
        was_banned += 1
    else:
        mystery_users += 1

    if progress % 20 == 0:
        print("Обработанно пользователей:", progress)

print("Количество выявленных друзей друзей:", len(res_ids))
print("Количество приватных пользоватей:", private_users)
print("Количество забанненых пользователей:", was_banned)
print("Количество друзей у которых не удалось выявить статус:", mystery_users)


