#!/usr/bin/env python3
import setuptools


setuptools.setup(
    name="installa_facile",
    author="Carmine Zaccagnino",
    license="EUPL-1.2",
    url="https://github.com/carzacc/installa-facile-cli",
    description="generamento con indicazione grandezza",
    package_dir={"": "installa_facile"},
    scripts=["bin/ita"],
    packages=setuptools.find_packages("installa_facile"),
    include_package_data=True
)

