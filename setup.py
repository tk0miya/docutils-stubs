from setuptools import setup
import os

def find_stubs(package):
    stubs = []
    for root, dirs, files in os.walk(package):
        for file in files:
            path = os.path.join(root, file).replace(package + os.sep, '', 1)
            stubs.append(path)
    return {package: stubs}

setup(
    name='docutils-stubs',
    version='0.0.2',
    description='PEP 561 type stubs for docutils',
    url='https://github.com/tk0miya/docutils-stubs',
    author='Takeshi KOMIYA',
    author_email='i.tkomiya@gmail.com',
    packages=['docutils-stubs'],
    install_requires=['docutils==0.14'],
    package_data=find_stubs('docutils-stubs'),
    zip_safe=False,
)
