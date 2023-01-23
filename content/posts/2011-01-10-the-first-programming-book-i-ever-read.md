Title: The First Programming Book I Ever Read
Category: Crappy Articles
Tags: programming
status: draft

Over the holidays someone gave me a copy of the first programming book I ever
read. In rereading it, I found almost as much as when I first experienced it at
nine years old.

![Book cover](|static|/img/content/basic_programming_for_kids.jpg "**BASIC
Programming for Kids** by Roz Ault")

The first thing you need to know is that since it was published in 1983, I
didn't know how to find an interpreter for the code in 1999. All examples were
run via thought experiment. Because of this fact, I think that this book did
more to get me excited about the idea of programming than it did to impart
knowledge. In this way, I think it follows a higher-level version of the "give
a man a fish..." saying.

> This book will teach you how to write simple programs in BASIC for your
> computer. Its purpose, however, is not to make you a programmer. Its purpose
> is to help you understand computers, to think about how computers can help
> you in all kinds of ways, and to discover how much fun you can have when you
> learn how to talk to computers.

## Content

**BASIC Programming for Kids** explains how to write simple BASIC programs for
The Apple II+/e, Atari 400/800, Commodore 64/PET/VIC 20, TI 99/4A, Timex
Sinclair 1000, and TRS-80. (The programs still run in Chipmunk Basic.) The fact
that such a book could be written for ten different platforms is a testament to
the ubiquity of BASIC in personal computers at the time, but the book does
spend a lot of time explaining special cases and how to rewrite the examples so
that they run on some of the platforms. (Apparently the Timex Sinclair 1000 was
an awful machine.)

It begins with a 30-page chapter on how to type and use the prompts on the
various platforms. Then the language is taught over ten chapters, with
exercises at the end of each chapter. There is a final chapter with some
example programs, and then appendices for reference, troubleshooting, editing,
and information about computers in general.

Here's a quick example to refresh your BASIC memory:

    NEW
    10 FOR J = 1 TO 5
    20 PRINT "JUMP";J
    30 FOR C = 1 TO 3
    40 PRINT "CLAP";C
    50 NEXT C
    60 NEXT J
    RUN

After rereading the book cover to cover, I have only two new thoughts. First,
that the author did a good job of conveying the joy of computing to young
readers. Second, that the BASIC language was an awful mess but succeeded for
very good reasons.

## Review: Positive

This is a good book. I'm glad I found it when I went looking for it. Here's an
example that follows a description of what variables are:

> You can put variables in a program, like this:
>
>     NEW
>     10 N = 2
>     20 X = 5
>     30 PRINT N + X
>
> What will that program print? Run it and see if you guessed correctly. Notice
> that lines 10 and 20 don't make anything happen on the screen when you run
> the program. They tell the program to do something _inside_ the computer, but
> only the word PRINT makes a message appear on the screen.
>
> Now change lines 10 and 20 to give the variables some different values.

It's a small, self-contained, understandable example with a concise, complete
explanation and an invitation to experiment. In this way, it mirrors the style
of Zed Shaw's [Learn Python The Hard
Way](http://learnpythonthehardway.com/). It never blames the reader for
being wrong, and in fact seems to encourage the reader to forgive his or her
own mistakes while writing programs.

So yes, it's a good book. But about this BASIC thing...

## BASIC Sucked, But Worse Was Better

Seriously, what is this crap? Specifying a line number for each statement
before the program is finished? REM? _No proper functions?_ How did anyone
survive this?

Oh, the alternative was to use assembly, or to slip into an AI laboratory. Right.

The two great things about BASIC as it existed in personal computers was that
it was _extremely_ simple, and it was _everywhere_. Ault was able to describe
almost the entire language with extensive examples in a hundred pages of large
print, and those pages covered the vast majority of PCs on the market at the
time.

The reason I was able to understand the book without actually using a computer
was because of the simplicity of BASIC and because of Ault's ability to explain
it using terms no more complex than necessary. At this point I should mention
that this book may not actually be the very first programming book I read, but
it was certainly the first one I understood. I really don't remember.

## ...And Also Worse

Before rereading this book, I had mostly forgotten what BASIC really was, and
didn't necessarily agree with the statement that BASIC causes brain damage. Now
I agree wholeheartedly, and I speak from experience. BASIC crippled me for
years.

At its core, BASIC is a crappy way to express a state machine. The syntax
encourages tight, unreadable balls of spaghetti. `GOSUB` is a poor way to break
out functions. Most of the punctuation feels very ad hoc.

I can't help but contrast this mess with Scheme. All other concerns aside,
Scheme makes a great teaching language because there is almost no syntax and
code is inherently hierarchical. Beginners simply learn new words. Everything
else is gravy.

But I didn't learn Scheme, I learned BASIC and stuck with it for about six
years. I went from [TrueBASIC](http://www.truebasic.com/) to [Visual
MacStandardBasic](http://www.vellios.com/2010/06/06/basic-compiler-opensourced/)
to [METAL
BASIC](http://web.archive.org/web/20080321015004/www.iit.edu/~sarimar/GDS/metal.html)
to [BlitzMax](http://www.blitzmax.com/). I would occasionally try to learn a
new language, but would quickly become frustrated with the lack of easy-to-use
IDEs and graphics libraries. (During this period I was writing nothing but
games.)

Languages like METAL BASIC had few features and libraries, but for me that was
as much of a strength as it was a weakness. Rather than spending hours
searching for which giant package to import, I could browse a complete list of
commands less than twenty pages long to find what I needed, modules and
namespaces be damned. When I was done writing a game, I could click "Compile"
and email it to my friends instead of asking them to download Joe Shmoe Player
3000 or tearing my hair out over config files. (For this reason, I think
Processing and BlitzMax are currently the best platforms to learn game
programming with.)

I spent so much time in the game bubble that I missed out on many early
opportunities to learn new language concepts.

## What Everyone Knows Is Wrong Today

Today's popular languages are objectively better than BASIC in every way.
Features, syntax, libraries, the works. But for a kid who wants to write games
by typing into a window and clicking COMPILE or RUN, the language options are
limited to Processing, BlitzMax, and whatever GameMaker uses. None of these
are real-world languages, so anyone starting out with them will not have a
smooth transition to the next stage in their development as a master of
technology.

I won't bother rehashing what others have said about this problem or yearn for
the days of the BASIC-prompt-as-main-interface. I'll just say this: make better
tools, write more books and tutorials.

## Resources

[Invent Your Own Computer Games with Python](http://www.inventwithpython.com/)
is comparable to _BASIC Programming for Kids_. Better, even. Python's tools are
not ideal for children, but they are good enough to teach programming with.

Here are some ways to create games with a good write/run/distribute tool, but
not necessarily with good documentation for those new to programming:

- [Processing](http://www.processing.org/)
- [BlitzMax](http://blitzmax.com/)
- [GameMaker](http://www.yoyogames.com/make)
