# edge_detector/utils.py
import cv2


def save_image(image, file_path):
    cv2.imwrite(file_path, image)
