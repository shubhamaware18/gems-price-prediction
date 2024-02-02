from setuptools import find_packages, setup
from typing import List

"""HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements"""


setup(
    name='DimondPricePrediction',
    version='0.1.0', 
    description='This is the demo project developed on the concept of MLOps',
    author='Shubham Aware',
    author_email='awareshubham1996@gmail.com',
    install_requires=["scikit-learn", "pandas", "numpy"],
    packages=find_packages(),
    license=''
)