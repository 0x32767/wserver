from jinja2.sandbox import SandboxedEnvironment
from websockets.utils import accept_key

env = SandboxedEnvironment()


def res(html: str, status=(200, "OK")) -> str:
    return f"HTTP/1.0 {status[0]} {status[1]}\n\n" + html


def render_template(path: str, *args, **kwargs) -> str:

    with open(path, "r") as f:
        return res(env.from_string(f.read()).render(*args, **kwargs))


def _decorate_ws(key: str) -> str:
    return f"""HTTP/1.1 101 Switching Protocols\r\nUpgrade: websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Accept: {key}\r\nSec-WebSocket-Protocol: chat"""


# an incoming websocket will give some random b64 int, we
# need to add some magic number to it and then sha1 it and
# return it as a b64
def accept_handshake(key: str):
    # hex to base 64
    return _decorate_ws(accept_key(key))
