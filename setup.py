from setuptools import find_packages, setup


PRJT_NAME = 'sample-ml-pipeline'
VERSION = '0.0.1'
AUTHOR = 'Manuel John'
EMAIL = 'manuelmathew39@gmail.com'


def get_requirements(file_path: str) -> list[str]:
    """
    This Function gets all the required libraries
    required in the project
    """

    HYPEN_E_DOT = "-e ."

    requirements = []

    with open(file=file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", ' ') 
                        for req in requirements
                        ]                       #replace \n from file

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

 #Build Package       
setup(name=PRJT_NAME, 
      version=VERSION, 
      author=AUTHOR, 
      author_email=EMAIL, 
      packages=find_packages(), 
      install_requires=get_requirements(file_path='requirements.txt')
      )