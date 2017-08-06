Title: PoweRL postmortem
Category: Articles
Slug: powerl-postmortem
Tags: games
Status: published

[Ludum Dare 39](https://ldjam.com) fell on a weekend when I wasn't busy, and I wanted an excuse to learn a bit about Apple's game libraries, so I made another [roguelike](), [PoweRL](https://irskep.itch.io/powerl):

![Screenshot](|filename|/img/powerl/screenshot.png)

<!-- PELICAN_END_SUMMARY -->

I wasn't in the mood for stress, so I set my standards very, very low. Ironically, the result is more commercially viable than most of what I make! That might not be apparent from the screenshot, but maybe this new version with updated art will convince you:

![Screenshot 2](|filename|/img/powerl/screenshot2.png)


## Swift, SpriteKit, and GameplayKit

"iOS engineer" is part of my normal job description, but in the past I've avoided using Swift or Objective-C for jams because it isn't cross-platform. But since I didn't really care about the outcome of this jam, I let my curiosity about SpriteKit and GameplayKit win out over portability.

I'm really glad I did, because after learning the frameworks, I spent almost no time worrying about the engine! My last Ludum Dare game, [Rogue Basement](/|filename|/posts/2017-05-04-the-design-and-implementation-of-rogue-basement.html), needed a lot of up-front work on the engine to get running, and then optimization work after completion. But with PoweRL, SpriteKit made for an efficient renderer and animation system, and GameplayKit gave me structure for gameplay code and a few nice utilities like pathfinding.

## Iteration

Swift is a great language for iteration. In a lot of ways you can treat it like a dynamically typed language, but still have a lot of problems caught by the compiler. Even though there's a compilation step between writing the code and testing it, I think I iterated more quickly than I do with Python because I never hit a typo at runtime.

GameplayKit's entity-component system is well designed and honestly taught me for the first time how that kind of architecture is supposed to work.

SpriteKit's `SKLabelNode` let me write almost the whole game in old-school roguelike style, with letters representing everything instead of graphics. But at the end, it was very easy to swap in bitmap art.

## Evolution of the design

Ever since starting to play [868-HACK](http://www.smestorp.com) on my phone, I've wanted to try making a game in the same genre (pocket roguelike). The SpriteKit template in Xcode immediately gives you a codebase that runs on macOS, iOS, and tvOS, so right from the start, I kept in mind a control scheme that could work on keyboards and touch screens alike. Swiping would move your character, and tapping would do something else.

The theme of the jam was "running out of power," so I did something dumb and obvious: I made a robot with a power meter. I put it in a level filled with walls, batteries, and "power drains." When I went to bed Friday night, that was it: a game about getting from Point A to Point B without running out of power, over and over again.

That's an interesting set of mechanics by itself because the player already has interesting decisions to make:

* What path should I take through the level to minimize power loss?
* Should I pick up all the batteries? Is that worthwhile?

The next day I added the butterfly, which moves one tile diagonally per turn. I added a health bar and some health pickups. Then I added a turtle, which moves one tile non-diagonally every other turn. Over lunch, I pondered other enemies I could add, and ultimately plopped in a literal chess knight.

These changes added a second dimension to the gameplay, which introduces new questions and tradeoffs. Players must now constantly decide whether they value power or health more, and act accordingly. They would be asking questions like this:

* Should I pick up the battery, even if enemies drain my health along the way?
* Can I make it through that pack of enemies?
* Should I run through that line of power drains, or make it past those enemies? Do I value health or power more right now?
* If I beeline for the exit, will I be able to recover the power in the next level, which is more difficult?

The enemies seemed to be able to get the best of the player too often, so I finally made use of the tap control: bullets! I added ammo pickups and a simple Bresenham line-based instakill shooting mechanic.

This change added an element of long-term strategy. Players could pick different values for these strategy-axes:

* Never pick up bullets to avoid wasting energy, or pick up all the bullets?
* Shoot everything on sight, or only shoot in dire situations?
* Use ammo early, or hoard for later?

With all the mechanics in place, I played through a few times for balance. I tweaked the level generator parameters for number of enemies, amount of health/ammo/batteries per level, number of walls, and movement cost. The game got too hard after level 8, so I added a win condition at level 8. And that was it!

### Influences

Two things influenced my approach toward designing this game. The first is Jesse Schell's book [The Art of Game Design: A Book of Lenses](https://www.amazon.com/Art-Game-Design-Lenses-Second/dp/1466598646/). It helps frame a lot of important questions. The second is roguelikes in general, which at their core are about creating interesting decisions for players every single turn of every game.

## Music

I spent an hour or so in Logic Pro with my 25-key MIDI controller, electric bass, and the Logic Pro Auto-Drummer. I started with the beat, added some bass, added some synths, wrote a new part with the bass, filled in with synths, and then shuffled it all around until it felt passable.

That's my normal way of working when I have limited time for music. For Rogue Basement, my last game, I wrote two songs just by holding down a single note for 5 minutes in an arpeggiating synthesizer and adding some occasional notes on a pad synth on top of it. Another Rogue Basement song was just a piano improvisation jam. When you only have 48 hours to make a game, you have to take as many shortcuts as you can get away with!

## Art

I used Apple's beautiful emojis for enemies during development, but I felt that it wouldn't be in the spirit of Ludum Dare to use them as my final sprites, since they are finely rendered illustrations that I did not create. So I vector-traced them by hand in Pixelmator, added bad gradients, and called it a day, finishing about 20 minutes before the deadline.

Those sprites are fine in that you can tell what's what, but I really dislike the aesthetic. Over the following few week nights, I redid all the sprites in 16x16 pixel art. It's more of an explicit 868-HACK ripoff with that style, but it's also the only style I can use myself to create art I'm happy with. I bet that's true of a lot of programmers.

I can't use the new sprites in the Ludum Dare judging, but I can at least use it as the canonical version when judging is over, and recover a bit of self-respect.

## Parting thoughts

I took a lot more breaks this time than I did in the past. These days I value my weekend chill-out a lot. But by being smart about tools, game design, and assets, I ended up with something I'm proud of.

For the next Ludum Dare, I'm going to try to join a team.