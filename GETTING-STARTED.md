# Getting started: your kid's first issue, step by step

No coding needed. Plan on about 30 minutes for setup and another 20-40 minutes while
Claude makes the first issue.

## What you need
- **A GitHub account** (free): sign up at [github.com](https://github.com).
- **Claude with Claude Code**: open [claude.ai/code](https://claude.ai/code). If it lets you
  start a session, you're set. If not, your Claude plan doesn't include it yet.
- **A colour printer.** Plain paper, normal quality is fine.

---

## Step 1. Make your own copy of this repo
1. At the top of this repo's page, click the green **Use this template** button, then
   **Create a new repository**.
   (No such button? Click **Fork** instead.)
2. Give it a name, e.g. `kids-weekly`.
3. Choose **Private** so your kid's details stay private.
4. Click **Create repository**.

You now have your own copy. Everything from here happens in *your* copy.

## Step 2. Fill in your profile
1. In your copy, click **PROFILE.md**.
2. Click the **pencil icon** (top right of the file) to edit.
3. Replace each `[bracketed hint]` with your answer: paper name, your kid's age and reading
   level, what they love, your heritage page and local page, topics to skip.
   Short plain sentences are fine. Leave anything you're unsure about as it is.
4. Click **Commit changes**, then **Commit changes** again in the pop-up.

## Step 3. Connect GitHub to Claude
1. Go to [claude.ai/code](https://claude.ai/code).
2. When asked, connect your GitHub account and allow access to the repo you just made.
   (You can give access to just that one repo.)

## Step 4. Ask Claude to make the issue
1. Start a new session and pick your repo.
2. Paste this:

   > Make this week's issue following RUNBOOK.md. When it passes QA, save the PDF as
   > issues/YYYY-MM-DD.pdf (the issue date), commit and push it, and tell me the judgment
   > calls you made.

3. Leave it running. It takes 20-40 minutes. You don't need to watch.

## Step 5. Get the PDF and read it first
1. In your repo on GitHub, open the **issues** folder and click the new PDF.
2. Click the **download** button (top right of the preview).
3. **Read it before your kid does**, at least for the first few weeks. It's real news.

## Step 6. Print
Print in colour, normal quality. US Letter size prints fine on A4 paper. Staple the corner
and it's a newspaper.

## Step 7. Make it better each week
After your kid reads it, tell Claude what to change, in plain words. For example:

> Update PROFILE.md: she found the quiz too easy, wants more animals, skip the business page,
> and use shorter sentences. Commit and push.

Two or three rounds of this and it fits your kid. Then each week you just repeat Step 4.

## Step 8 (optional). Make it arrive every week by itself
See [AUTOMATION.md](AUTOMATION.md) to schedule it, get a preview email, and even send it
straight to your printer.

---

## If something goes wrong
- **Claude says QA failed.** Ask it to fix the problems and rebuild. Usually a story is too
  long for its box.
- **Claude can't see my repo.** Go back to Step 3 and make sure the GitHub connection
  includes that repo.
- **No PDF in the issues folder.** Ask Claude: "Did you push the PDF? Push it to issues/."
- **A story isn't right for my kid.** Tell Claude to swap it out and rebuild, and add the
  topic to "Topics to skip" in PROFILE.md so it doesn't come back.
