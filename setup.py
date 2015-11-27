from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='IClojureKernel',
    version='0.1.0',
    description='Simple wrapper around Leiningen to support Clojure in Jupyter (IPython)',
    long_description=long_description,
    url='https://github.com/withrocks/iclojurekernel',
    author='withrocks',

    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='development deployment release',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['pexpect', 'ipykernel'],

    # $ pip install -e .[dev,test]
    extras_require={
        'dev': [],
        'test': [],
    },

    entry_points={
        'console_scripts': [
            'iclojurekernel-start=iclojurekernel.main:main',
        ],
    },
)

