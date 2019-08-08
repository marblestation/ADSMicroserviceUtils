
from __future__ import absolute_import, unicode_literals, division, print_function


class IgnorableException(Exception):
    """Dont mind, don't restart the worker."""
    pass


class ProcessingException(Exception):
    """Recoverable exception, should be reported to the
    ErrorHandler."""
    pass
