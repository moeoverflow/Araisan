# This is purely the result of trial and error.

import sys
import codecs

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import araisan

class PyTest(TestCommand):
    # `$ python setup.py test' simply installs minimal requirements
    # and runs the tests with no fancy stuff like parallel execution.
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = [
            '--doctest-modules', '--verbose',
            './araisan', './tests'
        ]
        self.test_suite = True

    def run_tests(self):
        import pytest
        sys.exit(pytest.main(self.test_args))


tests_require = [
    # Pytest needs to come last.
    # https://bitbucket.org/pypa/setuptools/issue/196/
    'pytest',
    'mock',
]

extras_require={}

install_requires = [
    'pyyaml',
]

devstatus = 'Development Status :: 5 - Production/Stable'
if 'b' in araisan.__version__:
    devstatus = 'Development Status :: 4 - Beta'
elif 'a' in araisan.__version__:
    devstatus = 'Development Status :: 3 - Alpha'

setup(
    name='araisan',
    version=araisan.__version__,
    description=araisan.__doc__.strip(),
    long_description='',
    url='https://github.com/moeoverflow/Araisan',
    download_url='https://github.com/moeoverflow/Araisan',
    author=araisan.__author__,
    author_email='0xbbc@0xbbc.com',
    license=araisan.__licence__,
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'araisan = araisan.__main__:main',
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    tests_require=tests_require,
    cmdclass={'test': PyTest},
    classifiers=[
        devstatus,
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Topic :: Terminals',
        'Topic :: Utilities'
    ],
)