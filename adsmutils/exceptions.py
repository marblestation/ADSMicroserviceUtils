
class IgnorableException(Exception):
    """Dont mind, don't restart the worker."""
    pass


class ProcessingException(Exception):
    """Recoverable exception, should be reported to the
    ErrorHandler."""
    pass

        