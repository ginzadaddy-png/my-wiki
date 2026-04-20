---
title: "What Makes a Good Combat System?"
source: "https://www.youtube.com/watch?v=8X4fx-YncqA"
author:
  - "[[Game Maker's Toolkit]]"
published: 2018-05-27
created: 2026-04-20
description: "🔴 Get bonus content by supporting Game Maker’s Toolkit - https://gamemakerstoolkit.com/support/ 🔴One of my most requested video topics is combat systems. S..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=8X4fx-YncqA)

## Transcript

### Intro

**0:00** · DANTE: So you're looking to play, huh? Alright, I guess I got some time to kill...

**0:06** · From Golden Axe and Double Dragon, to Bayonetta and God of War, there’s no shortage of games about beating the crap out of people in hand-to-hand combat, or close quarters sword fighting.

**0:17** · And so, it’s no surprise that one of my most requested video topics is melee combat systems.

**0:24** · How do you design a brawler that makes you think carefully about every move you make?

**0:28** · A game that’s so deep, you’ll still be learning the ropes a hundred hours in?

**0:33** · And one that just feels incredibly satisfying when you score a perfectly-timed parry?

**0:38** · What are the essential elements of a good combat system?

**0:42** · Well, the truth is, like most things in game design, there’s no one-size-fits all solution.

**0:48** · The needs of a fast-paced fighter like Devil May Cry, are very different to the slow and deliberate combat of Dark Souls, which are different again to the scrappy street fights of the Yakuza series.

**1:00** · So there will be some commonalities that are shared universally, but other design decisions that will change depending on the feel and flow of the game in question.

**1:10** · We’ll figure that all out as we go along.

**1:12** · But for now, though, let’s jump into the first major topic: attacking.

### Attacking Fast and Slow

**1:18** · Every protagonist in a combat game is defined by the ways they can attack.

**1:22** · That might mean swinging a giant sword in Monster Hunter, bouncing enemies into the air in Devil May Cry, chucking a hefty great axe in God of War, or cracking a whip in Castlevania.

**1:34** · Action game heroes typically have a small handful of base attacks - and each one will have its unique advantages.

**1:41** · It might be a particularly strong attack.

**1:44** · Or a very fast-moving strike.

**1:46** · It could have a wide area of effect, or a big range.

**1:49** · It might push enemies away, or knock them into the air, or bring them in closer.

**1:54** · The attack might let you fight from a distance.

**1:56** · Or perhaps it stuns the enemy, or breaks their block.

**2:00** · Of course, each of these attacks will be balanced with disadvantages.

**2:03** · A heavy, damage-dealing attack will often be quite slow to perform.

**2:08** · A move that can hit lots of nearby foes is great for crowd control, but doesn’t actually do much damage.

**2:14** · Maybe the move leaves you vulnerable after performing it, or requires a certain resource, or is on a cool-down timer to stop you spamming it.

**2:22** · Now, when we talk about fast and slow attacks - we’re really talking about frames of animation.

**2:28** · You see, when you hit the attack button in a brawler you don’t immediately strike your enemy: you just start the animation that will - eventually - land a blow on your prey.

**2:38** · Every animation can be split into three phases: the anticipation, which is the wind-up to the attack.

**2:44** · The contact, which is when the attack actually lands and does damage.

**2:48** · And the recovery, which is when the character goes back to a neutral state.

**2:52** · It’s mostly the anticipation phase that will dictate the speed of the attack.

**2:57** · Look at the light and heavy strikes in Transformers Devastation.

**3:01** · The light attack makes contact in just 14 frames, while the heavy attack takes a whopping 36.

**3:07** · That’s really worth considering, because you’re completely vulnerable during those anticipation frames, meaning the enemy could move away, start blocking, or - even worse attack you with a quick strike.

**3:19** · And if you want a really ridiculous example, try doing a heavy strike with the Black Knight Greatsword in Dark Souls, which has almost two seconds of anticipation before the move connects.

**3:29** · Plenty of time for enemies to poke you the tummy.

**3:32** · Now what makes Dark Souls really interesting is that during this time - plus another second or two of recovery afterwards - you can’t do anything.

**3:39** · You can’t dodge, do an attack, or block.

**3:42** · That’s because the Souls games don’t have “animation cancelling”, which is when you can interrupt one move with something else.

**3:48** · In stark comparison, check out Bayonetta where you can change your mind at any moment.

**3:53** · You can be halfway through an attack and then cancel that animation by instantly transitioning into a dodge.

