from setuptools import setup, find_packages
from typing import List

# Function to parse requirements from a file
def parse_requirements(filename: str) -> List[str]:
    """Load requirements from a pip requirements file."""
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.read().splitlines()
    requirements = [line.strip() for line in lines if line.strip() and not line.startswith('#')]
    return requirements

# Read the long description from the README file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Package metadata
__version__ = "0.0.4"
REPO_NAME = "MLOps_Package"
PKG_NAME = "mongodbconnectorpkg"
AUTHOR_USER_NAME = "sudheerpulapa"
AUTHOR_EMAIL = "sudheerpulapa@gmail.com"

# Read requirements
install_requires = parse_requirements('requirements.txt')
dev_requires = parse_requirements('requirements_dev.txt')

# Enhanced setup configuration
setup(
    name=PKG_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Python package for connecting with databases.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
        "Source Code": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
        "Documentation": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}#readme",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        "dev": dev_requires,
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries",
        "Topic :: Database",
    ],
    python_requires='>=3.7',
    keywords="mongodb database automation python package",
)

