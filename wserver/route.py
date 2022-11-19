from .errors import NoRouteSpecified, ErrorFunctionError
from abc import ABC, abstractmethod
from typing import Dict, Self, Tuple
from warnings import warn
from .html import res


class Route(ABC):
    route: str = ""

    def __init__(self: Self) -> None:
        if type(self).route == "":
            raise NoRouteSpecified(
                f"No route was specified"
                "for {self.__class__.__name__} or {self.__class__.__name__}.route could not be accessed"
            )

#    @property
    @abstractmethod
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
