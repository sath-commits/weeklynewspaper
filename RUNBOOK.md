# Weekly runbook (instructions for Claude)

This is what Claude follows to make one issue. A parent can kick it off by saying
"Make this week's issue following RUNBOOK.md". Follow it top to bottom.

## 0. Read the profile
Read `PROFILE.md`. It decides the paper's name, the reader's level, which pages exist,
the heritage and local pages, topics to skip and the house style. Where the profile is
blank, use the defaults in this file.

## 1. Setup
```
pip install -r requirements.txt          # add --break-system-packages on a managed Linux box
playwright install chromium              # only if the build can't launch a browser
```
The build also needs `pdftoppm` and `pdfinfo` (poppler-utils; `brew install poppler` on a Mac).

## 2. Research (last 7 days only)
Use parallel research subagents if you have them, all launched at once (a cheaper model
such as Sonnet is fine for research). One per news section in the profile, for example:
(a) world conflicts and diplomacy, (b) elections, health, climate, (c) science, space,
animals and nature, (d) tech, AI, business and money, (e) the heritage page, (f) the local page.

Each researcher returns, per story: headline, date, a 3-6 sentence summary, importance 1-5,
and a free-to-read URL that actually loaded. Verify every fact with a search or a fetch.
Keep each researcher to about 25 searches.

## 3. Write the issue
Create `issues/YYYY-MM-DD.py` (date = the Monday the paper is for) as a standalone file.
Use `examples/sample-issue.py` as the model for block types, page grids and copy style.

**Depth per news page:** 1 lead (120-170 words), 2-5 medium stories (40-80 words),
1 briefs box (4-8 one-liners). Pitch it at the reader level in the profile.

**QR codes:** 12-16 per issue, 1-2 per news page, only on big stories worth a deeper read.
Never on briefs. Only free, non-paywalled URLs that loaded. Skip QR codes entirely if the
profile says the reader has no tablet or phone.

**Activity pages (defaults):**
- Brain Gym: ONE sudoku (new `seed` every week) + 3 chess puzzles (use `mate_in_one` /
  `mate_line` so the build proves each answer).
- Make & Think: origami (alternate the built-in "cup" and "fox" models), 6 brain teasers,
  1 logic grid puzzle (check it has exactly one solution), 1 maze (new seed).
- Quiz page: 10 questions from this issue, a word search of 12 words from this week, and
  **every answer in the issue**: quiz, teasers, logic, chess and the sudoku solution
  (`sudoku_key` block with the same seed and givens). Never print an answer on the same
  page as its puzzle.

If space is tight: shrink the quiz first, then drop the logic puzzle.

## 4. Build and check
```
python3 build.py issues/YYYY-MM-DD.py
```
It must end with `QA: all clear`. The build fails if any box overflows, a chess move is
illegal, the sudoku doesn't have exactly one solution, or any QR code doesn't decode from
the printed PDF. Fix overflows by trimming copy or adjusting `rows`.

Then **look at every page PNG in `out/` yourself** before calling it done. QA catches
overflow, not ugliness.

## 5. Deliver
Copy the PDF to `issues/YYYY-MM-DD.pdf`, commit it with the issue file and push, so the
parent can download it from GitHub. Then give the parent a link to it plus a short note of judgment calls: sensitive
stories and how you handled them, anything you couldn't verify, and stories you left out
because of the profile's skip list.

If this run is automated (see AUTOMATION.md), follow the delivery steps in the task prompt.
If anything failed and couldn't be fixed, do not send anything to a printer: tell the parent
what broke instead.
