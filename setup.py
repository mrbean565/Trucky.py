from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="trucky.py",
    version="1.0.0.0",
    description="Simple API Wrapper for the Trucky API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrbean565/Trucky.py",
    author="mrbean565",
    author_email="bart6uj@gmail.com",
    license="GNU",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    keywords="api wrapper trucky",
    python_requires=">=3.7",
    packages=find_packages(),
    install_requires=[],
)
