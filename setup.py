from setuptools import find_packages,setup


setup(
    name = 'boimetric user authentication',
    version = '0.0.1',
    author= 'giddy',
    author_email= 'oviemunooboro@gmail.com',
    packages= find_packages(),
    install_requires  = [l.strip for l in open('requirements.txt')] 
)