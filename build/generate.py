"""Regenerate out/globals.json and out/<page>.json."""
import json
import classes
import page_home, page_services, page_gallery, page_about, page_contact

PAGES = {
    "home": page_home, "services": page_services, "gallery": page_gallery,
    "about": page_about, "contact": page_contact,
}


def main():
    c = classes.build()
    json.dump({"items": {x["id"]: x for x in c}, "order": classes.order(c)},
              open("out/globals.json", "w"), separators=(",", ":"))
    for slug, mod in PAGES.items():
        tree = mod.build()
        json.dump(tree, open("out/%s.json" % slug, "w"),
                  separators=(",", ":"))
        n = sum(_count(x) for x in tree)
        print("%-9s %2d sections %4d elements" % (slug, len(tree), n))
    print("%d global classes" % len(c))


def _count(n):
    return 1 + sum(_count(x) for x in n["elements"])


if __name__ == "__main__":
    main()
