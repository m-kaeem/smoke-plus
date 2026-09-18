"""The About page."""
from tree import div, heading, para, button, image
from classes import IMG
from common import eyebrow, section, page_head, TEL

STORY = [
    "Ishaq Mohamed opened the shop in 2022 with a simple idea. People were "
    "driving to one place for a vape and another place to get a phone screen "
    "fixed, so he put both under one roof at 215 Main St.",
    "He had already spent more than ten years in the business before that, "
    "which is how he knows what sells and what sits on a shelf collecting "
    "dust. That is why the walls here are full and the prices are lower than "
    "the chains on the same street.",
    "Five of us work the counters now. We card everyone, we answer questions "
    "straight, and we would rather point you at the right product than the "
    "expensive one.",
]

VALUES = [
    ("01", "Straight prices",
     "One price on the shelf, the same for everyone, no haggling required to "
     "get a fair number."),
    ("02", "Real selection",
     "If it is a brand people in Broome County ask for, we try to keep it in "
     "stock instead of ordering it later."),
    ("03", "Honest answers",
     "Ask what something does or whether you need it. We will tell you, even "
     "when the answer is no."),
]

STATS = [("5", "On the team"), ("10+", "Years of experience"),
         ("2022", "Year we opened"), ("Yes", "Licensed, insured and bonded")]

HOURS = [("Monday to Friday", "8:00am to 10:00pm"),
         ("Saturday", "9:00am to 10:00pm"),
         ("Sunday", "9:00am to 10:00pm"),
         ("Holidays", "Open, every one of them")]


def build():
    return [
        page_head("About us", "A Main Street shop, run by the owner",
                  "Smoke Plus Cellular has been on Main Street in Johnson "
                  "City since 2022. Same owner, same counters, same reason "
                  "people keep coming back."),

        section("paper", [], [
            div(["spc-split", "spc-split-top"], [
                div(["spc-split-col"], [
                    eyebrow("How it started", "dark"),
                    heading(["spc-h2", "spc-ink"],
                            "Two trips turned into one stop"),
                ] + [para(["spc-copy", "spc-copy-dark"], p) for p in STORY]),
                div(["spc-split-col"], [
                    image(["spc-service-img"], IMG["unnamed (21).jpg"]),
                ]),
            ])
        ]),

        section("ink", ["spc-stack-7"], [
            div(["spc-quote"], [
                para(["spc-quote-text"],
                     "Best prices in town. That is the whole pitch, and we "
                     "hold to it."),
                para(["spc-quote-by"], "Ishaq Mohamed, owner"),
            ]),
            div(["spc-row"], [
                div(["spc-card-feature"], [
                    para(["spc-card-num"], num),
                    heading(["spc-h3", "spc-on-dark"], title, tag="h3"),
                    para(["spc-copy", "spc-copy-light"], text),
                ]) for num, title, text in VALUES
            ]),
        ]),

        section("navy", ["spc-stack-6"], [
            eyebrow("The team and the paperwork", "light"),
            div(["spc-row"], [
                div(["spc-stat"], [
                    para(["spc-stat-num"], n),
                    para(["spc-stat-label"], label),
                ]) for n, label in STATS
            ]),
        ]),

        section("paper", [], [
            div(["spc-split", "spc-split-top"], [
                div(["spc-split-col"], [
                    div(["spc-panel", "spc-panel-col"], [
                        eyebrow("Hours", "dark"),
                        div(["spc-hours"], [
                            div(["spc-hours-row"], [
                                para(["spc-hours-day"], day),
                                para(["spc-hours-time"], time),
                            ]) for day, time in HOURS
                        ]),
                    ])
                ]),
                div(["spc-split-col"], [
                    div(["spc-panel", "spc-panel-col"], [
                        eyebrow("Where to find us", "dark"),
                        para(["spc-big-phone"], "215 Main St"),
                        para(["spc-copy", "spc-copy-dark"],
                             "Johnson City, NY 13790. Street parking out "
                             "front, next door to the barbershop. Customers "
                             "come to us, we do not deliver."),
                        div(["spc-button-row"], [
                            button(["spc-button-outline"], "Call the shop",
                                   TEL)]),
                    ])
                ]),
            ])
        ]),
    ]
