# main.py
import os

from edge_detector.detector import EdgeDetector
from edge_detector.utils import save_image


def main():
    # Caminho da imagem a ser processada
    # Substitua pelo caminho da sua imagem
    image_path = 'data/input/example.jpg'
    edge_detector = EdgeDetector(image_path)

    # Detecta bordas
    edges = edge_detector.detect_edges()

    # Define o caminho para salvar a imagem de bordas
    output_path = 'data/output/edges_output.jpg'

    # Verifica se o diretório é gravável
    if os.access(os.path.dirname(output_path) or '.', os.W_OK):
        save_image(edges, output_path)
        print(f'Imagem de bordas salva em: {output_path}')
    else:
        print('Erro: Não é possível salvar a imagem no caminho indicado.')

    # Mostra as imagens
    edge_detector.show_images(edges)


if __name__ == '__main__':
    main()
