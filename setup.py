from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '1.0.0'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='kendall-w',
    version=__version__,
    description='Computes Kendall\'s coefficient of concordance',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/ugolbck/kendall-w',
    download_url='https://github.com/ugolbck/kendall-w/tarball/' + __version__,
    license='BSD',
    classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.5',
      'Programming Language :: Python :: 3.6',
      'Programming Language :: Python :: 3.7',
      'Programming Language :: Python :: 3.8',
      'Topic :: Scientific/Engineering :: Mathematics',
    ],
    keywords=['kendall', 'annotator', 'agreement', 'rank', 'metric'],
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Ugo Loobuyck',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='ugo.loobuyck@gmail.com'
)
