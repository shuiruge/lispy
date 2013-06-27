from setuptools import setup, find_packages

setup(
    name='lispy',
    version='0.0.1',
    description='A configurable LISP dialect that can call python code',
    long_description=open('README.md').read(),
    author='Adam Haney',
    author_email='adam.haney@akimbo.io',
    download_url='https://github.com/adamhaney/lispy/downloads',
    tests_require=[
        'nose==1.3.0'
    ],
    test_suite='lispy.tests.tests',
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={'console_scripts': ['lispy=lispy:cli']},
    packages=['lispy']
)