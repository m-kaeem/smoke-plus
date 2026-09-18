"""Astra header/footer configuration matching the exported design.

Everything here lands in the `astra-settings` option, i.e. the theme's own
customizer. No stylesheet, no Additional CSS, no child theme.
"""
import json

INK = "#081924"
NAVY_DEEP = "#0D2637"
LIME = "#A8DB1E"
LIME_BRIGHT = "#C6F23E"
WHITE = "#FFFFFF"
MIST = "#C6D4DC"
STEEL = "#8CA0AC"
LINE = "#1D4964"
CAUTION = "#F4D04A"

F_LABEL = "'Barlow Condensed', sans-serif"
F_BODY = "'Barlow', sans-serif"
F_DISPLAY = "'Archivo Black', sans-serif"

TEL = "tel:+16072370051"


def resp(desktop, tablet="", mobile=""):
    return {"desktop": desktop, "tablet": tablet, "mobile": mobile}


def size(desktop, tablet="", mobile="", unit="px"):
    return {"desktop": desktop, "tablet": tablet, "mobile": mobile,
            "desktop-unit": unit, "tablet-unit": unit, "mobile-unit": unit}


def box(t="", r="", b="", l=""):
    return {"top": t, "right": r, "bottom": b, "left": l}


def spacing(d, t=None, m=None, unit="px"):
    return {"desktop": d, "tablet": t or box(), "mobile": m or box(),
            "desktop-unit": unit, "tablet-unit": unit, "mobile-unit": unit}


def bg(color):
    one = {"background-color": color, "background-image": "",
           "background-repeat": "repeat", "background-position": "center center",
           "background-size": "auto", "background-attachment": "scroll",
           "overlay-type": "", "overlay-color": "", "overlay-opacity": "",
           "overlay-gradient": ""}
    empty = dict(one, **{"background-color": ""})
    return {"desktop": one, "tablet": dict(empty), "mobile": dict(empty)}


def extras(transform="", letter_spacing="", ls_unit="em", line_height="",
           decoration=""):
    return {"line-height": line_height, "line-height-unit": "em",
            "letter-spacing": letter_spacing, "letter-spacing-unit": ls_unit,
            "text-transform": transform, "text-decoration": decoration}


