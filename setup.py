from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='dblpy-lib',
    packages=find_packages(include=['dblpy']),
    version='0.1.3',
    description='A wrapper for dblp.org search api',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Benedikt Maria Beckermann',
    author_email='hello@benedikt.click',
    url='https://github.com/greenBene/dblpy',
    license='CC0 1.0 Universal',
    install_requires=['requests~=2.27.1'],
    test_suite='tests'
)