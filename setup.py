from setuptools import setup, find_packages

# Read the long description from the README file
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

# Package metadata
__version__ = "0.0.4"
REPO_NAME = "mongodbconnectorpkg"
PKG_NAME = "databaseautomation"
AUTHOR_USER_NAME = "sudheerpulapa"
AUTHOR_EMAIL = "sudheerpulapa@gmail.com"

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
    install_requires=[
        "pymongo>=3.11.0",
        # Add other dependencies here
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "flake8>=3.8.0",
            "black>=20.8b1",
            # Add other development dependencies here
        ],
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

