---
title: "How Games Get Balanced"
source: "https://www.youtube.com/watch?v=WXQzdXPTb2A"
author:
  - "[[Game Maker's Toolkit]]"
published: 2019-04-11
created: 2026-04-20
description: "🔴 Get bonus content by supporting Game Maker’s Toolkit - https://gamemakerstoolkit.com/support/ 🔴Balancing a game is one of the most complex pursuits in ga..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=WXQzdXPTb2A)

## Transcript

### Introduction

**0:04** · If you’ve spent any amount of time in a multiplayer lobby, you’ve probably heard words like overpowered, cheap, and unfair.

**0:12** · What these players are arguing about is the game’s balance.

**0:16** · Balance is the art of making sure that all options in a multiplayer game are fair: so none are underpowered, and thus pointless to use. And none are overpowered, and thus dominate everything else.

**0:28** · Here’s the thing though: most video games aren’t just striving for balance. But balance among a wide range of distinctly different options.

**0:36** · You don’t have to work that hard to balance a symmetric game - which is one where all players have the exact same starting conditions. But most games are asymmetric - which means players are facing off against each other with completely different stuff.

**0:51** · And in a game where players can pick from 74 different fighters or 140 unique champions, the developers are counting on them all being equally viable among players of roughly the same skill level.

**1:03** · So how do they do it?

**1:04** · Now, I should say, balance is an incredibly difficult pursuit. It can be an entire department at certain companies, and Riot’s League of Legends has had more than 200 balance patches in the last decade. Plus it’s not just about numbers, but player psychology, with Overwatch’s Jeff Kaplan saying “the perception of balance is more powerful than balance itself”.

**1:26** · So this is not going to be an intensive tutorial. Instead, Game Maker’s Toolkit presents a whirlwind tour through the ways games are balanced - and rebalanced - and rebalanced and rebalanced.

### Creating trade-offs

**1:42** · So how do developers go about balancing a game in the first place? Well, the first consideration is trade-offs. This is when you essentially cancel out a character’s competitive advantages, with drawbacks.

**1:54** · Think of Mario Kart characters, where heavy racers like Donkey Kong have a high top speed, but low acceleration, while featherweight racers like Toad are the opposite. On the right track design, they’ll be almost evenly balanced.

**2:08** · You can think of characters as having a “power budget” - at least that’s why Riot calls it. Advantages are a cost, but disadvantages are a discount. If all characters are just about hitting the limit of the same power budget, they’ll be closer to being balanced.

**2:24** · It’s rarely that easy, of course. I mean, okay, sometimes you’ll get a card that does 1 damage to all minions and another that does 4 damage to all minions. That’s an easy one: just make the second card cost a bit more energy.

**2:39** · But how do you calculate the power budget for completely incomparable options like heroes in Overwatch? Or options with dozens of stats to tweak? Like, when Bungie was reigning in the initially overpowered sniper rifle in Halo 3, it had loads of stats it could tweak such as clip size, time to full zoom, reload time, and max ammo.

**2:59** · (It ultimately decided the best knob to tweak was the time between shots, which it bumped from 0.5 to 0.7 seconds).

**3:06** · What’s important, though, is to celebrate the big differences between choices. The sniper rifle and the shotgun offer a more exciting choice to players than two types of assault rifle - even though the latter is much easier to balance.

**3:19** · So I agree with ex-Blizzard designer Rob Pardo when he warns designers against using the maths to balance games into mediocrity, saying ROB PARDO: "you’re gonna end up with a game where everything kinda feels the same. And you can high five each other and say it’s balanced, but is it fun? Probably not”.

### Using counters

**3:38** · Another consideration is counters. This is when we give characters the ability to negate each other’s moves and strategies. For example: a quick Zerg rush in Starcraft is all well and good - unless your opponent is one step ahead and has already built defensive bunkers.

**3:54** · And what we ideally want is for everything to have a counter. So a defensive Starcraft player can, in turn, be countered by a more economical strategy, where you save up resources to build units that can eventually crush those bunkers into dust.

**4:10** · And we could make a counter to that counter, and so on - but then we’d be here for forever.

**4:15** · There’s a more elegant solution though, because how do you deal with someone who’s sitting around saving up money? Well… a rush.

**4:23** · And, wouldn’t you know it… it’s rock, paper, scissors. This goofy game you play to see who has to do the washing up might be incredibly simple and lacking any strategic depth, but it is perfectly balanced - because everything has a counter, and everything is a counter.

**4:40** · EDDIE: Damn man, killed those scissors.

**4:43** · And that’s why it forms the backbone of a lot of multiplayer games. Pretty much every fighting game has a system like this, such as Dead or Alive which boasts about its triangle system, where strikes beat throws, throws beat holds, and holds beat strikes.

