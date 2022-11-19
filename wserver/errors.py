class RouteNotFound(RuntimeWarning, KeyError):
    """
    This exception occurs when a rout has been used that has not been
    explicitly specified, e.g we may have a rout /abc/ and some bad fetch
    function in the front end tries to access /api/ .  This will
    obviousley fail but
    """


class DotCNFNotFound(RuntimeWarning):
    """
    In the root of your project you should have a file called ".cnf" this
    contains all metta data about the application this includes db settings
    and more. This is not required but if you want the error to go away
    then create a .cnf file (you can leave it blank if you want).
    """


class BadDiagramSerialization(RuntimeWarning, AttributeError):
    """
    It is possible to serialize a matplotlib or any image file, if an
    object can not be serialized then this error is thrown.
    """


class ErrorFunctionError(RuntimeWarning):
    """
    If there is a bad implemenetation for an error function e.g the
    function contains:
    >>> 0 / 0
    Or another bad thing then we can not render the on_error event because
    that will just cause anpther error. Instead we warn the user and send a
    message saying "INTERNAL SERVER ERROR" and a 500 status code.
    """


class NoRouteSpecified(Exception):
    """
    When Making a route you create a class that inherits from "Route", this
    class uses a class variable to define the route.
    >>> from PYFSD.typing import *
    >>> from PYFSD import Route
    >>>
    >>> class SomeRoute(Route):
    ...     route = "/define_your_route_here/and_here"
    ...
    ...     def on_error(self: Self, route: Dict) -> Tuple[str, int]:

    This is required when creating routes.
    """