**3:59** · This somewhat subtle change makes Dark Souls very deliberate, and forces you to consider every move carefully - and makes Bayonetta very free-flowing and non-committal.

**4:09** · But does it make the latter game easier?

**4:12** · Not necessarily.

**4:13** · When you’re given the opportunity to cancel any animation at any time, enemies can be more aggressive and won’t wait for you to finish up your current move.

**4:21** · Look at how you’re completely invulnerable during these finishing strikes in Ryse: Son of Rome, but you have to really be on your toes and ready to dodge when punishing foes in Bayonetta, as enemies will come up and fight you midway through a spanking.

**4:34** · Now when we talk about range, it really depends on how “sticky” the game is, which is how easily you snap you to nearby enemies.

### Attack Range

**4:41** · So in a game like Arkham Asylum, where Batman will magnetically snap to enemies in the next postcode whenever you hit the punch button, attack range is pretty irrelevant.

**4:51** · Whereas in Bloodborne, which has almost no snapping, it’s critical that you’re in the right spot before you strike - and that you think about the size, range, and shape of each attack.

**5:02** · As the game goes on, you’ll come to internalise things like the exact pixel distance your whip will reach when you jump.

**5:08** · A certain amount of stickiness is going to crop up in fast-paced games - but I think it’s generally a good idea to ask the player to think about positioning because it adds an extra dimension (or two) to consider.

**5:20** · And if you want, you can get incredibly specific - like with Marth in Super Smash Bros, who does much more damage with the very tip of his sword, compared to the rest of the blade.

### Tactical Options

**5:30** · So you can think of these different attacks as your tactical options.

**5:34** · And what designers should aim for is to have every move fill some niche, and with minimal overlap.

**5:40** · So when you see an enemy in an action game you shouldn’t just randomly hit one of the attack buttons, but carefully consider which will be the right move for this exact situation.

**5:50** · I guess it’s like the difference between weapons in a shooter: a shotgun, sniper rifle, and assault rifle all deal damage, but with very unique properties that make them tactically distinct.

**6:01** · The more moves the player has, the more options they will be granted - but the distinction between these different options will start to become very subtle in a way that novice players may never see.

**6:11** · Veteran players, however, will certainly appreciate the minute differences.

**6:15** · Still, there’s no need to put attacks on every button on the controller.

### Complex Inputs

**6:19** · After all: one of the most sophisticated action franchises around, Devil May Cry, has loads of unique moves with just one main attack button.

**6:27** · So we can look to my video on versatile verbs and perhaps grant the player a charged attack, if they hold the button down.

**6:34** · Or use buttons in tandem with one another: DMC’s basic attack becomes an uppercut if you hold the analogue stick back, or a darting stinger if you hold the analogue stick forward.

**6:44** · There are also plenty of opportunities for contextual moves, like Yakuza’s environmental finishing attacks, or the backstab in Dark Souls.

**6:51** · And, of course, there are combos.

**6:53** · These moves, which see you pushing buttons in a predetermined sequence - sometimes with a small delay between buttons - are an import from fighting games, and offer a reward for memory and timing.

**7:04** · They generally just grant extra damage, but sometimes they provide even more tactical options for the player.

**7:10** · Combos can be a bit overwhelming, mind you.

**7:12** · I can barely remember my PIN number, let alone all these moves in Bayonetta.

**7:16** · So more casual and accessible games like Assassin’s Creed and Ryse: Son of Rome, instead grant you extra damage if you hit the attack button as soon as the previous one lands.

**7:26** · This time, the games are testing and rewarding your timing and ability to read the animations rather than your memory.

### Block and Dodge

**7:35** · So attacking is one thing, but a great combat system also offers interesting ways to defend yourself from damage.

**7:42** · This typically comes in the form of a block and a dodge.

**7:45** · And, much like attacks, these defensive options should be distinct from one another to make you think about the right way to deal with the next incoming strike.

**7:54** · Let’s look at Dark Souls.

**7:56** · In that game a block is easy to perform, and typically negates all damage.

**8:01** · But it’s a big stamina drain, and some enemies will even break your block.

**8:05** · The dodge on the other hand lets you completely avoid an attack, because your character is made invincible during the roll, but it requires careful timing to pull off, also drains some stamina, leaves you vulnerable during the recovery, and changes your physical location.

**8:18** · Hm, decisions!

**8:19** · There’s one other defensive move, though, and it’s one you’ll see in a lot of good combat systems.

### Parry / Counter

**8:25** · I’m, of course, talking about the parry, or counter.

**8:29** · This is typically when you hit the block or dodge button just as the enemy’s attack lands, giving you some kind of bonus - often a lethal blow.

