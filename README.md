# Weekly Newspaper for Kids

A real weekly newspaper for your kid, printed at home: actual news from the past week
explained for their age, plus three pages of puzzles. Claude does the research and writing;
the code here does the layout, cartoons, puzzles and quality checks.

| Front page | Science page | Puzzle page |
|---|---|---|
| ![Front page](docs/page-01.png) | ![Science page](docs/page-04.png) | ![Puzzle page](docs/page-10.png) |

Full 12-page sample: [examples/sample-issue.pdf](examples/sample-issue.pdf)

## What's in an issue
- **9 news pages:** world, science and space, animals, tech and AI, money, plus a heritage
  page and a local page you choose. Every fact is checked against a real article that week.
- **QR codes** on the bigger stories, so kids can read the full article on a tablet.
- **3 activity pages:** sudoku, chess puzzles, origami, brain teasers, a logic puzzle, a maze,
  a quiz on that week's news and a word search. All answers on the last page.
- **Cartoon mascots** with tips and jokes throughout.

The build checks itself: it fails if any text overflows its box, any chess answer is wrong,
the sudoku has more than one solution, or a QR code doesn't scan from the printed page.

## How to use it
**New here? Follow [GETTING-STARTED.md](GETTING-STARTED.md).** It walks you through it
step by step, no coding needed:

1. Make your own private copy of this repo
2. Fill in [`PROFILE.md`](PROFILE.md) about your kid
3. Connect GitHub to Claude Code
4. Ask Claude to make this week's issue
5. Download the PDF, read it, print it
6. Give feedback so next week fits better

To have it arrive every week without asking, see [AUTOMATION.md](AUTOMATION.md).

## Building by hand (if you like code)
```
pip install -r requirements.txt
playwright install chromium
python3 build.py examples/sample-issue.py
```
Needs Python 3.10+ and poppler (`brew install poppler` / `apt install poppler-utils`).
Output lands in `out/`: the PDF plus a PNG of every page.

## What's where
| File | What it is |
|---|---|
| `GETTING-STARTED.md` | Step-by-step setup for parents. Start here. |
| `PROFILE.md` | Your kid and your paper. The only file most parents edit. |
| `RUNBOOK.md` | Step-by-step instructions Claude follows each week. |
| `AUTOMATION.md` | Optional: weekly schedule, preview email, auto-print. |
| `examples/sample-issue.py` | A complete real issue, used as the model for new ones. |
| `issues/` | Your issues go here: the issue file and its PDF, one pair per week. |
| `build.py` | Layout engine, PDF render and QA checks. |
| `lib/art.py` | Mascots, illustrations and icons. Ask Claude to add new ones. |
| `lib/widgets.py` | Chess boards, sudoku, maze, word search, origami diagrams. |
| `lib/style.css` | The look: colours, fonts, boxes. |

## Good to know
- **It's only as good as your feedback.** The first issue will be close but not right.
  Two or three rounds of "more of this, less of that" gets it there.
- **Read it before your kid does,** at least for the first few weeks. Real news includes
  wars and disasters; the rules keep it factual and non-graphic, but you know your kid.
- Fonts are from Google Fonts (SIL Open Font License).
