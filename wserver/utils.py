from .html import img, res, html, head, title, body
from .errors import BadDiagramSerialization
from io import BytesIO
import base64


def baseplate(*elements, **kwargs) -> str:
    return res(
        html()[
            head()[
                title()[kwargs.get("title", "document")],
                kwargs.get("head", None),
            ],
            body()[elements],
        ]
    )


def matplotlib_to_img(diagram, *args, **kwargs) -> str:
    # im also using *args and **kwargs
    if not hasattr(diagram, "savefig"):
        raise BadDiagramSerialization('diagram has no attr "savefig"')

    # fs is used as a fake file used to have the image content dumped into it
    fs = BytesIO()
    diagram.savefig(fs, format="png")

    # this will dump the fake file contense into the fig and serialize it
    fig = base64.b64decode(fs.getvalue()).decode("utf-8")

    # "<img src='data:image/png;base64,{}'>".format(fig) is equivilent
    return img(*args, src="data:image/png;base64,{}".format(fig), **kwargs)
