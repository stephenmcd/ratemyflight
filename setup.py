
from setuptools import setup, find_packages

from ratemyflight import __version__ as version


setup(

    name="ratemyflight",
    version=version,
    author="Stephen McDonald",
    author_email="stephen.mc@gmail.com",
    description="",
    long_description=open("README.rst").read(),
    license="BSD",
    url="http://ratemyflight.org/",
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),

    entry_points="""
        [console_scripts]
        ratemyflight=ratemyflight.scripts.create_project:create_project
    """,

    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI",
        "Topic :: Software Development :: Libraries :: "
                                            "Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ])

