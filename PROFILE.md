# Your newspaper profile

Fill this in once. Claude reads it every week before writing an issue, so everything
about *your* kid's paper lives here. Plain sentences are fine; delete the hints in
brackets as you go.

> Keep private details (email addresses, printer addresses, your kid's school) out of
> this file if the repo is public. Put them in the weekly task prompt instead (see AUTOMATION.md).

## The paper
- **Paper name:** [e.g. Maya's Weekly, The Kitchen Table Times]
- **Tagline:** [e.g. All the news that's fit to know, for curious minds]
- **Dateline town:** [shown under the masthead, e.g. Bellevue, Washington]
- **Paper size:** [US Letter or A4. Letter prints fine on A4 if that's what's in your printer]
- **Pages:** [12 is the tested default: 9 news + 3 puzzle pages. 8 works for younger kids]

## The reader
- **First name:** [used in the mascots' speech bubbles, optional]
- **Age and reading level:** [e.g. 10, reads well above age. Or: 7, early reader, short sentences please]
- **Loves:** [e.g. space, animals, chess, quizzes, how money works]
- **Not into yet:** [e.g. sports, celebrity news]
- **Has a tablet or phone for QR codes?** [yes / no. If no, Claude leaves QR codes out]

## Sections
[The default 12-page layout is below. Rename, swap or drop pages to suit your kid.]

1. Front page: lead story, week in headlines, word of the week, joke, mascots
2. World: conflicts and diplomacy
3. World: elections, health, climate
4. Science & Space
5. Animals & Nature
6. Tech & AI
7. Business & Money
8. **Heritage page:** [e.g. India & Singapore, Mexico, Korea, Nigeria. Or swap for another topic]
9. **Local page:** [your country + state/city, e.g. USA & Washington state, with stories near Seattle]
10. Brain Gym: sudoku + 3 chess puzzles
11. Make & Think: origami, brain teasers, logic puzzle, maze
12. Quiz, word search, and every answer in the issue

- **Language corner (optional):** [e.g. one Tamil word a week with meaning, in the heritage page. Leave blank to skip]
- **Festivals to count down to (optional):** [e.g. Diwali, Lunar New Year, Eid, Thanksgiving]

## Editorial rules
[These defaults have worked well. Edit any you disagree with.]
- Real, substantive news explained plainly. No filler (minor traffic updates, celebrity gossip).
- Politics strictly neutral: give each side's position, no opinions.
- War and violence: facts only, no graphic detail.
- Every fact comes from an article fetched that week. If it can't be verified, leave it out.
- **Topics to skip:** [e.g. anything about our employer, crime stories, stories that might scare a 7-year-old]
- **Style:** [e.g. no em dashes, British or American spelling]

## Mascots
The paper comes with four cartoon mascots that pop up with tips and jokes:
Scoop the fox, Bolt the robot, Prof. Hoot the owl and Mayil the peacock.
- **Keep them?** [yes / rename them / ask Claude to draw new ones in lib/art.py]
