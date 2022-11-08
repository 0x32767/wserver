from typing import Tuple, Any, Dict


def res(html: str, status=(200, "OK")) -> str:
    return f"HTTP/1.0 {status[0]} {status[1]}\n\n" + html


class GenericHTMLElement:
    def __init__(self, name: str, self_closing: bool = False, *args, **kwargs) -> None:
        # this genorates the id="some-name" part of an element
        self.attrs = " ".join(
            [str(k) + '="' + str(v) + '" ' for k, v in kwargs.items()]
        ) + " ".join(args)
        # the arrgs are for example hidden

        # together this makes up the:
        # hidden id="123"
        # part of the html element
        # <button hidden id="123"></button>

        self.self_closing = self_closing
        self.name = name

    def __getitem__(self, items):
        return self.render(items)

    def render(self, element) -> str:
        if isinstance(element, str):
            return f"<{self.name} {self.attrs}>\n{element}\n</{self.name}>"

        if self.self_closing:
            return f"<{self.name} {self.attrs} />"

        inner = "".join(self.render(e) for e in element)
        return f"<{self.name} {self.attrs}>\n{inner}\n</{self.name}>"


html = lambda *args, **kwargs: GenericHTMLElement("html", False, *args, **kwargs)
abbr = lambda *args, **kwargs: GenericHTMLElement("abbr", False, *args, **kwargs)
acronym = lambda *args, **kwargs: GenericHTMLElement("acronym", False, *args, **kwargs)
address = lambda *args, **kwargs: GenericHTMLElement("address", False, *args, **kwargs)
a = lambda *args, **kwargs: GenericHTMLElement("a", False, *args, **kwargs)
applet = lambda *args, **kwargs: GenericHTMLElement("applet", False, *args, **kwargs)
area = lambda *args, **kwargs: GenericHTMLElement("area", False, *args, **kwargs)
artcile = lambda *args, **kwargs: GenericHTMLElement("artcile", False, *args, **kwargs)
aside = lambda *args, **kwargs: GenericHTMLElement("aside", False, *args, **kwargs)
audio = lambda *args, **kwargs: GenericHTMLElement("audio", False, *args, **kwargs)
base = lambda *args, **kwargs: GenericHTMLElement("base", True, *args, **kwargs)
basefont = lambda *args, **kwargs: GenericHTMLElement("basefont", True, *args, **kwargs)
bdi = lambda *args, **kwargs: GenericHTMLElement("bdi", False, *args, **kwargs)
bdo = lambda *args, **kwargs: GenericHTMLElement("bdo", False, *args, **kwargs)
bgsound = lambda *args, **kwargs: GenericHTMLElement("bgsound ", True, *args, **kwargs)
big = lambda *args, **kwargs: GenericHTMLElement("big", False, *args, **kwargs)
blockquote = lambda *args, **kwargs: GenericHTMLElement(
    "blockquote", False, *args, **kwargs
)
body = lambda *args, **kwargs: GenericHTMLElement("body", False, *args, **kwargs)
b = lambda *args, **kwargs: GenericHTMLElement("b", False, *args, **kwargs)
br = lambda *args, **kwargs: GenericHTMLElement("br", True, *args, **kwargs)
button = lambda *args, **kwargs: GenericHTMLElement("button", False, *args, **kwargs)
caption = lambda *args, **kwargs: GenericHTMLElement("caption", False, *args, **kwargs)
canvas = lambda *args, **kwargs: GenericHTMLElement("canvas", False, *args, **kwargs)
center = lambda *args, **kwargs: GenericHTMLElement("center", False, *args, **kwargs)
cite = lambda *args, **kwargs: GenericHTMLElement("cite", False, *args, **kwargs)
code = lambda *args, **kwargs: GenericHTMLElement("code", False, *args, **kwargs)
colgroup = lambda *args, **kwargs: GenericHTMLElement(
    "colgroup", False, *args, **kwargs
)
col = lambda *args, **kwargs: GenericHTMLElement("col", True, *args, **kwargs)
data = lambda *args, **kwargs: GenericHTMLElement("data", False, *args, **kwargs)
datalist = lambda *args, **kwargs: GenericHTMLElement(
    "datalist", False, *args, **kwargs
)
dd = lambda *args, **kwargs: GenericHTMLElement("dd", False, *args, **kwargs)
define = lambda *args, **kwargs: GenericHTMLElement("define", False, *args, **kwargs)
delete = lambda *args, **kwargs: GenericHTMLElement("delete", False, *args, **kwargs)
details = lambda *args, **kwargs: GenericHTMLElement("details", False, *args, **kwargs)
dialog = lambda *args, **kwargs: GenericHTMLElement("dialog ", False, *args, **kwargs)
dir = lambda *args, **kwargs: GenericHTMLElement("dir", False, *args, **kwargs)
div = lambda *args, **kwargs: GenericHTMLElement("div", False, *args, **kwargs)
dl = lambda *args, **kwargs: GenericHTMLElement("dl", False, *args, **kwargs)
dt = lambda *args, **kwargs: GenericHTMLElement("dt", False, *args, **kwargs)
embed = lambda *args, **kwargs: GenericHTMLElement("embed", True, *args, **kwargs)
fieldset = lambda *args, **kwargs: GenericHTMLElement(
    "fieldset", False, *args, **kwargs
)
figcaption = lambda *args, **kwargs: GenericHTMLElement(
    "figcaption", False, *args, **kwargs
)
figure = lambda *args, **kwargs: GenericHTMLElement("figure", False, *args, **kwargs)
font = lambda *args, **kwargs: GenericHTMLElement("font", False, *args, **kwargs)
footer = lambda *args, **kwargs: GenericHTMLElement("footer", False, *args, **kwargs)
form = lambda *args, **kwargs: GenericHTMLElement("form", False, *args, **kwargs)
frame = lambda *args, **kwargs: GenericHTMLElement("frame", True, *args, **kwargs)
frameset = lambda *args, **kwargs: GenericHTMLElement("frameset", True, *args, **kwargs)
head = lambda *args, **kwargs: GenericHTMLElement("head", False, *args, **kwargs)
header = lambda *args, **kwargs: GenericHTMLElement("header", False, *args, **kwargs)
h1 = lambda *args, **kwargs: GenericHTMLElement("h1", False, *args, **kwargs)
h2 = lambda *args, **kwargs: GenericHTMLElement("h2", False, *args, **kwargs)
h3 = lambda *args, **kwargs: GenericHTMLElement("h3", False, *args, **kwargs)
h4 = lambda *args, **kwargs: GenericHTMLElement("h4", False, *args, **kwargs)
h5 = lambda *args, **kwargs: GenericHTMLElement("h5", False, *args, **kwargs)
h6 = lambda *args, **kwargs: GenericHTMLElement("h6", False, *args, **kwargs)
hgroup = lambda *args, **kwargs: GenericHTMLElement("hgroup", False, *args, **kwargs)
hr = lambda *args, **kwargs: GenericHTMLElement("hr", True, *args, **kwargs)
html = lambda *args, **kwargs: GenericHTMLElement("html", False, *args, **kwargs)
iframe = lambda *args, **kwargs: GenericHTMLElement("iframe", False, *args, **kwargs)
img = lambda *args, **kwargs: GenericHTMLElement("img", True, *args, **kwargs)
input = lambda *args, **kwargs: GenericHTMLElement("input", True, *args, **kwargs)
ins = lambda *args, **kwargs: GenericHTMLElement("ins", False, *args, **kwargs)
isindex = lambda *args, **kwargs: GenericHTMLElement("isindex", True, *args, **kwargs)
i = lambda *args, **kwargs: GenericHTMLElement("i", False, *args, **kwargs)
kpd = lambda *args, **kwargs: GenericHTMLElement("kpd", False, *args, **kwargs)
keygen = lambda *args, **kwargs: GenericHTMLElement("keygen", True, *args, **kwargs)
label = lambda *args, **kwargs: GenericHTMLElement("label", False, *args, **kwargs)
legend = lambda *args, **kwargs: GenericHTMLElement("legend", False, *args, **kwargs)
li = lambda *args, **kwargs: GenericHTMLElement("li", False, *args, **kwargs)
main = lambda *args, **kwargs: GenericHTMLElement("main", False, *args, **kwargs)
mark = lambda *args, **kwargs: GenericHTMLElement("mark", False, *args, **kwargs)
marquee = lambda *args, **kwargs: GenericHTMLElement("marquee", False, *args, **kwargs)
menuitem = lambda *args, **kwargs: GenericHTMLElement(
    "menuitem", False, *args, **kwargs
)
meta = lambda *args, **kwargs: GenericHTMLElement("meta", True, *args, **kwargs)
meter = lambda *args, **kwargs: GenericHTMLElement("meter", False, *args, **kwargs)
nav = lambda *args, **kwargs: GenericHTMLElement("nav", False, *args, **kwargs)
bobr = lambda *args, **kwargs: GenericHTMLElement("bobr", False, *args, **kwargs)
noembed = lambda *args, **kwargs: GenericHTMLElement("noembed", False, *args, **kwargs)
noscript = lambda *args, **kwargs: GenericHTMLElement(
    "noscript", False, *args, **kwargs
)
object = lambda *args, **kwargs: GenericHTMLElement("object", False, *args, **kwargs)
optgroup = lambda *args, **kwargs: GenericHTMLElement(
    "optgroup", False, *args, **kwargs
)
option = lambda *args, **kwargs: GenericHTMLElement("option", False, *args, **kwargs)
output = lambda *args, **kwargs: GenericHTMLElement("output", False, *args, **kwargs)
p = lambda *args, **kwargs: GenericHTMLElement("p", False, *args, **kwargs)
param = lambda *args, **kwargs: GenericHTMLElement("param", False, *args, **kwargs)
em = lambda *args, **kwargs: GenericHTMLElement("em", False, *args, **kwargs)
pre = lambda *args, **kwargs: GenericHTMLElement("pre", False, *args, **kwargs)
progress = lambda *args, **kwargs: GenericHTMLElement(
    "progress", False, *args, **kwargs
)
q = lambda *args, **kwargs: GenericHTMLElement("q", False, *args, **kwargs)
rp = lambda *args, **kwargs: GenericHTMLElement("rp", False, *args, **kwargs)
rt = lambda *args, **kwargs: GenericHTMLElement("rt", False, *args, **kwargs)
ruby = lambda *args, **kwargs: GenericHTMLElement("ruby", False, *args, **kwargs)
samp = lambda *args, **kwargs: GenericHTMLElement("samp", False, *args, **kwargs)
script = lambda *args, **kwargs: GenericHTMLElement("script", False, *args, **kwargs)
section = lambda *args, **kwargs: GenericHTMLElement("section", False, *args, **kwargs)
small = lambda *args, **kwargs: GenericHTMLElement("small", False, *args, **kwargs)
source = lambda *args, **kwargs: GenericHTMLElement("source", False, *args, **kwargs)
spacer = lambda *args, **kwargs: GenericHTMLElement("spacer", False, *args, **kwargs)
span = lambda *args, **kwargs: GenericHTMLElement("span", False, *args, **kwargs)
strike = lambda *args, **kwargs: GenericHTMLElement("strike", False, *args, **kwargs)
strong = lambda *args, **kwargs: GenericHTMLElement("strong", False, *args, **kwargs)
style = lambda *args, **kwargs: GenericHTMLElement("style", False, *args, **kwargs)
sub = lambda *args, **kwargs: GenericHTMLElement("sub", False, *args, **kwargs)
summary = lambda *args, **kwargs: GenericHTMLElement("summary", False, *args, **kwargs)
svg = lambda *args, **kwargs: GenericHTMLElement("svg", True, *args, **kwargs)
table = lambda *args, **kwargs: GenericHTMLElement("table", False, *args, **kwargs)
tbody = lambda *args, **kwargs: GenericHTMLElement("tbody", False, *args, **kwargs)
td = lambda *args, **kwargs: GenericHTMLElement("td", False, *args, **kwargs)
template = lambda *args, **kwargs: GenericHTMLElement(
    "template", False, *args, **kwargs
)
tfoot = lambda *args, **kwargs: GenericHTMLElement("tfoot", False, *args, **kwargs)
th = lambda *args, **kwargs: GenericHTMLElement("th", False, *args, **kwargs)
thead = lambda *args, **kwargs: GenericHTMLElement("thead", False, *args, **kwargs)
time = lambda *args, **kwargs: GenericHTMLElement("time", False, *args, **kwargs)
title = lambda *args, **kwargs: GenericHTMLElement("title", False, *args, **kwargs)
tr = lambda *args, **kwargs: GenericHTMLElement("tr", False, *args, **kwargs)
track = lambda *args, **kwargs: GenericHTMLElement("track", True, *args, **kwargs)
tt = lambda *args, **kwargs: GenericHTMLElement("tt", False, *args, **kwargs)
u = lambda *args, **kwargs: GenericHTMLElement("u", False, *args, **kwargs)
var = lambda *args, **kwargs: GenericHTMLElement("var", False, *args, **kwargs)
video = lambda *args, **kwargs: GenericHTMLElement("video", False, *args, **kwargs)
wbr = lambda *args, **kwargs: GenericHTMLElement("wbr", True, *args, **kwargs)
xmp = lambda *args, **kwargs: GenericHTMLElement("xmp", False, *args, **kwargs)
html = lambda *args, **kwargs: GenericHTMLElement("html", False, *args, **kwargs)
