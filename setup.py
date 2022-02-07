from setuptools import setup, find_packages
import os

def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()

VERSION="0.0.1"
DESCRIPTION="A tool for performing reconnaissance on web targets in Python."
LONG_DESCRIPTION="A tool for finding subdomain and directory information for various web targets."

setup(
    name='r3c0n',
    version=VERSION,
    license='MIT',
    license_files=["LICENSE"],
    author='Gacoka Mbui',
    author_email='<markgacoka@gmail.com>',
    description=DESCRIPTION,
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    url="https://github.com/markgacoka/r3c0n",
    download_url="https://github.com/markgacoka/r3c0n/releases",
    packages=find_packages('r3c0n'),
    install_requires=[''],
    py_modules=['r3c0n'],
    keywords='cybersecurity, reconnaissance, scanning, automation',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Security"
    ]
)