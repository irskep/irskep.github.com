Title: How I use git
Category: Articles
Slug: how-i-use-git
Tags: programming
Status: draft

When you use a tool for a long time, it can be easy to forget what it was like
to learn it for the first time. It becomes routine. As someone who passed this
point with git long ago, I thought it might be helpful to share my day-to-day
workflow in case someone wandering around the internet finds it helpful.

# Vocabulary

To understand this post you need to know what these words mean in the git
universe:

* Staging area
* Commit
* Amend
* Rebase
* Clone
* Branch
* Checkout

# My employer's git workflow

I work at Hipmunk. We use a rebase-and-squash workflow. this means that when
a pull request has been reviewed, the tests pass, and it's ready to go
"into production," all the commits from the branch are combined into one and
added as a single commit on the master branch, with the pull request
description as the commit message.

So this:

```
master:         [a]--->[b]--->[c]--->[d]
                   \
feature branch:     \->[e]--->[f]
```

Becomes this:

```
master:         [a]--->[b]--->[c]--->[d]--->[ef]
```

Most people use merges instead:

```
master:         [a]--->[b]--->[c]--->[d]-->[g]
                   \                     /
feature branch:     \->[e]--->[f]-------/
```

But we don't.

# Git remote setup

There are three git clones I care about:

* The canonical one at `github.com/Hipmunk/blah`. This is `upstream`.
* My GitHub clone at `github.com/irskep/blah`. This is `origin`.
* My local clone.

# Starting work on a new feature

The very first thing I do every time is `git fetch upstream`, to make sure I
make my new branch from the latest `master`. Then I
`git clone upstream/master -b BRANCH_NAME`.

For features, I name my branches like `pr/feature-name`. The `pr/` prefix
means this branch is meant to eventually be a pull request on GitHub, as
opposed to a scratchpad, merge of some unfinished demo code, or release branch.

Example:

```sh
git fetch upstream && git clone upstream/master -b pr/fix-the-bug
# I actually have that command aliased to "gbn", so in reality I type:
# gbn pr/fix-the-bug
```

## Git command recap

* `git fetch upstream` to make sure local clone of `upstream` is up to date
* `git checkout upstream/master -b BRANCH` creates a new branch starting from
  the `HEAD` of the `master` branch of the local `upstream` clone

# Working on the feature

I commit frequently, and I amend my commits frequently. My rules for committing
are:

* Always read the entire diff before staging. This means either running
  `git diff` before `git add .`, or staging with `git add -p .` to get only
  the changes I want.
* If code is for testing or debugging only, commit it without any other
  changes in the same commit. When I no longer need it, revert the commit.
* If I have written out a complete idea, and the code compiles, commit without
  executing it. Try to give commits descriptive names that define what should
  and should not be in the commit.
* If I run the code and it doesn't work, and I then fix the bug, then either
  amend the commit that introduced the bug immediately, or create a commit that
  refers to the buggy commit in its description.
* Commits containing unit tests should only contain the new tests, or fixes for
  bugs found by those tests. I don't have a good reason for doing this, it's
  just what I do most often.
* Code review feedback is in bite-sized pieces at the end.

When I feel like I'm ready to step back and either do somethinking or open a
pull request, I run `git rebase -i upstream/dev` to fix any issues with my
commit history.

Here's an example workflow:

```sh
# gbn = git fetch upstream && git checkout -b upstream/master $1
gbn pr/account-settings-loading-state
# ... work ...
git add -p .  # stage everything relevant. I alias this to `gap`.
git commit -m "Add loading state to account settings screen"
# ... run, find bug ...
git add -p .  # stage the bug fix
# this amends the most recent commit without prompting to change
# the message:
git commit --amend -CHEAD # I alias this to `gcaa`.
# ... write tests ...
git commit -am "Write tests"  # I admit this is what I really write.
# I alias gcam to `git commit -am` to save typing.
# ... run tests, find bug, fix bug
git diff    # check diff
git add .   # diff was fine, stage everything
git commit -m 'Fix initial implementation'
# Done, tests pass! Now to fix the history:
git rebase -i upstream/master
    # That will open a text editor containing these lines:
    pick 0abc Add loading state to account settings screen
    pick 5xyz Write tests
    pick qrs4 Fix initial implementation

    # I edit it to look like this:
    pick 0abc Add loading state to account settings screen
    fixup qrs4 Fix initial implementation
    pick 5xyz Write tests

    # Save and quit.
    # Now my commit history looks like this:
    e351 Add loading state to account settings screen
    facb Write tests
```

## Git command recap

* `git add -p` opens an interactive interface for adding lines to the staging
  area.
