#!/usr/bin/env python3
from setuptools import find_packages, setup

setup(
    name='customer-api',
    version='0.1.0',
    description="",
    include_package_data=True,
    install_requires=[
        'flask==2.3.2',
        'Flask-Mail==0.9.1',
        'Flask-SQLAlchemy==2.4.0',
        'Flask-WTF==0.14.2',
        'pymysql==0.9.3',
        'WTForms==2.2.1'
    ]
)
