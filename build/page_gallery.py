"""The Gallery page.

The design's category filter row is client-side JavaScript, which an
atomic build cannot reproduce without a script, so every shot is shown
in one grid instead. Order and captions follow the design's SHOTS list.
"""
from tree import div, para, image
from classes import IMG
from common import eyebrow, section, page_head, cta, U_CONTACT

SHOTS = [
    ("unnamed (12).jpg", "Straight down the middle of the store"),
    ("unnamed (21).jpg", "The front door on Main Street"),
    ("unnamed (1).png", "Lit up at night, open till 10"),
    ("unnamed (20).jpg", "Main Street frontage, parking out front"),
    ("unnamed (11).jpg", "Behind the front counter"),
    ("unnamed.jpg", "The disposable case"),
    ("unnamed (2).jpg", "Glass, silicone and hookah shelf"),
    ("unnamed (15).jpg", "The long glass wall"),
    ("unnamed (17).jpg", "Hookahs and shisha, floor to ceiling"),
    ("unnamed (16).jpg", "Grinders, bags and small glass"),
    ("unnamed (3).jpg", "Shisha stacked by the tin"),
    ("unnamed (9).jpg", "Shisha, candles and incense"),
    ("unnamed (5).jpg", "Wraps, cones and rolling papers"),
    ("unnamed (13).jpg", "Cigarettes, ZYN and pouches"),
    ("unnamed (6).jpg", "Kratom powder, capsules and extracts"),
    ("unnamed (19).jpg", "The cell phone counter"),
    ("unnamed (4).jpg", "Cases, earbuds and televisions"),
    ("unnamed (1).jpg", "Controllers, headsets and TVs"),
    ("unnamed (18).jpg", "Speakers, sunglasses and glass"),
    ("unnamed (7).jpg", "Wild Berry incense rack"),
    ("unnamed (8).jpg", "Hair and body care aisle"),
    ("unnamed (10).jpg", "Lighters and small goods case"),
]


def shot(img, caption):
    return div(["spc-shot"], [
        image(["spc-shot-img"], IMG[img]),
        para(["spc-shot-cap"], caption),
    ])


def build():
    return [
        page_head("Inside the shop", "Every wall, up close",
                  "No stock photos here. This is 215 Main St, shelf by "
                  "shelf, so you know what you are walking into."),

        section("paper", ["spc-stack-6"], [
            div(["spc-shots"], [shot(f, c) for f, c in SHOTS]),
        ]),

        section("cloud", [], [
            cta("Come see the rest of it in person",
                "Get directions", U_CONTACT),
        ]),
    ]
