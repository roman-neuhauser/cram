#!/usr/bin/env python

import sys
from distutils.core import setup, Command

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

class test(Command):
    description = 'run test suite'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import doctest
        import cram
        failures, tests = doctest.testmod(cram)
        sys.stdout.write('doctests: %s/%s passed\n' % (tests - failures, tests))
        cram.main(['-v', 'tests'])

setup(
    author='Brodie Rao',
    author_email='brodie@bitheap.org',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Unix Shell',
        'Topic :: Software Development :: Testing',
    ],
    cmdclass={'build_py': build_py, 'test': test},
    description='',
    download_url='http://bitheap.org/cram/cram-0.1.tar.gz',
    keywords='automatic functional test framework',
    license='GNU GPL',
    long_description="""
Cram is a testing framework for command line applications based on
Mercurial_'s `unified test format`_.

.. _Mercurial: http://mercurial.selenic.com/
.. _unified test format: http://www.selenic.com/blog/?p=663
""",
    name='cram',
    py_modules=['cram'],
    scripts=['scripts/cram'],
    url='http://bitheap.org/cram/',
    version='0.1',
)