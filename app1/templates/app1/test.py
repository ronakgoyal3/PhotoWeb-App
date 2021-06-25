from PIL import Image
import requests
from io import BytesIO
import cv2
import numpy as np




# METHOD #1: OpenCV, NumPy, and urllib
def url_to_image(url):
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image = np.uint8(image)
    # image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return(image)

if __name__ == "__main__":
    next="https://www.readsplash.com/wp-content/uploads/2021/03/10-Differences-Between-North-and-South-Korea.jpg"
    img=url_to_image(next)
    img = np.uint8(img)
    cv2.imshow('test',img)
    cv2.waitKey(0)
