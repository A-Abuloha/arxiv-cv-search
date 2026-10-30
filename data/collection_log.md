# Collection log

Collected on 25 October 2026 with `src/collect.py` (arXiv API).
120 newest papers per query, primary category cs.CV only, duplicates removed → 430 papers.

| Query | Papers | Date range |
|---|---|---|
| `cat:cs.CV AND abs:"object detection"` | 109 | Sep – Oct 2026 |
| `cat:cs.CV AND abs:"image segmentation"` | 114 | Jul – Oct 2026 |
| `cat:cs.CV AND abs:"image generation"` | 104 | Oct 2026 |
| `cat:cs.CV AND abs:"medical image analysis"` | 103 | Mar – Oct 2026 |

Date ranges come from the arXiv IDs (YYMM = submission year and month).

Page counts come from each paper's PDF (counted with pymupdf in `src/add_pages.py`):
347 long (10+ pages), 54 medium (7–9), 29 short (6 or fewer). 6-page papers are counted as short.