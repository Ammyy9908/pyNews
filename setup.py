from setuptools import setup



with open("README.md","r") as file:
    long_description = file.read()

setup(
    name="pyNewsApi",
    version="0.0.3",
    description="This module returns Latest News by category",
    long_description = long_description,
    long_description_content_type="text/markdown",
    py_modules = ["pyNewsApi"],
    package_dir={'':'src'},
    author="Sumit",
    author_email="sb78639@gmail.com",
    url="https://github.com/Ammyy9908/pyNews",
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent"
    ],
    install_requires = ["requests"],
    license = "GNU General Public License v2 or later (GPLv2+)",
    platform='PLatform Independent',
    extras_require = {
        "dev":["pytest>=3.7"]
    }
)
