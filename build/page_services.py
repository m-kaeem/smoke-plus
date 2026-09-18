"""The Services page."""
from tree import div, heading, para, button, image
from classes import IMG
from common import (eyebrow, section, page_head, bullets, notice, cta,
                    U_GALLERY, U_CONTACT, TEL)

SERVICES = [
    ("01", "unnamed.jpg", "Vapes and disposables",
     "The disposable case runs the length of the front counter. VIHO, Kumi, "
     "Lost Mary, JUUL and Geek Bar, in the flavors people actually come back "
     "for. If you are trying to get off cigarettes, tell us and we will talk "
     "you through it instead of selling you the biggest box.",
     ["Disposables from 5,000 to 50,000 puffs",
      "Pod systems and replacement pods",
      "E liquid and salt nicotine",
      "Coils, batteries and chargers",
      "Mods, tanks and spare glass"],
     "Ask what is in stock", U_CONTACT, False),

    ("02", "unnamed (14).jpg", "Glass, hookah and shisha",
     "Four walls of glass, from cheap silicone pieces that survive a drop to "
     "heavy beakers and rigs. Full hookah setups with hoses, bowls and "
     "charcoal, and shisha by the tin in every flavor we can get our hands "
     "on.",
     ["Water pipes, beakers and rigs",
      "Hand pipes, bubblers and silicone",
      "Full hookahs, hoses, bowls and charcoal",
      "Shisha tins, Eternal Smoke, Starbuzz and Mazaya",
      "Grinders, screens, torches and cleaner"],
     "See the glass wall", U_GALLERY, True),

    ("03", "unnamed (19).jpg", "Phones, accessories and repair",
     "The cell side is a real repair counter, not a rack of cases. Screens, "
     "batteries and back glass are done in store, usually the same day. We "
     "buy and sell used iPhones and we can put you on a prepaid line before "
     "you leave.",
     ["Screen, battery and back glass repair",
      "Buy and sell used iPhones",
      "Prepaid plans and SIM activation",
      "Cases, screen protectors, cables and chargers",
      "Earbuds, speakers, controllers and televisions"],
     "Get a repair quote", U_CONTACT, False),

    ("04", "unnamed (6).jpg", "Kratom, cigars and wraps",
     "Kratom in powder, capsules and extract from Klarity, Remarkable Herbs "
     "and OPMS. Premium cigars in the humidor, cigarillos by the box, and "
     "about every wrap, cone and paper brand we can fit on a shelf.",
     ["Kratom powder, capsules and extracts",
      "Premium cigars and cigarillos",
      "Zig Zag, Game, Show and Rillo wraps",
      "RAW, Elements and Bob Marley papers and cones",
      "Cigarettes, ZYN and nicotine pouches"],
     "Call about a brand", TEL, True),
]

ALT = {
    "unnamed.jpg": "Disposable vape case with VIHO, Kumi and Lost Mary",
    "unnamed (14).jpg": "Glass rigs, bongs and hookahs on wooden shelving",
    "unnamed (19).jpg": "Cell phone counter with cases, cables and accessories",
    "unnamed (6).jpg": "Kratom powders, capsules and extracts on the shelf",
}

EXTRAS = ["Wild Berry incense", "Candles and burners", "Lighters and torches",
          "Detox drinks", "Hair and body care", "Energy shots", "Sunglasses",
          "Bluetooth speakers", "Gaming accessories", "Snacks and gum",
          "Lottery"]


def service_row(num, img, title, copy, points, label, href, flip):
    cls = ["spc-service"] + (["spc-service-flip"] if flip else [])
    return div(cls, [
        div(["spc-service-media"], [
            image(["spc-service-img"], IMG[img]),
        ]),
        div(["spc-service-body"], [
            para(["spc-card-num"], num),
            heading(["spc-h2", "spc-ink"], title),
            para(["spc-copy", "spc-copy-dark"], copy),
            bullets(points),
            div(["spc-button-row"], [
                button(["spc-button-outline"], label, href)]),
        ]),
    ])


def build():
    return [
        page_head("What we do", "Four counters, one shop",
                  "Everything below is on the shelf at 215 Main St. Nothing "
                  "here ships and we do not deliver, so come in and we will "
                  "pull it down for you."),

        section("paper", [], [service_row(*s) for s in SERVICES]),

        section("ink", ["spc-stack-5"], [
            eyebrow("Also on the shelves", "light"),
            heading(["spc-h2", "spc-on-dark"],
                    "The stuff people forget we carry"),
            div(["spc-chips"],
                [para(["spc-chip", "spc-chip-dark"], t, tag="span")
                 for t in EXTRAS]),
        ]),

        section("paper", ["spc-stack-6"], [
            notice("ID required, every time",
                   "Tobacco, vape, nicotine and kratom products are sold to "
                   "customers 21 and over only. We card everyone, including "
                   "regulars. Bring a valid photo ID."),
            cta("Not sure if we have it? One call settles it",
                "607-237-0051", TEL),
        ]),
    ]
