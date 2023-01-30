import requests


class Vkontakte:

    def __init__(self, token, id):
        self.token = token
        self.id = id

    def upload_disk(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {
            'owner_id': self.id,
            'album_id': 'profile',
            'extended': '1',
            'photo_sizes': '1',
            'count': '5',
            'access_token': self.token,
            'v': '5.131'
        }
        response = requests.get(url=url, params=params)
        return response.json()

    def list_max_foto(self):
        list_foto = self.upload_disk()['response']['items']
        file_name = list()
        json_list = list()

        for foto in list_foto:
            size_dict = {'s': 1, 'm': 2, 'o': 3, 'p': 4, 'q': 5, 'r': 6, 'x': 7, 'y': 8, 'z': 9, 'w': 10}
            file_url = max(foto['sizes'], key=lambda x: size_dict[x['type']])
            name = foto['likes']['count']
            if name in file_name:
                name = f"{foto['likes']['count']}_{foto['date']}"
            file_name.append(name)
            json_file = {'file_name': f'{name}.jpg', 'size': file_url['type'], 'url': file_url['url']}
            json_list.append(json_file)
        return json_list
