from setuptools import setup, find_packages
from typing import List


# create variables. It should with be in UPPERCASE

PROJECT_NAME = 'project-structure-ewb'
VERSION = '0.0.1'
DESCRIPTION = 'This is the machine learning project with modular coding and skeleton'
AUTHOR_NAME = 'mohit kumar'
AUTHOR_EMAIL = 'mohit@python.md'

# REQUIREMENTS_FILE_NAME = requirements.txt

# def get_requirements_list()-> List(str):
#     with open(REQUIREMENTS_FILE_NAME) as requirements_file:
#         requirement_list = requirements_file.readlines()
#         requirement_list = [for libraries in requirement_list]
    
    
    
    

setup(
    name = PROJECT_NAME,
    version = VERSION,
    description = DESCRIPTION,
    author = AUTHOR_NAME,
    author_email = AUTHOR_EMAIL,
    url = 'https://github.com/mkr9395',
    # packages = find_packages(where='src'), # find packages inside src folder i.e __init__.py file of src
    # install_requires = get_requirements_list(), # with the help of requirements.txt file we will install this setup file using "-e ."
    
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)   