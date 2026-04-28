import os
import requests
import ctypes

imagesPath = os.path.join(os.path.expanduser("~"), "Desktop")

def changeWallpaper(imagePath):
    imagePath = os.path.abspath()
    ctypes.windll.user32.SystemParametersInfoW(20, 0, imagePath, 3)

def downloadImages(folder = "links"):
    os.makedirs(folder, exist_ok = True)

    for i in range(5):
        response = requests.get("https://api.waifu.im/images?IsNsfw=True")
        response.raise_for_status()

        data = response.json()
        image = data["items"][0]

        url = image["url"]
        archive_name = url.split("/")[-1]
        path = os.path.join(folder, archive_name)

        img_response = requests.get(url, stream= True)
        img_response.raise_for_status()

        with open(path, "wb") as f:
            for chunk in img_response.iter_content(chunk_size=8192):
                f.write(chunk)
        print("salvo")

downloadImages()
changeWallpaper(imagesPath)