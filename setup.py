from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='servercraft',
    version='0.0.2',
    description='Use django to build an online server',
    long_description=long_description,
    url='',
    author='Feng Zhang',
    author_email='15110700005@fudan.edu.cn',
    license='Apache-2.0',
    install_requires=['django==1.8.7'],
    classifiers=[
        'Development Status :: 3 - Alpha',      
        'Programming Language :: Python :: 2.7',
        
    ],

    
    keywords='django',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    extras_require={
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

    package_data={
        'servercraft': ['package_data.dat'],
    },

    entry_points={
        'console_scripts': [
            'servercraft=servercraft:main',
        ],
    },
)
