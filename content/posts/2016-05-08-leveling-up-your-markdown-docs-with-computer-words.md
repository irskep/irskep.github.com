Title: Leveling up your Markdown docs with Computer Words
Category: Articles
Tags: computerwords
Slug: leveling-up-your-markdown-docs-with-computer-words
Status: draft

Some time ago, you wrote some useful code and put it on GitHub with a simple
Markdown readme. In the spirit of open source, you and others added to it
over time, updating the readme with each change. Eventually, you split your
documentation up into several Markdown files, perhaps using the GitHub wiki
feature.

If this has happened to you, or you contribute to a similar project, then this
post is for you. I'm going to try to convince you to feed your Markdown files
into [Computer Words](https://steveasleep.com/computerwords), a program that
will turn them into a static web site and provides you with a few useful
authoring tools.

# Why Github + Markdown is popular for docs

1. You know Markdown and don't mind writing it, and that's also true of most
   potential contributors.
2. GitHub renders Markdown files in decent-looking HTML at permanent URLs.

In my opinion, these are must-haves for most projects without full-time
developer support. Ain't nobody got time to learn a new markup language or
deal with lots of configuration.

# But...

The drawbacks break down into two categories.

## Power

1. If you want to link to somewhere in your docs, you have to insert an anchor
   by hand, remember the filename of the target document, and construct a
   correct url that is either (a) relative, and prone to breaking if you move
   the source document, or (b) absolute, reliant on a base URL that is not
   technically guaranteed to remain constant.
2. If you use a wiki, your docs represent "whatever is in master." You can't
   document specific versions of your project without being potentially very
   verbose.
3. Extensibility is limited to what GitHub provides, and they take a
   lowest common denominator approach. If you want to document your APIs
   as source code docstrings, Python- or JSDoc-style, you can't include that
   information without an external tool and workflow. (In which case, might
   as well use mine!)
4. You can't use core features of the web. To have really good docs, you need
   to be able to add CSS, and sometimes JavaScript.
5. You have to write out your navigation markup manually in every place you
   want it to appear. There's no navigation sidebar. (And no, the GitHub
   wiki alphabetical order document list doesn't count.)

## Wishy washy moralizing

1. You are giving GitHub control over your URLs and perpetuating their
   monopoly on open source hosting. Having the canonical Git repo there is
   one thing; depending on them to host your user-facing materials
   indefinitely is riskier. In my opinion, you should own your URLs.
2. GitHub branding on your project is tacky.

# What you should do instead

Put your docs in a folder, install Computer Words, write a very short config
file, and use it to generate a static site you can host anywhere you like. By
doing this, you solve every single problem listed above.
