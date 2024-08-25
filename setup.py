from setuptools import setup, find_packages
from typing import List

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()     
   

_version_ = "0.0.16"
REPO_NAME = "mongodbconnector"
PKG_NAME= "databaseautomation"
AUTHOR_USER_NAME = "Pabitra-Biswas"
AUTHOR_EMAIL = "p.pabitrabiswas02@gmail.com"

setup(
    name=PKG_NAME,
    version=_version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A python package for connecting with database.",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    )






# - name: Publish Python Package
#   uses: pypa/gh-action-pypi-publish@release/v1
#   with:
#     password: ${{ secrets.PYPI_TOKEN }}
#     repository-url: https://upload.pypi.org/legacy/
#     # Use the commit SHA for reference or tagging
#     commit-sha: b4bd8ea94bfefe02b247434b6f81323f6fbbea9c
