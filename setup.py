'''
The steup.py file is an essential part of packaging and
distributing python projects. It is used by setuptools
(or distutils in older python versions) to define the configuration
of your project, such as metadata, dependencies and more
'''

from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    '''
    This function will return the list of requirements.
    ''' 
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines from the file
            lines = file.readlines()
            #Process each line
            for line in lines:
                requirement = line.strip()
                #Ignore empty lines and -e.
                if requirement and requirement != '-e.':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_list

setup(
    name = "NetworkDataSecurity",
    version = "0.0.1",
    author = "Nikhil Doye",
    author_email = "doye.n@northeastern.edu",
    packages = find_packages(),
    install_requires = get_requirements()
)   