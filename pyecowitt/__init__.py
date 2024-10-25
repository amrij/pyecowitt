""" Nothing to see here """
import sys

__version__ = "0.7"

__uri__ = 'https://github.com/amy/pyecowitt'
__title__ = "pyecowitt"
__description__ = 'Interface Library for Ecowitt Protocol'
__doc__ = __description__ + " <" + __uri__ + ">"
__author__ = 'André Rijkeboer'
__email__ = 'a.m.rijkeboer@am-rijkeboer.nl'
__license__ = "Apache 2.0"

__copyright__ = "Copyright (c) 2021 André Rijkeboer"

from .ecowitt import (
    EcoWittListener,
)

if __name__ == '__main__': print(__version__)
