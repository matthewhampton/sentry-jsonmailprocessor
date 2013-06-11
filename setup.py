#!/usr/bin/env python
from setuptools import setup, find_packages

install_requires = [
    'sentry>=5.0.21',
    ]

setup(
    name='sentry-jsonmailprocessor',
    version='0.0.2',
    author='Justin C',
    description='A Sentry extension that forwards Sentry events via SMTP in JSON format.',
    packages=find_packages(exclude=['test']),
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    entry_points={
        'sentry.plugins': [
            'jsonmailprocessor = sentry_jsonmailprocessor.models:JsonMailProcessor',
            ],
        },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
