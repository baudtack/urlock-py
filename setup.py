import os
import setuptools

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    name = "urlock",
    version = "0.1.12",
    author = "David Kerschner",
    author_email = "dkerschner@gmail.com",
    description = "Library for talking to a running Urbit ship",
    license = "MIT",
    keywords = "urbit urlock",
    url = "http://github.com/baudtack/urlock-py",
    packages=setuptools.find_packages(),
    install_requires=['requests', 'sseclient-py'],
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
)