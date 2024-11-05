from setuptools import find_packages, setup
from typing import List

HYPER_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    Returns a list of requirements from the specified file_path.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if HYPER_E_DOT.strip() in requirements:
            requirements.remove(HYPER_E_DOT.strip())
    
    return requirements

setup(
    name = 'HealthCare Diabetes',
    version= '0.0.1',
    author= 'Vinayak Anadinni',
    author_email= 'vinayak14anadinni@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)