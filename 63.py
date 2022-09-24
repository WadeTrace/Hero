                                    #Задание 1
import requests

ALL_SUPERHEROES_URL = "https://akabab.github.io/superhero-api/api/all.json"
SUPERHEROES_FOR_COMPARE = ["Hulk", "Captain America", "Thanos"]


def get_all_superheroes_info(url):
    all_superheroes_response = requests.get(url)
    all_superheroes_info = all_superheroes_response.json()
    return all_superheroes_info


def find_smartest_superhero(superheroes_list, all_superheroes_info):
    smartest_superhero = None
    smartest_superhero_intelligence = None

    for superhero in all_superheroes_info:
        if superhero["name"] in superheroes_list:
            superhero_intelligence = superhero["powerstats"]["intelligence"]
            if not smartest_superhero_intelligence or \
                    superhero_intelligence > smartest_superhero_intelligence:
                smartest_superhero = superhero["name"]
                smartest_superhero_intelligence = superhero_intelligence
                continue
            if superhero_intelligence == smartest_superhero_intelligence:
                smartest_superhero += ", " + superhero["name"]
    return smartest_superhero

def main():
    all_superheroes_info = get_all_superheroes_info(ALL_SUPERHEROES_URL)
    smartest_superhero = find_smartest_superhero(SUPERHEROES_FOR_COMPARE, all_superheroes_info)
    print(f"Самый умный супергерой {smartest_superhero}")

main()


                                                #задание 2

token = ""

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            "Content-Type": "application/json",
            "Authorization": f'OAuth {self.token}'
        }

    def upload(self, disk_file_path: str):
        upload_url = "https://cloud-api.yandex.net:443/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        respons = requests.get(upload_url, headers=headers, params=params)
        print(respons.json())
        return respons.json()

    def upload_file_disk(self, disk_file_path, name_file):
        link_dict = self.upload(disk_file_path=disk_file_path)
        href = link_dict["href"]
        response = requests.put(href, data=open(name_file, "rb"))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    uploader = YaUploader(token)
    result = uploader.upload_file_disk("Download/DZ.txt","ДЗ.txt")
    print(result)
