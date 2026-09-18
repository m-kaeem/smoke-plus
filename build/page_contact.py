"""The Contact page.

The design's form is a visual mockup. In its place the right-hand panel
holds one empty container, id `contact-form`, for a real form widget.
"""
from tree import div, heading, para, button, image
from classes import IMG
from common import eyebrow, section, page_head, notice, cta, U_HOME, TEL

MAP_ADDRESS = "215 Main St, Johnson City NY 13790"

PHOTOS = [("unnamed (20).jpg", "Main Street frontage"),
          ("unnamed (1).png", "The shop lit up at night"),
          ("unnamed (11).jpg", "Behind the front counter")]


def details_panel():
    return div(["spc-panel", "spc-panel-dark", "spc-panel-col"], [
        eyebrow("Phone", "light"),
        para(["spc-big-phone", "spc-big-phone-light"], "607-237-0051"),
        para(["spc-copy", "spc-copy-light"],
             "Best for stock questions, repair quotes and holding something "
             "at the counter."),
        eyebrow("Email", "light"),
        para(["spc-copy", "spc-copy-light"], "Smokpluswholesale@gmail.com"),
        eyebrow("Address", "light"),
        para(["spc-copy", "spc-copy-light"],
             "215 Main St<br>Johnson City, NY 13790"),
        div(["spc-button-row"], [
            button(["spc-button-primary"], "Call 607-237-0051", TEL)]),
    ])


def form_panel():
    return div(["spc-panel", "spc-panel-col"], [
        heading(["spc-h2", "spc-ink"], "Send us a question"),
        # Intentionally empty: drop a working form widget in here.
        div(["spc-form-slot"], [], _cssid={"$$type": "string",
                                           "value": "contact-form"}),
    ])


def build():
    return [
        page_head("Get in touch", "Call the shop",
                  "The phone is the fastest way to reach us. Someone is "
                  "behind the counter from 8am on weekdays and 9am on "
                  "weekends."),

        section("paper", [], [
            div(["spc-split", "spc-split-top"], [
                div(["spc-split-col"], [details_panel()]),
                div(["spc-split-col"], [form_panel()]),
            ])
        ]),

        section("cloud", ["spc-stack-6"], [
            eyebrow("Find the door", "dark"),
            heading(["spc-h2", "spc-ink"],
                    "215 Main St, Johnson City NY 13790"),
            div(["spc-map-slot"], [
                para(["spc-map-label"],
                     "Google Map embed goes here<br>" + MAP_ADDRESS),
            ]),
            div(["spc-row-tight"],
                [image(["spc-strip-img"], IMG[f]) for f, _ in PHOTOS]),
        ]),

        section("paper", ["spc-stack-6"], [
            notice("In store only",
                   "We do not sell online and we do not deliver. Everything "
                   "on this site is bought at the counter at 215 Main St, "
                   "and you must be 21 or older with a valid photo ID for "
                   "age restricted products."),
            cta("Open till 10pm, seven days a week",
                "Back to the top", U_HOME),
        ]),
    ]
