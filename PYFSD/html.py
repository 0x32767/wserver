from typing import Tuple, Any, Dict


def res(html: str, status=(200, "OK")) -> str:
    return f"HTTP/1.0 {status[0]} {status[1]}\n\n" + html


class GenericHTMLElement:
    def __init__(self, name: str, self_closing: bool = False, *args, **kwargs) -> None:
        # this genorates the id="some-name" part of an element
        self.attrs = " ".join([str(k) + "=\"" + str(v) + "\" " for k, v in kwargs.items()]) +\
            " ".join(args) # the arrgs are for example hidden

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
            return element

        if self.self_closing:
            return f"<{self.name} {self.attrs} />"

        inner = "".join(self.render(e) for e in element)
        return f"<{self.name} {self.attrs}>\n{inner}\n</{self.name}>"


class HTMLMetta(type):
    # this is a dict full of the html tags, the key is the name, and the value is if the
    # tag is self closing
    html_tags = {
        "html": False,
        "abbr": False,
        "acronym": False,
        "address": False,
        "a": False,
        "applet": False,
        "area": False,
        "artcile": False,
        "aside": False,
        "audio": False,
        "base": True,
        "basefont": True,
        "bdi": False,
        "bdo": False,
        "bgsound ": True,
        "big": False,
        "blockquote": False,
        "body": False,
        "b": False,
        "br": True,
        "button": False,
        "caption": False,
        "canvas": False,
        "center": False,
        "cite": False,
        "code": False,
        "colgroup": False,
        "col": True,
        "data": False,
        "datalist": False,
        "dd": False,
        "define": False,
        "delete": False,
        "details": False,
        "dialog ": False,
        "dir": False,
        "div": False,
        "dl": False,
        "dt": False,
        "embed": True,
        "fieldset": False,
        "figcaption": False,
        "figure": False,
        "font": False,
        "footer": False,
        "form": False,
        "frame": True,
        "frameset": True,
        "head": False,
        "header": False,
        "h1": False,
        "h2": False,
        "h3": False,
        "h4": False,
        "h5": False,
        "h6": False,
        "hgroup": False,
        "hr": True,
        "html": False,
        "iframe": False,
        "img": True,
        "input": True,
        "ins": False,
        "isindex": True,
        "i": False,
        "kpd": False,
        "keygen": True,
        "label": False,
        "legend": False,
        "li": False,
        "main": False,
        "mark": False,
        "marquee": False,
        "menuitem": False,
        "meta": True,
        "meter": False,
        "nav": False,
        "bobr": False,
        "noembed": False,
        "noscript": False,
        "object": False,
        "optgroup": False,
        "option": False,
        "output": False,
        "p": False,
        "param": False,
        "em": False,
        "pre": False,
        "progress": False,
        "q": False,
        "rp": False,
        "rt": False,
        "ruby": False,
        "samp": False,
        "script": False,
        "section": False,
        "small": False,
        "source": False,
        "spacer": False,
        "span": False,
        "strike": False,
        "strong": False,
        "style": False,
        "sub": False,
        "summary": False,
        "svg": True,
        "table": False,
        "tbody": False,
        "td": False,
        "template": False,
        "tfoot": False,
        "th": False,
        "thead": False,
        "time": False,
        "title": False,
        "tr": False,
        "track": True,
        "tt": False,
        "u": False,
        "var": False,
        "video": False,
        "wbr": True,
        "xmp": False
    }

    def __new__(cls, name: str, bases: Tuple[Any], attrs: Dict[str, Any]) -> None:
        # the key is the name of the the tag and the value is if the tag is self closing
        for k, v in cls.html_tags:
            # the atters are the functions and attribvutes the class has
            # here we are creating a new function, this function has access
            # to the namespace
            attrs[k] = lambda s, *args, **keargs:\
                GenericHTMLElement(
                    # This will define the the value of the element
                    name=k,
                    self_closing=v
                )

        """
        Although this aproach is a bit arquard it is much more eficiant than writing a class
        with all html attributes. The metaclass above is equivilent to the following code:
        >>> class HTML:
        ...     def a(self, *args, **kwargs):
        ...         return GenericHTMLElement("a", False, *args, **kwargs)
        ...
        ...     def div(self, *args, **kwargs):
        ...         return GenericHTMLElement("div", False, *args, **kwargs)
        ...
        ...     def img(self, *args, **kwargs):
        ...         return GenericHTMLElement("img", True, *args, **kwargs)
        ... # This parrern would continue with the mremaining of the html elements,
        """

        return type(name, bases, attrs)


class HTML(metaclass=HTMLMetta):
    ...
