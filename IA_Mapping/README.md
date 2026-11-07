# IA_Mapping: Phase 2 Information Architecture

Phase 2 of the Weber State class registration redesign. Builds on the Phase 1 Usability Audit in this repository.

| Folder | Contents |
| --- | --- |
| `01_card_sort/` | Card deck (`card_deck.csv`, `card_deck_printable.pdf`), facilitator protocol, raw participant data (`raw_data/`), analysis script, and generated similarity matrix, cluster diagram, and consensus summary (`analysis_output/`) |
| `02_sitemap/` | Current and revised sitemaps (SVG and PNG) |
| `03_user_flows/` | User flow diagrams for the two critical tasks |
| `04_wireframes/` | Wireframe exports with keyboard tab order and ARIA annotations |
| `05_semantic_html/` | Semantic HTML landmark skeletons for the primary layouts |

## Traceability

Every card in the deck lists the Phase 1 finding it came from (`card_deck.csv`, column `phase1_source`), so each part of the revised IA can be traced back to an observed problem.

## Reproducing the Analysis

```
cd IA_Mapping/01_card_sort
python3 analyze_card_sort.py
```

Requires Python 3 with pandas, numpy, scipy, and matplotlib.
