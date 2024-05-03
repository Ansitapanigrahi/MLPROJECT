from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        lines = file_obj.readlines()
        requirements = [line.strip() for line in lines if line.strip() and line.strip() != HYPEN_E_DOT]
    return requirements

setup(
    name='MLPROJECT',
    version='0.0.1',
    author='Ansita',
    author_email='ansitapanigrahi@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
