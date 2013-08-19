Title: How I Made a Realtime Multiplayer Art Piece in 48 Hours, and How It Turned Out
Tags: gamedev programming ludumdare
Slug: we-dreamers-postmortem

We Dreamers is an abstract online sandbox that placed sixth in the Innovation
category of Ludum Dare 26.
[You can play it here.](http://steveasleep.com/we_dreamers_2) It may take a
while for the 4+ MB of user data to download, so give it a minute or two.

Of all my programming escapades over the past couple of years, I'm most proud
of this one. Here's a comprehensive collection of my thoughts about it,
including a discussions of the technical aspects.

## Conception

During the final voting round for Ludum Dare 26, I spent a couple of hours
coming up with good ideas for every possible theme…except minimalism. No way
that would get through, right?

When that theme was chosen, and I had to throw out all of my wonderful schemes,
most of which were single player pseudo-roguelikes. Instead, I picked a vague
idea: a web-based multiplayer world where you dig out rooms underground in a
grid. Maybe there would be shapes and colors and stuff. Genius! I figured out
the rest as I went along.

<iframe width="560" height="315" src="//www.youtube.com/embed/2bmRw-QD1Bs" frameborder="0" allowfullscreen></iframe>

You can do a few things:

1. Move with the arrow keys or WASD.
2. Harvest color with space.
3. Dig out new rooms by bumping into walls. You need color to do this. The new 
   room will be the color of your dot, which is affected by the color in your 
   bucket.
4. Dump color with r, g, and b (or 1, 2, and 3) to change the color of your dot.
5. Leave notes on rooms (if you are level 2) that appear at the bottom of the 
   screen when you enter the room.
6. Put down big block letters (if you are level 3) that you can use to spell 
   [sometimes naughty] words.

You gain levels by adding content. If anyone else is online at the same time as
you, you can see their dot and any content they add, all live-updated.

![screenshot](http://www.ludumdare.com/compo/wp-content/uploads/2013/05/2m-300x207.png)

## Competition results

It placed 6th in the Innovation category out of 2,346 games. The rest of the
category scores aren't as impressive as raw numbers but are still nice in terms
of the number of games:

Category   | Ranking | Score
---------- | --------|------
Innovation | #6      | 4.38
Mood       | #210    | 3.36
Overall    | #238    | 3.51
Audio      | #464    | 2.85
Theme      | #492    | 3.60
Humor      | #549    | 2.23
Graphics   | #650    | 2.92
Fun        | #769    | 2.75

People tend to have one of two viewpoints. They’re either like
[wrongcoder](http://www.ludumdare.com/compo/ludum-dare-26/?action=preview&uid=22915):

> Neat. Quite unique. Technologically a marvel for the available time. To be
> honest, though, I don’t get the purpose of it.

or they’re like [BlennosoftGames](http://www.ludumdare.com/compo/ludum-dare-26/?action=preview&uid=8308):

> There is something very cheerful about this game. As far as I can tell you
> don’t “win” you just smile :)

Most players were in the second category, so I’m very happy with how it turned
out. People seem to understand what I’m trying to do: create a virtual canvas
where contribution is easy, bad behavior is difficult, and quirky things can be
found given a few minutes’ exploration.
[Hegemege](http://www.ludumdare.com/compo/ludum-dare-26/?action=preview&uid=11022)
said it “felt a bit like geocaching,” which really tickles me.

The numbers are encouraging as well. When I checked earlier today, there were
**3,019 rooms dug by 147 users.** 54% of players dug 5 or more rooms, with some
people digging over 100 rooms. 11% had a note on them. 18% had a stamp. So
people were definitely doing more than running around and bumping into walls.

At first I was surprised that more rooms had stamps than notes, since you have
to be level 2 to write a note, and level 3 to place a stamp. But it was pointed
out to me that a stamp is just one letter, and you have to think a lot less to
put one down. Want to spell DOG FART in huge letters? It’s only seven easy
pieces!

I got a friendly nod from a post on [Indie Statik's Ludum Dare
highlights](http://indiestatik.com/2013/04/29/ludum-dare-26/). They compared We
Dreamers to Peter Molyneux’s game Curiosity. I'm not sure if that's a
compliment, but it’s still nice to be noticed. They have a [second highlights
post](http://indiestatik.com/2013/05/02/ludum-dare-25-part-2/) as well.

## Technical details

You might be wondering, like
[StuStutheBloo](http://www.ludumdare.com/compo/ludum-dare-26/?action=preview&uid=20822)
in We Dreamers’s comments, **“How did you even put this together in the time
available?”**

The short answer is that I used [Firebase](https://www.firebase.com/), “a cloud
database designed to power real-time, collaborative applications.” Put another
way, it’s a magic, event-driven Javascript object that updates instantly across
all clients. I didn’t have to write a server, or even deal with much
multiplayer logic at all; I just designed all interactive objects to listen to
Firebase events. The only thing special about the dot you control, as opposed
to those controlled by others and displayed on your screen, is that your client
is updating a Firebase subtree for your data. Those updates are reflected
instantly for you, and very quickly for everyone else.

**If you want to try your hand at a multiplayer online game for Ludum Dare, I
strongly recommend that you try Firebase.** There are half a dozen two-player
games I haven’t been able to rate because I’d need to have another person
sitting next to me to play with. You don’t even need to get all crazy and
realtime – it’s also perfect for turn-based games. I hope to try something
head-to-head next time.

Now for a longer answer to StuStutheBoo’s question. Although Firebase was
essential to having the technical capability to build this kind of online
experience, it was even more important that I knew my tools extremely well. My
day job is to work on [Buildy](http://playbuildy.com/), an online multiplayer
realtime building sandbox where you can make just about anything. For LD26, I
brought out the same tools we use to make Buildy: HTML5, CSS,
[Coffeescript](http://coffeescript.org/), [Grunt](http://gruntjs.com/),
[Bacon.js](https://github.com/raimohanska/bacon.js),
[SoundManager2](http://www.schillmania.com/projects/soundmanager2/),
[jQuery](http://jquery.com/), [Mousetrap](http://craig.is/killing/mice), and
[underscore.js](http://underscorejs.org/). The whole game is a bunch of static
files hosted on Github Pages, just like the rest of steveasleep.com.  To
deploy, all I had to do was push to the `gh-pages` branch.

I didn’t do anything I hadn’t done before. All of the rendering is just styled
`<div>` elements. I’m familiar with each of those Javascript libraries. I’m
comfortable with the Chrome dev tools. Static files are incredibly easy to
deploy and serve without paying a dime. As a result of using all these familiar
pieces, I spent almost no time debugging simple (or even complicated) issues.

If you’re looking for advice about how to do Ludum Dare well, here’s mine:
**learn your tools.** Make sure you know how to write, run, and deploy your
game.  Don’t give yourself any surprises. (Python developers have a
particularly tough time with this one. There are still a few that ask you to
install PyGame to play and rate their game. I sympathize, having used py2app
for LD19.)

If you spend any time in Javascript, try to get your head around
[Bacon.js](https://github.com/raimohanska/bacon.js). It can decrease game logic
complexity by quite a lot if you’re willing to invest your brain resources in
it. We Dreamers would have had 30% more code and been 30% buggier without it.

## Downsides and difficulties

There’s another, secret reason why I was able to write We Dreamers so fast: I
didn’t give more than a passing thought about scale. I had no idea how much
data users would generate (currently ~4 MB) or how well browsers would deal
with 6000+ DOM elements moving around (not very well). Buildy partitions its
worlds into squares, so it’s easy to only load a piece at a time. We Dreamers
has no such wisdom, so every user loads the entire world when the page loads.
Threeish megabytes isn’t so bad for a game, but DOM performance turned out to
be a huge issue once things got big. To help players deal with the speed, I now
provide a stripped down version that web browsers can handle better.

I chose to do all the rendering via styled `<div>`s because I wanted to spend
as little time as possible on drawing code. I gambled that web browsers would
be smart enough to efficiently clip offscreen nodes. It almost worked, but I
really should have used `<canvas>`. It wouldn't have been much more work.

I had a tiny bit of trouble with cross-browser compatibility.
`requestAnimationFrame` still hasn’t been un-prefixed in Firefox or Safari.
Safari didn’t like any of the CSS gradient variants I tried either, so the
doors are all white when viewed in that browser. In the end, though, I was able
to make it widely compatible and consistent. (This is another issue that would
have been avoided had I used `<canvas>`.)

Despite using Firebase, here was one aspect of distributed computing I did have
to deal with: syncing the time across all clients to get the color harvesting
to look right. I thought I was being clever by using a public web service that
gives you the current time in JSON. Unfortunately it’s hosted on Google App
Engine and blew through its quota soon after voting started, so now all the
players’ clocks are wrong anyway. It doesn’t affect the game much, but I should
have seen it coming.

There was one last issue that I was always aware of but never had time to deal
with: access controls. There are no API-level restrictions on who can edit what
data. At least one person exploited it to leave me an amusing note, but
fortunately there were no abusers. Firebase has the ability to use access
controls, but I didn't have time to learn their API. Another reason to know
my tools really well, I suppose.

## In closing,

I had a fun and intense time this year. Of my three attempts to date, We
Dreamers is far and away my best Ludum Dare effort yet. I plan to come back for
another round in August for LD27.