**4:59** · In strategy games, it’s not just the strategies that work like this, but the individual units.

**5:04** · And the different Pokemon types all sit in a massive web of interlocking counters - but starting, of course, with fire, water, and grass.

**5:12** · Rock, paper, scissors is a great balancing framework to start from, because you can ensure that no element is overpowered - it’s countered by something. And no choice is irrelevant it at least works as a counter to something else.

**5:26** · And also, in strategy games at least, it encourages mixed strategies, it makes you into a multi-disciplinary player, and it forces you to switch tactics on the fly in a really dynamic way.

**5:37** · And in class-based games, it’s a great way of automatically making mixed teams.

**5:42** · Take Team Fortress 2, where seven of its nine classes fit into a complex web of interlocking and interchangeable triangles of rock, paper, scissors. Here, teams must pick complementary classes to protect each other from weaknesses. If you’re an Engineer and Spies keep sapping your sentries, then you’re going to need to get one of your team mates to switch to Pyro.

**6:05** · These counters are often described as hard counters if they completely shut something down - like a punch is a hard counter to a throw in ARMS because it will nullify the effect every single time. But soft counters just mean one choice will have an advantage over the other. McCree will outperform Tracer, but his chance of winning is far from 100%.

**6:28** · When it comes to counters, it’s really important to figure out what are the hands and what are the throws.

**6:34** · The hands are the things that get locked in before the match even starts. You know, the characters and the races. The throws are the things you pick during the match. The moves, the units, and the strategies. And in a team-based game, like Overwatch, the entire team is the hand, while the individual players are the throws.

**6:55** · The throws are specifically designed to be unbalanced against each other, to create that back-and-forth counter-play and teamwork. But the hands are supposed to be balanced, and so they should have access to all of the throws. If Zangief simply couldn’t block, for example, he would be unusable.

### Testing the balance

**7:17** · So you’ve got a bunch of characters, with trade-offs and counters, and you think you’ve made them balanced. But how do you actually make sure that’s true? Well this is when we start collecting data - either from internal play-testers, or the millions of people playing your game online.

**7:32** · Now you might think that all you need to do is track how often each character results in success - i.e it’s “win rate”. And if a character has a 50 percent win rate, it’s balanced.

**7:43** · But, like all stats, this can be misleading. Imagine a fighting game with three characters and if Ryu won every match against Chun-Li and lost every match against Cammy, his win-rate would be 50 percent. Perfectly balanced, though? I think not.

**7:58** · That’s why match-up charts, where you where you can see the win rate of a character, when played against all other characters, are so important.

**8:06** · But even that’s not going to tell you everything. Riot had a problem with the League of Legends character Akali. The numbers said she was pretty balanced, with a 44 percent win-rate perhaps a tad underpowered. So how come she secured a 72 percent win rate at the 2018 World Championship, and was banned more times than any other champion?

**8:25** · It’s because while she was really powerful, she was difficult to play effectively. She had a super high skill floor, in other words. So while top-tier players could use her to wipe the floor with the competition, the low-ranking players using Akali were getting killed left, right, and center. Therefore, her win-rate was being dragged down.

**8:45** · That’s why it’s important to look at a character’s win-rate and match-ups across all skill levels.

**8:51** · And finally, win-rate doesn’t really tell you what’s actually going on in the game.

**8:56** · We need to know what characters people are actually picking. People might be avoiding a character who is otherwise well balanced because that character is not much fun to play, or is only useful in certain situations.

**9:08** · Blizzard found that Overwatch hero Symmetra was a largely balanced character, but she wasn’t being picked as much because her use was highly situational. So in her first complete redesign, they tried to make her more popular by giving her two ultimates to pick from: a teleporter or a shield generator.

**9:26** · That’s why player feedback is so important - as well as pick-rate, which tells you how often a character is actually getting used. For Rainbow Six Siege, Ubisoft uses a matrix to cross reference both win rate and pick rate -with different considerations needed for operators who fall into these four buckets.

**9:45** · And the pick-rates help tell you the state of the meta - which is essentially just the characters, cards, strategies, and so on that the community at large have found the most effective and are currently using.

**9:57** · This is often shared through forum posts, fan-made tier lists, YouTube videos, and eSport victories. When a kid called Jason won the Clash Royale tournament in Helsinki, his chosen cards suddenly became massively popular.

**10:12** · The meta can actually act as a self-balancing force. Let’s say everyone discovered that a certain character was overpowered, and everyone started using it. It’s now in everyone’s best interest to try and discover strategies that can counter or out perform that favourite.

