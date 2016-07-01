import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'requirements.txt')) as f:
    REQUIREMENTS = [line for line in iter(f) if not line.startswith('--')]

setup(name='trollcat',
      version='0.0.1',
      description='Trollcat Twetstorm',
      classifiers=[
        "Programming Language :: Python",
        ],
      url='',
      keywords='trollcat longcat',
      packages=find_packages(),
      include_package_data=True,
      scripts=['bin/trollcat'],
      zip_safe=False,
      install_requires=REQUIREMENTS,
      )
