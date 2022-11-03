from jinja2.sandbox import SandboxedEnvironment
from base64 import b64encode
from hashlib import sha1

env = SandboxedEnvironment()


def res(html: str, status=(200, "OK")) -> str:
    return f"HTTP/1.0 {status[0]} {status[1]}\n\n" + html


def render_template(
    path: str, *args, **kwargs
) -> str:

    with open(path, "r") as f:
        return res(env.from_string(f.read()).render(*args, **kwargs))


# an incoming websocket will give some random b64 int, we
# need to add some magic number to it and then sha1 it and
# return it as a b64
def accept_handshake(key: str, magic: int):
    # hex to base 64
    return b64encode(bytes.fromhex(
        # this is the important part, this will add a magic
        # number and then sha1 it, this is just how
        # websockets work
        sha1(int(key, 64) + magic).hexdigest()
    )).decode()