**10:26** · And if players find it, the meta might change.

**10:29** · This rolling meta keeps the game fresh, and gives the players who found the counter a real sense of satisfaction. Overwatch’s Jeff Kaplan says “regarding the meta changing because players have innovated a new strategy – well – this is the best-case scenario.

**10:44** · We’ve seen this happen time and time again.”

### Nerfing and buffing

**10:48** · Of course, that’s not always going to work. Sometimes the designers will have to go in and change things. If a strategy is overpowered, if a character is never getting played, or if a play-style is proving annoying then it’s time to swing the hammer.

**11:02** · First, the devs need to figure out the exact reason why that character, or strategy, or whatever is unbalanced. It’s easy to see that a character is dominating the match-up charts, but can be harder to pin-point why.

**11:14** · So for a character like Meta Knight in Super Smash Bros Brawl, it was mostly because of his extremely fast attack speed, and an ability to cancel his momentum in mid-air and avoid being KO’d. He had lots of advantages, and not enough trade-offs - and other characters don’t have the tools to counter him.

**11:31** · Once the source has been found, you’ve got to figure out what to nerf and what to buff.

**11:36** · Nerfing means making something less powerful, like reducing their speed, limiting their range, or cutting down their strength. Buffing is the opposite: making it more powerful.

**11:45** · You don’t necessarily have to buff the weak characters and nerf the strong ones, though. You could leave an overpowered character alone, but buff the characters who counter them, and still solve the same problem. Make sure you watch this Core-A Gaming video on why buffs are, generally, better than nerfs.

**12:02** · Balance changes can be anything from a tiny tweak to a character’s movement speed, to a complete overhaul of how a character works. It might be a fundamental change to the rules of the game - Rainbow Six Siege made attacking and defending more balanced by changing the match time to three minutes. And sometimes you’ve just to pull things from the game entirely, like when Epic scrapped the overpowered infinity blade in Fortnite.

**12:25** · Any change is going to affect players - especially those who are very used to the way a specific character, or its counters, work. So when the game gets patched, it’s important to communicate the changes through patch notes, videos, and so on.

**12:38** · In fact, patch notes are so important that Riot once put out of a note saying a champion was nerfed, but forgot to actually implement the nerf in the code. Even so, the character’s pick rate plummeted, and even his win rate decreased a bit. Didn’t I say that player psychology was an important factor?

### Balancing across skill levels

**12:57** · Now, at the beginning of this video, i said that balance was about trying to make characters equally viable among players of roughly the same skill level. But what happens when players aren’t at the same skill level?

**13:09** · Well, a lot of highly competitive games use matchmaking systems to pair up similarly skilled players.

**13:15** · But for more accessible, party-style games, we may want to build in negative feedback loops, or catch-up mechanics, where players who are doing poorly get a helping hand. Examples are the deathstreak mechanic in Modern Warfare 2 where you get a special bonus for dying a whole bunch. And the item system in Mario Kart where powerful items - including that pesky blue shell - are only given to players at the back of the pack. These are pretty contentious, and must be used sparingly.

**13:42** · We can also reduce the value of skill by adding in more luck. We see this in most family board games like Snakes and Ladders and Monopoly which are heavily based on the luck of the die roll. But in video games, you see this in games like Apex Legends, where your chances of winning are shifted, based on what goodies you find when you drop into the map.

**14:03** · Game can also offer handicapping modes. And in team-based games, we can give players alternate play styles that allow them to contribute to the team without needing to do highly-skilled, front-line action, like being a medic or an engineer.

### Conclusion

**14:18** · So balancing a game is a really challenging job. The more you make characters distinct, the harder it is to put them on an even playing field. And that’s not taking into account players of unequal skill level.

**14:30** · We can try to design in trade-offs, to ensure characters don’t have too many advantages.

**14:35** · And give characters counters, so they can keep each other in check. But even the best designs won’t stand up to scrutiny when put in front of millions of players.

**14:43** · So we need to constantly determine the balance, by watching win-rates, match-ups, pick-rates, and player feedback. And while hopefully the meta will naturally shift in response to imbalance sometimes devs have to go in and make the hard changes.

**14:57** · And then you introduce a whole new character and everything breaks again. Sigh. I said this wasn’t an easy job. So let me know: what do you think is the most balanced game around, and have you ever played a game where the devs just got it oh so wrong? Let me know your experience with balance in the comments below.

### Patreon Credits

**15:15** · Thanks for watching! I had a lot of help on this one, from people who know multiplayer games really well to developers who have worked on games like League of Legends, Dirty Bomb, and Rainbow Six Siege. There’s definitely more to talk about - like balancing multiplayer maps in shooters. But we can get to that in the future.