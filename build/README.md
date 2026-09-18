# Elementor v4 build

Generates the Smoke Plus Cellular site from the exported design
(`Smoke Plus Cellular website/Smoke Plus Cellular.dc.html`) as Elementor v4
atomic elements.

- `props.py` — prop-value builders for Elementor's atomic style/settings
  schema, plus the kit's global variable ids.
- `classes.py` — every repeated class from the design as an Elementor global
  class, with tablet/mobile variants and hover states.
- `tree.py` — element-tree builders (`e-div-block`, `e-heading`,
  `e-paragraph`, `e-image`, `e-button`).
- `page_home.py` — the Home page.
- `out/` — generated JSON, applied to WordPress through the Novamira MCP
  endpoint.

Regenerate:

    cd build && python3 -c "import json, classes, page_home; \
      c = classes.build(); \
      json.dump({'items': {x['id']: x for x in c}, 'order': classes.order(c)}, \
                open('out/globals.json','w'), separators=(',',':')); \
      json.dump(page_home.build(), open('out/home.json','w'), separators=(',',':'))"

## Notes

- Sizes cannot be Elementor global variables: `Variables_Service::load()`
  drops `global-size-variable` entries when Elementor Pro is absent, so the
  design's size/spacing custom properties live in global classes instead.
  Colours and font families are global variables.
- Gradient colour stops take `Color_Prop_Type` only, not a global colour
  variable, so the hero scrims use literal rgba values (see `props.LIT`).
