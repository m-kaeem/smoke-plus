"""Every repeated class from the exported design, as Elementor global classes.

Names carry an `spc-` prefix so they cannot collide with Astra's or a
plugin's own classes. The returned ORDER list is highest-CSS-priority
first: Elementor emits global class CSS in reverse of the stored order,
so whatever sits earlier here wins the cascade.
"""
from props import *

UPPER = st("uppercase")
FLEX = st("flex")
COL = st("column")
BLOCK = st("block")
WRAP = st("wrap")
START = st("flex-start")
CENTER = st("center")
SOLID = st("solid")
POINTER = st("pointer")

LH_HERO = unitless(1.02)
LH_HEAD = unitless(1.1)
LH_TIGHT = unitless(1.35)
LH_BODY = unitless(1.6)
TRACK_WIDE = em(0.08)
TRACK_WIDER = em(0.14)
TRACK_TIGHT = em(-0.01)

ZERO = pad(0, 0, 0, 0)

# Attachment ids in the media library, by the design's source file name.
IMG = {
    "unnamed.jpg": 9,      "unnamed (1).jpg": 10,  "unnamed (1).png": 11,
    "unnamed (2).jpg": 12, "unnamed (3).jpg": 13,  "unnamed (4).jpg": 14,
    "unnamed (5).jpg": 15, "unnamed (6).jpg": 16,  "unnamed (7).jpg": 17,
    "unnamed (8).jpg": 18, "unnamed (9).jpg": 19,  "unnamed (10).jpg": 20,
    "unnamed (11).jpg": 21,"unnamed (12).jpg": 22, "unnamed (13).jpg": 23,
    "unnamed (14).jpg": 24,"unnamed (15).jpg": 25, "unnamed (16).jpg": 26,
    "unnamed (17).jpg": 27,"unnamed (18).jpg": 28, "unnamed (19).jpg": 29,
    "unnamed (20).jpg": 30,"unnamed (21).jpg": 31, "unnamed.png": 32,
}


