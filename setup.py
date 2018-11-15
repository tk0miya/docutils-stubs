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
    version='0.0.10',
    description='PEP 561 type stubs for docutils',
    long_description=open('README.rst').read(),
    url='https://github.com/tk0miya/docutils-stubs',
    author='Takeshi KOMIYA, cocoatomo',
    author_email='i.tkomiya@gmail.com, cocoatomo77@gmail.com',
    packages=['docutils-stubs'],
    install_requires=['docutils==0.14'],
    python_requires=">=3.5",
    package_data=find_stubs('docutils-stubs'),
    zip_safe=False,
)
