Title: What It's Like to Write a Sphinx Extension
Tags: programming python sphinx mrjob
Slug: what-its-like-to-write-a-sphinx-extension
Status: draft

Why I wanted to write a Sphinx extension
========================================

As the de facto Director of Documentation for [mrjob](mrjob), I spend a lot of
time dealing with [Sphinx](sphinx)—certainly more time than anyone else. So
more than anyone else, I notice pain points in the process of writing
documentation for mrjob.

[mrjob]: http://pythonhosted.org/mrjob/
[sphinx]: http://sphinx-doc.org/

The pain point I identified most recently was how many places you have to
document a configuration option. You see, almost every option in mrjob can be
set in a config file or on the command line. So it needs to be documented in
the `--help` string, it needs to have a detailed description on the appropriate
doc page, and it needs to appear in the "quick reference" table.

Let's take the `interpreter` option as an example. It's defined as an option in
`mrjob/options.py`:

```
opt_group.add_option(
    '--interpreter', dest='interpreter', default=None,
    help=("Interpreter to run your script, e.g. python or ruby.")),
```

It has an entry in the reference table in `configs-reference.rst`:

```rst
======================================================= ================================================================== ============================== ================
Option                                                  Switches                                                           Default                        Data type
======================================================= ================================================================== ============================== ================
...
:ref:`interpreter <opt_interpreter>`                    :option:`--interpreter`                                            (value of *python_bin*)        |dt-command|
```

(Incomprehensibility of large reStructuredText tables at small column
widths intentionally preserved.)

And finally, it has a description in `configs-all-runners.rst`:

```rst
.. _opt_interpreter:

**interpreter** (:option:`--interpreter`)
    Interpreter to launch your script with. Defaults to the value
    of **python_bin**. Change this if you're using a language
    besides Python 2.5-2.7 or if you're running using
    :py:mod:`virtualenv`.
```

The above block contains (in order): an anchor for the reference table entry to
link to, the config file version of the option in bold, the command line
version of the option in the style of the `option` role (normally italic), and
a description of what the option does.

There are several ways in which the above system of documention an option is
suboptimal.

1. You have to describe the same option in three places. It's tedious and the
   likelihood of leaving a piece of information out of date is high. (In fact,
   I found several out-of-date descriptions while writing my extension.)

2. reStructuredText (hereafter RST) tables are terrible to define and badly
   implemented. `docutils`, the library that generates the HTML from the RST,
   generates a `<colgroup>` element that defines the width of each column based
   on the *number of `=` characters above it in the text definition*. When most
   of your table content is actually just link markup, this implementation
   detail balloons the widths of tables.
   
   Additionally, if you increase the length of the longest option name by
   adding a new option `--with-a-really-long-name`, you have to add whitespace
   to every. single. freaking. table. row.

3. The markup for detailed option descriptions is prone to copy/paste error and
   laziness in formatting on the part of the untrained contributor.

How I improved the situation
============================

I wrote a Sphinx extension that replaces the above process with this one:

1. Describe the command line option in `options.py`.

2. Make sure `.. mrjob-optlist:: all` is somewhere in the documentation, to
   collect all options with `:set: all`. You basically never need to do this.

3. Describe the option on the appropriate doc page with this syntax:

```rst
.. _opt_interpreter:

.. mrjob-opt::
    :config: interpreter
    :switch: --interpreter
    :type: :ref:`string <data-type-string>`
    :set: all
    :default: value of \
      :ref:`python_bin <opt_python_bin>` (``'python'``)

    Interpreter to launch your script with. Defaults to the value
    of **python_bin**, which is deprecated. Change this if you're
    using a language besides Python 2.5-2.7 or if you're running
    using :py:mod:`virtualenv`.
```

And you're done.

I'll be the first to admit that the above syntax still has flaws. But it has a
few key advantages:

1. You don't need to edit the reference table by hand. Fewer duplications of
   text and no idiotic RST tables.

2. You define the different components of the option (config key, command line
   switches, default value) semantically instead of by convention.

In the future, I'd like to have it automatically generate the `opt_X` and
`:type:` links to remove even more manual labor from the process of documenting
options, but this is enough of an improvement that I went ahead and submitted a
[pull request](pr) for it.

[pr]: https://github.com/Yelp/mrjob/pull/702

How I wrote the extension
=========================

This section will describe not only how the code works, but also how I went
about learning how to write Sphinx extensions and how to get the results I
wanted.
