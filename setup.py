from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='urlock',
    version='0.1',
    description='Library for connecting to a running Urbit ship',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='David Kerschner',
    author_email='dkerschner@gmail.com',
    keywords=['urlock', 'urbit'],
    url='https://github.com/baudtack/urlock',
    download_url='https://pypi.org/project/urlock/'
)

install_requires = [
    'datetime',
    'random',
    'json',
    'requests',
    'sseclient'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)