from setuptools import setup

setup(
    name='messenger-api',
    packages=['messenger_api'],
    license='The MIT License (MIT)',
    version='0.0.1',
    description='Python client for FB Messenger Platform Bot',
    long_description=open('README.md').read(),
    author='Rohit Ahuja',
    author_email='rahuja95@gmail.com',
    url='https://github.com/rohitahuja',
    keywords='facebook messenger api',
    install_requires=['requests']
)
