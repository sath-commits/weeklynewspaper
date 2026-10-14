# Making it run every week on its own (optional)

You don't need this to start. Make a few issues by hand first (README, "Quick start"),
tune your `PROFILE.md`, and only then automate.

## What the automated version does
1. A scheduled Claude task fires once a week (e.g. Friday 5am).
2. It clones your copy of this repo, reads `RUNBOOK.md` and `PROFILE.md`, researches,
   writes and builds the issue, and checks every page.
3. It emails you a preview with the PDF.
4. Optionally, it schedules a second email to your printer's email-print address a few
   hours later, so you can cancel if you spot a problem in the preview.

## What you need
- **Claude with scheduled tasks and a code environment** (Claude Code on the web, or the
  Claude app with code and scheduled tasks turned on).
- **Your own copy of this repo** on GitHub, connected to Claude.
- **A way to send email with an attachment**, through a Claude connector such as Resend
  or Gmail. The PDF is about 2 MB.
- **(Optional) a printer email address.** Many home printers (Epson, HP, Canon and others)
  have an email-print feature in their app: anything emailed to that address gets printed.
  Turn it on in your printer's app and allow your sending address.

## The task prompt
Create a scheduled task with a prompt like this. Fill in the bits in brackets. Your email
addresses live here, not in the repo.

```
Build and deliver this week's issue of [PAPER NAME].

1. Attach and clone the repo [your-github-user]/[repo-name] with push access.
2. Read PROFILE.md and RUNBOOK.md and follow RUNBOOK.md top to bottom.
3. The issue date is the Monday after today. Research news from the last 7 days only.
4. The build must finish with "QA: all clear" and you must look at every page image.
   If anything can't be fixed, do NOT email the printer. Email me what broke instead.
5. On success: commit issues/<date>.py and push it. Then email [your email] a preview
   with the PDF attached and a short list of judgment calls.
6. [Optional] Schedule a second email with the same PDF to [printer email-print address]
   for [Friday 2pm], and put that email's ID in the preview so I can cancel it.
```

## Tips from running it
- **Do the preview-then-print gap.** A few hours lets you catch a story you'd rather your
  kid didn't read.
- **Cost:** research is most of the work. Running research on a cheaper model (e.g. Sonnet)
  and the writing and checks on a stronger one keeps usage sensible.
- **Email-print comes out single-sided** on most printers. Re-feed pages if you want double-sided.
