from setuptools import setup

setup(
    name='messenger-platform',
    packages=['messenger_platform'],
    license='The MIT License (MIT)',
    version='0.0.1',
    description='Python client for FB Messenger Platform',
    long_description=open('README.md').read(),
    author='Rohit Ahuja',
    author_email='rahuja95@gmail.com',
    url='https://github.com/rohitahuja/messenger-platform',
    keywords='facebook messenger platform wrapper',
    install_requires=['requests']
)
