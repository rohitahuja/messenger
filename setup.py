from setuptools import setup

setup(
    name='messenger',
    package_dir={
        'messenger': 'messenger',
        'messenger.send_api': 'messenger/send_api',
        'messenger.thread_settings': 'messenger/thread_settings',
        'messenger.user_profile': 'messenger/user_profile'
    },
    packages=[
        'messenger',
        'messenger.send_api',
        'messenger.thread_settings',
        'messenger.user_profile',
    ],
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
