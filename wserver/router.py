from configparser import ConfigParser
from colorama import init, Fore
from typing import Dict, List
from .core import _run_server
from re import Pattern
from .errors import *


init(autoreset=True)
config = ConfigParser()
config.read(".cnf")


routes = {
    # this route is halfway reserved, the route can be overwritten
    # but I want to explicitly throw an error to be safe
    "/favicon.ico": "HTTP/1.0 404 NOT FOUND\r\nFile Not Found\r\n\r\n",
}


def parse_http(info: str):
    if not info:
        return ""

    res: Dict[str, str] = {}

    dat: List[str, str] = info.split("\r\n")

    top = dat[0].split(" ")
    res["method"] = top[0]
    res["route"] = top[1]

    del dat[0]

    for x in dat:
        l: List[str, str] = x.split(":")

        if len(l) == 1:
            res[l[0].strip()] = None

        else:
            res[l[0].strip()] = l[1].strip()

    return res


def render_routes(inf: str, conn):
    # TODO return of the conn should close
    # TODO make this shit multithreaded:
    #   + this shit is just too slow
    route: dict[str, any] = parse_http(inf)

    # this is eather None or a route class
    try:
        cls = routes[route["route"]]

    # all routes are stored in a dict, if a key error is thrown then
    # the route was not specified
    except KeyError as ke:
        # here we loop over the route and route class and check if the regex matches up
        for k, v in routes.items():
            if isinstance(k, Pattern):
                if k.fullmatch(route):
                    return v.handel_request(route)

        # if we have not found a match with regex
        else:
            # this is the worst case senario, where there is not good route
            print(
                f'"{ke.args[0]}" was not defined but wass atempted to be accessed, returning 404'
            )

            # return a not found response
            return routes["***error"].invalid_route(route)

    except TypeError as te:
        return routes["***error"].bad_request(route)


    # if we got the class successfully
    if cls is None:
        print(f'{Fore.GREEN}@{route} responding with ""')
        return route["/error"].bad_request(route)

    elif isinstance(cls, str):
        return cls

    else:
        print(f'{Fore.GREEN}@{route} responding with "{type(cls).__name__}"')
        return cls.handel_request(route)

def add_route(route) -> None:
    routes[route.route] = route


def run(server: str, port: int):
    print(f"http://{server}:{port}")
    _run_server(server, port, render_routes)