**8:37** · These are super fun to pull off, and a real test of timing that make you feel amazing when they work.

**8:42** · But they can become overpowered, drowning out the rest of the combat system and turning the whole thing into a waiting game, and a simple test of reflexes.

**8:50** · I’m not even exaggerating: if you’ve ever played the early Assassin’s Creed games you’ll know the, uh, “joy” of standing around with your sword up, countering one enemy after another.

**9:04** · So how can we avoid this?

**9:05** · Well one way is to make parries more risky.

**9:08** · You see, designers need to pick the exact moment during the enemy’s attack animation that a parry is viable.

**9:14** · Games like Batman are way too generous, making it effortless to counter every attack.

**9:19** · Whereas something like Nioh makes it a lot, lot tougher.

**9:23** · You can also increase the punishment for missing a parry, like how if you mistime a dodge in Breath of the Wild you’ll be trapped in a recovery animation and vulnerable to being attacked.

**9:33** · Another option is to limit the number of parries you can perform, like in Bloodborne where you have to fire quicksilver bullets to stun enemies and leave them open for attack.

**9:42** · That ammo limitation makes you think carefully about which moves you’ll try to counter.

**9:46** · Other games simply don’t let the parry be a one-hit kill.

**9:49** · In Bayonetta, dodging at the last second lets you enter a slow-mo Witch Time - while in God of War, a well timed counter puts your enemy into a stun.

**9:57** · Both help you, but you’ll need to use the full combat system to actually defeat enemies.

**10:02** · So those are some ways to stop a game becoming too reliant on defence.

**10:06** · But on the flip side, some games let you get away with being so aggressive that you don’t really need to block, dodge, or parry at all.

### Stun Locking

**10:14** · This is often down to the way that enemies get stunned when you attack them.

**10:18** · Hit an enemy during its anticipation frames and it will cancel your foe’s attack and leave it unable to move or dodge while you tee up your next attack.

**10:26** · This is generally called ”stun-locking” an enemy, and lets you just wail on foes without needing to worry about them fighting back.

**10:32** · One way to fix this is to give enemies a stat that stops them from being stunned until you do enough damage.

**10:37** · Dark Souls calls this poise, while most fighting games call it super armour.

**10:42** · Another way is to have some form of stamina, like in Nioh, to stop you from infinitely spamming attacks.

**10:47** · Or you could have multiple enemies attacking you at once, so you can’t focus all of your time on one enemy and must block and dodge those incoming foes.

**10:56** · Or you could just make certain attacks impossible to interrupt.

**10:59** · Or let enemies break out of stun lock.

**11:00** · I mean it’s not very hard to implement - designers just have to remember to do it.

**11:05** · Basically, we don’t want the player to aggressively chew through enemies without ever thinking about defence - but we also don’t want players to hide behind their shield, waiting to pull off parries.

**11:15** · An exciting and dynamic back and forth between offence and defence should be encouraged at all times.

**11:21** · And really, the main way to encourage this sort of behaviour is through interesting enemy design.

### Enemy Design

**11:27** · Enemies should test you on both your offensive and defensive skills, with a wide range of foes that move in different ways, attack at different speeds, and can block, dodge, and perhaps even parry your moves.

**11:37** · Plus: the player should be prioritising different enemies, like focusing on attacking those who can attack from a great distance or quickly killing off healers who can respawn fallen enemies.

**11:47** · Picking your targets is yet another thing to think about.

**11:50** · These enemies should be given clear designs - with distinct colours and easily readable silhouettes - so players can learn which enemies are capable of which attacks, and then pick them out from a crowd with ease.

**12:00** · Plus, those all-important anticipation frames should be hugely exaggerated on enemies, because they should be telegraphing upcoming attacks.

**12:08** · Other games, like Bayonetta, also use sound and visual effects - like glints on the enemy’s weapon - to give you a heads up that an enemy is about to strike.

**12:17** · Handy, when the game is just buckets of visual stimuli being pumped into your eyeballs.

**12:22** · What designers want to avoid, I think, is enemies that can only be killed with very specific moves.

**12:28** · This essentially crushes all those tasty options we just came up with, down to just one dominant strategy.

**12:34** · However, enemies that are resistant to certain attacks - like big brutes who can’t be parried in God of War - are good because they force you to use other moves and strategies.

**12:43** · Because interesting enemies are a major way to encourage you to use the full move-set on offer - and not just rely on the same few attacks, or a couple memorable combos, for the entire game.

### Encouraging the Full Move Set

