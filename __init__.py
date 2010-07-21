"""
Built upon nose.
This copy is a personal bug fix and new feature fork.
"""
from nose.core import collector, main, run, run_exit, runmodule
from nose.exc import SkipTest, DeprecatedTest
from nose.tools import with_setup

__author__ = 'Jason Pellerin, Anthony Long'
__versioninfo__ = (0, 11, 5)
__version__ = '.'.join(map(str, __versioninfo__))
__all__ = [
    'main', 'run', 'run_exit', 'runmodule', 'with_setup',
    'SkipTest', 'DeprecatedTest', 'collector'
    ]
