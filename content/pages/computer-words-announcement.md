Title: Why I wrote a new documentation system, and why you might like it
Tags: computer-words
Slug: computer-words-announcement
Date: 2016-04-29

TL;DR [Computer Words](http://steveasleep.com/computerwords)

I write a lot of documentation. I do it for two reasons: I like writing, and I
like to be understood. Documentation is what takes software from “something
`@irskep` put on GitHub” to something you can actually use.

But I’m not happy with the available tools. Open source documentation for young
projects tends to fall into one of three modes if they have it at all:

1. A GitHub wiki
2. A directory of Markdown files
3. A proper web site, but requires a tool no one wants to install or a syntax
   no one knows, except one maintainer

Some ecosystems have good, fairly well known tools (see Python and Sphinx), but
with the prevalence of Markdown and the convenience of hosting Markdown files
on GitHub, I suspect people have been tending toward the solutions with less
friction.

I want it to be easier to produce good documentation sites (without GitHub
branding), with a bare-minimum learning curve and a sky's-the-limit plugin
architecture, so that more projects have  better documentation.

I think I've succeeded. [Computer Words](http://steveasleep.com/computerwords)
is a tool written in Python 3 that lets you turn your [directory of Markdown
files](https://github.com/irskep/computerwords/tree/master/docs) into a
[beautiful web site](http://steveasleep.com/computerwords). It vaguely
resembles [Sphinx](http://www.sphinx-doc.org/en/stable/) in its design, so it
has the potential for powerful plugins, but I did my best to keep it small and
easy to use.

If your docs are currently in Markdown, these features might interest you:

* All extensions use HTML tag syntax, so your editor's syntax highlighting
  won't break. Other tools may or may not like it, depending on how they parse HTML within Markdown.
* Semantic linking. Rather than baking an HTML reference into your links,
  define a `<heading-alias name="blah" />` above any heading and insert a link
  to that heading with the correct name as `<heading-link name="blah" />`.
* Automatic multi-document table of contents auto-generated from your headings.
* A reasonable configuration can be as short as 4 obvious lines copied from the
  Computer Words home page.

If you want to auto-generate docs from a programming language besides Python,
and you are willing to write a docstring parser for your language (in your
language!), I would love to help you. The interchange format is very simple.

If you currently use Sphinx and reStructuredText, you should probably keep
doing that, but you might also want to read the [Related
Work](http://steveasleep.com/computerwords/related_work.html) and [Frequently
Anticipated Criticisms](http://steveasleep.com/computerwords/faq.html) sections
of the docs.
