from setuptools import find_packages, setup
from typing import List

HYPHEN_e_DOT = '-e .'
def get_requirements(file_path:str)-> List[str]:
    '''
    This function will return the requirements
    '''
    requirements = []
    with open(file=file_path) as temp_obj:
        requirements = temp_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
    
    if HYPHEN_e_DOT in requirements:
        requirements.remove(HYPHEN_e_DOT)

    return requirements

setup(

name= "MLproject_1",
version= "0.0.1",
author= "Vignesh",
author_email= "vigneshr1711@gmail.com",
packages= find_packages(),
install_requires = get_requirements('requirements.txt')



)