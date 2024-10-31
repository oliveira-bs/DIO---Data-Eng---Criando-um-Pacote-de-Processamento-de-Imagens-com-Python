from setuptools import find_packages, setup

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="edge_detector",
    version="0.0.1",
    author="bruno_oliveira",
    author_email="oliveira.email.pro@gmail.com",
    description="Software that implements edge detection in a simple and modular way, demonstrating how to use OpenCV in Python.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oliveira-bs/DIO---Data-Eng---Criando-um-Pacote-de-Processamento-de-Imagens-com-Python",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.10',
)
