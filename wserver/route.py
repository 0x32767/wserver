from .errors import NoRouteSpecified, ErrorFunctionError
from typing import Dict, Self, Callable
from functools import partial, wraps
from warnings import warn
from .html import res


class Route:
    route: str = ""

    def __init__(self: Self, **kwargs) -> None:
        self.routes: Dict[str, Callable[...]] = {}

        if isinstance(kwargs.get("route"), str):
            type(self).route = kwargs["route"]

        elif type(self).route == "":
            raise NoRouteSpecified(
                f"No route was specified"
                f"for {self.__class__.__name__} or {self.__class__.__name__}.route could not be accessed"
            )

    def request(self: Self, func: function, **kwargs):
        if not func.__name__ in ["on_post", "on_get", "on_put", "on_delete", "on_head", "on_options", "on_trace", "on_patch"]:
            raise NameError(
                f'Bad function name \"{func.__name__}\" needs to be one of "on_get", "on_post", "on_put", ech...'
            )

        if func.__name__ in self.routes.keys():
            raise NameError(f"Route {func.__name__} has already been defined")

        self.routes[func.__name__] = func

        @wraps(func)
        def wrapper(*args, **kwargs):
            ret_v = func(*args, **kwargs)
            return ret_v

        return wrapper

    def on_error(self: Self, route: Dict | None = None) -> str:
        """
        This method is an abstract class property and therefor needs to be overwritten
        when instantiating the class, wlse it wont work. e.g
        >>> class SpamRoute(Route):
        ...     route = "/spam"
        ...     ...
        ...
        ...     def on_error(self, req) -> Tuple[str, int]:
        ...         return "404 not found", 404
        ...
        The reason why the method needs to be overwritten is so that the user can add
        spicific functionality.
        """

        return res("404 not found", (404, "Not Found"))

    """
    The method handelers cna be used in two ways:
     * Inheriting from the class and overriding the methods
     * Instantiate the class and use the decoraotr syntax

    ::The OOP way::
    >>> ...
    >>> class MyRoute(Route):
    >>>     route: str = "/"
    >>> ...
    >>>     def on_get(self, req) -> str:
    >>>         return res("Hello world")

    ::The functional way::
    >>> ...
    >>> route = Route("/")
    >>> ...
    >>> @route.request()
    >>> def on_get(cls, req) -> str:
    >>>     return res("Hello world")

    """
    def on_get(self: Self, req) -> str:
        return self.on_error(req)

    def on_post(self: Self, req) -> str:
        return self.on_error(req)

    def on_put(self: Self, req) -> str:
        return self.on_error(req)

    def on_head(self: Self, req) -> str:
        return self.on_error(req)

    def on_delete(self: Self, req) -> str:
        return self.on_error(req)

    def on_options(self: Self, req) -> str:
        return self.on_error(req)

    def on_trace(self: Self, req) -> str:
        return self.on_error(req)

    def on_patch(self: Self, req) -> str:
        return self.on_error(req)

    def handel_request(self: Self, req: Dict[str, str]) -> str:
        if (fnc := self.routes.get(f"on_{req['method']}", None)):
            return fnc(req)

        try:
            return getattr(self, "on_" + req["method"].lower())(req)

        except Exception as e:
            try:
                # then we must have a problem with the on_error function
                return self.on_error(req)

            except Exception as e2:
                error = ExceptionGroup("nested", [ErrorFunctionError(), e, e2])

                warn(error)
                # send a request
                return res("internal server error", status=(500, "internal server error"))

            finally:
                warn(e)
