from setuptools import setup, find_packages

setup(
    name='messenger',
    packages=find_packages(),
    license='The MIT License (MIT)',
    version='0.0.1',
    description='Python client for FB Messenger Platform',
    long_description=open('README.md').read(),
    author='Rohit Ahuja',
    author_email='rahuja95@gmail.com',
    url='https://github.com/rohitahuja/messenger',
    keywords='facebook messenger platform wrapper',
    install_requires=['requests']
)
