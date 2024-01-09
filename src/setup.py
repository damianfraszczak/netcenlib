import re

from setuptools import setup, find_packages
from codecs import open
from os import path, read


def find_version(*path_parts):
    """Find the current version string."""
    version_file_contents = read(*path_parts)
    version_match = re.search(
        r'^__version__ = ["\'](?P<version>[^"\']*)["\']',
        version_file_contents,
        re.M,
    )
    if not version_match:
        raise RuntimeError("Unable to find version string.")
    version = version_match.group("version")
    return version

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(path.join(here, "requirements.txt"), encoding="utf-8") as f:
    requirements = f.read().splitlines()


setup(
    name="netcenlib",
    version=find_version("netcenlib", "version.py"),
    license="MIT",
    description="Network centrality library",
    url="https://github.com/damianfraszczak/nclib",
    author="Damian Frąszczak, Edyta Frąszczak",
    author_email="damian.fraszczak@wat.edu.pl",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    keywords="node_importance centrality_measures centrality complex-networks",
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    extras_require={
        "lint": [
            "bandit",
            "black",
            "flake8",
            "flake8-debugger",
            "flake8-docstrings",
            "flake8-isort",
            "mypy",
            "pylint",
        ],
    },
    packages=find_packages(
        exclude=["*.test"]
    ),
)
