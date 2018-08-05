from setuptools import setup

setup(name='schleppy',
      version='0.1',
      description='Utilities for traversing and transforming data structures',
      long_description='Collection of simple functions to ease the burden of reading and shaping data',
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Data Processing :: path',
      ],
      keywords='dict list path dot notation',
      url='http://github.com/bradodarb/schleppy',
      author='Brad Murry',
      license='MIT',
      packages=['schleppy'],
      include_package_data=True,
      zip_safe=False)