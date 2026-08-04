# Section 17 — Git & Version Control

> **Senior Flutter / Mobile Engineer — Interview Prep**
> For **remote** and **Bangladesh (BD)** company interviews.
> Every answer is in **simple English**, **fully explained step by step**, and **linked** so you can jump around and prepare gradually. Commands shown as you'd actually type them.

---

## How to use this section

Each question has the same shape:

- **Short answer (say this)** — the 2–3 sentence reply to say first in the interview.
- **Let's understand it fully** — a step-by-step explanation with real commands.
- **Why interviewers ask** · **Common mistake** · **Follow-ups they may ask**
- **Related** — jump to connected questions · **Back to top** — return to the index.

Each question is tagged with how often it is asked (**Very common / Common / Deeper**) and its difficulty (**Easy / Medium / Hard**).

> **Interview tip:** For Git, explain *what the command does to your history* (the commit graph), not just the syntax. Knowing *why* `rebase` rewrites history is the senior signal.

---

<a id="toc"></a>

## Table of Contents

**A. Everyday commands**
1. [Core commands (init/clone/status/add/commit/push/pull)](#q1) · *Very common*
2. [Branching (create/switch/delete)](#q2) · *Very common*
3. [`fetch` vs `pull`](#q3) · *Common*

**B. Combining work**
4. [`merge` vs `rebase`](#q4) · *Very common*
5. [Resolving merge conflicts](#q5) · *Very common*
6. [`cherry-pick`](#q6) · *Common*

**C. Undoing & fixing**
7. [`reset` — soft / mixed / hard](#q7) · *Very common*
8. [`revert` vs `reset`](#q8) · *Common*
9. [Undo the last commit (keep changes)](#q9) · *Common*
10. [`stash`](#q10) · *Common*

**D. History & debugging**
11. [`log` & `blame`](#q11) · *Common*
12. [`bisect` — find the bad commit](#q12) · *Deeper*
13. [Detached HEAD](#q13) · *Deeper*

**E. Workflows & team**
14. [`.gitignore` (Flutter entries)](#q14) · *Common*
15. [Git Flow vs GitHub Flow vs Trunk-Based](#q15) · *Common*
16. [Conventional Commits](#q16) · *Common*
17. [Squashing commits](#q17) · *Common*
18. [Pull Requests & code review](#q18) · *Very common*
19. [Hotfix on production](#q19) · *Common*

**Quick links:** [How to prepare gradually](#study-plan) · [Cheat Sheet (last-night review)](#cheatsheet)

---

<a id="study-plan"></a>

## How to prepare gradually (study plan)

**Stage 1 — The daily basics (start here).**
→ [Q1 Core commands](#q1) · [Q2 Branching](#q2) · [Q3 fetch vs pull](#q3)

**Stage 2 — Combining and fixing.**
→ [Q4 merge vs rebase](#q4) · [Q5 Conflicts](#q5) · [Q7 reset](#q7) · [Q9 Undo last commit](#q9)

**Stage 3 — Undo tools & history.**
→ [Q8 revert vs reset](#q8) · [Q10 stash](#q10) · [Q11 log & blame](#q11)

**Stage 4 — Team workflows.**
→ [Q15 Branching strategies](#q15) · [Q16 Conventional commits](#q16) · [Q18 PRs & review](#q18) · [Q19 Hotfix](#q19)

**Stage 5 — The deeper tools.**
→ [Q6 cherry-pick](#q6) · [Q12 bisect](#q12) · [Q13 Detached HEAD](#q13) · [Q17 squash](#q17)

**Short on time?** Review [Q1](#q1) · [Q2](#q2) · [Q4](#q4) · [Q5](#q5) · [Q7](#q7) · [Q9](#q9), then the [Cheat Sheet](#cheatsheet).

---

# A. Everyday commands

---

<a id="q1"></a>
## 1. What do `git init`, `clone`, `status`, `add`, `commit`, `push`, and `pull` do?

> Very common · Easy

**Short answer (say this):**
"These are the everyday commands. `init` starts a repo, `clone` copies a remote one. `status` shows what changed, `add` stages changes, `commit` saves them to history. `push` sends commits to the remote, `pull` brings remote commits down. The flow is: edit → add → commit → push."

**Let's understand it fully:**

**Step 1 — The mental model: three areas.**
- **Working directory** — your files as you edit them.
- **Staging area (index)** — changes you've marked to include in the next commit (`add`).
- **Repository** — the saved history of commits (`commit`).

**Step 2 — Starting a repo.**

```bash
git init               # turn the current folder into a new Git repo
git clone <url>        # copy an existing remote repo (with its history)
```

**Step 3 — The daily cycle.**

```bash
git status             # what changed / what's staged
git add file.dart      # stage one file  (git add . = stage everything)
git commit -m "feat: add login"   # save staged changes to history
git push               # upload commits to the remote (e.g. GitHub)
git pull               # download + merge remote commits into your branch
```

**Step 4 — A commit is a save point.**
Think of a commit as a labeled save point in a video game — you can always go back to it. Each commit records *what* changed, *who* changed it, and *when*.

**Why interviewers ask:** It's the absolute baseline; they confirm you understand the staging → commit → push flow.

**Common mistake:** Confusing `add` (stage) with `commit` (save). `add` only marks changes; `commit` records them.

**Follow-ups they may ask:**
- *"add vs commit?"* → `add` stages; `commit` saves the staged changes.
- *"What does a commit store?"* → A snapshot, an author, a message, and a link to its parent commit.

**Related:** [Q2 — branching](#q2) · [Q3 — fetch vs pull](#q3)

[↑ Back to top](#toc)

---

<a id="q2"></a>
## 2. How do you create, switch to, and delete a branch?

> Very common · Easy

**Short answer (say this):**
"A branch is a separate line of work so you can build a feature without touching the main code. You create and switch with `git switch -c name`, move between branches with `git switch`, and delete a merged branch with `git branch -d`. The modern commands are `switch` and `restore`; older tutorials use `checkout`."

**Let's understand it fully:**

**Step 1 — A real-life picture: a parallel workspace.**
A branch is like a copy of the project where you can experiment freely. If it works, you merge it back; if not, you delete it — main stays safe.

**Step 2 — The commands.**

```bash
git branch                 # list branches
git switch -c feature/login   # create AND switch to a new branch
git switch main            # switch back to main
git branch -d feature/login   # delete a merged branch (-D to force)
git push -u origin feature/login  # push the new branch to the remote
```

(`git checkout -b feature/login` is the older equivalent of `switch -c`.)

**Step 3 — Why branches matter.**
They let many people work in parallel without stepping on each other, and keep `main` always releasable. You merge a finished branch back via a Pull Request ([Q18](#q18)).

**Why interviewers ask:** Branching is fundamental to team workflows; they confirm you work in branches, not directly on main.

**Common mistake:** Committing straight to `main`. Real teams protect `main` and merge via reviewed branches.

**Follow-ups they may ask:**
- *"switch vs checkout?"* → `switch`/`restore` are the newer, clearer commands; `checkout` does both jobs (and more), which is confusing.

**Related:** [Q15 — branching strategies](#q15) · [Q18 — pull requests](#q18)

[↑ Back to top](#toc)

---

<a id="q3"></a>
## 3. What is the difference between `git fetch` and `git pull`?

> Common · Easy–Medium

**Short answer (say this):**
"`fetch` downloads the latest commits from the remote but doesn't change your working branch — it just updates your knowledge of the remote. `pull` does a `fetch` and then immediately merges those changes into your current branch. So `pull = fetch + merge`."

**Let's understand it fully:**

**Step 1 — `fetch` — look, don't touch.**

```bash
git fetch          # download remote commits; your files are unchanged
git log origin/main   # you can now inspect what's new before merging
```

`fetch` is safe — it never changes your working files. It just updates the remote-tracking branches (`origin/main`).

**Step 2 — `pull` — fetch and merge in one step.**

```bash
git pull           # = git fetch + git merge origin/<branch>
```

This updates your current branch immediately. Convenient, but it can create a surprise merge or conflict.

**Step 3 — When to use which.**
- **`fetch`** when you want to review remote changes first (safer).
- **`pull`** when you just want to get up to date quickly.
- `git pull --rebase` replays your local commits on top of the remote ones, keeping history linear (see [rebase](#q4)).

**Why interviewers ask:** It tests whether you understand that `pull` quietly merges, which can surprise you.

**Common mistake:** Thinking `fetch` updates your files (it doesn't), or `pull`-ing onto uncommitted changes and getting a messy conflict.

**Follow-ups they may ask:**
- *"What is `origin`?"* → The default name for the remote you cloned from.

**Related:** [Q1 — core commands](#q1) · [Q4 — merge vs rebase](#q4)

[↑ Back to top](#toc)

---

# B. Combining work

---

<a id="q4"></a>
## 4. What is the difference between `git merge` and `git rebase`? When do you use each?

> Very common · Medium

**Short answer (say this):**
"Both combine work from two branches, but differently. `merge` joins them with a new merge commit, keeping the true history (branches visibly came together). `rebase` replays your commits on top of another branch, making a clean, linear history — but it rewrites your commits. The golden rule: never rebase commits you've already shared/pushed."

**Let's understand it fully:**

**Step 1 — `merge` — joins, keeps history.**

```bash
git switch main
git merge feature   # creates a merge commit tying the two histories together
```

History shows the branch split and came back — honest, but can look busy.

**Step 2 — `rebase` — replays, makes it linear.**

```bash
git switch feature
git rebase main     # moves feature's commits to sit on top of latest main
```

It looks as if you started your work *after* the latest main — a clean straight line. But the commits are *rewritten* (new IDs).

**Step 3 — The picture.**

```
merge:                 rebase:
  A---B---C main         A---B---C main
       \   \                      \
        D---E feature              D'--E' feature (replayed on top)
```

**Step 4 — The golden rule.**
**Never rebase commits that others already have** (e.g. pushed to a shared branch). Rebase rewrites history, so it would break everyone else's copy. Rebase *local, unpushed* work; merge shared branches.

**Why interviewers ask:** It's the classic Git judgment question — clean history vs safety.

**Common mistake:** Rebasing a shared/pushed branch and force-pushing, breaking teammates' history.

**Follow-ups they may ask:**
- *"Why does rebase change commit IDs?"* → It creates new commits with the same changes but new parents, so the hashes differ.
- *"pull --rebase?"* → Fetches then rebases your local commits on top — keeps history linear.

**Related:** [Q5 — conflicts](#q5) · [Q3 — fetch vs pull](#q3) · [Q17 — squash](#q17)

[↑ Back to top](#toc)

---

<a id="q5"></a>
## 5. What causes a merge conflict, and how do you resolve one step by step?

> Very common · Medium

**Short answer (say this):**
"A conflict happens when two branches change the *same lines* of the same file in different ways, so Git can't decide which to keep. You resolve it by opening the marked file, choosing the correct final code, removing the conflict markers, then staging and committing. Tests after resolving are essential."

**Let's understand it fully:**

**Step 1 — A real-life picture.**
Two people edit the same sentence in a shared document. The system can't know which version is right, so it asks a human (you) to decide.

**Step 2 — What a conflict looks like.**

```
<<<<<<< HEAD
final color = Colors.blue;     // your version
=======
final color = Colors.green;    // their version
>>>>>>> feature
```

**Step 3 — Resolve it step by step.**

```bash
# 1. Git tells you which files conflict
git status

# 2. Open each file, pick the correct final code, and DELETE the
#    <<<<<<<, =======, >>>>>>> marker lines.

# 3. Stage the resolved file
git add lib/theme.dart

# 4. Finish the merge
git commit          # (or: git rebase --continue if rebasing)

# 5. Run the app/tests to confirm nothing broke
```

**Step 4 — Make conflicts rarer.**
Pull/rebase often (small, frequent merges), keep branches short-lived, and keep functions small so two people are less likely to touch the same lines.

**Why interviewers ask:** Everyone hits conflicts; they want to see you resolve them calmly and correctly, not panic or `--force`.

**Common mistake:** Leaving a `<<<<<<<` marker in the file (it breaks the build), or blindly accepting one side without checking the logic.

**Follow-ups they may ask:**
- *"How to abort?"* → `git merge --abort` (or `git rebase --abort`) returns to the state before you started.

**Related:** [Q4 — merge vs rebase](#q4) · [Q10 — stash](#q10)

[↑ Back to top](#toc)

---

<a id="q6"></a>
## 6. What is `git cherry-pick`, and when would you use it?

> Common · Medium

**Short answer (say this):**
"`cherry-pick` copies one specific commit from another branch onto your current branch, without merging the whole branch. You use it to grab a single fix — for example, applying a bug fix to a release branch without bringing along everything else from main."

**Let's understand it fully:**

**Step 1 — A real-life picture: picking one cherry.**
Instead of taking the whole tree (a full merge), you pick exactly one cherry (one commit) you want.

**Step 2 — How to use it.**

```bash
git switch release/1.2
git cherry-pick a1b2c3d   # copy that one commit's changes onto this branch
```

It creates a *new* commit on your branch with the same changes (a new ID).

**Step 3 — The common use: backport a fix.**
A critical bug fix was merged to `main`, but you also need it on an older `release` branch that isn't ready to take all of main. Cherry-pick just that fix commit onto the release branch.

**Step 4 — Watch out.**
Cherry-picking the same change onto branches that later merge can create duplicate commits or conflicts. Use it deliberately, for isolated fixes.

**Why interviewers ask:** It tests whether you can move a single change precisely — a real release-management need.

**Common mistake:** Cherry-picking lots of commits instead of merging — that's error-prone; merge/rebase is better for many commits.

**Follow-ups they may ask:**
- *"Cherry-pick vs merge?"* → Cherry-pick grabs one commit; merge brings a whole branch.

**Related:** [Q19 — hotfix](#q19) · [Q4 — merge vs rebase](#q4)

[↑ Back to top](#toc)

---

# C. Undoing & fixing

---

<a id="q7"></a>
## 7. What is the difference between `git reset --soft`, `--mixed`, and `--hard`?

> Very common · Medium

**Short answer (say this):**
"All three move the branch pointer back to an earlier commit; they differ in what they do to your changes. `--soft` keeps changes staged, `--mixed` (the default) keeps them unstaged, and `--hard` throws the changes away entirely. `--hard` is the dangerous one — it deletes work."

**Let's understand it fully:**

**Step 1 — They all rewind history; the difference is your files.**

| Mode | Moves branch back? | Staging area | Working files |
|---|---|---|---|
| `--soft` | yes | keeps changes **staged** | kept |
| `--mixed` (default) | yes | changes become **unstaged** | kept |
| `--hard` | yes | cleared | **discarded (gone)** |

**Step 2 — Examples.**

```bash
git reset --soft HEAD~1    # undo last commit, keep changes staged (re-commit easily)
git reset --mixed HEAD~1   # undo last commit, changes back to unstaged
git reset --hard HEAD~1    # undo last commit AND delete the changes — careful!
```

**Step 3 — The safe mental model.**
- `--soft` / `--mixed` → "undo the commit, keep my work."
- `--hard` → "undo the commit and erase my work." Only use when you're sure.

**Step 4 — Reset rewrites history.**
Like rebase, `reset` changes history — don't reset commits you've already pushed to a shared branch. For shared branches, use `revert` ([Q8](#q8)).

**Why interviewers ask:** It tests precise undo knowledge and awareness that `--hard` destroys work.

**Common mistake:** Running `git reset --hard` and losing uncommitted work. (Sometimes recoverable via `git reflog`, but don't rely on it.)

**Follow-ups they may ask:**
- *"How to recover after a bad reset?"* → `git reflog` shows where HEAD has been; you can reset back to the lost commit.

**Related:** [Q8 — revert vs reset](#q8) · [Q9 — undo last commit](#q9)

[↑ Back to top](#toc)

---

<a id="q8"></a>
## 8. What is `git revert`, and how does it differ from `git reset`?

> Common · Medium

**Short answer (say this):**
"`revert` creates a *new* commit that undoes a previous commit's changes, leaving history intact. `reset` moves the branch pointer backward and rewrites history. So `revert` is the safe choice for shared/public branches, and `reset` is for local cleanup before you've pushed."

**Let's understand it fully:**

**Step 1 — `revert` — undo by adding a new commit.**

```bash
git revert a1b2c3d   # makes a new commit that reverses a1b2c3d's changes
```

History keeps both the original commit and the revert — honest and safe for shared branches.

**Step 2 — `reset` — undo by rewinding history.**

```bash
git reset --hard a1b2c3d   # moves the branch back; later commits vanish from history
```

This rewrites history, so it's unsafe once others have those commits.

**Step 3 — The rule.**

| | `revert` | `reset` |
|---|---|---|
| History | preserved (adds a commit) | rewritten (moves pointer) |
| Safe on shared branches? | **yes** | no |
| Use for | undoing a pushed/public commit | local cleanup before pushing |

**Step 4 — A picture.**
`revert` says "I'll add a new step that cancels the old one." `reset` says "let's pretend the old step never happened." On a team branch, you want the honest, additive `revert`.

**Why interviewers ask:** It tests whether you pick the safe undo for shared history.

**Common mistake:** Using `reset --hard` on a pushed branch and force-pushing, which breaks teammates. Use `revert` there.

**Follow-ups they may ask:**
- *"Revert a merge commit?"* → `git revert -m 1 <merge>` to specify which parent to keep.

**Related:** [Q7 — reset modes](#q7) · [Q19 — hotfix](#q19)

[↑ Back to top](#toc)

---

<a id="q9"></a>
## 9. How do you undo the last commit without losing your changes?

> Common · Easy–Medium

**Short answer (say this):**
"Use `git reset --soft HEAD~1`. It removes the last commit but keeps all your changes staged, so you can fix the message or add more and commit again. If you only want to fix the message or add a forgotten file, `git commit --amend` is even simpler."

**Let's understand it fully:**

**Step 1 — Undo the commit, keep the work.**

```bash
git reset --soft HEAD~1   # last commit undone; changes stay staged
# edit/add more, then:
git commit -m "feat: better message"
```

`HEAD~1` means "one commit before the current one."

**Step 2 — Just fixing the last commit? Use `--amend`.**

```bash
git commit --amend -m "fix: correct typo in message"   # rewrite the last commit
git add forgotten.dart && git commit --amend --no-edit  # add a forgotten file
```

**Step 3 — The caution.**
Both rewrite history. If you already pushed the commit, amending/resetting means you'd need a force-push — only do that on your own branch, never a shared one ([Q8](#q8)).

**Why interviewers ask:** It's an everyday task; they check you know the safe, change-preserving way.

**Common mistake:** Using `git reset --hard HEAD~1` (deletes the changes) when you wanted to keep them — use `--soft`.

**Follow-ups they may ask:**
- *"Amend vs reset?"* → Amend edits the last commit in place; reset removes it and restages the work.

**Related:** [Q7 — reset modes](#q7) · [Q17 — squash](#q17)

[↑ Back to top](#toc)

---

<a id="q10"></a>
## 10. What does `git stash` do, and how do you apply stashed changes?

> Common · Easy

**Short answer (say this):**
"`stash` temporarily shelves your uncommitted changes so you have a clean working directory — useful when you need to switch branches quickly without committing half-done work. You bring the changes back with `stash pop`."

**Let's understand it fully:**

**Step 1 — A real-life picture: a drawer for unfinished work.**
You're mid-feature when an urgent bug comes in. You can't commit half-done code, so you put it in a drawer (stash), fix the bug, then take it back out.

**Step 2 — The commands.**

```bash
git stash             # shelve current changes; working dir is now clean
git switch main       # go fix something
git switch feature
git stash pop         # bring the changes back AND remove them from the stash
```

**Step 3 — Useful variants.**

```bash
git stash list        # see all stashes
git stash apply       # bring back changes but KEEP them in the stash
git stash -u          # also stash untracked (new) files
git stash drop        # delete a stash
```

**Step 4 — When to use it.**
For short interruptions. For longer pauses, a quick commit (even WIP) on a branch is safer than a forgotten stash.

**Why interviewers ask:** It's a common everyday tool; they check you can context-switch cleanly.

**Common mistake:** Forgetting about stashed work (`git stash list` reveals it), or stashing across branches and getting confused about where it applies.

**Follow-ups they may ask:**
- *"pop vs apply?"* → `pop` applies and removes the stash; `apply` keeps it in the stash list.

**Related:** [Q5 — conflicts](#q5) · [Q2 — branching](#q2)

[↑ Back to top](#toc)

---

# D. History & debugging

---

<a id="q11"></a>
## 11. How do you use `git log` and `git blame`?

> Common · Easy

**Short answer (say this):**
"`git log` shows the commit history — who changed what and when. `git blame` shows, line by line, which commit last changed each line of a file. Together they help you understand history and find when and why a line was introduced."

**Let's understand it fully:**

**Step 1 — `git log` — the history.**

```bash
git log --oneline --graph --all   # compact, visual history of all branches
git log -p file.dart              # history with the actual diffs for a file
git log --author="srana"          # commits by a person
```

`--oneline --graph` is the most useful day-to-day view.

**Step 2 — `git blame` — who last touched each line.**

```bash
git blame lib/login.dart          # each line annotated with its last commit + author
```

This is for *understanding*, not blaming people — you use it to find the commit that introduced a line so you can read its message and context.

**Step 3 — A common workflow.**
See a confusing line → `git blame` to find its commit → `git show <commit>` to read why it was added (the message and the full change).

**Why interviewers ask:** Reading history is a core debugging and onboarding skill.

**Common mistake:** Treating `blame` as assigning fault. It's a tool to find *context*, not to point fingers.

**Follow-ups they may ask:**
- *"How do you find when a bug was introduced?"* → `git bisect` ([Q12](#q12)).

**Related:** [Q12 — bisect](#q12) · [Q1 — core commands](#q1)

[↑ Back to top](#toc)

---

<a id="q12"></a>
## 12. How do you find which commit introduced a bug using `git bisect`?

> Deeper · Medium

**Short answer (say this):**
"`git bisect` does a binary search through your history to find the commit that introduced a bug. You mark a known-good commit and a known-bad one, and Git checks out the middle commit for you to test, repeatedly halving the range until it pinpoints the exact bad commit."

**Let's understand it fully:**

**Step 1 — The idea: binary search on commits.**
If the bug appeared somewhere in the last 100 commits, bisect finds it in about 7 steps (log₂ 100), not 100 — by halving each time ([binary search](section11_data_structure_and_algorithm.md#q11)).

**Step 2 — The workflow.**

```bash
git bisect start
git bisect bad                # the current commit is broken
git bisect good v1.0          # this older commit/tag worked

# Git checks out a commit in the middle. Test it, then tell Git:
git bisect good   # if this commit works
git bisect bad    # if it's broken

# Repeat. Git narrows down until it names the first bad commit.
git bisect reset  # when done, return to your branch
```

**Step 3 — Automate it.**
If you have a test script, `git bisect run ./test.sh` runs it on each step automatically — Git finds the bad commit with no manual testing.

**Why interviewers ask:** It tests advanced debugging — and that you can apply binary search to real problems.

**Common mistake:** Hunting commit-by-commit manually when bisect would find it in a handful of steps.

**Follow-ups they may ask:**
- *"Why is it fast?"* → It halves the search range each step — O(log n).

**Related:** [Q11 — log & blame](#q11) · [Q11 (DSA) — binary search](section11_data_structure_and_algorithm.md#q11)

[↑ Back to top](#toc)

---

<a id="q13"></a>
## 13. What is a detached HEAD state? How does it happen, and how do you recover?

> Deeper · Medium

**Short answer (say this):**
"Normally HEAD points to a branch. A 'detached HEAD' means HEAD points directly at a specific commit instead of a branch — usually because you checked out a commit hash or a tag. Any commits you make there aren't on a branch and can be lost. To recover, create a branch from where you are before switching away."

**Let's understand it fully:**

**Step 1 — What 'detached HEAD' means.**
HEAD is "where you are now." Usually it follows a branch (`main`). If you check out a raw commit, HEAD points straight at that commit — there's no branch to save new commits to.

```bash
git checkout a1b2c3d   # now in detached HEAD — HEAD points at the commit, not a branch
```

**Step 2 — Why it's risky.**
If you make commits here and then `switch` to another branch, those commits aren't attached to anything and become hard to find (eligible for cleanup).

**Step 3 — How to recover / use it safely.**

```bash
# If you made commits you want to keep, create a branch right here:
git switch -c my-fix
# Now your commits are safely on the 'my-fix' branch.
```

If you made no commits, just `git switch main` to leave safely.

**Step 4 — When it's intentional.**
It's fine for *looking* at an old commit or tag (read-only). Just don't do important work there without first making a branch.

**Why interviewers ask:** It tests deeper understanding of HEAD, branches, and how commits get "lost."

**Common mistake:** Making commits in detached HEAD, switching away, and losing them. Always branch first.

**Follow-ups they may ask:**
- *"Lost a commit — can you get it back?"* → `git reflog` shows recent HEAD positions; you can branch from the lost commit.

**Related:** [Q2 — branching](#q2) · [Q7 — reset (reflog recovery)](#q7)

[↑ Back to top](#toc)

---

# E. Workflows & team

---

<a id="q14"></a>
## 14. What is `.gitignore`, and what are common Flutter entries?

> Common · Easy

**Short answer (say this):**
"`.gitignore` lists files and folders Git should not track — build outputs, secrets, and machine-specific files. For Flutter, you ignore `build/`, `.dart_tool/`, IDE files, and anything with secrets like `.env` or signing keys. The goal is to keep the repo clean and never commit generated or sensitive files."

**Let's understand it fully:**

**Step 1 — Why ignore files.**
- **Generated** files (build output) just bloat the repo and cause conflicts.
- **Secrets** (API keys, keystores) must never be committed.
- **Machine-specific** files (IDE config) differ per developer.

**Step 2 — A typical Flutter `.gitignore`.**

```gitignore
# Dart/Flutter
build/
.dart_tool/
.packages
.flutter-plugins
.flutter-plugins-dependencies
pubspec.lock        # (apps usually commit this; packages often don't)

# IDE
.idea/
*.iml
.vscode/

# Secrets — never commit these
.env
*.keystore
*.jks
ios/Runner/GoogleService-Info.plist  # if it holds secrets
android/key.properties
```

**Step 3 — If you already committed a secret.**
Adding it to `.gitignore` doesn't remove it from history. You must remove it from history (e.g. `git filter-repo`) **and** rotate the leaked key, because it's still in past commits.

**Why interviewers ask:** It tests basic repo hygiene and security awareness (not committing secrets).

**Common mistake:** Committing `build/` or secrets, then thinking `.gitignore` removes them — it only ignores *untracked* files going forward.

**Follow-ups they may ask:**
- *"Ignore an already-tracked file?"* → `git rm --cached file` to untrack it, then it respects `.gitignore`.

**Related:** [Q20 (Security) — secrets](section_20_mobile_app_security.md#q1) · [Q1 — core commands](#q1)

[↑ Back to top](#toc)

---

<a id="q15"></a>
## 15. Compare Git Flow, GitHub Flow, and Trunk-Based Development.

> Common · Medium

**Short answer (say this):**
"They're branching strategies with different amounts of structure. Git Flow has many long-lived branches (main, develop, feature, release, hotfix) — powerful but heavy. GitHub Flow is simple: branch off main, PR, merge, deploy. Trunk-Based keeps everyone committing to main behind feature flags, with tiny short-lived branches — best for continuous delivery."

**Let's understand it fully:**

**Step 1 — Git Flow — structured, many branches.**
- Branches: `main` (releases), `develop` (integration), plus `feature/`, `release/`, `hotfix/`.
- Good for scheduled releases and versioned software.
- Downside: complex, lots of merging, slower.

**Step 2 — GitHub Flow — simple, PR-based.**
- One main branch; create a short feature branch, open a Pull Request, review, merge, deploy.
- Good for web apps and continuous deployment.
- Simple and fast; the most common team flow.

**Step 3 — Trunk-Based — everyone on main.**
- Very short-lived branches (hours), merged to `main` constantly; unfinished work hidden behind **feature flags**.
- Enables true continuous integration/delivery.
- Needs strong automated tests and feature-flag discipline.

**Step 4 — How to choose.**

| Strategy | Best for | Complexity |
|---|---|---|
| Git Flow | versioned/scheduled releases | high |
| GitHub Flow | most apps, continuous deploy | low |
| Trunk-Based | fast CI/CD, mature teams | medium |

**Why interviewers ask:** It tests team/process awareness for senior roles.

**Common mistake:** Defaulting to heavy Git Flow for a small team that ships continuously, where GitHub Flow is simpler and better.

**Follow-ups they may ask:**
- *"What enables trunk-based?"* → Feature flags + strong automated tests, so incomplete code can live on main safely.

**Related:** [Q2 — branching](#q2) · [Q18 — pull requests](#q18)

[↑ Back to top](#toc)

---

<a id="q16"></a>
## 16. What are Conventional Commits, and why do teams adopt them?

> Common · Easy

**Short answer (say this):**
"Conventional Commits is a standard format for commit messages: a type, an optional scope, and a description — like `feat(auth): add Google login`. Teams adopt it because the consistent format makes history readable and lets tools auto-generate changelogs and version numbers."

**Let's understand it fully:**

**Step 1 — The format.**

```
<type>(<optional scope>): <description>

feat(auth): add Google sign-in
fix(cart): correct total when quantity is zero
docs(readme): update setup steps
refactor(home): extract header widget
```

**Step 2 — The common types.**
- `feat` — a new feature.
- `fix` — a bug fix.
- `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `ci`.

**Step 3 — Why teams adopt it.**
- **Readable history** — you can scan what each commit did.
- **Automated versioning** — tools bump the version: `fix` → patch, `feat` → minor, a `BREAKING CHANGE` → major (semantic versioning).
- **Auto changelogs** — generated from the commit types.

**Step 4 — Keep messages meaningful.**
The description should say *what changed and why* in the imperative ("add", "fix"), not "stuff" or "wip".

**Why interviewers ask:** It signals you care about clean, tool-friendly history — a team-maturity indicator.

**Common mistake:** Vague messages ("update", "fix bug", "asdf") that tell the next reader nothing.

**Follow-ups they may ask:**
- *"How does it link to versioning?"* → Tools map `feat`/`fix`/`BREAKING CHANGE` to minor/patch/major version bumps.

**Related:** [Q18 — pull requests](#q18) · [Q1 — commits](#q1)

[↑ Back to top](#toc)

---

<a id="q17"></a>
## 17. What does it mean to "squash" commits, and when would you do it?

> Common · Medium

**Short answer (say this):**
"Squashing combines several commits into one. You do it to turn a messy work-in-progress history (`wip`, `fix typo`, `try again`) into one clean, meaningful commit before merging. Many teams 'Squash and merge' a Pull Request so each feature becomes a single tidy commit on main."

**Let's understand it fully:**

**Step 1 — Why squash.**
While developing, you make many small messy commits. The rest of the team doesn't need that noise — they want one clear commit that says what the feature did.

**Step 2 — How (interactive rebase).**

```bash
git rebase -i HEAD~3   # edit the last 3 commits
# In the editor, keep the first as 'pick', mark the others as 'squash' (or 's')
# Save → write one combined commit message.
```

**Step 3 — The easy way: Squash and merge.**
On GitHub/GitLab, the "Squash and merge" button on a PR combines all the branch's commits into one when merging — no manual rebase needed. This is the most common approach.

**Step 4 — The caution.**
Squashing rewrites history. Do it on your own feature branch *before* it's merged, not on shared history.

**Why interviewers ask:** It tests whether you keep `main`'s history clean and understand interactive rebase.

**Common mistake:** Squashing already-shared commits, or squashing away useful separation (sometimes a few logical commits are better than one giant one).

**Follow-ups they may ask:**
- *"Squash vs merge commit?"* → Squash = one tidy commit per feature; merge commit = full branch history preserved.

**Related:** [Q4 — rebase](#q4) · [Q18 — pull requests](#q18)

[↑ Back to top](#toc)

---

<a id="q18"></a>
## 18. What are best practices for Pull Requests and code review (as author and reviewer)?

> Very common · Medium

**Short answer (say this):**
"As the author: keep PRs small and focused, write a clear description of what and why, and make sure tests pass. As the reviewer: be timely, kind, and specific — ask questions instead of giving orders, focus on correctness and design over style (let the formatter handle style), and approve once it's good enough, not perfect."

**Let's understand it fully:**

**Step 1 — As the author.**
- **Small and focused** — one concern per PR; big PRs get shallow reviews.
- **Clear description** — what changed, why, and how to test it.
- **Green checks** — tests, lints, and format pass before asking for review.
- **Self-review first** — read your own diff; catch obvious issues.

**Step 2 — As the reviewer.**
- **Be timely** — a blocked teammate is expensive; review promptly.
- **Be kind and specific** — "What happens if the list is empty?" beats "This is wrong."
- **Prioritize** — correctness and design first; don't nitpick style a linter handles.
- **Approve when good enough** — not when perfect; suggest follow-ups for minor things.

**Step 3 — Why small PRs matter.**
A 50-line PR gets a careful review; a 2,000-line PR gets a rubber-stamp "LGTM". Small PRs catch more bugs and merge faster.

**Step 4 — Tone is everything.**
Reviews are about the code, not the person. Questions and suggestions keep it collaborative; commands and "why did you…" feel like attacks.

**Why interviewers ask:** Code review is a daily senior responsibility; they assess your collaboration and judgment.

**Common mistake:** Giant PRs (unreviewable), or reviews that nitpick formatting while missing real design/correctness issues.

**Follow-ups they may ask:**
- *"How big should a PR be?"* → Small enough to review carefully in one sitting — often a few hundred lines or less.

**Related:** [Q16 — conventional commits](#q16) · [Q14 (Clean Code) — enforcing](section_16_clean_code.md#q14)

[↑ Back to top](#toc)

---

<a id="q19"></a>
## 19. How do you handle a hotfix on production while feature branches are in progress?

> Common · Medium

**Short answer (say this):**
"I branch the hotfix directly off the production branch (or the latest release tag), not off in-progress feature work, so the fix contains only the fix. I fix, test, and deploy it, then merge it back into main so the fix isn't lost — or cherry-pick it where needed. Feature branches later pull main to get the fix."

**Let's understand it fully:**

**Step 1 — Branch off production, not off your feature.**
The production code may be different from your half-done feature. Start clean from what's actually live.

```bash
git switch main          # or the release branch/tag that's in production
git switch -c hotfix/login-crash
# fix, commit, test
```

**Step 2 — Deploy the fix fast, then merge it back.**
Ship the hotfix, then make sure it lands in `main` so future releases include it:

```bash
git switch main
git merge hotfix/login-crash   # main now has the fix
git push
```

If an older release branch also needs it, **cherry-pick** the fix commit there ([Q6](#q6)).

**Step 3 — Feature branches catch up.**
In-progress feature branches then `merge main` (or rebase) to pick up the hotfix, so they don't reintroduce the bug.

**Step 4 — Why keep the hotfix isolated.**
A hotfix must be tiny and low-risk. Mixing it with unfinished features makes it risky and slow to deploy — exactly what you can't afford during an incident.

**Why interviewers ask:** It tests real release management under pressure — a senior responsibility.

**Common mistake:** Fixing the bug on a feature branch full of unfinished work, so you can't deploy the fix alone, or forgetting to merge the hotfix back into main (the bug returns next release).

**Follow-ups they may ask:**
- *"How does Git Flow handle this?"* → It has a dedicated `hotfix/` branch off `main`, merged back into both `main` and `develop`.

**Related:** [Q6 — cherry-pick](#q6) · [Q15 — branching strategies](#q15)

[↑ Back to top](#toc)

---

<a id="cheatsheet"></a>

# Cheat Sheet (last-night review)

Read this the morning of your interview. Tables first, then one-line reminders.

## Everyday commands

| Command | Does |
|---|---|
| `git add` / `commit` | stage / save to history |
| `git push` / `pull` | upload / download+merge |
| `git switch -c name` | create + switch branch |
| `git stash` / `stash pop` | shelve / restore changes |

## Undo tools

| Want to... | Use |
|---|---|
| Undo last commit, keep changes | `git reset --soft HEAD~1` |
| Undo a pushed commit safely | `git revert <commit>` |
| Discard all local changes | `git reset --hard` (careful) |
| Fix the last commit | `git commit --amend` |

## merge vs rebase vs reset vs revert

| | Keeps history? | Safe on shared branch? |
|---|---|---|
| merge | yes (merge commit) | yes |
| rebase | no (rewrites) | no |
| reset | no (rewrites) | no |
| revert | yes (new commit) | yes |

## One-line reminders

- Flow: edit → `add` → `commit` → `push`. ([Q1](#q1))
- **`pull` = `fetch` + `merge`**; `fetch` is safe (no file changes). ([Q3](#q3))
- **merge** keeps history; **rebase** makes it linear but rewrites — never rebase shared commits. ([Q4](#q4))
- **Conflict** = same lines changed two ways; resolve, remove markers, `add`, commit. ([Q5](#q5))
- **`reset --hard` deletes work**; `--soft`/`--mixed` keep it. ([Q7](#q7))
- **`revert`** is the safe undo for pushed commits (adds a commit). ([Q8](#q8))
- **Undo last commit, keep work** → `git reset --soft HEAD~1`. ([Q9](#q9))
- **`cherry-pick`** copies one commit (backport a fix). ([Q6](#q6))
- **`bisect`** = binary search for the bad commit. ([Q12](#q12))
- **Detached HEAD** = on a commit, not a branch — `git switch -c` to save work. ([Q13](#q13))
- **GitHub Flow** (branch→PR→merge) suits most teams; Git Flow is heavier. ([Q15](#q15))
- **Conventional Commits** (`feat:`, `fix:`) → readable history + auto versioning. ([Q16](#q16))
- **Small PRs + kind, specific reviews** catch more bugs. ([Q18](#q18))
- **Hotfix** off production, merge back to main. ([Q19](#q19))

[↑ Back to top](#toc)

---

# Practice: how interviewers go deeper

Interviewers probe judgment, not just syntax. Practice out loud:

1. *"merge or rebase here?"* → rebase local cleanup; merge shared branches; never rebase pushed commits.
2. *"You committed a secret — now what?"* → remove from history AND rotate the key; .gitignore alone isn't enough.
3. *"Production is down and your feature is half-done — fix it."* → branch the hotfix off production, deploy, merge back to main.
4. *"Find which commit broke it."* → `git bisect` (binary search), automate with `bisect run`.
5. *"Your PR is 1,500 lines — comfortable reviewing it?"* → no; split into small, focused PRs.

Explaining *what each command does to history* and *which is safe on shared branches* is the senior signal — in both remote and BD interviews.

[↑ Back to top](#toc)
