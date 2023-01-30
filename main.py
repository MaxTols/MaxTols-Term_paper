import json
from vk import Vkontakte
from ya import Yandex

with open('token_vk.txt', 'r') as file_object:
    token_vk = file_object.read().strip()

if __name__ == '__main__':
    id_vk = input('Enter user id: ')
    token_ya = input('Enter your Yandex token: ')
    vk = Vkontakte(token_vk, id_vk)
    json_list = vk.list_max_foto()

    folder = 'Term_paper_1'
    ya = Yandex(token_ya)
    ya.create_folder(folder)

    for file in json_list:
        ya.uploads(file['url'], f"{folder}/{file['file_name']}")

    with open('file.json', 'w') as f:
        json.dump(json_list, f, indent=2)
