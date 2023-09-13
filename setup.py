from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "recommendation system for books"
AUTHOR_USER_NAME = "Pranav Tondgaonkar"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Pranav Tondgaonkar",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pranavtondgaonkar/REC-SYS-BOOK",
    author_email="pranavrelds@gmail.com",
    packages=find_packages(),
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
