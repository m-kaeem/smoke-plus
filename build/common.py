"""Page fragments shared by every page."""
from tree import div, heading, para, button, image

U_HOME = "{{URL:home}}"
U_SERVICES = "{{URL:services}}"
U_GALLERY = "{{URL:gallery}}"
U_ABOUT = "{{URL:about}}"
U_CONTACT = "{{URL:contact}}"
TEL = "tel:+16072370051"


def eyebrow(text, tone):
    """The lime rule plus its label. `tone` is 'dark' or 'light'."""
    return div(["spc-eyebrow"], [
        div(["spc-rule"]),
        para(["spc-eyebrow-text", "spc-eyebrow-" + tone], text, tag="span"),
    ])


def section(tone, shell_classes, children):
    return div(["spc-section", "spc-section-" + tone], [
        div(["spc-shell"] + shell_classes, children)
    ], tag="section")


def page_head(tone_label, title, lead):
    """The dark banner every inner page opens with."""
    return div(["spc-section-ink"], [
        div(["spc-shell", "spc-page-head"], [
            eyebrow(tone_label, "light"),
            heading(["spc-h1", "spc-on-dark"], title, tag="h1"),
            para(["spc-lead", "spc-lead-light"], lead),
        ])
    ], tag="section")


def bullets(items, text_classes=("spc-list-text",)):
    return div(["spc-list"], [
        div(["spc-list-item"], [
            div(["spc-list-bullet"]),
            para(list(text_classes), t),
        ]) for t in items
    ])


def notice(head, text):
    return div(["spc-notice"], [
        para(["spc-notice-head"], head),
        para(["spc-notice-text"], text),
    ])


def cta(title, label, href):
    return div(["spc-cta"], [
        heading(["spc-cta-title"], title),
        div(["spc-button-row"], [button(["spc-button-outline"], label, href)]),
    ])
