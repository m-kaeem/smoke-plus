"""Elementor v4 atomic prop-value builders + the design's variable ids."""

# Global variable ids as stored in the Elementor kit (post 7) meta
# _elementor_global_variables. Label == emitted CSS custom property name.
V = {
    "color-ink":        "e-gv-6c1e3bc",
    "color-navy-deep":  "e-gv-227ad5e",
    "color-navy":       "e-gv-83a245c",
    "color-navy-soft":  "e-gv-23171ee",
    "color-lime":       "e-gv-8b42d8f",
    "color-lime-bright":"e-gv-2ca3c4a",
    "color-white":      "e-gv-1303fa8",
    "color-paper":      "e-gv-b12ccc5",
    "color-cloud":      "e-gv-a12b2e1",
    "color-mist":       "e-gv-3032858",
    "color-steel":      "e-gv-c593c1d",
    "color-slate":      "e-gv-e1c99e9",
    "color-line":       "e-gv-a3c0761",
    "color-line-light": "e-gv-ca52fa3",
    "color-caution":    "e-gv-62759c7",
    "color-scrim":      "e-gv-a845ff4",
    "color-scrim-soft": "e-gv-d1a829e",
    "color-chrome":     "e-gv-af9e2f3",
    "color-chrome-2":   "e-gv-2f36232",
    "color-chrome-3":   "e-gv-b4e7102",
    "color-chrome-text":"e-gv-9094060",
    "font-display":     "e-gv-c2c7d36",
    "font-body":        "e-gv-2095506",
    "font-label":       "e-gv-fa4fee0",
    "font-mono":        "e-gv-81e1fce",
}

# Literal colour values, needed where a prop type accepts only `color`
# (gradient stops) and cannot take a global colour variable.
LIT = {
    "color-scrim":      "rgba(6, 18, 26, 0.74)",
    "color-scrim-soft": "rgba(6, 18, 26, 0.30)",
    "color-ink":        "#081924",
}

# --- scalar prop values ------------------------------------------------------

def col(name):    return {"$$type": "global-color-variable", "value": V[name]}
def rawcol(v):    return {"$$type": "color", "value": v}
def fnt(name):    return {"$$type": "global-font-variable", "value": V[name]}
def st(v):        return {"$$type": "string", "value": v}
def num(v):       return {"$$type": "number", "value": v}
def px(v):        return {"$$type": "size", "value": {"size": v, "unit": "px"}}
def em(v):        return {"$$type": "size", "value": {"size": v, "unit": "em"}}
def pct(v):       return {"$$type": "size", "value": {"size": v, "unit": "%"}}
def unitless(v):  return {"$$type": "size", "value": {"size": str(v), "unit": "custom"}}
AUTO =            {"$$type": "size", "value": {"size": "", "unit": "auto"}}

# --- composite prop values ---------------------------------------------------

def dims(t, r, b, l):
    return {"$$type": "dimensions", "value": {
        "block-start": t, "inline-end": r, "block-end": b, "inline-start": l}}

def pad(t, r, b, l): return dims(px(t), px(r), px(b), px(l))

def bwidth(t, r, b, l):
    return {"$$type": "border-width-v2", "value": {
        "block-start": px(t), "inline-end": px(r),
        "block-end": px(b), "inline-start": px(l)}}

def radius(v):
    s = px(v)
    return {"$$type": "border-radius-v2", "value": {
        "start-start": s, "start-end": s, "end-start": s, "end-end": s}}

def gap(row, column=None):
    column = row if column is None else column
    return {"$$type": "layout-direction",
            "value": {"row": px(row), "column": px(column)}}

def flex(grow, shrink, basis):
    return {"$$type": "flex", "value": {
        "flexGrow": num(grow), "flexShrink": num(shrink), "flexBasis": basis}}

def shadow(h, v, blur, spread, color):
    return {"$$type": "box-shadow", "value": [
        {"$$type": "shadow", "value": {
            "hOffset": px(h), "vOffset": px(v), "blur": px(blur),
            "spread": px(spread), "color": color}}]}

# --- background --------------------------------------------------------------

def bg_color_overlay(color):
    return {"$$type": "background-color-overlay", "value": {"color": color}}

def bg_image_overlay(attachment_id, size="cover", position="center center",
                     repeat="no-repeat"):
    return {"$$type": "background-image-overlay", "value": {
        "image": {"$$type": "image", "value": {
            "src": {"$$type": "image-src", "value": {
                "id": {"$$type": "image-attachment-id", "value": attachment_id},
                "url": None}},
            "size": st("full")}},
        "size": st(size),
        "position": st(position),
        "repeat": st(repeat),
        "attachment": st("scroll"),
    }}

def bg_linear_gradient(angle, stops):
    """stops: [(css_colour, offset_percent), ...]"""
    return {"$$type": "background-gradient-overlay", "value": {
        "type": st("linear"),
        "angle": num(angle),
        "stops": {"$$type": "gradient-color-stop", "value": [
            {"$$type": "color-stop", "value": {
                "color": rawcol(c), "offset": num(o)}} for c, o in stops]},
    }}

def background(color=None, overlays=None):
    val = {}
    if overlays:
        val["background-overlay"] = {"$$type": "background-overlay",
                                     "value": overlays}
    if color is not None:
        val["color"] = color
    return {"$$type": "background", "value": val}

# --- style variants ----------------------------------------------------------

def variant(props, breakpoint="desktop", state=None):
    return {"meta": {"breakpoint": breakpoint, "state": state}, "props": props}

def gclass(name, desktop, tablet=None, mobile=None, hover=None):
    """A global class. `name` becomes both the css class and the label."""
    variants = [variant(desktop)]
    if tablet:
        variants.append(variant(tablet, "tablet"))
    if mobile:
        variants.append(variant(mobile, "mobile"))
    if hover:
        variants.append(variant(hover, "desktop", "hover"))
    return {
        "id": "g-" + name,
        "label": name,
        "type": "class",
        "variants": variants,
    }
