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


class NoRouteSpecified(Exception):
    """
    When Making a route you create a class that inherits from "Route", this
    class uses a class variable to define the route.
    >>> class SomeRoute(Route):
    ...     route = "/define_your_route_here/and_here"

    This is required when creating routes.
    """
