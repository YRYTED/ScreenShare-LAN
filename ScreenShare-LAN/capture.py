import mss
import cv2
import numpy as np
from PIL import Image
import io


sct = mss.mss()


def capture_screen():
    monitor = sct.monitors[1]

    screenshot = sct.grab(monitor)

    img = np.array(screenshot)

    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)

    _, buffer = cv2.imencode(
        ".jpg",
        img,
        [cv2.IMWRITE_JPEG_QUALITY, 60]
    )

    return buffer.tobytes()