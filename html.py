from jinja2.sandbox import SandboxedEnvironment
from htmlBuilder.tags import *


env = SandboxedEnvironment()


def res(html: str, status=(200, "OK")) -> str:
    return f"HTTP/1.0 {status[0]} {status[1]}\n\n" + html


def render_template(path: str, *args, **kwargs) -> str:
    with open(path, "r") as f:
        return res(env.from_string(f.read()).render(*args, **kwargs))
