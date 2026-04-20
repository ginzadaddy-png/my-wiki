---
title: "How To Think Like A Game Designer"
source: "https://www.youtube.com/watch?v=iIOIT3dCy5w"
author:
  - "[[Game Maker's Toolkit]]"
published: 2023-02-18
created: 2026-04-20
description: "🔴 Get bonus content by supporting Game Maker’s Toolkit - https://gamemakerstoolkit.com/support/ 🔴When it comes to mechanics, a great source of inspiration ..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=iIOIT3dCy5w)

## Transcript

### Intro

**0:00** · Okay, so during the development of Alien: Isolation, the game had a pretty basic save system.

**0:06** · It would automatically cache your data whenever you tripped invisible checkpoints, which were dotted throughout each level.

**0:13** · It was added because it was easy to implement, simple to understand - and, in truth, because that's how saving worked in pretty much every game.

**0:21** · Design director Gary Napper said "like any development team, we all play a lot of games and each have our favourites.

**0:28** · Often our decisions and choices are coloured by the games we play".

**0:32** · But...

**0:33** · as development went along, the team started to question if this save system was actually the right choice.

**0:39** · You see, because players knew that if they died they'd only lose a couple minutes of progress, they would just waltz around the space station without a care in the world.

**0:49** · Not ideal...

**0:50** · in a horror game.

**0:51** · \*Alien scream\* So while these checkpoints might have worked in Call of Duty and Bioshock - Napper says it was "not the right approach when making a game that is designed from its core to terrify and put people on edge".

**1:05** · Because here's the thing.

**1:06** · It's totally fine to take influence from other games.

**1:09** · Many designers borrow mechanics from their favourite titles - often evolving, combining, and remixing them into something new.

**1:17** · But: it’s essential to understand why those mechanics work in one game, before copying and pasting them into yours.

**1:24** · How do you do that? Well, I'm Mark Brown, and this is Game Maker's Toolkit.

### What is MDA?

**1:33** · Alright, so...

**1:34** · way way back in 2004, , three game designers got together and wrote an academic paper, featuring a framework that would prove to be perfect for analysing the mechanics in games.

**1:44** · It's called MDA, and it breaks games down into three, neat sections: mechanics, dynamics, and aesthetics.

**1:53** · Mechanics describes the actual workings of the game: like the rules, the systems, what the buttons do, and all of the individual stats and numbers.

**2:02** · For example, one mechanic could be the maximum amount of ammo the player can hold - and we could set that number really high.

**2:10** · Then, dynamics is how the player acts and behaves, in response to those mechanics.

**2:15** · So because the player has tonnes of ammo, they may storm into battle, and shoot wildly in the general direction of every enemy they spot.

**2:24** · And, finally, aesthetics - not to be confused with the graphics or the art style.

**2:29** · Here, aesthetics is how the player feels when acting in that way.

**2:33** · Their emotional response.

**2:35** · So this wild shooting could make you feel reckless, powerful, unstoppable - basically, like this.

**2:42** · \*Machine gun fire\* To put it another way - mechanics happen in the code, dynamics happen in the player's actions, and aesthetics happen in the player's feelings.

**2:52** · Now, unfortunately, game designers can't just go inside the player's head and directly alter their actions or feelings.

**3:00** · But they can change the code - and because MDA describes a casual relationship, these changes will cascade down and alter the dynamics and aesthetics.

**3:10** · For example, if we tweak that knob the other way, and massively limit the player's ammo stash, that's definitely going to change the player's behaviour.

**3:18** · Now, they will act cautiously before heading into battle, or might not engage enemies at all.

**3:24** · Every shot fired will be done with careful consideration, and more time will be spent hunting for ammo in the environment.

**3:30** · And this will lead to completely different aesthetics: like disempowerment, fear, and caution.

### Analysing with MDA

**3:37** · So, this MDA framework takes mechanics - and then puts them into a wider context, which asks 'how do they make the player act, and how do they make the player feel?'

**3:47** · And we can use these questions to analyse the mechanics in the games we play.

**3:51** · Like, we could ask 'why do swords break in Zelda: Breath of the Wild?'.

