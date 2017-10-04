# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "netapp.santricity"
VERSION = "1.1"



# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.10", "six >= 1.9", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Python SDK for accessing NetApp Santricity Web Services",
    author="NetApp",
    license = "The Clear BSD License",
    author_email="ng-hsg-engcustomer-esolutions-support@netapp.com",
    url="https://github.com/NetApp/santricity-webapi-pythonsdk",
    keywords=["Swagger", "NetApp", "Santricity"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    NetApp E-Series SANtricity Python SDK for Web Services
    """
)









