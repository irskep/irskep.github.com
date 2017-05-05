Title: The Design and Implementation of Rogue Basement
Category: Articles
Slug: the-design-and-implementation-of-rogue-basement
Tags: games
Status: published

# Introduction

This year I participated in [Ludum Dare 38](https://ldjam.com), a 48-hour game programming "competition." I've been thinking about trying my hand at a roguelike for a while now, and it seemed like the perfect opportunity to give it a shot. I made [Rogue Basement](https://ldjam.com/events/ludum-dare/38/rogue-basement), a bare-bones, single-level game with ASCII graphics.

In this article, I'll cover the game design decisions I made, how they affect the player's experience, and a bit of how they're implemented.

![screenshot](|filename|/img/rogue_basement/screenshot2.png)

# What is a roguelike?

A "roguelike" is a game that is "like Rogue," a text-based game from the 1980s that looks like this:

![Rogue_Screen_Shot_CAR.png](|filename|/img/rogue_basement/257BD0D6AB2E10E523C6F74028CBC005.png)

Typical features of these games include:

*   Procedurally generated levels
*   Permadeath (one life)
*   Turn-based action
*   Top-down 2D graphics, often just text
*   Simulation-oriented; interesting stories arise from the game's rules and behavior
*   Very difficult to win without lots of practice

The combination of these features makes the games fun to play over and over again. You have to play a lot to get good, but since the game is procedurally generated, you're always facing new situations. You have to use your wits to survive.

# Environment

I started on Friday night with a level generator. When you're time-constrained, you have to make very careful decisions about where to innovate, and I chose to stick to a roguelike trope for my basic layout: boxy rooms connected by narrow corridors, with doors where corridors meet rooms.

I could have placed a bunch of rooms randomly and made sure each one was connected to another, but it's tricky to use space efficiently that way. A common way to avoid this problem is to use a **binary space partitioning tree.**

The basic idea here is that you take a rectangular area, like this:

```
+----------------------------------------+
|                                        |
|                                        |
|                                        |
|                                        |
|                                        |
|                                        |
|                                        |
|                                        |
|                                        |
|                                        |
|                                        |
+----------------------------------------+
```

Divide it along the X or Y axis at a random point, like this, and label each side:

```
+----------------------------------------+
|                 |                      |
|                 |                      |
|                 |                      |
|                 |                      |
|                 |                      |
|       a         |          b           |
|                 |                      |
|                 |                      |
|                 |                      |
|                 |                      |
|                 |                      |
+----------------------------------------+
```

Within each side, divide again on the other axis at a random point:

```
+----------------------------------------+
|                 |                      |
|       aa        |         ba           |
|                 |                      |
|-----------------|                      |
|                 |                      |
|                 |----------------------|
|                 |                      |
|                 |                      |
|       ab        |         bb           |
|                 |                      |
|                 |                      |
+----------------------------------------+
```

Divide some more...

```
+----------------------------------------+
|       |         |              |       |
|  aaa  |   aab   |     baa      |  bab  |
|       |         |              |       |
|-----------------|              |       |
|          |      |              |       |
|          |      |----------------------|
|          |      |       |              |
|   aba    | abb  |       |              |
|          |      |  bba  |     bbb      |
|          |      |       |              |
|          |      |       |              |
+----------------------------------------+
```

When the cells get too small, stop dividing. Inside each cell, decide how to use the space. The most basic strategy is to just completely fill each cell. Here's a screenshot I took when I got to this point:

![Screenshot 2017-04-21 21.00.42.png](|filename|/img/rogue_basement/F883885B86DCA6D8BD0F58083AB16166.png)

But it's more interesting to mix it up with different sizes of rectangles.

```
+----------------------------------------+
| +--+  | +------+|   +------+   |       |
| |  |  | |      ||   |      |   |+-----+|
| +--+  | +------+|   |      |   ||     ||
|-----------------|   |      |   ||     ||
|          |+--+  |   +------+   |+-----+|
|          ||  |  |----------------------|
|   +----+ ||  |  |+-----+|              |
|   |    | ||  |  ||     ||+-----+       |
|   |    | |+--+  ||     |||     |       |
|   +----+ |      ||     |||     |       |
|          |      |+-----+|+-----+       |
+----------------------------------------+
```

You probably noticed I annotated all the cells with `aab` and such. We'll use that information to add corridors. For every pair of areas that share the first 2 letters of their identifier ("siblings in the tree"), we add an L-shaped corridor from a random point in one to a random point in the other. If a point is already inside a room, we'll leave it alone. If a point is on a wall, we'll turn it into a door.

```
+----------------------------------------+
| +--+    +------+|   +------+           |
| |  '####'      ||   |      |    +-----+|
| +--+    +------+|   |      '####'     ||
|-----------------|   |      |    |     ||
|           +--+  |   +------+    +-----+|
|     ######'  |  |----------------------|
|   +-'--+  |  |  |+-----+               |
|   |    |  |  |  ||     | +-----+       |
|   |    |  +--+  ||     '#'     |       |
|   +----+        ||     | |     |       |
|                 |+-----+ +-----+       |
+----------------------------------------+
```

Now we do it again, but the random point in each section will come from a random room in each respective section:

```
+----------------------------------------+
| +--+    +------+|   +------+           |
| |  '####'      ||   |      |    +-----+|
| +--+    +'-----+|   |      '####'     ||
|          #      |   |      |    |     ||
|          #+--+  |   +-'----+    +-----+|
|     ######'  |  |     #                |
|   +-'--+ #|  |  |+----'+               |
|   |    | #|  |  ||     | +-----+       |
|   |    +##+--+  ||     '#'     |       |
|   +----+        ||     | |     |       |
|                 |+-----+ +-----+       |
+----------------------------------------+
```

And finally we'll do it again to the top-level pair:

```
+----------------------------------------+
| +--+    +------+    +------+           |
| |  '####'      '#   |      |    +-----+|
| +--+    +'-----+#   |      '####'     ||
|          #      #   |      |    |     ||
|          #+--+  #   +-'----+    +-----+|
|     ######'  |  #     #                |
|   +-'--+ #|  |  #+----'+               |
|   |    | #|  |  #|     | +-----+       |
|   |    +##+--+  #'     '#'     |       |
|   +----+         |     | |     |       |
|                  +-----+ +-----+       |
+----------------------------------------+
```


And here's how it looked during development:

![Screenshot 2017-04-21 21.50.39.png](|filename|/img/rogue_basement/B74AF325D250255EA7B86A64BE1AAFD0.png)

We now have a few guarantees:

*   All rooms are reachable from all other rooms.
*   No rooms intersect.
*   For a given pair of room groups (everything under `a` vs everything under `b`, for example), there is exactly one path between them.

That last point has some good and bad ramifications. On the bad side, it worsens replayability, because the corridors are roughly organized the same way from game to game. I noticed this while playtesting; after 3 games it's obvious that the rooms generally have the same layout.

But those characteristics allowed me to take a simple approach to matching the theme of Ludum Dare 38: "A Small World." The first two splits don't have to be random; if they always split the sections evenly, then the map will have 4 even quadrants. I used this to create 4 distinct areas of increasing difficulty, so I could have a "one-level roguelike" with some actual progression.

I split up the map like this:

```
+-------------------+--------------------+
|                   |                    |
|                   |                    |
|         aa        |         ba         |
|    (start here)   |     (end here)     |
|         |         |         ^          |
|---------|---------+---------|----------|
|         v         |         |          |
|                   |                    |
|         ab     ------->     bb         |
|                   |                    |
|                   |                    |
+----------------------------------------+
```


The player starts in `aa` and moves to `ab`, then `bb`, then `ba`, where the goal is.

Here's another map from early development, which splits the map in this way:

![Screenshot 2017-04-22 10.54.30.png](|filename|/img/rogue_basement/2EE2A79C08555276A852AAEA4DBEA9C7.png)

And here's one with just the first two partition lines, so you can see how the map is divided:

![Screenshot 2017-04-22 10.56.58.png](|filename|/img/rogue_basement/6F0FA752B4F575565A46B67ABF9120B6.png)

And finally, here are the hallways that mark the transitions between each section:

![Screenshot 2017-04-22 11.40.44.png](|filename|/img/rogue_basement/360C018F2FCC756A1A59049EB36E67AA.png)

Originally the colors were just for debugging, but I ended up leaving them in place because they signal specialness.

To add variety, I created a `rooms.csv` file to define a few room types:

```
                                                      Monster   Item
Shape,      Difficulty, Monsters,   Chance, Color,    Density,  Density
box_random, 0.00,       *,          1.00,   #666666,  5.00,     5.00
box_random, 1.00,       *,          1.00,   #886666,  5.00,     4.00
box_random, 2.00,       *,          1.00,   #668866,  5.00,     3.00
box_random, 3.00,       *,          1.00,   #886688,  5.00,     2.00
box_full,   *,          verp_1      0.20,   #6666ff,  2.00,     4.00
                          |verp_2
                          |verp_3
                          |verp_4,
```

So within each quadrant, there is an 80% chance a room will have shape `box_random`, a quadrant-specific color, 5 monsters per 100 tiles, 5 items per 100 tiles, and allow any area-appropriate monster. But there is a 20% chance that the room will have the shape `box_full` (fill its entire BSP tree cell) and contain only verps, 2 per 100 tiles.

# Inhabitants

## The player

The first inhabitant of the world is the player, represented by an `@` (because the cell with the `@` is "where you are at"). All world inhabitants, henceforth called "monsters" (after all, humans are the real monsters) and defined in `monsters.csv`:

```
id,     Char, Color,    Difficulty, Chance, Behaviors,          hp_max, strength, items
player, @,    #ffffff,  -1,         0.00,   keyboard_movement,  100,    5.00,
```

"Difficulty" determines which quadrant a monster can spawn in. The player is a special case, so the level generator ignores it. The player moves in response to keyboard events, has 100 hit points, and hits other monsters for 5 damage. (The combat system in Rogue Basement is not sophisticated. There is no randomness. Remember, I had to be careful about where to spend innovation-points!)

## NPCs

Generally speaking, NPCs (non-player characters) in video games and tabletop RPGs are differentiated based on three important things:

1.  What they can do
2.  How they behave
3.  How many hits they take to kill, depending on what the player can do

All of those things affect the player's behavior, strategy, and tactics. For a time-constrained game like Rogue Basement, I wanted to stick to the absolute basics.

The monsters are all defined in a CSV file (`monsters.csv`). The very first monster I added was `v`, the "verp":

```
id,     Char, Color,    Difficulty, Chance, Behaviors,          hp_max, strength, items
verp,   v,    #ffff00,  0.00,       1.00,   beeline_visible,    10,     2.00,
                                            |random_walk
```

In human terms, that definition reads as: "The 'verp' monster, represented by a yellow `v`, appears in difficulty-zero rooms (first quadrant) with a random weight of 1.0, moves randomly unless it sees the player in which case it moves toward them, has 10 hit points, does 2 damage to the player when hitting, and has no items at the game start."

Behaviors are implemented as Python classes. After the player moves, each monster has a chance to move as well. Behaviors can be stacked, meaning that if one behavior decides it can't do anything, control can be passed to the next behavior in the list. So the verp's `beeline_visible` behavior either says "I see the player, I move toward them" or "I do not see the player, let some other behavior act this turn."

After adding the verps, I wanted to balance them out with a monster that attacks from a distance. I started by defining a behavior `range_5_visible` which acts like `beeline_visible`, but instead of trying to move onto the player's space, the monster tries to be exactly 5 tiles away. If the player approaches the monster, it will run away unless it is backed into a corner.

I attached this behavior to a new enemy type, the `wibble` (`w`). But a monster that only runs away isn't very challenging! So it was time to deepen the simulation by adding items.

Items have simple characteristics:

*   Monsters (including the player) can hold them in an unlimited inventory.
*   When a monster dies, its items are dropped on the ground.

I only had time to add one kind of item: the rock (`*`). The rock has one use: you can throw it. When you do, the game spawns a new enemy with this definition:

```
id,             Char, Color,    Difficulty, Chance, Behaviors,        hp_max, strength, items
rock_in_flight, *,    #c1a073,  -1,         0,      path_until_hit,   2,      2,
```

Since its "difficulty" is -1, it never spawns in the initial level. Its only behavior is to move along a path until it hits a wall, a monster, or the player. It has 2 hit points.

This is a special item, so the game ignores the `strength` and `items` attributes in the CSV file. Instead, the `rock_in_flight`'s strength value is taken from _the monster that threw the rock_, and the original rock item is added to the `rock_in_flight`'s inventory! When the `rock_in_flight`'s `path_until_hit` behavior detects that its life is over, the `rock_in_flight` "dies" and the contents of its inventory (the `rock`) are dropped on the ground.

Now that I had throwable rocks, I could put a couple in each `wibble`'s inventory and give them the ability to throw them. The `wibble` definition looked like this:

```
id,     Char, Color,    Difficulty, Chance, Behaviors,          hp_max, strength, items
wibble, w,    #90582c,  0.00,       20,     range_5_visible     10,     2,        ROCKx1
                                              |throw_rock_slow
                                              |sleep,
```

I added a "sleep" behavior to differentiate wibbles from verps. When the player isn't around, verps are hyperactive and run around randomly; wibbles sit and meditate. It seemed in keeping with their fighting styles.

That all worked great, but when wibbles ran out of rocks, the game got really easy! So I added another behavior, `pick_up_rocks`, which makes a wibble either move toward any adjacent rocks, or pick them up if it's standing on one.

The "conservation of rocks" principle introduces a new tactic into the game: players can pick up all the rocks to deprive the wibbles of their ammunition. Fortunately the player's backpack is infinitely large!

## Stun effect

At this point, combat consisted of punching verps and dodging or punching rocks. (Yeah, you can punch rocks! They are just monsters after all!) I wanted to make it possible to avoid almost all damage, though, by understanding the game's systems, and the verps made it too hard to do that by being relentless.

So I made every hit by the player stun the target monster for 2 turns. This is done using a behavior called `stunnable`, which just says "if I've been hit within the last 2 turns, turn blue and do nothing."

For experienced roguelike players this makes the game easy once you figure it out, but I believe it's still a rewarding experience to figure it out in the first place. It is very, very difficult to make a game by yourself in 48 hours that has more than a few minutes of worthwhile gameplay, so I was aiming to just make those few minutes as good as possible and then let players feel like they could put it down after a good experience.

## Healing

To make each section its own challenge, I decided to have the colored hallways between sections heal the player completely. This is another difficulty decrease that I could probably have left out, but I decided to err on the side of easy because I knew I had some user interface issues and wanted to be "extra" fair to players.

# Unintended consequences

The simulation has a few features I didn't intend, but that I don't regret—that's half the fun!

These features mainly have to do with rocks, and the fact that when you throw them, they become monsters. Specifically:

* You can punch rocks out of the air.
* If you throw a rock, and then walk in its direction, you will punch it dead before it has a chance to move.
* If two wibbles throw rocks at you at the same time, they may collide in midair and die.
* You can embed rocks in walls. (Okay, not so happy about this one.)

# Atmosphere

## Music

I took 90 minutes to write 4 tracks, adding up to 11 minutes of music. Each map quadrant plays one of the tracks. [You can listen to them here.](https://soundcloud.com/irskep/sets/rogue-basement-ost)

The music fades down when you're in a colored hallway and fades up again when you enter a room in a map quadrant. My intention is to build tension and give the player a clue, in addition to the different colors, that the monsters are about to get tougher.

## Title screen

I made this adorable title screen, and reused the ASCII art in the manual:

![title screen](|filename|/img/rogue_basement/screenshot1.png)

# Takeaways

## Scope

Features I had planned to add but didn't:

*   Multiple basements and an overworld
*   Health potions
*   Fire/ice missiles
*   2 more enemy types to use those missiles

From past experience, I knew that scope was always a problem, so I tackled the highest-priority mechanics first, which means I ended up with a real game instead of a tech demo.

## Difficulty is hard

It's very difficult to tune for difficulty without time to playtest and fix things! I kept making the game easier because developers almost always make games too hard on the first pass, and I wanted to overcompensate to make it more likely that people would finish it in one sitting.

The feedback so far seems to indicate that the difficulty is just about right. No one says it's too hard, and some people say they've been playing for 25 minutes(!!!) and haven't beaten it yet.

## CSVs and roguelikes are best friends

Every time I moved some data out of Python code into a CSV file, it got 10x easier to add new content, but not for the reason you might thing. Yes, copy/pasting CSV rows is an easy way to add new things, but the act of _designing_ the file format made me think about how the whole program worked and put flexible systems in place that would let me do more cool stuff later.

I can already see the limitations of CSV, so I think next I'm going to switch to CSV, but with YAML values for each column. I really like the efficiency of editing CSV, but it's not flexible enough to do what I want.

## Preparation matters

The week before Ludum Dare 38, I worked on an ASCII user interface and roguelike development framework. I didn't want to spend a bunch of time making a crappy title screen, I wanted to focus on gameplay! By writing and releasing the framework, I had all the relevant APIs in memory as soon as the competition started, and I could get going immediately on the important stuff.

## Music makes a difference

The music is really simple, but it adds a huge amount of atmosphere and is a strong signal of progression. It was time well spent, especially since when I made it (the middle of the night) my programmer brain wasn't working anymore. Most of the positive reviews mention the music, so I think it will affect my score even outside the Audio category.

## ASCII is a Ludum Dare graphics cheat code

Since ASCII is traditional for roguelikes, I don't think it's going to cost me too many points in the Graphics category. I've always had a difficult time making nice-looking graphics, and ASCII means it's a non-issue.

## Making videos ameliorates loneliness

Whenever I felt like I hit a milestone, I did a quick [video update](https://www.youtube.com/playlist?list=PLuzdytAQSpVhUCVgJvtgDNEQ2DI41KiKr). I didn't really expect anyone to watch them, but it helped give me perspective on my progress. And it simulated human interaction a little bit, which was nice because I was alone in the house for the entire weekend.

# Conclusion

This is probably the most fun game I have ever made, and the most fun I have ever had making a game. Thanks for reading! You can watch all this happen at super-speed in this timelapse video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/Jo8d34N3tdY?list=PLuzdytAQSpVhUCVgJvtgDNEQ2DI41KiKr" frameborder="0" allowfullscreen></iframe>