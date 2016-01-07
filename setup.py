from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='incf.countryutils',
      version=version,
      description="A convenience API for transformations between different ISO 3166 country codes.",
      long_description=open(os.path.join("incf", "countryutils", "README.txt")).read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords="Python 'ISO 3166' 'country codes'",
      author='Raphael Ritz',
      author_email='raphael.ritz@incf.org',
      url='',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['incf'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
