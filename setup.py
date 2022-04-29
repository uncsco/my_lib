from setuptools import setup
#import os

VERSION = "0.1"

'''
def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()
'''

setup(
    name="My Lib",
    description="Brief description...",
    #long_description=get_long_description(),
    #long_description_content_type="text/markdown",

    license="[TBC] Apache License, Version 2.0",
    version=VERSION,
    packages=["my_lib"],
    install_requires=["pydantic"], ## `pydantic`
    extras_require={"test": ["pytest"]},
    python_requires=">=3.6",
)