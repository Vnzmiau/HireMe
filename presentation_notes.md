# HireMe — A Failed Project and What I Learned From It

Source material for a presentation. It covers what the project was, how it went, why it failed, and the lessons I took from it into later projects. The focus is on planning, habits and working style rather than code.

---

## 1. What the project was

- **Name:** HireMe (first named "НаемиМе", the Bulgarian for "Hire Me").
- **Idea:** A website for finding workers. Job seekers post an application with their profession, education, work experience and a file such as a CV. Employers browse the applications and send messages to the candidates.
- **Built with:** Python and Django, using a simple SQLite database.
- **Team:** Just me. I planned, designed, coded and tested everything alone.
- **Timeline:** Started on 24 May 2024. The last work was on 18 June 2024, and I never came back to it.

## 2. What actually got built

By the time I stopped, the project had:

- A user account system: register, log in and log out with an email address.
- An "Application" (a job seeker's profile) that could be created, viewed, edited and deleted.
- Messages attached to an application.
- A very basic page layout with a navigation bar.

What was **missing**:

- The home page only said "This is HireMe!".
- The navigation bar still said "MyWebsite". The "Services" and "Contact" links went nowhere, and the browser tab title was "Document".
- There was no page for creating an application. That only worked by sending raw data to the server, which a normal user can't do.
- The Delete and Update buttons on the applications page didn't actually work from the website.
- Nothing separated employers from job seekers, even though the whole idea depended on two kinds of users.
- There was no search or filtering, which is the main thing an employer would need.
- There were no tests and no real description of the project. The README was one line.
- The site was never put online, so nobody except me ever used it.

**Bottom line:** I spent a lot of time on the "engine" of the site and almost none on what a real user would see and use. The project stopped before it became something a person could actually use.

## 3. The story in numbers (from the project history)

| Period | What happened | Commits |
|---|---|---|
| 24–25 May | Created the project; renamed it several times (НаемиМе → HireMe) | 11 |
| 26 May – 13 June | **Nothing: a 3-week gap** | 0 |
| 14–18 June | Almost all of the real work, crammed into 5 days | 61 |

- 72 commits in total. About **85% of the work happened in the last 5 days.**
- Many of those commits were late in the evening, between 9 PM and midnight.
- About a fifth of the first-weekend commits went on renaming the project and its folders, not on building features.
- Commit messages such as "reworked the view because it doesnt work", "fixed an issue in the code" and "fixed some issues" show a lot of trial and error and fixing things after the fact.

## 4. Why it failed (root causes)

### 4.1 No clear plan or definition of "done"
I started coding with only a one-sentence idea: "a website for finding staff". I never wrote down:
- who the users were (job seekers? employers? both?),
- the 3–5 most important things each user must be able to do,
- what the *minimum* finished version looked like.

Because of that, I built whatever seemed next, not what mattered most. The core feature, letting employers find workers, never got built.

### 4.2 Poor time management: procrastination, then cramming
After the first weekend I did nothing for three weeks, then tried to build everything in five days. Cramming led to:
- rushed decisions and code I had to redo ("reworked… because it doesn't work"),
- late-night work, when mistakes are more likely,
- running out of time and energy before the project was usable.

### 4.3 Focusing on the wrong things first
- I spent early energy on things that didn't matter yet, such as the project's name, renaming folders and setup.
- I built the hidden technical parts first and left the user-facing pages for "later". Later never came.
- I built some things more completely than needed, such as several different ways to edit the same data, while the basic pages were missing.

### 4.4 Working completely alone, with no feedback
- Nobody reviewed my work, so nobody pointed out problems early, like buttons that didn't work.
- I had no deadlines from anyone else and nobody to report progress to. That made it easy to put the project off for weeks.
- I never showed the site to a possible user, so I never found out what they actually needed.

### 4.5 Never tested or showed it to anyone
I never checked the site the way a real user would, by clicking through every page. So I didn't notice that key buttons were broken or that some features couldn't be reached from the website at all.

### 4.6 Little documentation
The README was one line, the commit messages were vague and there were no notes on how to run the project. If I came back months later, or someone wanted to help, it would be hard to pick up where I left off. That probably contributed to never coming back.

## 5. What I learned (the main lessons)

1. **Plan before you build.** Write down who the project is for, what the core features are and what "finished" means *before* writing any code. Even a half-page plan would have saved this project.
2. **Start with a small, complete version (MVP).** Build the smallest version a real person can use from start to finish, then add to it. A small finished project beats a big unfinished one.
3. **Work a little every day instead of cramming.** Steady progress beats a last-minute rush. Breaking the work into small tasks with dates makes procrastination harder.
4. **Do the most important thing first.** Don't spend energy on names, logos or extra features before the core works.
5. **When working alone, build in outside feedback.** Show your work to a friend, classmate or teacher early and often. Set your own deadlines and tell someone about them so you're accountable.
6. **Test like a user.** Regularly click through the whole thing as if you were the customer. If a user can't do something, it isn't done.
7. **Write things down.** Clear notes, a proper README and descriptive commit messages help your future self (and others) understand what was done and why.
8. **Know when to cut scope.** When time runs short, cut features rather than quality, and finish *something*.

## 6. How these lessons helped my later projects

How I work differently now:

- **I write a short plan first:** the goal, the users, a list of must-have and nice-to-have features, and a rough schedule.
- **I split the work into small tasks** on a to-do list or task board and tick them off, so I can always see my progress.
- **I aim for a working basic version early** and only then add extras.
- **I spread the work out** over the available time and set mini-deadlines for myself.
- **I show my progress to other people** (classmates, friends, teachers) early to get feedback.
- **I check the project from the user's point of view** before calling anything finished.
- **I keep better notes and write clearer commit messages,** so I can come back to a project easily.

*(Swap in a concrete example from a later project here, e.g. "In my next project, X, I made a plan first and finished on time because…". A real example makes this part much stronger.)*

## 7. Key takeaway

> HireMe didn't fail because the idea was bad or because I couldn't code. It failed because of **how I managed the project**: no plan, no priorities, poor time management and no feedback. Those are exactly the skills I've worked on since, and they've made my later projects more successful.

---

## Suggested presentation structure (for NotebookLM)

1. Title: "HireMe: A Failed Project and What It Taught Me"
2. What the project was and what I wanted it to be
3. What actually got built vs. what was missing
4. Timeline: the 3-week gap and the 5-day cram
5. Why it failed (4–6 root causes)
6. Lessons learned
7. How I apply these lessons now
8. Key takeaway / conclusion
