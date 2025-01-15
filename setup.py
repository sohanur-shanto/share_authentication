from setuptools import setup, find_packages

setup(
    name='shared_auth',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'djangorestframework',
        'PyJWT',
    ],
)