**3:56** · Well - how does that change player behaviour? Maybe players will rely less on direct attacks, and so spend more time sneaking past enemies, or finding creative ways to ambush foes.

**4:08** · It will certainly encourage players to use different weapons - and constantly seek out new ones.

**4:14** · It can also lead to exciting moments of drama in the middle of a fight - (so far I've used dynamics to refer to player actions, but dynamics can also be used to describe consequences that might bubble out of the game's systems).

**4:27** · So how does that feel? Well, it could make you feel underpowered, it could make you feel crafty and creative, and it will likely make you feel like an explorer...

**4:37** · in a world that's decaying, and falling apart.

**4:40** · If there's one hard part of this analysis process, it can be putting words to the subconscious feelings that arise when playing games.

**4:48** · We're looking for way more than just "this game was fun", - we're looking for strong, emotive feelings like, this game made me feel powerful, creative, sneaky, tense, intimidated, curious, deceitful, cooperative, flustered.

### Fitting Your Vision

**5:04** · So MDA lets us see game mechanics as powerful vessels for delivering emotions to players.

**5:10** · And so when borrowing mechanics from other games - or making entirely new ones - you can pick ones with associated dynamics and aesthetics that will compliment the rest of your design - and avoid ones that will clash.

**5:23** · For instance, designer Jenova Chen says that the game Flower once had a level-up system, spells you could cast, resource management, and time limitations - expected features of other video games.

**5:35** · But they all had to go, because they went against the intended emotions of relaxation, calm, and peace.

**5:42** · Chen says "we’ve played so many games growing up these bad habits form.

**5:46** · A lot of the time we like to make things very fun, but fun doesn’t always help the emotion you want to deliver".

**5:52** · That's why it's useful to truly understand your game's vision - the overarching feeling or experience you want to give the player.

**6:00** · Because if you know you want to make the player feel, say, scared, then you know you'll want to pick mechanics that induce feelings of fear, dread, isolation, and disempowerment.

**6:10** · That vision could be a single statement: Subnautica was based around the phrase "thrill of the unknown", and every mechanic had to suit this idea.

**6:20** · Resident Evil Village was built under the banner of "struggle to survive" - and so when playtesters hated the game's messy combat, the designers could use that phrase as, like, a lodestar to rebalance and rethink the game's mechanics.

**6:34** · The vision could also be a fantasy that you're trying to deliver.

**6:38** · Perhaps you want the player to feel like Batman, or an assassin, or a world leader.

**6:43** · It could be a feeling - like how Flower tried to make you feel relaxed.

**6:47** · Or it could be a specific experience - when making FTL, the devs said their starting point was "we wanted to recreate the atmosphere of commanding a starship".

**6:56** · With a strong vision in mind, it becomes easier to evaluate whether game mechanics are the right choice for the game you're making.

**7:03** · And, of course, it goes beyond game mechanics.

**7:06** · All the other elements in the game, like visual style, music, animation, story, colour, camera framing, and so on - those all create aesthetics too.

**7:18** · (Just, without the dynamics bit).

**7:19** · For example, Dead Space composer Jason Graves said that EA originally requested a predictable sci-fi soundtrack for the game - full of electronics and drums.

**7:28** · "After we did that first little piece of gameplay," says Graves, "EA came back and said that it wasn’t scary enough.

**7:34** · The music made players feel heroic, and they wanted them \[to feel\] scared."

**7:39** · And ultimately I think games are most clear and coherent when absolutely everything is pointing in the same direction.

**7:46** · Jenova Chen says "all the elements have to sing the same notes to make the impact strong".

**7:52** · Perhaps the best example of this - for me - is DOOM, from 2016.

**7:57** · It also had a strong vision statement - in this case, "push forward combat".

**8:02** · And pretty much everything in the game supports this statement.

**8:05** · You can see it in the game mechanics - from the rapid movement speed, to the way you pounce on enemies to get health, to the way certain demons are told to run away from you - every feature pushes you to race towards enemies like an unstoppable predator.

**8:18** · And that's supported by the non-game elements, like the heavy metal soundtrack, the violent animations, and the Doom Slayer's visual design and personality.

