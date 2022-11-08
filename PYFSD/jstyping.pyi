from typing import Union, Any, Callable, List

Name = Union[str, None]
Type = Union[str, None]
InnerHTML = Union[str, None]
Element = Union[element, None]
Style = Union[dict[str, str], None]
HTMLCollection = Union[List[element], None]

class element:
    id: Name = None
    name: Name = None
    type: Type = None
    style: Style = None
    hidden: bool = False
    parent: Element = None
    className: Name = None
    innerText: InnerHTML = None
    innerHTML: InnerHTML = None
    children: HTMLCollection = None

    def addEventListener(element: Callable[[event], element]) -> None: ...

class event: ...

class dom:
    def __getattribute__(self, __name: str) -> element: ...