def build():
    C = []

    # ---- shell / sections ---------------------------------------------------
    C.append(gclass("spc-shell",
        {"display": FLEX, "flex-direction": COL, "width": pct(100),
         "max-width": px(1200),
         "margin": dims(px(0), AUTO, px(0), AUTO),
         "padding": pad(0, 48, 0, 48)},
        tablet={"padding": pad(0, 32, 0, 32)},
        mobile={"padding": pad(0, 20, 0, 20)}))

    C.append(gclass("spc-section",
        {"display": FLEX, "flex-direction": COL, "padding": pad(96, 0, 96, 0)},
        tablet={"padding": pad(64, 0, 64, 0)},
        mobile={"padding": pad(44, 0, 44, 0)}))

    for name, var in (("paper", "color-paper"), ("cloud", "color-cloud"),
                      ("ink", "color-ink"), ("navy", "color-navy-deep")):
        C.append(gclass("spc-section-" + name,
                        {"background": background(color=col(var))}))

    for n, g in ((4, 16), (5, 24), (6, 32), (7, 48)):
        C.append(gclass("spc-stack-%d" % n,
            {"display": FLEX, "flex-direction": COL, "gap": gap(g)}))

    # ---- rows / splits ------------------------------------------------------
    C.append(gclass("spc-row",
        {"display": FLEX, "flex-wrap": WRAP, "gap": gap(24)}))

    C.append(gclass("spc-split",
        {"display": FLEX, "flex-wrap": WRAP, "gap": gap(64),
         "align-items": CENTER},
        tablet={"gap": gap(32)},
        mobile={"flex-direction": COL, "align-items": st("stretch"),
                "gap": gap(32)}))

    C.append(gclass("spc-split-top", {"align-items": START}))

    C.append(gclass("spc-split-col",
        {"flex": flex(1, 1, px(380)), "display": FLEX, "flex-direction": COL,
         "gap": gap(24), "align-items": START},
        tablet={"flex": flex(1, 1, px(320))}))

    # ---- eyebrow / rules ----------------------------------------------------
    C.append(gclass("spc-eyebrow",
        {"display": FLEX, "align-items": CENTER, "gap": gap(12),
         "margin": ZERO}))

    C.append(gclass("spc-eyebrow-text",
        {"font-family": fnt("font-label"), "font-size": px(13),
         "text-transform": UPPER, "letter-spacing": TRACK_WIDER,
         "margin": ZERO}))

    C.append(gclass("spc-eyebrow-dark", {"color": col("color-slate")}))
    C.append(gclass("spc-eyebrow-light", {"color": col("color-lime")}))

    C.append(gclass("spc-rule",
        {"display": BLOCK, "width": px(48), "height": px(3),
         "background": background(color=col("color-lime")),
         "flex": flex(0, 0, AUTO)}))

    C.append(gclass("spc-dot-sep",
        {"display": BLOCK, "width": px(6), "height": px(6),
         "border-radius": radius(999),
         "background": background(color=col("color-steel")),
         "flex": flex(0, 0, AUTO)},
        mobile={"display": st("none")}))

    # ---- headings -----------------------------------------------------------
    C.append(gclass("spc-hero-title",
        {"font-family": fnt("font-display"), "font-size": px(72),
         "line-height": LH_HERO, "letter-spacing": TRACK_TIGHT,
         "color": col("color-white"), "margin": ZERO},
        tablet={"font-size": px(50)}, mobile={"font-size": px(36)}))

    C.append(gclass("spc-h2",
        {"font-family": fnt("font-display"), "font-size": px(38),
         "line-height": LH_HEAD, "letter-spacing": TRACK_TIGHT,
         "color": col("color-ink"), "margin": ZERO},
        tablet={"font-size": px(30)}, mobile={"font-size": px(25)}))

    C.append(gclass("spc-h3",
        {"font-family": fnt("font-display"), "font-size": px(23),
         "line-height": LH_TIGHT, "color": col("color-ink"), "margin": ZERO},
        tablet={"font-size": px(21)}, mobile={"font-size": px(19)}))

    C.append(gclass("spc-ink", {"color": col("color-ink")}))
    C.append(gclass("spc-on-dark", {"color": col("color-white")}))

    # ---- body copy ----------------------------------------------------------
    C.append(gclass("spc-lead",
        {"font-family": fnt("font-body"), "font-size": px(21),
         "line-height": LH_BODY, "margin": ZERO, "max-width": px(640),
         "color": col("color-slate")},
        tablet={"font-size": px(19)}, mobile={"font-size": px(17)}))

    C.append(gclass("spc-copy",
        {"font-family": fnt("font-body"), "font-size": px(17),
         "line-height": LH_BODY, "margin": ZERO, "max-width": px(640),
         "color": col("color-slate")}))

    C.append(gclass("spc-lead-dark", {"color": col("color-slate")}))
    C.append(gclass("spc-lead-light", {"color": col("color-mist")}))
    C.append(gclass("spc-copy-dark", {"color": col("color-slate")}))
    C.append(gclass("spc-copy-light", {"color": col("color-mist")}))

    # ---- buttons ------------------------------------------------------------
    btn_base = {
        "display": st("inline-flex"), "align-items": CENTER,
        "justify-content": CENTER, "gap": gap(8),
        "font-family": fnt("font-label"), "font-size": px(19),
        "text-transform": UPPER, "letter-spacing": TRACK_WIDE,
        "border-radius": radius(4), "cursor": POINTER,
        "text-decoration": st("none"),
    }

    C.append(gclass("spc-button-row",
        {"display": FLEX, "flex-wrap": WRAP, "align-items": CENTER,
         "gap": gap(16)}))

    C.append(gclass("spc-button-primary",
        dict(btn_base, **{
            "color": col("color-ink"),
            "background": background(color=col("color-lime")),
            "border-width": bwidth(0, 0, 0, 0),
            "padding": pad(16, 24, 16, 24)}),
        mobile={"width": pct(100), "justify-content": CENTER},
        hover={"background": background(color=col("color-lime-bright"))}))

    C.append(gclass("spc-button-ghost",
        dict(btn_base, **{
            "color": col("color-white"),
            "border-width": bwidth(3, 3, 3, 3), "border-style": SOLID,
            "border-color": col("color-line"),
            "padding": pad(12, 24, 12, 24)}),
        mobile={"width": pct(100), "justify-content": CENTER},
        hover={"border-color": col("color-lime"),
               "color": col("color-lime")}))

    C.append(gclass("spc-button-outline",
        dict(btn_base, **{
            "color": col("color-ink"),
            "border-width": bwidth(3, 3, 3, 3), "border-style": SOLID,
            "border-color": col("color-ink"),
            "padding": pad(12, 24, 12, 24)}),
        mobile={"width": pct(100), "justify-content": CENTER},
        hover={"background": background(color=col("color-ink")),
               "color": col("color-lime")}))

    # ---- hero ---------------------------------------------------------------
    C.append(gclass("spc-hero",
        {"display": FLEX, "flex-direction": COL,
         "justify-content": st("flex-end"), "min-height": px(620),
         "background": background(color=col("color-ink"))},
        tablet={"min-height": px(520)}, mobile={"min-height": px(540)}))

    C.append(gclass("spc-hero-home",
        {"background": background(color=col("color-ink"), overlays=[
            bg_linear_gradient(90, [(LIT["color-scrim"], 0),
                                    (LIT["color-scrim-soft"], 100)]),
            bg_image_overlay(IMG["unnamed (12).jpg"], "cover",
                             "center center")])},
        mobile={"background": background(color=col("color-ink"), overlays=[
            bg_linear_gradient(180, [(LIT["color-scrim-soft"], 0),
                                     (LIT["color-scrim"], 100)]),
            bg_image_overlay(IMG["unnamed (21).jpg"], "cover",
                             "top center")])}))

    C.append(gclass("spc-hero-inner",
        {"display": FLEX, "flex-direction": COL, "gap": gap(24),
         "align-items": START, "padding": pad(96, 0, 96, 0),
         "max-width": px(800)},
        tablet={"padding": pad(64, 0, 64, 0)},
        mobile={"padding": pad(44, 0, 44, 0)}))

    C.append(gclass("spc-hero-strip",
        {"display": FLEX, "flex-wrap": WRAP, "align-items": CENTER,
         "gap": gap(12)},
        mobile={"flex-direction": COL, "align-items": START, "gap": gap(8)}))

    C.append(gclass("spc-hero-strip-text",
        {"font-family": fnt("font-label"), "font-size": px(15),
         "text-transform": UPPER, "letter-spacing": TRACK_WIDE,
         "color": col("color-mist"), "margin": ZERO}))

    # ---- category cards -----------------------------------------------------
    C.append(gclass("spc-card-cat",
        {"flex": flex(1, 1, px(240)), "display": FLEX, "flex-direction": COL,
         "background": background(color=col("color-white")),
         "border-width": bwidth(1, 1, 1, 1), "border-style": SOLID,
         "border-color": col("color-line-light"),
         "border-radius": radius(10), "padding": ZERO,
         "overflow": st("hidden"), "cursor": POINTER,
         "text-align": st("start"), "text-decoration": st("none")},
        tablet={"flex": flex(1, 1, px(320))},
        mobile={"flex": flex(1, 1, pct(100))},
        hover={"border-color": col("color-lime")}))

    C.append(gclass("spc-card-cat-img",
        {"display": BLOCK, "width": pct(100), "aspect-ratio": st("4 / 3"),
         "object-fit": st("cover")}))

    C.append(gclass("spc-card-cat-body",
        {"display": FLEX, "flex-direction": COL, "gap": gap(8),
         "padding": pad(24, 24, 24, 24)}))

    C.append(gclass("spc-card-cat-name",
        {"font-family": fnt("font-display"), "font-size": px(23),
         "color": col("color-ink"), "margin": ZERO},
        tablet={"font-size": px(21)}, mobile={"font-size": px(19)}))

    C.append(gclass("spc-card-cat-text",
        {"font-family": fnt("font-body"), "font-size": px(15),
         "line-height": LH_TIGHT, "color": col("color-slate"),
         "margin": ZERO}))

    # ---- feature cards ------------------------------------------------------
    C.append(gclass("spc-card-feature",
        {"flex": flex(1, 1, px(240)), "display": FLEX, "flex-direction": COL,
         "gap": gap(12),
         "background": background(color=col("color-navy-deep")),
         "border-radius": radius(10), "padding": pad(32, 32, 32, 32)},
        tablet={"flex": flex(1, 1, px(320))},
        mobile={"flex": flex(1, 1, pct(100)),
                "padding": pad(24, 24, 24, 24)}))

    C.append(gclass("spc-card-num",
        {"font-family": fnt("font-display"), "font-size": px(38),
         "color": col("color-lime"), "margin": ZERO},
        tablet={"font-size": px(30)}, mobile={"font-size": px(25)}))

    # ---- stats --------------------------------------------------------------
    C.append(gclass("spc-stat",
        {"flex": flex(1, 1, px(180)), "display": FLEX, "flex-direction": COL,
         "gap": gap(8), "border-width": bwidth(3, 0, 0, 0),
         "border-style": SOLID, "border-color": col("color-lime"),
         "padding": pad(16, 0, 0, 0)},
        mobile={"flex": flex(1, 1, px(130))}))

    C.append(gclass("spc-stat-num",
        {"font-family": fnt("font-display"), "font-size": px(54),
         "color": col("color-white"), "margin": ZERO},
        tablet={"font-size": px(40)}, mobile={"font-size": px(30)}))

    C.append(gclass("spc-stat-label",
        {"font-family": fnt("font-label"), "font-size": px(13),
         "text-transform": UPPER, "letter-spacing": TRACK_WIDER,
         "color": col("color-steel"), "margin": ZERO}))

    # ---- lists --------------------------------------------------------------
    C.append(gclass("spc-list",
        {"display": FLEX, "flex-direction": COL, "gap": gap(12),
         "margin": ZERO, "padding": ZERO}))

    C.append(gclass("spc-list-item",
        {"display": FLEX, "align-items": START, "gap": gap(12)}))

    C.append(gclass("spc-list-bullet",
        {"display": BLOCK, "width": px(6), "height": px(6),
         "border-radius": radius(999),
         "background": background(color=col("color-lime")),
         "flex": flex(0, 0, AUTO), "margin": dims(px(12), px(0), px(0), px(0))}))

    C.append(gclass("spc-list-text",
        {"font-family": fnt("font-body"), "font-size": px(17),
         "line-height": LH_BODY, "margin": ZERO,
         "color": col("color-slate")}))

    # ---- media --------------------------------------------------------------
    C.append(gclass("spc-service-img",
        {"display": BLOCK, "width": pct(100), "aspect-ratio": st("4 / 3"),
         "object-fit": st("cover"), "border-radius": radius(10)}))

    C.append(gclass("spc-strip",
        {"display": FLEX, "flex-wrap": WRAP, "gap": gap(16)}))

    C.append(gclass("spc-strip-img",
        {"display": BLOCK, "flex": flex(1, 1, px(180)), "height": px(200),
         "object-fit": st("cover"), "border-radius": radius(4)},
        mobile={"flex": flex(1, 1, pct(100))}))

    # ---- chips --------------------------------------------------------------
    C.append(gclass("spc-chips",
        {"display": FLEX, "flex-wrap": WRAP, "gap": gap(12)}))

    C.append(gclass("spc-chip",
        {"font-family": fnt("font-label"), "font-size": px(17),
         "text-transform": UPPER, "letter-spacing": TRACK_WIDE,
         "color": col("color-ink"),
         "background": background(color=col("color-white")),
         "border-width": bwidth(1, 1, 1, 1), "border-style": SOLID,
         "border-color": col("color-line-light"),
         "border-radius": radius(999), "padding": pad(8, 16, 8, 16),
         "margin": ZERO}))

    # ---- closing cta --------------------------------------------------------
    C.append(gclass("spc-cta",
        {"display": FLEX, "flex-wrap": WRAP, "align-items": CENTER,
         "justify-content": st("space-between"), "gap": gap(32),
         "background": background(color=col("color-lime")),
         "border-radius": radius(20), "padding": pad(64, 64, 64, 64)},
        mobile={"flex-direction": COL, "align-items": st("stretch"),
                "padding": pad(32, 32, 32, 32),
                "border-radius": radius(10)}))

    C.append(gclass("spc-cta-title",
        {"font-family": fnt("font-display"), "font-size": px(38),
         "line-height": LH_HEAD, "color": col("color-ink"),
         "margin": ZERO, "max-width": px(430)},
        tablet={"font-size": px(30)}, mobile={"font-size": px(25)}))

    # ---- inner page heads ---------------------------------------------------
    C.append(gclass("spc-page-head",
        {"display": FLEX, "flex-direction": COL, "gap": gap(16),
         "align-items": START, "padding": pad(96, 0, 96, 0)},
        tablet={"padding": pad(64, 0, 64, 0)},
        mobile={"padding": pad(44, 0, 44, 0)}))

    C.append(gclass("spc-h1",
        {"font-family": fnt("font-display"), "font-size": px(54),
         "line-height": LH_HEAD, "letter-spacing": TRACK_TIGHT,
         "color": col("color-ink"), "margin": ZERO},
        tablet={"font-size": px(40)}, mobile={"font-size": px(30)}))

    # ---- service rows -------------------------------------------------------
    C.append(gclass("spc-service",
        {"display": FLEX, "flex-wrap": WRAP, "gap": gap(64),
         "align-items": START, "padding": pad(64, 0, 64, 0),
         "border-width": bwidth(1, 0, 0, 0), "border-style": SOLID,
         "border-color": col("color-line-light")},
        tablet={"gap": gap(32)},
        mobile={"flex-direction": COL, "gap": gap(24),
                "padding": pad(32, 0, 32, 0)}))

    C.append(gclass("spc-service-flip",
        {"flex-direction": st("row-reverse")},
        mobile={"flex-direction": COL}))

    C.append(gclass("spc-service-media",
        {"flex": flex(1, 1, px(380))},
        tablet={"flex": flex(1, 1, px(320))}))

    C.append(gclass("spc-service-body",
        {"flex": flex(1, 1, px(380)), "display": FLEX, "flex-direction": COL,
         "gap": gap(16), "align-items": START},
        tablet={"flex": flex(1, 1, px(320))}))

    # ---- dark chips / notices ----------------------------------------------
    C.append(gclass("spc-chip-dark",
        {"color": col("color-mist"),
         "background": background(color=col("color-navy-deep")),
         "border-color": col("color-line")}))

    C.append(gclass("spc-notice",
        {"display": FLEX, "flex-direction": COL, "gap": gap(8),
         "border-width": bwidth(1, 1, 1, 1), "border-style": SOLID,
         "border-color": col("color-caution"),
         "border-radius": radius(10), "padding": pad(24, 24, 24, 24)}))

    C.append(gclass("spc-notice-head",
        {"font-family": fnt("font-label"), "font-size": px(13),
         "text-transform": UPPER, "letter-spacing": TRACK_WIDER,
         "color": col("color-ink"), "margin": ZERO}))

    C.append(gclass("spc-notice-text",
        {"font-family": fnt("font-body"), "font-size": px(15),
         "line-height": LH_BODY, "color": col("color-slate"),
         "margin": ZERO}))

    # ---- gallery ------------------------------------------------------------
    C.append(gclass("spc-shots",
        {"display": FLEX, "flex-wrap": WRAP, "gap": gap(16)}))

    C.append(gclass("spc-shot",
        {"flex": flex(1, 1, px(260)), "max-width": px(360), "display": FLEX,
         "flex-direction": COL, "gap": gap(12)},
        tablet={"max-width": pct(100)},
        mobile={"flex": flex(1, 1, pct(100)), "max-width": pct(100)}))

    C.append(gclass("spc-shot-img",
        {"display": BLOCK, "width": pct(100), "height": px(300),
         "object-fit": st("cover"), "border-radius": radius(10)},
        tablet={"height": px(250)}, mobile={"height": px(260)}))

    C.append(gclass("spc-shot-cap",
        {"font-family": fnt("font-label"), "font-size": px(15),
         "text-transform": UPPER, "letter-spacing": TRACK_WIDE,
         "color": col("color-slate"), "margin": ZERO}))

    # ---- quote --------------------------------------------------------------
    C.append(gclass("spc-quote",
        {"display": FLEX, "flex-direction": COL, "gap": gap(16),
         "align-items": START, "border-width": bwidth(3, 0, 0, 0),
         "border-style": SOLID, "border-color": col("color-lime"),
         "padding": pad(24, 0, 0, 0)}))

    C.append(gclass("spc-quote-text",
        {"font-family": fnt("font-display"), "font-size": px(23),
         "line-height": LH_TIGHT, "color": col("color-white"),
         "margin": ZERO, "max-width": px(640)},
        tablet={"font-size": px(21)}, mobile={"font-size": px(19)}))

    C.append(gclass("spc-quote-by",
        {"font-family": fnt("font-label"), "font-size": px(13),
         "text-transform": UPPER, "letter-spacing": TRACK_WIDER,
         "color": col("color-lime"), "margin": ZERO}))

    # ---- panels -------------------------------------------------------------
    C.append(gclass("spc-panel",
        {"display": FLEX, "flex-direction": COL, "gap": gap(24),
         "align-items": START,
         "background": background(color=col("color-white")),
         "border-width": bwidth(1, 1, 1, 1), "border-style": SOLID,
         "border-color": col("color-line-light"),
         "border-radius": radius(20), "padding": pad(48, 48, 48, 48)},
        tablet={"padding": pad(32, 32, 32, 32)},
        mobile={"padding": pad(24, 24, 24, 24),
                "border-radius": radius(10)}))

    C.append(gclass("spc-panel-dark",
        {"background": background(color=col("color-navy-deep")),
         "border-color": col("color-line")}))

    C.append(gclass("spc-panel-col",
        {"flex": flex(1, 1, px(380))},
        tablet={"flex": flex(1, 1, px(320))}))

    # ---- hours --------------------------------------------------------------
    C.append(gclass("spc-hours",
        {"display": FLEX, "flex-direction": COL, "gap": gap(8),
         "width": pct(100)}))

    C.append(gclass("spc-hours-row",
        {"display": FLEX, "align-items": CENTER,
         "justify-content": st("space-between"), "gap": gap(16),
         "border-width": bwidth(0, 0, 1, 0), "border-style": SOLID,
         "border-color": col("color-line-light"),
         "padding": pad(0, 0, 8, 0)}))

    C.append(gclass("spc-hours-day",
        {"font-family": fnt("font-label"), "font-size": px(17),
         "text-transform": UPPER, "letter-spacing": TRACK_WIDE,
         "color": col("color-slate"), "margin": ZERO}))

    C.append(gclass("spc-hours-time",
        {"font-family": fnt("font-body"), "font-size": px(17),
         "color": col("color-ink"), "margin": ZERO}))

    # ---- contact ------------------------------------------------------------
    C.append(gclass("spc-big-phone",
        {"font-family": fnt("font-display"), "font-size": px(38),
         "color": col("color-ink"), "margin": ZERO},
        tablet={"font-size": px(30)}, mobile={"font-size": px(25)}))

    C.append(gclass("spc-big-phone-light", {"color": col("color-white")}))

    C.append(gclass("spc-row-tight",
        {"display": FLEX, "flex-wrap": WRAP, "gap": gap(16)}))

    C.append(gclass("spc-map-slot",
        {"display": FLEX, "align-items": CENTER, "justify-content": CENTER,
         "min-height": px(320), "border-width": bwidth(1, 1, 1, 1),
         "border-style": st("dashed"), "border-color": col("color-steel"),
         "border-radius": radius(10),
         "background": background(color=col("color-cloud")),
         "padding": pad(32, 32, 32, 32)}))

    C.append(gclass("spc-map-label",
        {"font-family": fnt("font-mono"), "font-size": px(15),
         "line-height": LH_BODY, "color": col("color-slate"),
         "margin": ZERO, "text-align": CENTER}))

    # Empty on purpose: the Contact page's working form drops in here.
    C.append(gclass("spc-form-slot",
        {"width": pct(100), "min-height": px(160)}))

    return C


# Highest CSS priority first. Modifier classes must beat the base classes
# they are combined with, whatever order an element lists them in.
PRIORITY_FIRST = [
    "spc-on-dark", "spc-ink",
    "spc-panel-dark", "spc-chip-dark", "spc-big-phone-light",
    "spc-service-flip", "spc-map-label",
    "spc-lead-light", "spc-lead-dark", "spc-copy-light", "spc-copy-dark",
    "spc-eyebrow-light", "spc-eyebrow-dark",
    "spc-split-top", "spc-hero-home",
]


def order(classes):
    ids = ["g-" + n for n in PRIORITY_FIRST]
    rest = [c["id"] for c in classes if c["id"] not in ids]
    known = {c["id"] for c in classes}
    return [i for i in ids if i in known] + rest