* `git commit -m` turns the staging area into a commit with the given message.
* `git commit --amend -CHEAD` amends the latest commit to include the changes
  in the staging area without altering the commit message.
* `git commit -am` adds all change to the staging area (except untracked files)
  and creates a new commit with the given message.
* `git diff` shows all unstaged changes (except untracked files).
* `git add .` adds all changes, including untracked files, to the staging area.
* `git rebase -i ANCESTOR` lets you interactively reorder, omit, and
  combine all commits in the current branch back to `ANCESTOR`.
   
# Getting sidetracked

If I'm working on a task but notice something else that needs to be done, I'm
not always disciplined about staying on track. If I do decided to wander out of
scope for my current branch, here's what I do:

```sh
# starting on pr/original-branch...
git add -p .  # stage everything that matters to this branch
git checkout -b pr/distraction
# Develop pr/distraction using normal workflow
git rebase -i upstream/master
    # Using interactive rebase, I remove all commits from pr/original-branch,
    # keeping only the ones I added after creating pr/distraction.
```

Now I can open a pull request containing only the changes from
`pr/distraction`, and avoid creating a huge, badly-scoped diff! And I can
`git checkout pr/original-branch` to keep working on what I was before.

# Keeping up to date

When working quickly on a small team, it's not uncommon to need to rebase
on `upstream/master` to get the latest version of an API or fix a conflict.
The first step of this process is just `git rebase upstream master`.

But what if there's a conflict? Forget opening a text editor and dealing
with all those `<<<<<<<<<<` garbage lines. Instead, I do this:

```sh
git mergetool -t opendiff  # aliased to `gmto`
```

This uses Apple's graphical diff tool. Press Command+D to scroll to the next
conflict. Use the bottom right option control to choose different resolutions,
or manually edit the bottom area yourself.

# Getting ahead of myself

At Hipmunk, we try to keep patches small so that reviewers can do their best
work. But I'm an impatient person, so I'll often write the first half of a
feature, like the data models, open a pull request for that, and start working
on the second half, like the UI, before the first pull request has been
reviewed and committed.

Let's say the first pull request is for `pr/account-page-data-models`. There
are two commits:

```
aaa: Account page data models
bbb: Account page data model tests
```

On a branch starting at that point, `pr/account-page-ui`, we add three commits:

```
ccc: Account page view controller
ddd: Account page content
eee: Account page UI tests
```

At this point, we check our email and see that `pr/account-page-data-models`
has some code review feedback we need to address. So take care of that:

```sh
git checkout pr/account-page-data-models
# type type type
git commit -am "Address code review feedback"
```

At that point, the reviewer approves the pull request, and we commit
`pr/account-page-data-models` to `upstream/master`.

Now we are in a pickle, because `upstream/master` has ONE commit for the
first set of changes, but our branch `pr/account-page-ui` has TWO commits for
the same changes! If we `git fetch upstream && git rebase upstream/master`,
we will almost certainly have conflicts.

```
upstream/master:
    fff: PR #1234 Account page data models + tests
pr/account-page-ui:
    aaa: Account page data models
    bbb: Account page data model tests
    ccc: Account page view controller
    ddd: Account page content
    eee: Account page UI tests
```

I have two strategies for dealing with this situation. One is more
straightforward and has more steps. The other is more confusing and has
fewer steps.

## The straightforward version

```sh
git checkout pr/account-page-ui
git rebase -i aaa^  # rebase starting at aaa's parent
    pick aaa
    fixup bbb
    pick ccc
    pick ddd
    pick eee: Account page UI tests
```

By squashing all commits from the first pull request, we end up with a commit
whose diff is identical to the one in `upstream/master`, so a rebase no longer
reports conflicts.

## The confusing version

When `git rebase upstream/master` reports conflicts, simply `git rebase --skip`
until it succeeds!

This works because conflicts will only appear on commits that ended up as part
of the combined commit.

# A final note about aliases

Almost every command I use daily has an alias. There is no reason to keep
recalling the arcane interface of git. By using aliases, I no longer think of
these commands as "git commant plus necessary options." Instead, I think of
them as single verbs. Who the heck wants to remember "amend the latest commit
with my changes" as `git commit --amend -CHEAD`? What a pain!

Exceptions to the rule for me are `git add` and `git rebase`, which make sense
on their own.

* `gfu`: `git fetch upstream`
* `gcb`: `git checkout upstream/master -b BRANCH`
* `gap`: `git add -p`
* `gcm`: `git commit -m`
* `gcaa`: `git commit --amend -CHEAD`
* `gcam`: `git commit -am`
* `gd`: `git diff`
* `gbn`: `git fetch upstream && gcb $1`