**8:27** · Of course, none of this as easy as I'm making it sound - and there are so many other considerations to make when designing a game.

### Other Considerations

**8:35** · For starters, a game isn't just one mechanic - but hundreds, perhaps thousands if you want to go super granular.

**8:43** · My interactive video essay, Platformer Toolkit, shows how a single character can be defined by dozens of distinct stats - which could change the game from feeling like Inside, to feeling like Super Meat Boy.

**8:54** · And these mechanics interact, overlap, and can even undermine each other.

**8:59** · In The Callisto Protocol, you have very limited ammo, which is intended to make the player feel underpowered and fearful.

**9:06** · Buuut, you also have a one-button, insta-kill stealth attack with a slick animation - which can make you feel powerful and unstoppable.

**9:14** · Also, while you can make best guesses about how a player will act in response to a mechanic, you can't know for sure until you do a lot of play-testing.

**9:23** · Players might misunderstand or ignore a mechanic - or do something completely unexpected.

**9:29** · Sometimes that's a fun, emergent behaviour - like the flying cars in Rocket League, which suited the vision just fine, and so could be kept in the game.

**9:38** · But at other times it can create degenerate strategies that undermine your emotional goals.

**9:43** · Going back to Alien: Isolation, the automatic checkpoints meant that if you got jumped by the Xenomorph, a smart strategy was to just beeline it towards to the next checkpoint, get killed, and respawn in safety.

**9:54** · Furthermore, sometimes you want to have different emotions, at different times in the game.

**9:59** · And so will need to change the mechanics accordingly.

**10:02** · If the story depicts a character who starts out weak and naive - but ends the game feeling competent and powerful, how could you reflect that growth in the game mechanics?

**10:12** · And finally - and perhaps most importantly - aesthetics are, ultimately, subjective.

**10:18** · A scoring system might make one player feel competitive - and eager to replay every level.

**10:24** · But it could make another player feel judged - and eager to get a Steam refund.

**10:29** · Time pressure might feel fun and exhilarating to one person - but anxiety-inducing to another.

**10:35** · And this is often related to skill and ability.

**10:38** · Take the new Tango game, Hi-Fi Rush: it clearly wants you to feel like a rockstar as you brawl along to the beat - but as someone with zero musical ability, I just felt like a bumbling idiot.

**10:51** · At the end, I’ll recommend a video about balancing a fantasy with differing player skills.

### Conclusion

**10:58** · So, going back to Alien: Isolation - the team eventually tried a different save system.

**11:03** · Something closer to older games.

**11:05** · Now the game features a small number of save points that you have to operate manually.

**11:11** · And - to make things worse - it takes a while for the save point to turn on, and for your game to actually save...

**11:17** · giving the alien a chance to sneak up and kill you.

**11:21** · And this new mechanic changed everything - completely altering the player's behaviours and emotions.

**11:27** · "We were afraid," says Napper.

**11:31** · "If we didn’t make it to the save point and successfully save, we would lose our progress.

**11:35** · Saving became tense.

**11:37** · Looking for a save became tense. The simple act of saving had become supportive to the game's driving factors of terror and isolation".

**11:46** · So - it's fine to borrow game mechanics - but you need to understand why they work.

**11:51** · MDA is a powerful tool for this because it helps us predict how a game mechanic will make players act, and make players feel.

**11:59** · If those feelings compliment the vision for your game - then awesome.

**12:03** · If they clash, then they probably need to go.

**12:06** · Because, when it comes to picking, pinching, or producing game mechanics - you should listen to Shovel Knight studio Yacht Club Games, who says "it depends on the game you are trying to create, the emotions you’re trying to evoke, and the experience you want your players to have".

### Patreon Credits

**12:26** · Hey, thanks so much for watching! This video was originally given as a lecture at universities in London, Breda, Boden, and Skellefteå.

**12:35** · If you'd like me to visit your school, please get in touch - you can find my email in YouTube's about section.

**12:40** · I'm also going to GDC next month, so if you see me - say hi! For now, though, click here to watch that video about delivering a specific fantasy, to players of different abilities.