from setuptools import setup , find_packages
from typing import List

def get_requirements() -> List[str] : 

    requirement_lst:List[str] = []
    try:
        with open('requirements.txt' , 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement  = line.strip()
                # ignore empty lines and -e.
                if requirement and requirement != '-e .' :
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("Hey! , The requirements.txt file is not found")

    return requirement_lst

setup(
    name="Network Security",
    version="0.0.1" ,
    author="Harsh Upadhyay",
    author_email="harshupadhyayofficial5@gmail.com" ,
    packages = find_packages() ,
    install_requires  = get_requirements()
)

