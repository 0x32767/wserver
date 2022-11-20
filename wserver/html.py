from typing import Tuple


def res(inner: str, status: Tuple[int, str] = (200, "OK")) -> str:
    return f"HTTP/1.0 {status[0]} {status[1]}\n\n" + inner


class GenericHTMLElement:
    def __init__(self, name: str, self_closing: bool = False, *args, **kwargs) -> None:
        # this generates the id="some-name" part of an element
        self.attrs = " ".join(
            [str(k) + '="' + str(v) + '" ' for k, v in kwargs.items()]
        ) + " ".join(args)
        # the args are for example hidden

        # together this makes up the:
        # hidden id="123"
        # part of the html element
        # <button hidden id="123"></button>

        self.self_closing = self_closing
        self.name = name

    def __getitem__(self, items):
        return self.render(items)

    def render(self, element) -> str:
        if isinstance(element, list) and len(element) == 1:
            return self.render(element[0])

        if isinstance(element, str):
            return f"<{self.name} {self.attrs}>\n{element}\n</{self.name}>"

        if self.self_closing:
            return f"<{self.name} {self.attrs} />"

        inner = "".join(self.render(e) for e in element)
        return f"<{self.name} {self.attrs}>\n{inner}\n</{self.name}>"


def html(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("html", False, *args, **kwargs)


def abbr(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("abbr", False, *args, **kwargs)


def acronym(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("acronym", False, *args, **kwargs)


def address(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("address", False, *args, **kwargs)


def a(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("a", False, *args, **kwargs)


def applet(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("applet", False, *args, **kwargs)


def area(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("area", False, *args, **kwargs)


def artcile(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("artcile", False, *args, **kwargs)


def aside(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("aside", False, *args, **kwargs)


def audio(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("audio", False, *args, **kwargs)


def base(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("base", True, *args, **kwargs)


def basefont(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("basefont", True, *args, **kwargs)


def bdi(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("bdi", False, *args, **kwargs)


def bdo(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("bdo", False, *args, **kwargs)


def bgsound(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("bgsound ", True, *args, **kwargs)


def big(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("big", False, *args, **kwargs)


def blockquote(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("blockquote", False, *args, **kwargs)


def body(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("body", False, *args, **kwargs)


def b(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("b", False, *args, **kwargs)


def br(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("br", True, *args, **kwargs)


def button(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("button", False, *args, **kwargs)


def caption(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("caption", False, *args, **kwargs)


def canvas(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("canvas", False, *args, **kwargs)


def center(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("center", False, *args, **kwargs)


def cite(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("cite", False, *args, **kwargs)


def code(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("code", False, *args, **kwargs)


def colgroup(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("colgroup", False, *args, **kwargs)


def col(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("col", True, *args, **kwargs)


def data(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("data", False, *args, **kwargs)


def datalist(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("datalist", False, *args, **kwargs)


def dd(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("dd", False, *args, **kwargs)


def define(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("define", False, *args, **kwargs)


def delete(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("delete", False, *args, **kwargs)


def details(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("details", False, *args, **kwargs)


def dialog(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("dialog ", False, *args, **kwargs)


def dir_(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("dir", False, *args, **kwargs)


def div(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("div", False, *args, **kwargs)


def dl(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("dl", False, *args, **kwargs)


def dt(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("dt", False, *args, **kwargs)


def embed(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("embed", True, *args, **kwargs)


def fieldset(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("fieldset", False, *args, **kwargs)


def figcaption(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("figcaption", False, *args, **kwargs)


def figure(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("figure", False, *args, **kwargs)


def font(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("font", False, *args, **kwargs)


def footer(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("footer", False, *args, **kwargs)


def form(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("form", False, *args, **kwargs)


def frame(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("frame", True, *args, **kwargs)


def frameset(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("frameset", True, *args, **kwargs)


def head(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("head", False, *args, **kwargs)


def header(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("header", False, *args, **kwargs)


def h1(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("h1", False, *args, **kwargs)


def h2(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("h2", False, *args, **kwargs)


def h3(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("h3", False, *args, **kwargs)


def h4(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("h4", False, *args, **kwargs)


def h5(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("h5", False, *args, **kwargs)


def h6(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("h6", False, *args, **kwargs)


def hgroup(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("hgroup", False, *args, **kwargs)


def hr(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("hr", True, *args, **kwargs)


def iframe(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("iframe", False, *args, **kwargs)


def img(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("img", True, *args, **kwargs)


def input_(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("input", True, *args, **kwargs)


def ins(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("ins", False, *args, **kwargs)


def isindex(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("isindex", True, *args, **kwargs)


def i(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("i", False, *args, **kwargs)


def kpd(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("kpd", False, *args, **kwargs)


def keygen(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("keygen", True, *args, **kwargs)


def label(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("label", False, *args, **kwargs)


def legend(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("legend", False, *args, **kwargs)


def li(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("li", False, *args, **kwargs)


def main(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("main", False, *args, **kwargs)


def mark(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("mark", False, *args, **kwargs)


def marquee(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("marquee", False, *args, **kwargs)


def menuitem(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("menuitem", False, *args, **kwargs)


def meta(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("meta", True, *args, **kwargs)


def meter(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("meter", False, *args, **kwargs)


def nav(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("nav", False, *args, **kwargs)


def bobr(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("bobr", False, *args, **kwargs)


def noembed(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("noembed", False, *args, **kwargs)


def noscript(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("noscript", False, *args, **kwargs)


def object_(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("object", False, *args, **kwargs)


def optgroup(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("optgroup", False, *args, **kwargs)


def option(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("option", False, *args, **kwargs)


def output(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("output", False, *args, **kwargs)


def p(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("p", False, *args, **kwargs)


def param(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("param", False, *args, **kwargs)


def em(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("em", False, *args, **kwargs)


def pre(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("pre", False, *args, **kwargs)


def progress(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("progress", False, *args, **kwargs)


def q(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("q", False, *args, **kwargs)


def rp(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("rp", False, *args, **kwargs)


def rt(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("rt", False, *args, **kwargs)


def ruby(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("ruby", False, *args, **kwargs)


def samp(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("samp", False, *args, **kwargs)


def script(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("script", False, *args, **kwargs)


def section(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("section", False, *args, **kwargs)


def small(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("small", False, *args, **kwargs)


def source(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("source", False, *args, **kwargs)


def spacer(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("spacer", False, *args, **kwargs)


def span(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("span", False, *args, **kwargs)


def strike(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("strike", False, *args, **kwargs)


def strong(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("strong", False, *args, **kwargs)


def style(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("style", False, *args, **kwargs)


def sub(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("sub", False, *args, **kwargs)


def summary(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("summary", False, *args, **kwargs)


def svg(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("svg", True, *args, **kwargs)


def table(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("table", False, *args, **kwargs)


def tbody(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("tbody", False, *args, **kwargs)


def td(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("td", False, *args, **kwargs)


def template(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("template", False, *args, **kwargs)


def tfoot(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("tfoot", False, *args, **kwargs)


def th(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("th", False, *args, **kwargs)


def thead(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("thead", False, *args, **kwargs)


def time(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("time", False, *args, **kwargs)


def title(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("title", False, *args, **kwargs)


def tr(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("tr", False, *args, **kwargs)


def track(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("track", True, *args, **kwargs)


def tt(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("tt", False, *args, **kwargs)


def u(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("u", False, *args, **kwargs)


def var(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("var", False, *args, **kwargs)


def video(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("video", False, *args, **kwargs)


def wbr(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("wbr", True, *args, **kwargs)


def xmp(*args, **kwargs) -> GenericHTMLElement:
    return GenericHTMLElement("xmp", False, *args, **kwargs)