**12:53** · But there are more ways to do that - like how Furi gives you some health back if you pull off a difficult parry, or how Transformers lets you do a high damage vehicle attack at the end of successful combos.

**13:03** · Of course, the most obvious way to achieve this is through a scoring system, as seen in pretty much every Clover and Platinum game.

**13:11** · These give you points for pulling off combos, mixing up your attack patterns, and fighting enemies in quick succession - but remove points for taking damage.

**13:18** · A scoring system allows novice players to get through the game with simple button mashing but bad grades - but provides an extra challenge for those who have learnt all the intricacies of the combat system.

**13:29** · One other way to make sure you’re using every tool in your arsenal is to have enemies adapt to your playstyle.

**13:34** · It’s not something we’ve seen in a lot of action games, but it cropped up in last year’s Middle Earth: Shadow of War.

**13:39** · In one memorable battle, an enemy got wise to me jumping over its head and so started to deflect that move - forcing me to find another option.

**13:47** · Namely, shooting him in the arse.

### Making an Impact

**13:53** · So: you’ve made lots of distinct attacks.

**13:56** · And you’ve crafted some great defensive moves.

**13:58** · And you’ve used interesting enemy designs to keep a good balance between offence and defence.

**14:03** · But your game still sucks. Why?

**14:05** · Well, it probably just doesn’t feel very good.

**14:08** · Hits feel weak, and counters don’t have that crunch that make you feel like you just pulled off the most difficult move in all of gaming.

**14:14** · So to properly provide this feeling, action game developers spend huge amounts of time on art, animation, and sound to really sell the impact of every attack you make.

**14:24** · So, remember those three animation phases I talked about earlier?

**14:27** · Well they’re also used to make attacks feel more impactful.

**14:31** · Check out this ridiculously satisfying punch finisher from Resident Evil 6.

**14:38** · If we break it down, there’s a huge wind-up where Chris leans back, then a very quick snap to the enemy’s face, a brief pause upon impact, and then a lengthy recovery where Chris’s arm hangs in the air afterwards.

**14:52** · This is the secret to a good, crunchy attack.

**14:55** · Huge anticipation - in God of War 3, we even get some some cheeky slow mo at the start of heavy attacks to increase the animation frames.

**15:02** · Then a very quick strike towards to the enemy - in Ryse, this is so fast that huge chunks of the animation are cut out.

**15:09** · From one frame to the next, your sword can travel great distances.

**15:13** · Then a brief moment to pause upon impact - in Transformers, the two characters stay in the exact same pose for three frames upon impact.

**15:21** · And finally, a hefty recovery, to show that your hero really put their all into the attack.

**15:27** · And all this can be accentuated with visual effects like coloured lines of motion, which are super prominent in God of War and also help explain the unique shape of each attack.

**15:37** · Or blurring the screen upon impact.

**15:39** · Big sparks and other fireworks.

**15:41** · The enemy flashing red, or playing a hurt animation, or being bounced off to the other side of the room.

**15:46** · And, of course, some good, crunchy sound effects.

**15:49** · Here’s a great video on making a powerful punch sound from scratch.

### Conclusion

**15:55** · So, what makes a good combat system?

**15:58** · Well, ultimately, an action game is all about making decisions.

**16:01** · About which enemy to hit.

**16:03** · Where to stand.

**16:04** · Which attack to use.

**16:05** · And when to use it.

**16:07** · Plus, how to react to incoming attacks.

**16:09** · In some games this can be quite thoughtful and considered - in others, you’re making these decisions at a thousand miles an hour.

**16:15** · These games might be overcome by just mashing buttons, but good enemy design and addictive scoring systems push you to be more precise in your movements.

**16:24** · But every design decision must be made carefully to contribute to the overall feel of the game.

**16:29** · Everything from the camera - which swoops out wide in free-flowing fighters, but hangs in close for one-on-one brawlers - to the stickiness of your character, to the use of animation cancelling, to the generosity of when you can parry moves, should all fit each game’s unique feel and flow.

**16:45** · And on top of all that, the game should just feel amazing to play - with all sorts of subtle animation tricks to make every attack hit as hard as a truck.

**16:54** · Nail all that, throw in some innovative new mechanics, and you might just have a combat system worthy of the greats.

### Patreon Credits

**17:04** · Thanks so much for watching!

**17:05** · In the future, we might be able to look at some specific gamesand see how their melee systems are designed to fit a specific style of combat.

**17:12** · For now though, lemme know your favourite combat systems in the comments below.

**17:16** · GMTK is supported by viewers just like you, who kick a few dollars a month my way over on Patreon.