import os
import re

from setuptools import find_packages, setup


def read(*path_parts):
    """Retrieve content of a text file."""
    file_path = os.path.join(os.path.dirname(__file__), *path_parts)
    with open(file_path) as file_obj:
        return file_obj.read()


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


setup(
    name="netcenlib",
    version=find_version("src", "netcenlib", "version.py"),
    license="MIT",
    description="Network centrality library",
    url="https://github.com/damianfraszczak/nclib",
    author="Damian Frąszczak, Edyta Frąszczak",
    author_email="damian.fraszczak@wat.edu.pl",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    keywords="node_importance centrality_measures centrality complex-networks",
    install_requires=[
        "networkx>=3.0",
        "numpy",
        "scipy",
    ],
    long_description=read("README.md"),
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
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
