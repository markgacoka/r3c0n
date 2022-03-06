import pathlib
from setuptools import setup

# The directory containing this file
PATH = pathlib.Path(__file__).parent

# The text of the README file
README = (PATH / "README.md").read_text()

VERSION="1.2.4"
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
    long_description=README,
    long_description_content_type='text/markdown',
    url="https://github.com/markgacoka/r3c0n",
    download_url="https://github.com/markgacoka/r3c0n/releases",
    packages=['r3c0n', 'r3c0nutils', 'r3c0n.engines'],
    include_package_data=True,
    install_requires=['beautifulsoup4', 'requests', 'urllib3', 'yarl'],
    entry_points={
        "console_scripts": [
            "r3c0n=r3c0n.__main__:main"
        ]
    },
    keywords='cybersecurity, reconnaissance, scanning, automation',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Security"
    ]
)