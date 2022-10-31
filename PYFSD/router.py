from configparser import ConfigParser
from colorama import init, Fore
from .errors import *
from typing import Dict, List
from .html import res
from .core import _run_server


init(autoreset=True)
config = ConfigParser()
config.read(".cnf")


routes = {
    "/favicon.ico": "HTTP/1.0 404 NOT FOUND\n\nFile Not Found",
}


def parse_http(info: str):
    res: Dict[str, str] = {}

    dat: List[str, str] = info.split("\r\n")

    top = dat[0].split(" ")
    res["method"] = top[0]
    res["route"] = top[1]

    del dat[0]
    x: int

    for x in dat:
        l: List[str, str] = x.split(":")

        if len(l) == 1:
            res[l[0]] = None

        else:
            res[l[0]] = l[1]

    return res


def render_routes(inf: str):
    route: dict[str, any] = parse_http(inf)

    # this is eather None or a route class
    try:
        cls = routes[route["route"]]

    # all routes are stored in a dict, if a key error is thrown then
    # the route was not specified
    except KeyError as ke:
        print(
            f'"{ke.args[0]}" was not defined but wass atempted to be accessed, returning 404'
        )

        # return a not found response
        return res(
            open(routes[config["errors"]["not-found"]], "r").read(), (404, "not found")
        )

    if cls is None:
        print(f'{Fore.GREEN}@{route} responding with ""')
        return ""

    elif isinstance(cls, str):
        print(f"{Fore.GREEN}@{route} responding with a string")
        return cls

    else:
        print(f'{Fore.GREEN}@{route} responding with "{type(cls).__name__}"')
        return getattr(cls, f"on_{route['method'].lower()}")(route)


def add_route(route) -> None:
    routes[route.route] = route


def run(server: str, port: int):
    print(f"http://{server}:{port}")
    _run_server(server, port, render_routes)
