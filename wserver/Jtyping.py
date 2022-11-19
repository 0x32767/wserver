from __future__ import annotations

from typing import overload, Callable, Union, List


class HTMLCollection:
    ...


class Event:
    ...


class HTMLElement:
    def on(self: HTMLElement,
            event: str,
            func: Callable[
                [Event, HTMLElement],
                Union[HTMLElement, HTMLCollection]
            ]) -> None: ...


@overload
def doc(name: str) -> HTMLElement:
    ...


def doc(name: str) -> Union[HTMLElement, HTMLCollection]:
    if name[0] == "#":
        return HTMLElement()
