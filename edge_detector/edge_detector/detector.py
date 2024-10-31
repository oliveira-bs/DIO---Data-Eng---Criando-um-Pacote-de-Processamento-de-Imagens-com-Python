# edge_detector/detector.py
import cv2


class EdgeDetector:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    def detect_edges(self, low_threshold=50, high_threshold=150):
        # Converte a imagem para escala de cinza
        gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        # Aplica o detector de bordas Canny
        edges = cv2.Canny(gray_image, low_threshold, high_threshold)
        return edges

    def show_images(self, edges):
        cv2.imshow('Original Image', self.image)
        cv2.imshow('Edges', edges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
