import math
import urllib.request
from cv2 import resize
import pyautogui
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from PIL import Image
from resizeimage import resizeimage
import time

load_dotenv()

API_KEY = os.getenv('API_KEY')
SEARCH_ENGINE_ID = os.getenv('SEARCH_ENGINE_ID')

# def scrollDown():
#     pyautogui.scroll(-10)

# def googleSearch(query, api_key, cse_id, **kwargs):
#     service = build("customsearch", "v1", developerKey=api_key)
#     res = service.cse().list(q=query, cx=cse_id, **kwargs).execute()
#     return res['items']

# def downloadImage(emp):
#     opener=urllib.request.build_opener()
#     opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
#     urllib.request.install_opener(opener)

#     inp = int(input('Download index: '))
#     filename = f"images\content.jpg"
#     image_url = emp[inp]
#     urllib.request.urlretrieve(image_url, filename)

# results = googleSearch(input('Enter query: '), API_KEY, SEARCH_ENGINE_ID, num=10)
# emp = []
# for result in results:
#     try:
#         src = result['pagemap']['cse_image'][0]['src']
#         emp.append(src)
#         print(f"[{emp.index(src)}] {result['title']} - {src}")
#     except:
#         continue

# downloadImage(emp)

image = Image.open('images\content.jpg').convert("RGB")
# image.thumbnail((75, 75), Image.ANTIALIAS)
image = resizeimage.resize_thumbnail(image, (75, 75))
# image.show()
pixelList = list(image.getdata())
# print(pixelList)

# colorList = [
#     {(0, 0, 0), (890, 73)},
#     {(255, 255, 255), (890, 103)},
#     {(127, 127, 127), (917, 70)},
#     {(136, 0, 22), (946, 70)},
#     {(237, 27, 36), (973, 70)},
#     {(255, 127, 38), (997, 70)},
#     {(254, 242, 0), (1021, 70)},
#     {(35, 177, 77), (1053, 71)},
#     {(0, 163, 232), (1080, 73)},
#     {(63, 71, 204), (1108, 71)},
#     {(163, 73, 163), (1135, 71)},
#     {(195, 195, 195), (918, 103)},
#     {(185, 122, 87), (943, 105)},
#     {(253, 174, 201), (966, 103)},
#     {(255, 201, 13), (1025, 103)},
#     {(239, 227, 175), (1052, 98)},
#     {(181, 229, 29), (1082, 100)},
#     {(154, 217, 234), (1110, 100)},
#     {(112, 146, 191), (1137, 100)},
#     {(199, 191, 230), ()}
#             ]
colorList = [
    (0, 0, 0),
    (255, 255, 255),
    (127, 127, 127),
    (136, 0, 22),
    (237, 27, 36),
    (255, 127, 38),
    (254, 242, 0),
    (35, 177, 77),
    (0, 163, 232),
    (63, 71, 204),
    (163, 73, 163),
    (195, 195, 195),
    (185, 122, 87),
    (253, 174, 201),
    (255, 201, 13),
    (239, 227, 175),
    (181, 229, 29),
    (154, 217, 234),
    (112, 146, 191),
    (199, 191, 230)
            ]

def euclidianDistance(pixel, color):
    return math.sqrt(sum((pixel[i]-color[i])**2 for i in range(3)))

def similarColor(pixelList, colorList):
    newPixelList = []
    for pixel in pixelList:
        error = math.inf
        new_color = colorList[0]
        for color in colorList:
            if euclidianDistance(pixel, color) < error:
                error, new_color = euclidianDistance(pixel, color), color
        newPixelList.append(new_color)
    return newPixelList
        
newPixelList = similarColor(pixelList, colorList)
print(len(newPixelList))

time.sleep(2)
for i in range(20):
    x, y = pyautogui.position()
    pyautogui.click(x, y)
    x += 10
    print(x)

