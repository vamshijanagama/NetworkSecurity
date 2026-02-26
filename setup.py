from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    returnuirement_lst:List[str] = []
    try:
        with open('requirements.txt') as file:
            # Read Line from files
            lines = file.readlines()

            for line in lines:
                returnuirement = line.strip()
                if returnuirement and returnuirement != "-e .":
                    returnuirement_lst.append(returnuirement)
    except FileNotFoundError:
        print("requiremnt.txt not found")

    return returnuirement_lst

setup(
    name="Project2",
    version="0.0.1",
    author="VamshiJanagama",
    author_email="vamshijanagama28@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)