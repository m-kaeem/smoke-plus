"""Elementor v4 atomic element-tree builders."""
import itertools
from props import st

_counter = itertools.count(0x1000000)


def eid():
    return "%07x" % next(_counter)


def html(text):
    return {"$$type": "html-v3",
            "value": {"content": st(text), "children": []}}


def link(dest, tag="a", blank=False):
    return {"$$type": "link", "value": {
        "destination": {"$$type": "url", "value": dest},
        "isTargetBlank": {"$$type": "boolean", "value": blank},
        "tag": st(tag)}}


def classes(names):
    return {"$$type": "classes", "value": ["g-" + n for n in names]}


def _el(el_type, settings, children=None, widget_type=None):
    node = {
        "id": eid(),
        "elType": el_type,
        "settings": settings,
        "elements": children or [],
        "isInner": False,
        "styles": {},
        "editor_settings": {},
        "version": "0.0",
    }
    if widget_type:
        node["widgetType"] = widget_type
    return node


def div(cls, children=None, tag=None, href=None, **extra):
    s = {"classes": classes(cls)}
    if tag:
        s["tag"] = st(tag)
    if href:
        s["link"] = link(href)
    s.update(extra)
    return _el("e-div-block", s, children)


def flexbox(cls, children=None, **extra):
    s = {"classes": classes(cls)}
    s.update(extra)
    return _el("e-flexbox", s, children)


def heading(cls, text, tag="h2"):
    return _el("widget", {"classes": classes(cls), "tag": st(tag),
                          "title": html(text)},
               widget_type="e-heading")


def para(cls, text, tag="p"):
    return _el("widget", {"classes": classes(cls), "tag": st(tag),
                          "paragraph": html(text)},
               widget_type="e-paragraph")


def button(cls, text, href):
    return _el("widget", {"classes": classes(cls), "text": html(text),
                          "link": link(href), "tag": st("a")},
               widget_type="e-button")


def image(cls, attachment_id, size="full"):
    return _el("widget", {
        "classes": classes(cls),
        "image": {"$$type": "image", "value": {
            "src": {"$$type": "image-src", "value": {
                "id": {"$$type": "image-attachment-id",
                       "value": attachment_id},
                "url": None}},
            "size": st(size)}}},
        widget_type="e-image")
