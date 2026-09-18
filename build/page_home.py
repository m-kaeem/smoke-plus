"""The Home page, rebuilt from the exported design as atomic elements.

Page content only: the hero starts below the theme's navigation and the
closing CTA ends above the theme's footer.
"""
from tree import div, heading, para, button, image
from classes import IMG
from common import (eyebrow, section, bullets, cta,
                    U_SERVICES, U_GALLERY, U_CONTACT, TEL)


def hero():
    return div(["spc-hero", "spc-hero-home"], [
        div(["spc-shell"], [
            div(["spc-hero-inner"], [
                eyebrow("215 Main St, Johnson City NY", "light"),
                heading(["spc-hero-title"], "More than smoke.", tag="h1"),
                para(["spc-lead", "spc-lead-light"],
                     "Vapes, glass, hookah, kratom, cigars, phones and phone "
                     "repair, all on one floor on Main Street. We stock deep "
                     "and we price it to beat the chains up the road."),
                div(["spc-button-row"], [
                    button(["spc-button-primary"], "Call 607-237-0051", TEL),
                    button(["spc-button-ghost"], "See what we carry",
                           U_SERVICES),
                ]),
                div(["spc-hero-strip"], [
                    para(["spc-hero-strip-text"],
                         "Open till 10pm every night", tag="span"),
                    div(["spc-dot-sep"]),
                    para(["spc-hero-strip-text"],
                         "Walk in, no appointment", tag="span"),
                    div(["spc-dot-sep"]),
                    para(["spc-hero-strip-text"], "Cash and card", tag="span"),
                ]),
            ])
        ])
    ], tag="section")


CATEGORIES = [
    ("unnamed.jpg", "Vapes and disposables",
     "A full case of disposables, pods, salt nic and coils in the flavors "
     "people ask for."),
    ("unnamed (2).jpg", "Glass, hookah and shisha",
     "Rigs, beakers, bubblers and full hookah setups, plus shisha by the "
     "tin."),
    ("unnamed (19).jpg", "Phones and repair",
     "Screens, batteries, back glass, cases, prepaid plans and used "
     "iPhones."),
    ("unnamed (6).jpg", "Kratom, cigars and wraps",
     "Powders, capsules, extracts, premium cigars, cigarillos, cones and "
     "papers."),
]


def categories():
    cards = [
        div(["spc-card-cat"], [
            image(["spc-card-cat-img"], IMG[img]),
            div(["spc-card-cat-body"], [
                heading(["spc-card-cat-name"], name, tag="h3"),
                para(["spc-card-cat-text"], text),
            ]),
        ], href=U_SERVICES)
        for img, name, text in CATEGORIES
    ]
    return section("paper", ["spc-stack-6"], [
        eyebrow("Four counters under one roof", "dark"),
        heading(["spc-h2", "spc-ink"],
                "Pick a wall and we will walk you to it"),
        div(["spc-row"], cards),
    ])


FEATURES = [
    ("01", "We price against the whole county",
     "Tell us what you paid somewhere else in Broome County and we will do "
     "what we can to beat it. That is how the shop got busy in the first "
     "place."),
    ("02", "The shelves are actually full",
     "Four walls of glass, a case of disposables, shisha stacked to the "
     "ceiling and kratom in powder or capsules. You are not leaving empty "
     "handed."),
    ("03", "Repairs happen in store",
     "Cracked screen, dead battery, smashed back glass. Bring the phone to "
     "the counter and we quote you before we touch it."),
]


def features():
    cards = [
        div(["spc-card-feature"], [
            para(["spc-card-num"], num),
            heading(["spc-h3", "spc-on-dark"], title, tag="h3"),
            para(["spc-copy", "spc-copy-light"], text),
        ])
        for num, title, text in FEATURES
    ]
    return section("ink", ["spc-stack-6"], [
        eyebrow("Why people skip the chain store", "light"),
        heading(["spc-h2", "spc-on-dark"],
                "Best prices in town, and we mean it"),
        div(["spc-row"], cards),
    ])


REPAIR_POINTS = [
    "Screen, battery and back glass replacement",
    "Charging port and speaker cleanup",
    "We buy and sell used iPhones",
    "Prepaid plans and SIM activation",
    "Cases, protectors, chargers and earbuds",
]


def phone_side():
    return section("paper", [], [
        div(["spc-split", "spc-split-top"], [
            div(["spc-split-col"], [
                eyebrow("The phone side of the shop", "dark"),
                heading(["spc-h2", "spc-ink"],
                        "We fix phones, sell phones and set up your plan"),
                para(["spc-copy", "spc-copy-dark"],
                     "The cell counter sits just inside the front door. Most "
                     "screen and battery jobs are done the same day. We also "
                     "buy and sell used iPhones, so bring the old one in when "
                     "you upgrade."),
                bullets(REPAIR_POINTS),
                div(["spc-button-row"], [
                    button(["spc-button-outline"], "Ask for a repair quote",
                           U_CONTACT),
                ]),
            ]),
            div(["spc-split-col"], [
                image(["spc-service-img"], IMG["unnamed (4).jpg"]),
            ]),
        ])
    ])


STATS = [("2022", "Opened on Main Street"),
         ("5", "People behind the counters"),
         ("10+", "Years in the business"),
         ("14", "Hours open every weekday")]


def stats():
    return section("navy", ["spc-stack-6"], [
        eyebrow("The shop in numbers", "light"),
        div(["spc-row"], [
            div(["spc-stat"], [
                para(["spc-stat-num"], n),
                para(["spc-stat-label"], label),
            ]) for n, label in STATS
        ]),
    ])


STRIP = ["unnamed (15).jpg", "unnamed (3).jpg", "unnamed (5).jpg",
         "unnamed (18).jpg", "unnamed (13).jpg"]


def inside_the_shop():
    return section("paper", ["spc-stack-6"], [
        eyebrow("Inside the shop", "dark"),
        heading(["spc-h2", "spc-ink"], "Have a look before you come in"),
        div(["spc-strip"],
            [image(["spc-strip-img"], IMG[f]) for f in STRIP]),
        div(["spc-button-row"], [
            button(["spc-button-outline"], "See the full gallery", U_GALLERY),
        ]),
    ])


TOWNS = ["Johnson City", "Binghamton", "Endicott", "Endwell", "Vestal",
         "Port Dickinson", "Chenango Bridge", "Conklin", "Broome County"]


def catchment():
    return section("cloud", ["spc-stack-5"], [
        eyebrow("Who comes in", "dark"),
        heading(["spc-h2", "spc-ink"], "Minutes from most of Broome County"),
        para(["spc-copy", "spc-copy-dark"],
             "Parking is right out front on Main Street. People drive in from "
             "all over the area, usually because someone told them about the "
             "prices."),
        div(["spc-chips"],
            [para(["spc-chip"], t, tag="span") for t in TOWNS]),
    ])


def closing_cta():
    return section("paper", [], [
        cta("Call first and we will hold it at the counter",
            "607-237-0051", TEL)
    ])


def build():
    return [hero(), categories(), features(), phone_side(), stats(),
            inside_the_shop(), catchment(), closing_cta()]
