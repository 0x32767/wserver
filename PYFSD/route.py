from abc import abstractmethod, ABC, abstractproperty
from .errors import NoRouteSpecified
from typing import Dict, Self, Tuple


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

    def on_connect(self: Self, req) -> Tuple[str, int]:
        return self.on_error()

    def on_options(self: Self, req) -> Tuple[str, int]:
        return self.on_error()

    def on_trace(self: Self, req) -> Tuple[str, int]:
        return self.on_error()

    def on_patch(self: Self, req) -> Tuple[str, int]:
        return self.on_error()

    def handel_request(self: Self, req: Dict[str, str]) -> Tuple[str, int]:
        if req["method"] == "GET" and req.get("Sec-WebSocket-Key"):
            return self.on_connect(req)

        return getattr(self, "on_" + req["method"].lower())(req)

