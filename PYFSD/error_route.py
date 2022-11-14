from typing import Union, Tuple
from .html import res

class ErrorRoute:
    route = "***error"

    def invalid_route(self, route) -> str:
        """
        If a user were to make a request to:
        /banana
        and the banana route was not implemented then this function would be called.
        """
        return res("ERROR: Invalid Route", ("bad route", 400))

    def bad_request(self, route) -> str:
        """
        If the server gets a bad request than this is trigered.
        """

        return res("ERROR: bad request", ("bad request", 400))
