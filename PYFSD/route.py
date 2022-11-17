from .errors import NoRouteSpecified, ErrorFunctionError
from abc import ABC, abstractproperty
from typing import Dict, Self, Tuple
from warnings import warn
from .html import res


class Route(ABC):
    route: str = ""

    def __init__(self: Self) -> None:
        if type(self).route == "":
            raise NoRouteSpecified(
                f"No route was specified for {self.__class__.__name__} or {self.__class__.__name__}.route could not be accessed"
            )

    @property
    @abstractproperty
    def on_error(route: Dict) -> Tuple[str, int]:
        """
        This method is an abstract class property and therefor needs to be overwritten
        when instantiating the class, wlse it wont work. e.g
        >>> class SpamRoute(Route):
        ...     route = "/spam"
        ...     ...
        ...     def on_error(self, req) -> Tuple[str, int]:
        ...         return ("404 not found", 404)
        ...
        The reason why the method needs to be overwritten is so that the user can add
        spicific functionality.
        """
        pass

    def on_get(self: Self, req) -> Tuple[str, int]:
        return self.on_error()

    def on_post(self: Self, req) -> Tuple[str, int]:
        return self.on_error()

    def on_put(self: Self, req) -> Tuple[str, int]:
        return self.on_error()

    def on_head(self: Self, req) -> Tuple[str, int]:
        return self.on_error()

    def on_delete(self: Self, req) -> Tuple[str, int]:
        return self.on_error()

    def on_options(self: Self, req) -> Tuple[str, int]:
        return self.on_error()

    def on_trace(self: Self, req) -> Tuple[str, int]:
        return self.on_error()

    def on_patch(self: Self, req) -> Tuple[str, int]:
        return self.on_error()

    def handel_request(self: Self, req: Dict[str, str]) -> Tuple[str, int]:
        try:
            return getattr(self, "on_" + req["method"].lower())(req)

        except Exception as e:
            try:
                # then we must have a problem with the on_error function
                return self.on_error(e, req)

            except Exception as e2:
                error = ExceptionGroup("nested", [ErrorFunctionError(), e, e2])

                error.add_note("This exception was also raised in the on_error function\n{}")

                warn(error)
                # send a request
                return res("internal server error", (500, "internal server error"))

            finally:
                warn(e)