def header():
    return {
        # --- layout ---------------------------------------------------------
        "header-desktop-items": {
            "popup": {"popup_content": ["mobile-menu"]},
            "above": {"above_left": [], "above_left_center": [],
                      "above_center": [], "above_right_center": [],
                      "above_right": []},
            "primary": {"primary_left": ["logo"], "primary_left_center": [],
                        "primary_center": ["menu-1"],
                        "primary_right_center": [],
                        "primary_right": ["html-1", "button-1"]},
            "below": {"below_left": [], "below_left_center": [],
                      "below_center": [], "below_right_center": [],
                      "below_right": []},
        },
        "header-mobile-items": {
            "popup": {"popup_content": ["mobile-menu"]},
            "above": {"above_left": [], "above_center": [], "above_right": []},
            "primary": {"primary_left": ["logo"], "primary_center": [],
                        "primary_right": ["button-1", "mobile-trigger"]},
            "below": {"below_left": [], "below_center": [], "below_right": []},
        },

        # --- the bar itself -------------------------------------------------
        "hb-header-bg-obj-responsive": bg(INK),
        "hb-header-main-sep": 3,
        "hb-header-main-sep-color": LIME,
        "hb-header-main-layout-width": "content",
        "hb-header-height": {"desktop": 86, "tablet": 78, "mobile": 68},
        # Astra free reads the row's padding from the section key, not
        # hb-header-spacing (which has no dynamic CSS without Astra Pro).
        "section-primary-header-builder-padding": spacing(
            box(12, 48, 12, 48), box(12, 32, 12, 32), box(12, 20, 12, 20)),
        "hb-header-main-menu-align": "inline",

        # --- logo -----------------------------------------------------------
        "ast-header-responsive-logo-width": resp(94, 82, 67),
        "display-site-title-responsive": resp(False, False, False),
        "display-site-tagline-responsive": resp(False, False, False),

        # --- primary menu ---------------------------------------------------
        "header-menu1-color-responsive": resp(MIST),
        "header-menu1-h-color-responsive": resp(WHITE),
        "header-menu1-a-color-responsive": resp(LIME),
        "header-menu1-font-family": F_LABEL,
        "header-menu1-font-weight": "600",
        "header-menu1-font-size": size(19, 19, 19),
        "header-menu1-font-extras": extras("uppercase", "0.08", "em"),
        "header-menu1-menu-spacing": spacing(box(8, 12, 8, 12)),

        # --- "Open till 10pm" badge ----------------------------------------
        "header-html-1": "● Open till 10pm",
        "header-html-1color": resp(LIME),

        # --- call button ----------------------------------------------------
        "header-button1-text": "Call 607-237-0051",
        "header-button1-link-option": {"url": TEL, "new_tab": False,
                                       "link_rel": ""},
        "header-button1-text-color": resp(INK),
        "header-button1-back-color": resp(LIME),
        "header-button1-text-h-color": resp(INK),
        "header-button1-back-h-color": resp(LIME_BRIGHT),
        "header-button1-font-family": F_LABEL,
        "header-button1-font-weight": "600",
        "header-button1-font-size": size(19, 17, 15),
        "header-button1-font-extras": extras("uppercase", "0.08", "em"),
        "header-button1-padding": spacing(box(16, 24, 16, 24),
                                          box(14, 20, 14, 20),
                                          box(12, 16, 12, 16)),
        "header-button1-border-size": box(0, 0, 0, 0),
        "header-button1-border-radius-fields": spacing(box(4, 4, 4, 4)),

        # --- off-canvas drawer ----------------------------------------------
        "off-canvas-background": {
            "background-color": NAVY_DEEP, "background-image": "",
            "background-repeat": "repeat",
            "background-position": "center center", "background-size": "auto",
            "background-attachment": "scroll", "overlay-type": "",
            "overlay-color": "", "overlay-opacity": "", "overlay-gradient": ""},
        "off-canvas-close-color": WHITE,
        "header-offcanvas-content-alignment": "flex-start",
        "header-mobile-menu-color-responsive": resp(WHITE, WHITE, WHITE),
        "header-mobile-menu-h-color-responsive": resp(LIME, LIME, LIME),
        "header-mobile-menu-a-color-responsive": resp(LIME, LIME, LIME),
        "header-mobile-menu-font-size": size(23, 21, 19),
        "header-mobile-menu-font-family": F_LABEL,
        "header-mobile-menu-font-weight": "600",
        "header-mobile-menu-font-extras": extras("uppercase", "0.08", "em"),
        "header-mobile-menu-submenu-item-border": True,
        "header-mobile-menu-submenu-item-b-size": "1",
        "header-mobile-menu-submenu-item-b-color": LINE,
        "header-mobile-menu-menu-spacing": spacing(box(16, 0, 16, 0)),
        "header-trigger-icon": "menu",
        "mobile-header-toggle-btn-style": "outline",
        "mobile-header-toggle-btn-border-size": box(1, 1, 1, 1),
        "mobile-header-toggle-border-radius-fields": spacing(box(4, 4, 4, 4)),
    }


SHELVES = ("Vapes and disposables", "Glass, hookah and shisha",
           "Phones, cases and repair", "Kratom, cigars and wraps",
           "Incense, ZYN and lighters")

WARNING = ("Age restricted products — You must be 21 or older to buy "
           "tobacco, vape, nicotine or kratom products in New York State. We "
           "card everyone. Bring a valid photo ID. Nicotine is an addictive "
           "chemical.")

META = ("Smoke Plus Cellular · Johnson City, New York · Serving "
        "Broome County since 2022")


