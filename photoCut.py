import cv2
import base64
import numpy as np


def base2opencv(base64_code):
    img_data = base64.b64decode(base64_code.encode())
    img_array = np.fromstring(img_data, np.uint8)
    img = cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)
    return img


def checkcutcur(height, width, x1, x2, y1, y2):
    if(x2 < x1 or y2 < y1):
        return False
    if(x2 > width or y2 > height):
        return False
    return True


def photocut(jsonData, base64Code):
    length = len(jsonData)
    img = base2opencv(base64Code)
    height = img.shape[0]
    width = img.shape[1]
    croppedArray = []
    for i in range(0, length):
        x1 = jsonData[i]['x1']
        x2 = jsonData[i]['x2']
        y1 = jsonData[i]['y1']
        y2 = jsonData[i]['y2']
        if(checkcutcur(height, width, x1, x2, y1, y2) != True):
            res = {
                "errMsg": "error",
                "detail": "Crop position is not correct."
            }
            return res
        cropped = img[y1:y2, x1:x2]
        buffer = cv2.imencode('.png', cropped)[1]
        croppedArray.append(base64.b64encode(buffer).decode())

    res = {
        "errMsg": "successful",
        "resPhoto": croppedArray
    }
    return res