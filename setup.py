"""

servercraft-0.0.1

"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='servercraft',
    version='0.0.1',
    description='Use django to build an online server',
    long_description=long_description,
    url='',
    author='Feng Zhang',
    author_email='15110700005@fudan.edu.cn',
    license='GPL',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: ',
        'Topic :: ',

        
        'License :: OSI Approved :: GPL License',


        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
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

    #data_files=[('my_data', ['data/data_file'])],
    entry_points={
        'console_scripts': [
            'servercraft=servercraft:main',
        ],
    },
)