def footer():
    cfg = {
        # --- layout: above = 4 columns, primary = notice, below = meta ------
        "footer-desktop-items": {
            "above": {"above_1": ["widget-1"], "above_2": ["widget-2"],
                      "above_3": ["widget-3"], "above_4": ["widget-4"],
                      "above_5": []},
            "primary": {"primary_1": ["html-1"], "primary_2": [],
                        "primary_3": [], "primary_4": [], "primary_5": []},
            "below": {"below_1": ["copyright"], "below_2": ["html-2"],
                      "below_3": [], "below_4": [], "below_5": []},
        },

        # --- rows -----------------------------------------------------------
        "footer-bg-obj-responsive": bg(INK),
        "hba-footer-bg-obj-responsive": bg(INK),
        "hb-footer-bg-obj-responsive": bg(INK),
        "hbb-footer-bg-obj-responsive": bg(INK),

        "hba-footer-column": "4",
        "hba-footer-layout": {"desktop": "4-lheavy", "tablet": "2-equal",
                              "mobile": "full"},
        "hba-footer-layout-width": "content",
        "hba-footer-vertical-alignment": "flex-start",
        "hba-footer-separator": 3,
        "hba-footer-top-border-color": LIME,
        "section-above-footer-builder-padding": spacing(
            box(96, 48, 48, 48), box(64, 32, 32, 32), box(44, 20, 24, 20)),

        "hb-footer-column": "1",
        "hb-footer-layout": {"desktop": "full", "tablet": "full",
                             "mobile": "full"},
        "hb-footer-layout-width": "content",
        "hb-footer-main-sep": 0,
        "section-primary-footer-builder-padding": spacing(
            box(0, 48, 32, 48), box(0, 32, 24, 32), box(0, 20, 24, 20)),

        "hbb-footer-column": "2",
        "hbb-footer-layout": {"desktop": "2-equal", "tablet": "2-equal",
                              "mobile": "full"},
        "hbb-footer-layout-width": "content",
        "hbb-footer-separator": 1,
        "hbb-footer-top-border-color": LINE,
        "section-below-footer-builder-padding": spacing(
            box(24, 48, 32, 48), box(24, 32, 32, 32), box(20, 20, 24, 20)),

        # --- the notice ------------------------------------------------------
        "footer-html-1": WARNING,
        "footer-html-1color": resp(MIST),
        "footer-html-1-alignment": resp("left"),

        # --- bottom line -----------------------------------------------------
        "footer-copyright-editor": META,
        "footer-copyright-color": STEEL,
        "footer-copyright-alignment": resp("left", "left", "left"),
        "footer-html-2": "Smokpluswholesale@gmail.com",
        "footer-html-2color": resp(STEEL),
        "footer-html-2-alignment": resp("right", "right", "left"),
    }

    # --- the four columns ----------------------------------------------------
    for i in (1, 2, 3, 4):
        cfg["footer-widget-%d-title-color" % i] = resp(LIME)
        cfg["footer-widget-%d-color" % i] = resp(MIST)
        cfg["footer-widget-%d-link-color" % i] = resp(MIST)
        cfg["footer-widget-%d-link-h-color" % i] = resp(WHITE)
        cfg["footer-widget-%d-font-family" % i] = F_LABEL
        cfg["footer-widget-%d-font-weight" % i] = "600"
        cfg["footer-widget-%d-font-size" % i] = size(13)
        cfg["footer-widget-%d-text-transform" % i] = "uppercase"
        cfg["footer-widget-%d-content-font-family" % i] = F_BODY
        cfg["footer-widget-%d-content-font-size" % i] = size(17)
        cfg["footer-widget-alignment-%d" % i] = resp("left")

    # The brand column's blurb is quieter than the link columns.
    cfg["footer-widget-1-color"] = resp(STEEL)
    return cfg


def widgets():
    """Classic widgets, so Astra's own widget-title styling applies."""
    return {
        "media_image": {
            2: {"attachment_id": 32, "url": "", "title": "",
                "caption": "", "alt": "Smoke Plus Cellular", "align": "none",
                "size": "custom", "width": 220, "height": 145,
                "link_type": "none",
                "link_url": "", "image_classes": "", "link_classes": "",
                "link_rel": "", "link_target_blank": False,
                "image_title": ""},
        },
        "text": {
            2: {"title": "",
                "text": "One stop on Main Street for vapes, glass, hookah, "
                        "kratom, cigars, phones and phone repair. Walk in, ask "
                        "for what you want, pay less than you expect.",
                "filter": True, "visual": True},
            3: {"title": "On the shelves",
                "text": "\n".join(SHELVES),
                "filter": True, "visual": True},
            4: {"title": "Find us",
                "text": "607-237-0051\n\n215 Main St\nJohnson City, NY 13790"
                        "\n\nMon to Fri, 8am to 10pm\nSat and Sun, 9am to 10pm"
                        "\nOpen every holiday",
                "filter": True, "visual": True},
        },
        "nav_menu": {
            2: {"title": "Pages", "nav_menu": 2},
        },
    }


SIDEBARS = {
    "footer-widget-1": ["media_image-2", "text-2"],
    "footer-widget-2": ["nav_menu-2"],
    "footer-widget-3": ["text-3"],
    "footer-widget-4": ["text-4"],
}


def build():
    cfg = {}
    cfg.update(header())
    cfg.update(footer())
    return {"settings": cfg, "widgets": widgets(), "sidebars": SIDEBARS}


if __name__ == "__main__":
    json.dump(build(), open("out/astra.json", "w"), separators=(",", ":"))
    print("astra.json written")
