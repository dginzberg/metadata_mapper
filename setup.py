#! /user/bin/env python
from importlib_metadata import entry_points
from setuptools import find_namespace_packages, setup, find_packages
from os.path import join, dirname

setup(
    # ...
    name="metadata_mapper",
    version="1.0",
    description="Ingesting and mapping metadata files",
    license="ACA",
    homepage="https://github.com/ACA-Group/ecomms-scripts/tree/MB/feature/CAT-3908-expanded-metadata-handling/UAT/onBox/catelas/shared/scripts/metadata_mapper",
    package_dir={
        "mapper_pkg": "metadata_mapper/mapper_pkg",
        "utils_pkg": "metadata_mapper/utils_pkg",
        "types_pkg": "metadata_mapper/mapper_pk/types_pkg",
    },
    packages=(
        find_packages(where="metadata_mapper", include="*_pkg")
        + find_packages(where="metadata_mapper.mapper_pkg", include="*_pkg")
    ),
    install_requires=[
        "pytest",
        "pytz",
        "psutil",
        "black",
        "importlib_metadata",
        "xmltodict",
        "wheel"
    ],
    long_description=open(join(dirname(__file__), "README.md")).read(),
    entry_points={
        "console_scripts": [
            "metadata_mapper = mapper_pkg.__main__:run",
        ],
    },
    # ...
)
