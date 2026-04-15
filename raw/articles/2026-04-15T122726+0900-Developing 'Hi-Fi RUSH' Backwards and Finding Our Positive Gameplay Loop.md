---
title: "Developing 'Hi-Fi RUSH' Backwards and Finding Our Positive Gameplay Loop"
source: "https://www.youtube.com/watch?v=pG4UxqRMNX0"
author:
  - "[[GDC Festival of Gaming]]"
published: 2024-05-14
created: 2026-04-15
description: "In this session, Game Director John Johanas shares how the initial concept for Hi-Fi RUSH came to be. From there, he provides in-depth details into the development team's early learnings on approachin"
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=pG4UxqRMNX0)

In this session, Game Director John Johanas shares how the initial concept for Hi-Fi RUSH came to be. From there, he provides in-depth details into the development team's early learnings on approaching this type of rhythm-action title.  
  
GDC returns to San Francisco in March 2025! For more information, be sure to visit our website and follow the #GDC2025 hashtag on social media.  
  
Subscribe to the GDC newsletter and get regular updates via Facebook, Twitter, LinkedIn, or RSS.  
  
Join the GDC mailing list: http://www.gdconf.com/subscribe  
  
Follow GDC on Twitter: https://twitter.com/Official\_GDC  
  
GDC talks cover a range of developmental topics including game design, programming, audio, visual arts, business management, production, online games, and much more. We post a fresh GDC video every day. Subscribe to the channel to stay on top of regular updates, and check out GDC Vault for thousands of more in-depth talks from our archives.

## Transcript

**0:07** · Hi, everyone today, I'm here to talk about this game.

**0:10** · We made Hi Fi Rush and more specifically how we went about designing it and our methods for iterating on our gameplay loop to reach the result that we wanted for the project.

**0:19** · Uh So as most of, you know, this was a new challenge for us at the studio and we knew that we would be doing a lot of learning while developing.

**0:26** · But I think the biggest thing we came away with was how we basically completely reapproached development in order to design elements to make the game that we wanted to make work.

**0:35** · So looking back, it's strange, but we developed in a way that I would call backwards, hence the title of this presentation.

**0:42** · And just for reference, there are some musical terminology being used in here, but I don't think anything is too complicated.

**0:48** · But before I get into this, let me just give you a quick overview over who I am.

**0:53** · Um So my name is John Johannes and I've been working at Tango Gameworks as a game designer for about 13 years now.

**0:59** · Um I joined when the studio started and I had no prior game design or development experience.

**1:05** · So for me, everything was learning while doing and the projects I worked on this before um were the evil within which I did game and level design.

**1:14** · Um After that, I worked on both story DLC s we did for the game, the assignment and the consequence where I was not only director on the projects, but I did story and script writing.

**1:24** · And then following that, I was the director on the sequel, The Evil Within Two.

**1:29** · And when that wrapped up, I began working on a project um that we should be familiar with as hi fi Rush, um which I was the director on this title as well and to clear up what a director does at Tango since depending on the studio, um director might mean a lot of things.

**1:44** · Um for us, it really means a game director and a creative director all in one role.

**1:50** · Now that being said, I was pretty hands on for this project for a long time since we were quite a small team until the sort of the end part of development.

**1:59** · Um So I did things again, like I, I created the story and wrote the script.

**2:03** · Um I assisted in level design, even gray boxing things sometimes um putting together things in engine.

**2:09** · Um I had my hands in all parts of the game design with the game design team, including about half the game's boss fights and um again, we were a small team for a while and because of the nature of this game, which I'll go into later, it required everyone to be extra hands on and wear many hats.

**2:27** · So it wasn't just myself.

**2:28** · Most of the team members had their hands in multiple features sometimes outside of their skill set.

**2:35** · So a quick look at what I want to talk about today.

**2:37** · Uh The first is I wanna go over how this project started.

**2:41** · Um How are we kind of came with our initial pitch and then how we started developing it and determining our approach to developing the full game?

**2:51** · And then from that approach, I'll go over the what we call positive gameplay loop that we discovered and how we iterated on it to match our image of how the game should play ideally to the vision of that we had in our heads.

**3:05** · Then I'd like to show how we took those early learnings from the project, this sort of working backwards idea and incorporated into almost all aspects of the game development and our workflow.

**3:15** · Um There'll be examples from just general gameplay, there'll be level design and the sequences that we made around licensed music choices.

**3:23** · Um And how we had to essentially reverse engineer those from what we would call our musical impact.

**3:29** · And then I have some takeaways.

**3:31** · Um while you know, a lot of the methods on this project are very bespoke and unique to the type of game that this is, I think a lot of learnings that we took away from it are applicable to any project that's probably trying something new or outside of your sort of safety zone.

**3:46** · And so for the first section, I'll kind of jump into how this project Tafi Rush all started and our goals for the project kind of just beginning with the pitch.

**3:56** · So this is uh quite abridged. But, um, I initially brought this game idea to the table after finishing the evil within two as a nontraditional game from our studio, we knew that we were working on Ghost Wire Tokyo next, which is in the same sort of thread.

**4:12** · Um And we're kind of being solidified as a horror studio.

**4:15** · So I pitched a concept that I was personally very passionate about.

**4:19** · It was very different and I've been planning it in my mind for a while and obviously, it was like nothing we had developed before.

**4:25** · And I pitched something that I said was a colorful and stylish action game, combining music, describing it specifically as a 3d action game where everything in the world, including your actions, syncs to the music, creating the feeling of a music video being edited around you.

**4:43** · And um probably as surprised as uh most of you would be um the initial reaction to me pitching, this was actually positive.

**4:51** · I expected them to walk out of the room laughing.

**4:53** · Um But that didn't happen.

**4:56** · Um however, there were a bit of concerns about the project. Um While we as a studio thought it was cool, we did have no experience at all in this type of genre.

**5:06** · And obviously, it was the complete opposite of everything that we had done before.

**5:09** · So we had our studio image, like I mentioned before, that was focusing on horror um as well as the games that Bethesda at that point was known for.

**5:17** · Um So just sort of pitching it on paper, we thought would be an extremely difficult sell, but we thought it had promise, we thought it was a cool idea and we thought it had potential and we wanted to try something new and it was a good opportunity for us at the studio at the time.

**5:32** · So we decided to prototype the idea.

**5:35** · Uh We wanted to prove the concept and if we can nail it, we could use it to kind of push the idea internally with less friction.

**5:42** · Um And if we did a good job, it could be the groundwork for when we actually started developing, developing the project to kind of hit the ground running.

**5:52** · So when I pitched the game, I defined the gameplay as rhythm action and I immediately got a lot of questions asking what that meant.

**6:00** · Was it a rhythm game? Was it an action game?

**6:02** · And I had an image of what I meant with rhythm action.

**6:05** · And I usually explained it by comparing it to both genres individually.

**6:09** · So to explain this, I kind of put both genres on a spectrum, both rhythm games and action games.

**6:15** · Uh On one hand, we have rhythm games and this is a very general and extreme statement, but I defined it as where the gameplay is strictly matching your, your gameplay to an existing song.

**6:26** · So there would be low player freedom and limitations to game play since essentially, you're just matching to a music track.

**6:33** · But on the other hand, we had action games and again, this is very extreme, but these usually would normally be considered having a high level of player freedom and few to almost no restrictions to gameplay.

**6:44** · And for hi fi rush, I imagined it much closer to action games.

**6:49** · I wanted there to be a freedom of choosing your actions and that free flowing action game play you expect from these character action games.

**6:55** · But there was a musicality to your actions in this case, literally, um is everything I wanted to be tied to the music.

**7:02** · And for that, I wanted specifically there to be no U I telling you where to play.

**7:07** · Um There would have to be a natural cadence to gameplay where everything would just work in tandem with the music.

**7:14** · The goal being that music co ordination wouldn't feel restrictive but actually enhance the action elements.

**7:22** · So um we went into this prototype phase and I set the goal of the prototype to define that ideal form of rhythm action make it not just that concept that I put on that chart, but actually a playable actuality.

**7:34** · So people could understand what the game is supposed to be and so quick rundown of what we did to make this work. Um We basically just had a team of two people. Um It was myself and our lead programmer and we had some assist work from action, uh sorry animation sound and V FX at various points.

**7:52** · And the whole dev time we took about nine months with to come up with a 10 to 15 minute playable demo, which fleshed out the core concept, focusing, focusing mainly on combat, but included some touches on the general tone of the game and visual nuances, like how the world would react to the music.

**8:08** · But an important thing that we decided very on was that we intentionally included no art in this prototype.

**8:13** · So we can focus purely on this gameplay experience, the music and gameplay combination.

**8:18** · Um And actually this was usually successful for us as it did prove the initial concept of rhythm action into a fun, understandable playable experience and helped us to get the project, the project fully green lit.

**8:34** · But it also did what I hoped it would do, which is kind of set up the fundamentals of how we could approach designing the full game.

**8:40** · And I have a short video here kind of showing you a little bit of what that prototype was.

**8:45** · So let's take a look at that.

**8:49** · Mhm Pop. Pop.

**9:09** · Hm.

**9:57** · Ok.

**9:57** · So as you can see, and if you play the game, you know that this is actually extremely, extremely close to how the final project was in terms of direction and functionality in the gameplay.

**10:08** · So I'm going to jump back a little bit of talking about the sort of design fundamentals that we had when we were kind of planning out this prototype and then going into the full game.

**10:17** · Um So, of course, what I, what I imagine rhythm action to be was having gameplay action, synchronize their impact with the music beat.

**10:25** · Um And when I say beat in musical terms, I mean a quarter note interval.

**10:29** · So in my mind, this made sense, having the impact land with the music as it would basically make the impact, feel stronger, but not only that um having that uh the beat and interact with the impact as well would also reinforce synchronization with the music.

**10:46** · And honestly, I just thought this would feel really good in general.

**10:49** · Um The core idea was that you were the star of a music video and if you look at any music video or movie or trailer that's edited to the music or does something similar, it al they always do it where the hit of the action lands with the music giving it that extra power.

**11:03** · But we had a problem because we weren't making a video or a music video or anything like that, we're making a game and in action terms, gameplay specifically, you know, technical action gameplay, we really kind of think of the gameplay in terms of your input and the gameplay response is usually the result of that.

**11:20** · And I was, I was always looking at the result that sort of impact of synchronization of music and action um is something that I wanted the player to feel.

**11:28** · And we had to figure out a way to make a game that somehow gave the player that feeling.

**11:32** · So what I designed with our programmer was the pro in the prototype phase was the foundation for the game, the sort of work backwards approach.

**11:41** · So basically, we started with what we wanted and then just figured out how to get there.

**11:46** · Um The solution we came up with was to interpolate all aspects of gameplay regardless of when the player inputted their actions to synchronize with the music.

**11:55** · We use the sound system wise to take the music data playing in the game.

**11:59** · Um We then converted the B PM or the speed of the song into a tick.

**12:03** · Um That with the game, we used to define where the beats or quarter note intervals were.

**12:09** · And then we would interpolate animation and actions to run in co ordination with that tick, which was again generally in quarter notes to drive all aspects of the game.

**12:18** · And we called this for us we called it the rhythm synchro system or RSS, which basically meant, you know, hey, don't worry where the beat is.

**12:25** · We'll find it for you and we'll make it sync up for you.

**12:29** · So as developers, we're assuming that the player will not press the buttons on the beat and create and create a system that works backwards to ensure that we cover for player error so that they get the desired impact no matter how they play.

**12:42** · And I'll kind of show you how this works with an example.

**12:45** · Um That example being the player's one beat light attack, the basic attack that you do in the game.

**12:50** · So this is an an attack that takes one quarter note or beat from inputting the attack to landing on the next following beat.

**12:57** · The goal being that no matter where the player inputs their action, the attack will always land on a quarter note interval.

**13:04** · So here's the extremely crude timeline for quarter notes and their subdivision and eighth note.

**13:09** · And in this situation, which I'm going to show you, we have just timing, which is what the attack was based around one beat from input to impact.

**13:17** · So in this case, ideally, the player would input their attack on the beat and the impact would be on the next beat and we don't need to do anything because it's, there's no interpolation.

**13:25** · It's exactly as planned. This is fantastic, but we knew that this would never be the case because people will miss this or not play with the beat sometimes.

**13:35** · So let's say the player inputs their beat late, sorry inputs their input late, which would be a little bit after the beat timing.

**13:42** · In this case, we speed up the animation.

**13:44** · So the impact will still land in the same place.

**13:47** · The animation is the same, it's just slightly sped up.

**13:51** · The same goes for with the players pressing their input early, the animation would be extended to land on the beat.

**13:57** · But again, the impact timing is always the same.

**14:01** · And this process of looking for players inputs and assigning the correct impact timing was constantly happening on the back end with our RSS system.

**14:09** · And this logic even worked for passive inputs like the player just pressing the stick and having the player's foot, uh footsteps interact with the beat, like running.

**14:20** · OK.

**14:20** · So we had our basic kind of logic with this RSS system and the, and the underlying systems that we developed.

**14:26** · But now I just want to talk about how this kind of worked in our favor to finding our key core game loop and then how we expanded on it to hit the intended player reaction that we wanted.

**14:37** · So the great part about having actions impact on the beat is that with our logic, we had actually inadvertently created what we called our positive feedback loop uh within the system that we made.

**14:49** · Um So this helped players play the music, even without U I telling them to do so.

**14:53** · And again, uh we wanted to create a game that had natural flowing action without gameplay telling the player when they should play.

**15:01** · Um with U I.

**15:03** · So how did this work? Um And I will use combat again as an example.

**15:08** · Um And it all starts with the input.

**15:10** · So the player is gonna input something and in this case, it will be an attack which just for the case of, of this graph, we're gonna assume it to be perfect timing if input on beat.

**15:20** · Um But again, we're not going to force that on the player, they can press the button whenever they want, we only guide them to that.

**15:26** · So again, if they press an action whenever input it, the next, the action will impact on B and if you do combos by linking attacks and the impact is on beat by just attacking again, when the attack hits, it will then have the player responding in perfect timing to continue attacking.

**15:45** · And if the player somehow gets offbeat, let's say they button mash or they miss something, they just need to look at their next action or attack to get back on and continue playing in rhythm.

**15:54** · So at its core, again, we essentially created a self servicing cycle, which we called our positive gameplay loop.

**16:03** · So we had that philosophy that was working out great for us.

**16:05** · The general systems were working together to support the player playing to the music.

**16:09** · But we wanted to feel even more special because the idea is we wanted you to feel like a rock star.

**16:14** · So part of that approach that we took uh was focusing on these points.

**16:19** · Um The first being we wanted you to have a positive reaction when playing to the music to encourage that type of rhythm action game play that we ideally help you to play with.

**16:29** · But at the same time, we wanted to not punish the player for messing up or not always attacking in rhythm.

**16:35** · The key goal was that this would be an accessible experience to those without a musical background.

**16:41** · And that was constantly providing the player with a positive feeling.

**16:45** · And to do that, we need to figure out ways to inform the player how to play that they're playing well and also not discourage them if they weren't.

**16:53** · And um for you to be able to play in like a rock star without having, without playing musically uh without having musical experience, you may notice this directly correlates to our protagonist and the narrative um who himself doesn't have a musical background.

**17:08** · So this is all sort of coalescing in this sort of uh a full pack package experience as we expanded on this.

**17:15** · So the main approach we used was making it clear when you succeeded, but downplaying if you didn't perform perfectly, one of the basics of successfully playing in perfect timing was that we would have an audio response and try to make your actions feel more like part of the song.

**17:32** · So if you were to attack on beat, um, if you play the game, you know, there's a vocalized, hey, or yeah, that has an immediate response and in game it looked and sounded like this, which you probably don't.

**17:44** · She, another example would be if the player was dashing, um, it had a normal sound effect with it, but when done in rhythm, we would add a drum high hat to it to add to a musical element to the dash effect so subtle, but um these small things kind of added up to just sort of make it feel like more part of the music.

**18:15** · Um But we didn't stop there.

**18:17** · We had a lot of U I also respond to just timing attacks to give the player more feedback as if they were playing to the music.

**18:25** · So we had a visualization of just timing around the player with a note mark as well as added VFX around your metronome like covering cat companion 808.

**18:34** · Um We also have the health and square meter react similarly with vivid colors flashing when actions are timed correctly.

**18:42** · Um And of course, we did things like include physical feedback with a controller rumble when things were timed perfectly.

**18:49** · And then we had our score ranking system which along with indicating just timing, like I showed you previously al also adjusted its rank dynamically increasing more when the player played with better rhythm um with bonuses and, and scores.

**19:02** · But the score system didn't penalize you for not playing in time.

**19:05** · It just adjusted the way the meter changed.

**19:08** · And then there was more of a secret element, but we added damage bonuses to just timing attacks which made battles quicker when played in time.

**19:16** · And we specifically didn't show damage points in game to not make you feel like you're doing less damage.

**19:22** · So it's more of a subtle hidden feature where you just tend to feel like you're playing better when you're playing in rhythm and on the opposite. If you didn't plan time, we just didn't have any of these features show.

**19:38** · So the thing is that the U I didn't have additional effects, you wouldn't get that sound feedback and the score system wouldn't have those bonuses along with your damage being this normal level, but your attacks still landed with the music no matter what.

**19:50** · And our sound design had hits, always play with musical audio all the time as well.

**19:55** · So overall not having these extras didn't feel like a failure and wouldn't distract you when playing.

**20:01** · The only obvious thing was after battle, we would give you a rank that reflected your performance to show where you need an improvement, but we didn't want to discourage you during combat.

**20:12** · However, there was, there were clear game elements um that when they were explicitly tied with a very specific timing.

**20:19** · Um We were, we did use U I to show the player how they were performing.

**20:24** · Um We did want you to know where there was room for improvement when it really mattered in gameplay.

**20:28** · Um The most obvious version of this being um the combo finishers, which we call beat hits.

**20:34** · Um So looking at from the uh the perfect version on the left, um this game in the game, they have an explicit countdown.

**20:42** · So performing in perfect timing, we're gonna acknowledge that timing, we show you specifically the word perfect will appear on the screen and you can even see some screen effects come in to sort of support that as well to make it feel like you did a great job as well as you can see the follow up attack that the sort of two bursts of energy that appear on the ground.

**21:00** · Now, if the player performed what we would consider a good timing, not quite perfect, um We would still count it as a success and the attack will play out as normal.

**21:09** · But um we do, we do let you know that it wasn't perfect, of course.

**21:12** · Um You can see the good instead of perfect good is being shown.

**21:16** · And if you notice there's even those sort of elements, the screen elements of uh sort of lines coming in on the side, those are not there.

**21:23** · Um Again, not too distracting that you wouldn't notice that they weren't there, but again, not as intense as if they were perfect.

**21:30** · Um And in this case, we actually do have a failure to state its technically amiss.

**21:34** · Um, but the character still proceeds with their final attack, but they don't have that sort of bonus attack of those two energy, uh, things that are coming out after them.

**21:43** · And so while this is technically a failure, um, the final attack does play out normally and the player doesn't stall or feel like you can't attack, so it doesn't feel terrible.

**21:51** · Um And we try to downplay failure as much as possible.

**21:54** · You'll notice there's no negative U I, we don't tell you miss on the screen.

**21:58** · Um And the center two circles just sort of fade to red instead of just feeling like like me put an X on it to make you feel like you, you missed your timing or things like that.

**22:07** · So clear enough so that the player could understand that the attack didn't proceed but not enough to be discouraging was what we thought.

**22:15** · And again, when there was a key timing element that alters gameplay, we want to make sure that we were clear with UI information.

**22:22** · We decided to do this with some special attacks which had rhythm game like U I or a rhythm parry system which visualizes a call and repeat pattern.

**22:31** · Since again, these were specific musical games with a success and failure rate and we didn't want the player to guess on how their performance was when they were playing these sections.

**22:42** · So that combat system, which I've just been talking about was arguably our biggest challenge, but also our greatest strength as it was our key gameplay mechanic.

**22:51** · Um the iteration and small touches all added up to a positive experience for players that we felt and even got feedback that was informative on how to play but not overbearing, which, which was great for us.

**23:02** · But as we flushed out how to make the rest of the game, we needed to take our learnings that were the foundation that led us to finding that core gameplay that's sort of working backwards from the impact idea and ingrain it in everything else with the rest of the game.

**23:15** · So going forward, I'll use the word impact again, but you should think of it less of a physical hit and more of about the combination of a feature and music experience intersecting together.

**23:29** · So we had a system that helped things arrive at our impact points with the RSS system.

**23:34** · Um But as developers, we kind of needed to adjust our approach to make sure we knew what we were designing towards and to do that, we had to start essentially thinking backwards, adjusting our workflow.

**23:46** · So when designing every part of the game, I instructed the team to think of every aspect of the game is something that contributes to a world that is synchronized with the music supporting the player experience.

**23:56** · We learned early in the prototype phase that designing a feature then adding in musicality afterwards, didn't work to make the experience feel coherent.

**24:04** · Instead it kind of made it feel tacked on or sometimes even dissonant with the music.

**24:10** · So we applied the approach of thinking from the desired impact and then working backwards with the intended musicality.

**24:17** · Um and a much simpler version of this uh to explain it is uh we would just basically think of where every action should hit ideally musically.

**24:28** · And then we would create features leading into that timing.

**24:32** · So the music or beat would continue regardless of what the player would do.

**24:37** · Obviously, we can't change music, we can't change, we can't just stop the music and restart it when the player wants to do what they want to do that's going to continue regardless.

**24:46** · But um we can change uh how the player could interact with the music.

**24:51** · So to do this, we had to kind of rethink how we would design features in the game and adjust our workflow.

**24:57** · So almost every aspect of the game was synchronized to the music and we needed to know what musical timing we wanted to hit.

**25:04** · Sometimes it would be a single beat, sometimes it was the beginning of a measure of, of a, a part of the song and sometimes it was a specific part of the song, like a guitar solo or uh or the, or the chorus kicks in or something like that.

**25:16** · So everything in the game had an ideal timing of when it would occur.

**25:21** · So if the game is always moving with the music and this was a constant sort of just a timeline that was always proceeding, um We would basically identify what's the ideal timing for the features impact the combination of, of the, of the result with the music.

**25:36** · And then with that in mind, we then work backwards to know when things needed to start to get that desired result naturally in gameplay.

**25:44** · And just like in the combat example, since the user defines the initial interaction, we also need to know how to adjust or interpolate each feature to make it work.

**25:53** · So I showed you some very big things like the whole combat mechanics.

**25:56** · Um But even very small things in the game were designed with this in mind, for example, um something that all developers can relate to is doors.

**26:07** · Um So for our game doors, not, not, not only just needed to open, which is the ideal thing that we want doors to do, but they needed to sync up with the music opening on beat based off proximity with the player.

**26:19** · Um So that it worked with the musicality of the world and I'm going to show you a video and it's going to seem very, very subtle, but you can see that the speed of the store opening depending on when the player interacts with, it will either be faster or slower depending on when the player interacts with it.

**26:37** · And that's how it hits its ideal musical timing, which is that the door should always open on beat to support the music of the game.

**27:05** · OK. Very, very subtle.

**27:07** · Um But you also may have noticed we have a debug menu on the bottom and that helped us sort of see the game in a musical view and tell and see is that impact timing where we ideally would want things to occur, happening where it's intended to be, and we would always check to make sure things were working correctly.

**27:24** · Um So that was a very, uh that was something that we used throughout the entire game.

**27:28** · The doors were used in multiple levels and things like that.

**27:30** · But we also had more unique experiences and we call these kind of unique events or bespoke events.

**27:36** · And this one actually is another door fantastically. Um And this is one that we needed to sync to the first speed of a measure to transition musical tracks.

**27:45** · And I'll kind of let this put video play and then I'll talk about it.

**27:56** · OK?

**27:57** · So in this case, we don't know when the player is gonna hit that button to, to open the door.

**28:01** · Um We know that the final action will be on a beat, but we don't know what beat it will be.

**28:05** · Um So we we did things like create an addition, an initial loop state after it activated to basically wait until the next measure would occur, where then we can then do the opening animation that transition with the musical element so that it would transition correctly into the next musical section.

**28:21** · Um And it all worked from again, working backwards from when the song should change to when the door door should open to what happens when the player interacts with it always thinking backwards from there.

**28:33** · So these were small details for the levels.

**28:35** · Um But on the macro scale, the level design itself was also based around musicality.

**28:40** · Um our approach to level design um structure focused focused on musical peaks and valleys, which was a starting point before we even went into gray boxing levels.

**28:49** · And I have a video uh sorry uh an image of what our game design document look like.

**28:54** · Um And um I apologize for being in Japanese, but I just want to show you the original documentation, but basically this is uh the initial draft of a level design document for our game.

**29:05** · Um We had story beats and event beats that coincided with musical points.

**29:09** · We wanted to impact together in the level.

**29:11** · We would often model them around song structure, for example, choruses where fights and verses were the in between platform.

**29:18** · And these were kind of like mood graphs that gave us the sort of impact points in our level goals.

**29:23** · Which then we would lock in and work backwards from before we even started laying out the levels physically.

**29:31** · So all these features, both large and small were designed in a fairly similar fashion.

**29:36** · We would plan them out making a detailed timeline of how things would occur on paper.

**29:40** · In a way we could, we could see things musically and gameplay wise, making sense.

**29:45** · Then we would build them out in a prototype or gray box form.

**29:48** · This was very important for us.

**29:50** · But in this phase, we would focus on getting all the key elements, especially sound design um in and functional as soon as possible to ensure that the proposed idea was working as intended.

**30:00** · So I'll come back to this in the takeaways, but this approach was immensely helpful in identifying what worked quickly and what needed to be adjusted.

**30:08** · So if adjustments were needed, depending on the severity, we would adjust them right there in the prototype phase until we got them to where we wanted them to be or if they didn't work, we basically returned and rethought the whole plan.

**30:20** · But if the early version was clearly the right step, we would lock in the timing and feature set and then build them out with everyone on the team.

**30:27** · It was important that we didn't leave features dangling if they would work on later if they would work out later on.

**30:33** · Um We wanted to identify those impact points that they, that they were working correctly early and then we could spend more time iterating and improving the quality of.

**30:43** · And so those were just some uh some, some ways that we approached uh the workflow.

**30:48** · But then we had a very extreme version of this.

**30:51** · And this was any time that we were using the license music in the game.

**30:55** · And this was because of uh my stance on using the license music was that I wanted to pay tribute to the songs that we were using and not just use them as background music.

**31:05** · So these sections were essentially reverse engineered around the song so that the gameplay would sync up with it.

**31:10** · In all aspects, we had boss fights where phases and actions were determined by the structure as well as specific rhythmic patterns of the songs dictating attacks or move sets.

**31:20** · And then we had full stages which were again made completely around the structure of the song.

**31:25** · And these were by far the most complicated thing that we had to do in this game.

**31:28** · Um I have examples from both of these sections to give you a rundown on kind of how we made them work and the challenges that we had with them.

**31:36** · Um But first again, when I say pay tribute to the songs, what do I mean?

**31:40** · Um It really means that we would literally design the entire selection uh the entire sections around the song as if there were a music video, we would break apart the song, we would analyze it and bring gameplay and event beats into the song.

**31:53** · And this required an even more intense production and pre production timeline.

**31:57** · And for a detailed example, I'll use the first boss of the game against a robot named Q A One Mill, which we used the license song 1 million by nine inch nails.

**32:08** · So we always started with a general image or idea of what the Boss Fight would entail including story beats, a visual, the type of fight we wanna have.

**32:18** · Um But once we knew what song we were putting it towards, we followed these steps.

**32:22** · Um The first being is that we would take the song and we would break it apart, we would identify its structure and just kind of lay it all out.

**32:29** · Um We'd identified parts of the songs that could theoretically be looped, which meant longer game play port opportunity and parts that could not.

**32:37** · And then we put it all in a timeline and start assigning where we think gameplay would be um where in game events could occur and things like that.

**32:46** · And we took our initial ideas for the fight, you know, like general attack ideas and phases and how we could match how the song feels at certain intervals, cut scenes and story beats were tied in with the music to not only be fun, of course, but to reinforce the connection with the song and make sure that they're musically connected.

**33:06** · And after we had that general layout to find, we would then go into the specifics of each section.

**33:11** · Um Creating cut scenes was comparatively easy because we were setting them mostly to establish lanes of songs.

**33:17** · But it was the playable portions that had to be broken down to ensure that the song was always syncing appropriately to how you play it.

**33:25** · So here's a visual breakdown again, sorry for the Japanese, but this is how we just kind of wanted to show you the original documentation.

**33:32** · Um We, we created a flow chart based off how the music should change based off the player's progress um to prevent the song from awkwardly changing.

**33:40** · We identified sections that needed to play out like the lyrical sections.

**33:43** · We didn't want to cut those off midway through a through a lyric.

**33:47** · So we did things like adjust the boss's HP.

**33:49** · So the song structure would be kept if the player was playing too well.

**33:53** · Um The opposite was if the player was taking too long, we factor that in with looping sections to keep the song in the consistent phase without making it feel awkward or feeling like a broken record.

**34:04** · And this page is just a visualization of how we broke down the lyrics and looping sections of one phase of one boss fight.

**34:11** · Um Each boss fight and each phase and each song was different.

**34:14** · So they each kind of require their own unique take on how they would work.

**34:18** · So we need to break down each one individually.

**34:23** · So then once we had this kind of overall structure done, we would comb through the actual musical audio data or what we call stems looking for rhythms that can be used for certain movements or attacks.

**34:35** · So at this point, we had general attack ideas for how the bosses would fight.

**34:40** · But it's now when we would kind of finalize the rhythm that these attacks would come up with.

**34:44** · So in general, we follow the approach that any time an attack would be specifically tied to a musical part of the song, they should happen exactly when that section happens in the music.

**34:55** · And we would do that by dictating it by with cues set up in the audit uh in the audio data and then also determined by the enemy A I based on how the player was playing.

**35:04** · And a good example um is a video I'm gonna show you here but um because of cool uh my music licensing restrictions, I can't actually play you the song.

**35:13** · Um But I can play the sound effects.

**35:15** · Uh So it's close enough but, and I think it kind of gives the, it helps with understanding what I'm talking about.

**35:22** · Let's check this out.

**35:24** · OK.

**35:29** · What, what, what?

**35:31** · OK. So if you play the game, you probably know this section and the song, but this boss uses, obviously uses his lasers out of his hand as a sort of gameplay mechanic that we wanted to do.

**35:40** · But it obviously has a musicality to it with this guitar riff that's included this da da, da, da, da, da da da.

**35:48** · And if you play that song and if you play the game and you know that song that, that guitar is constantly happening in the background.

**35:53** · And so we made it that obviously, we want the player to experience this sort of attack as a way to play the play the fight, but that we made sure that that attack was always happening in tandem with when that part of the song was playing.

**36:06** · So that was just one example of one attack, sort of syncing up with the music.

**36:12** · And then once we had sort of the gameplay aspect done, we would then turn to non gameplay related elements to tie to the song.

**36:20** · We look at the environment design and start breaking apart.

**36:23** · We would identify things that could be that could pulse and match the song's B PM or speed or maybe there were things that we could flash or move to specific melodies to make it feel like it's part of the song.

**36:35** · Um And then depending on the songs change in mood or volume, we maybe would change the colors of objects or the way things move just to match that.

**36:45** · And there were a lot of other things that just kind of tied to specific ways that the player interacted with the boss things that the player could do special attacks that the boss can do.

**36:55** · And this all was basically around the same concept, right?

**36:57** · If we were making a music video, we needed everything in the game to sync up, so everything felt synchronized.

**37:05** · So that was our very basic approach. Some stuff worked and some didn't.

**37:09** · And we were constantly iterating to find what matched the song times and expressions perfectly.

**37:14** · One thing that we kind of kept consistent was we rarely have ever changed the initial structure and this is just based off what I talked about before is we were building it from an existing song.

**37:23** · We were, we're not going to change that song.

**37:26** · But that final steps of adjusting the rules of each gameplay section, creating and adjusting actions and attacks to the movement and adjusting the environment were always to get it as close to the song as possible.

**37:38** · And this was constant even to the end of development.

**37:41** · Um So realistically, it felt like it never ended. There was never a clear cut. OK?

**37:44** · It's good enough.

**37:46** · Um Probably one of the final things we did before even finishing sending this, the, the game off was adjusting the way lights flashed during boss fights and things like that.

**37:55** · Um And while it was a lot of work, I would say that it wasn't that bad because um the stages that we set to license music were much, much harder to do.

**38:06** · Um The idea here was that we wanted you of course to play to the music, but we wanted to keep the freedom of how you played and not feel like you were just on a linear path.

**38:17** · Um So to do this, we had to find lots of ways to make the stages sync up with your actions.

**38:22** · Sometimes it required thinking of unique solutions for every section the way that the levels transitioned.

**38:29** · Um An example I have is, is a sequence very early in the game of an escape sequence in the, in the level um where we had to think of multiple ways for the player to re sync with the song transition of how they based off how they encountered it so they can change cleanly into the chorus of the or battle portion of the stage.

**38:47** · And so the song didn't feel like it was changing awkwardly.

**38:51** · So remember that we always wanted the player to feel like these sections worked even if they were playing in a non perfect way.

**38:57** · Um And I have videos of this and again, I can't play the original license song.

**39:02** · Um But I can use the unique version we made for players who stream the game which follows the same structure and gives that point across.

**39:10** · So for now, I just wanted you to see how the section plays through.

**39:13** · Um But setting it up, if you haven't played the game, the players running through a level that they're kind of free to sort of move around and, and do some actions based off, you know how they feel about doing them.

**39:22** · Um But they're leaving this area and we want them to transition to a battle which acts as a chorus and we want that transition to be very clean and match with how the song is supposed to play.

**39:33** · And the player is gonna transition using these grappling or magnet points to eventually transition to a fight sequence.

**39:39** · So this is the official correct timing that I'm gonna show you.

**39:49** · Yeah.

**39:55** · OK. So that should have sounded like it matched to the music.

**40:00** · So the issue here is we don't know when the player will start the sequence of events because they're free to play in this section.

**40:05** · But we wanted to transition correctly to again match the song again.

**40:09** · We knew a desired impact point, but we needed to work backwards to figure out how the player experiences it correctly and adjust for their play style.

**40:18** · So for that part, we took two sections, we could adjust to make sure you can match up with the song transition that being the magnet points and the landing animation.

**40:27** · So depending on how on what beat you grabbed the first magnet and how many beats were left until the song needed to naturally change over.

**40:34** · We would adjust how many magnets you had to grab and how long the land landing animation was and there were lots of mixes and matches um for example, five magnets or one beat animation or 44 magnets or two beats of landing animation.

**40:48** · Um And I think there were up to 18 different combinations in this case of how this can play out.

**40:52** · And all of this effort, ideally, you would never notice and it would just work.

**40:57** · But to show you that I'm not making this up, I will show you what some of these variations look like.

**41:04** · So this is a version where there's three magnets and you'll have the longest three beat landing animation to connect.

**41:17** · No.

**41:23** · OK. So that should still sound like it works, right?

**41:27** · And then for this version, it's when the game determines you need five magnets and the shortest a one beat landing animation to sync up plus, all right.

**41:47** · And this was just one small part of a big sequence with a bunch of these type of situations.

**41:53** · Um There wasn't one answer that solved every problem and we needed to approach each sit situation with a unique angle.

**41:59** · But the development logic realistically was always the same.

**42:02** · We were always working backwards from the impact of when the player should land to start the course for this fight, for example.

**42:09** · So realistically, it was a lot of hard work and clever engineering.

**42:12** · Um But the end goal was the same, we just wanted the player to feel like they were playing correctly no matter how they played.

**42:19** · Even if technically the last two examples I showed were theoretically wrong.

**42:26** · OK.

**42:26** · So, so, so those are some very specific things showing how our workflow changed and how we approach design from musical perspective.

**42:33** · But as I spoke before, this extended to almost every section of our team, so each section had their own unique adjustments to coordinate their approach, which required section leads to rethink their methods and when they should get involved in features, the the most obvious example is something like music and sound.

**42:50** · They had to completely overhaul the work timeline to assist in features at a very early state instead of coming in later in development to finish polishing up things.

**42:59** · And all of this was on top of all the other challenges we had like our attempt at a new art style that required animation, art teams and cut scene production to use all new to learn all new techniques.

**43:10** · But in the end, you know, sort of clearly deciding the direction having the whole team buy in early to the concept and always reinforcing it from myself in section leads kept the team focused on what we were making.

**43:23** · And so now some takeaways and again, you may not all be making a rhythm action game like this, but some ways we approach this new challenge may work for you if you are thinking of branching into something that you or your team isn't quite familiar with.

**43:36** · And I'll preface this by saying that I I realized this when I was writing it that a lot of this seems like very basic common sense.

**43:43** · Um But it is frighteningly surprisingly how easy it is to forget these things when you're struggling to make sense of a brand new concept and figuring things out as you go even for an experienced team.

**43:54** · So that being said, one of the biggest takeaways that will echo throughout this section is that we spent a good deal of time early on in the project finding a process and workflow that worked for the unique challenges that making this game required.

**44:09** · And a lot of these methods were almost the opposite of how we approach things on previous projects.

**44:14** · So realigning the team was both difficult as well as actually eye opening.

**44:18** · Since the techniques mentioned here, we can see ourselves using on future projects going forward regardless of the content of the game.

**44:26** · So first for hi fi rush, we always had a final goal that was communicated to the team members giving us a blueprint to work backwards from right from the start.

**44:34** · It's often in game development, you have members working forward without a clear image of of where things end and you have things like scope creep.

**44:41** · But here instead of making things abstract, we tried to make that goalpost clear to avoid confusion as multiple sections work together to build features and scope to a finish line.

**44:52** · The next is that thing is that I I discussed this earlier.

**44:55** · But with our blueprint, we focus first on getting everything in and playable, especially our key features, which in our case were our impact points and how they work with the music.

**45:05** · The goal here was taking anything conceptual which can be confusing.

**45:08** · And in hi fi Russia's case, musicality sometimes is and making it real.

**45:13** · So any lingering questions from the team could be answered in a gameplay form.

**45:18** · And this led to our next point um that by having an early version running with temporary directionally close assets, iteration was much quicker and allowed us to adjust scope.

**45:29** · Um As we locked in ideas, polishing was easier to see and focus on and direction was less likely to be misinterpreted.

**45:36** · But all this really meant was that the images uh the image of what the final product would be became clear to the teams at a much earlier state.

**45:43** · This was in stark contrast to our previous projects um that finally, the vision was kind of coalescing and seen at the end.

**45:50** · So here we were able to in some ways reverse that late dev worry of is this all gonna come together and instead just worry at the beginning of how complicated it was gonna be.

**46:01** · And while we learned a lot and had a lot of great success with this project, um it did not come without its caveats and challenges.

**46:08** · Um For example, there was this big production timeline before starting to dive in and make anything as you saw, the license music sessions were even the the most extreme example of this.

**46:19** · Another was that when the game was kind of close to complete, it was hard or next to impossible to make big sweeping changes because of how closely combined gameplay and music was, which basically meant you would have to redo everything.

**46:35** · Another thing that was uh that almost every part of the game even reused asset had to be custom tailored to each section of the game.

**46:43** · So B PM changes song nuances, those all kind of can change, even uh things that we assumed would be reused.

**46:51** · Um And that required a lot of hand adjustment.

**46:53** · So players had to uh game developers had to go back and constantly reiterate on things that they, that theoretically were working but not perfect and this is something similar but that there was just just an insane amount of detail management, making sure that everything in this game moved to the music and felt correct and felt is kind of like a theoretical thing.

**47:13** · Um Because obviously we did have things program on a program side automatically synced to the music.

**47:18** · Sometimes music isn't always logical and balancing gameplay and music required combing through every part of the game to fine tune details to match with the music.

**47:27** · Because the reality was that if it wasn't perfect, the game just wouldn't feel synchronized and the perception of, you know, this world being set to the music would be broken.

**47:36** · So how do we handle this?

**47:38** · Um Well, here's the thing and I think this is an important point that we often forget.

**47:42** · Um just because we have challenges during development doesn't mean that everything needs to be fixed.

**47:48** · Um Instead it just needs to be recognized.

**47:51** · So any developer will tell you that there is no perfect way to make a game.

**47:55** · Um So we learned early that making this type of game was going to be a difficult and b really annoying.

**48:01** · Um Even though we knew it would be fun as well.

**48:03** · Um So all those key issues that I showed you before that we, that we knew would come up with development.

**48:10** · We basically just acknowledged them early and planned around them.

**48:13** · Um We could have spent time trying to fix, trying to find a fix for everything, but in a way accepting the challenge and all the caveats, let us focus on just making the content and quality of the game.

**48:23** · So all those challenges we faced, we knew that they were inherent to the game that we were making and we kind of prepared ourselves for them, picking our battles based on what our team could do because again, we weren't a big team and couldn't solve every issue that we would come up with.

**48:38** · But outside of the important lesson, we learned about accepting the difficulty of the project, there's some strong points that I think applies to any project, trying something new, which we learned during development of Hi Fi Rush.

**48:49** · Again.

**48:49** · All this sounds very basic, but it's amazing that even a professional team can forget these points.

**48:55** · The first is you want to approach a challenge like what it is something you are unfamiliar with.

**48:59** · Um, for this title, we basically told ourselves, we need to relearn how to make a game.

**49:04** · We worked on horror titles for so long that we had to put all of that know how aside and just focus on work for what Hi Fi Rush was supposed to be.

**49:12** · Um We couldn't be overconfident and we actually had to humble ourselves.

**49:16** · Um And we used all of our learned knowledge as reference.

**49:20** · Um And this helped us prevent um the game losing its sort of originality and identity in exchange for a safe and known experience by just relying on sort of our, what we thought game design should be.

**49:35** · The next lesson was getting things running as soon as possible.

**49:38** · Um Once we planned everything out and the team was kind of aligned on goals, um getting it running and playable while executing on the core idea allows for the team to align quicker on that final goal.

**49:50** · This provides everyone with a good way to give good feedback, which by good, I consider constructive feedback that leads to achieving the goal of the game rather than just a personal opinion.

**50:03** · And then for my final obvious point.

**50:05** · Um But for hi fi rush, we took the time of really figuring out what the core of the game is and understanding what's necessary to build it.

**50:13** · Um We obviously had our core pillars as a project.

**50:16** · Um And we acknowledged the difficulties and we decided to work around them instead of fixing everything.

**50:21** · Since there is no correct way of making a game, it really is about finding a process that works for you and what your team is capable of doing.

**50:29** · But most importantly, of what the game itself requires to be made.

**50:33** · So whatever it is, if the, what you want to do is find that early and stick with it.

**50:38** · Um Warts and all because it's immensely important to realizing your vision.

**50:42** · Um Just like we had to learn as we were doing it that sometimes to get to the end, we had to work backwards from it and that's it.

**50:51** · All right. So thank you uh for listening.

**50:54** · Uh Thank you.

**51:02** · Yeah, I hope this was useful and enlightening uh for you.

**51:05** · And um if there are any questions, we do have some Q and A time, I, I manage sufficient time, but I must remind you, you must fill out the survey for this talk.

**51:13** · They actually won't let you leave if you, if you're letting people you can't leave and to follow the survey.

**51:16** · So, um that is very important I was told. So, hi. Uh I just want to say, I love the game.

**51:25** · Um So what was the process for deciding which license tracks to use and like for which sequences?

**51:33** · So like one example, I really liked the use of the prodigy track in like one of the later kind of big fights.

**51:40** · And so like, what was the process for deciding which songs you wanted and when they kind of use them for which sequences?

**51:47** · OK.

**51:47** · Uh The process for choosing licensing music, license, music was uh purely, I just chose what I like and then I put it in.

**51:54** · Um But uh I got some feedback from members about stuff that, hey, wouldn't it be cool if that worked here or that it doesn't work as well?

**52:02** · And then we adjusted some stuff, for example, the prodigy section was something that was, we, we, that situation was made, but actually wasn't actually tied to the prodigy song.

**52:11** · And then a team member came back and said, what if we co coordinate to that section?

**52:15** · And then we decided to make that that sequence happen like that?

**52:21** · Thank you.

**52:22** · Thanks so much for the talk.

**52:23** · Uh I was really impressed about how y'all, you know, made something new and unique that you've never done before.

**52:28** · Uh You know, in your talk, you said you spent about nine months in the prototype phase.

**52:32** · Uh But with it being something you've never done before, how did you decide on, on that timeline to be able to make a prototype.

**52:38** · Uh Well, the nine month timeline was actually just sort of uh what we were told is like you got nine months.

**52:43** · Um So we uh it was, there was a lot of panic, but realistically, I think probably the first six months or so was like us figuring out actually, this was our first time using unreal as well.

**52:54** · So we were figuring out how to make things work as a game in general and then figuring out what we can do.

**53:00** · Um But a lot of it was playing around like all the stuff you saw with like the environment moving to the beat.

**53:05** · It was just me playing around with, hey, hey, look, I made this, this cube move to the music. That's cool.

**53:10** · And we just made it a feature.

**53:12** · Um But yeah, it was really just playing around until probably the final three months where we, we figured out what the gameplay was like and then we just got everything in and figuring out that, that loop and supporting it and working from there.

**53:23** · -- Awesome. Sounds tough. But thanks for your hard -- work. Awesome.

**53:27** · -- Hi there, love the -- game.

**53:29** · Um One of the key mechanics of the game is being able to summon other characters to do like ASIS attacks and ties into combat and also the music.

**53:37** · What was the development process of that like?

**53:39** · And how did that felt affect the work backwards mentality?

**53:43** · OK.

**53:44** · So the uh questions about the partner attacks and how that the working backwards work there.

**53:49** · Um So that was the partner attack was just mainly uh came from when we were kind of expanding on gameplay ideas as well as story ideas of working as like a a team and, and uh more ways to sort of add depth to the combat.

**54:04** · Um But we, for those, we decided, OK, how, how can these attacks work from a musical angle as well as a gameplay angle?

**54:13** · So for example, like the, the peppermint character, we said it's hard for the player to play in triplets.

**54:19** · What if we had an assist character do that and add their own musicality to that?

**54:22** · So we decided, ok, so that should be the timing whenever you summon them in. When should those triplets happen?

**54:28** · And it's kind of reverse engineered from that and each kind of character had their own sort of uh timing for that, but it was all sort of based off the same concept, you know, if you're pressing a button that's on the beat, um they'll come in on the next following beat. It's the, the lessons we learned by just creating a simple light attack with chai.

**54:46** · We just kind of applied them to all the other characters as well.

**54:48** · All right, cool. Thank you very much. Thank you.

**54:52** · Hi.

**54:53** · Um Naturally some people have bad or no rhythm at all.

**54:58** · Was that ever an issue in development or was it just something that you guys kind of overcame.

**55:04** · Yeah. So if the question is uh in development, if people didn't have rhythm, what were the issues?

**55:11** · Um That was a massive issue. Uh I, I, the biggest, the funniest example being the original prototype was made with two people myself and our lead programmer, um our lead programmer had no musical knowledge.

**55:23** · Um So basically, I was there instructing him.

**55:25** · I was like, this is a beat, this is a quarter note and um I'd write all these diagrams and do all this stuff.

**55:30** · And then um as people join the team, some were more musically inclined, which you didn't have to speak to them.

**55:36** · A good example is our lead animator I still think to this day um does not quite understand some of the musicality stuff um which is always fun.

**55:44** · Um But uh it's kind of interesting to see how people just naturally got into it, but it did help us a lot early on when we were talking about making an accessible experience.

**55:55** · If we, it was two people making this game who were very, very musically oriented oriented, we probably would have made a game that was not accessible.

**56:02** · Um I was giving out ideas early on and our lead programmer was putting them in and playing them and he's like, this can't play this game. Well, to me, it made sense.

**56:09** · Um So that was kind of another eye opening experience of OK, we need to take this down a level so that even if my lead programmer can play it, then it's more accessible to other people.

**56:19** · Does that play into the optional toggle uh U I for the, the rhythm mechanic?

**56:26** · Oh So the optional U I toggle for rhythm was actually one of the final things we implemented as uh something that we, I was adamant about not doing.

**56:34** · Um But um we realized that people did need that assist and so we put it as an option for them. Yes, -- cool. Thank -- you.

**56:44** · Uh You mentioned haptic feedback and I was wondering if you had any specific challenges with like controller rumble, especially spinning motor style rumble that takes time to spin up before you feel it and, and syncing that with the music.

**56:57** · Yeah. Um Controller rumble in general.

**56:59** · Um Since we were designing it with a traditional rumble, um there were problems with that. Uh We tried to try a lot, a lot of stuff to do to do these like quick, quick beats and things like that and that was not working.

**57:12** · Um So that's why I think one of the first things we tried, which people still ask us, why did you not make the controller rumble with every beat is because realistically it would never stop um rumbling because it's constantly gonna be revving that wheel.

**57:25** · So we decided to time it only to the beats, the impact beats.

**57:29** · Uh Yes.

**57:30** · So that's one of those things that we just kind of do trial and error figured out there was no specific uh kind of final ideal goal for that. We just figured out what worked.

**57:39** · Thanks.

**57:40** · Awesome.

**57:41** · Hey, as an animator, I did not use the U I toggle, I got used to the rhythm and it was really nice playing the game.

**57:46** · Uh So my question is, were there any specific challenges when you know, you faced with the animation team in, in -- particular, with respect to the gameplay -- loops, -- the language and the language with -- the animation team as an animator, you know, -- with not a lot of musical -- knowledge and stuff. Oh The animation.

**58:02** · OK. So um that's like a whole another presentation to be honest um of how the animation had to be done. But basically the animation team needed to instead of just animating cool animations, they need to divide their animations into 15 frame intervals because 15 frames was the idea of one beat.

**58:19** · So everything, no matter what they made was made with beat intervals in their, in their animation timeline.

**58:24** · And so we said, OK, if the attack is here, how do we make it?

**58:27** · So it leads every 15 frame interval, you have a feeling of a beat or an impact in the animation that makes it feel musical without making a feeling, feeling stilted.

**58:36** · Um So it was very, very challenging, but it also kind of in a way helped because they knew their limitations of how they built that animation.

**58:43** · And this, this was decided in the prototype phase, right, in the prototype phase even. Yeah, that's what he figured out. Yeah, thank you.

**58:49** · Yeah.

**58:49** · Hey, thank you for your talk. Um I guess, yeah, my question, I mean, I, I may have missed this because I showed up a little late.

**58:55** · But what motivated the overall game design decision to make it? So even if the player doesn't time and action specifically to the beat, chai himself always moves in time.

**59:09** · Yeah, essentially, like no matter, no matter what the player does, the game state more or less always stays synchronized.

**59:14** · And I'm, I guess I'm curious what motivated that um the motivation for just uh you know, making sure it automatically synced to the beat was um was kind of that initial idea that I just had in my head.

**59:26** · I love those character action games.

**59:28** · Um Anything that I saw that was a, was a rhythm game.

**59:31** · You, you have an immediate reaction.

**59:32** · It's the moment you press the button, the action comes out.

**59:35** · But if you want to have things like a wind up or something that makes it feels like you're hitting a character, um you had to ha want to keep that in.

**59:42** · And so when we were iterating on the idea of how do we keep that in but keep the rhythm applied?

**59:47** · Um the idea of interpolating it. So you still got the, the sort of the wind up or the, or the intro to the attack and then having a land with the beat just made it feel much more like a traditional action game.

**1:00:00** · But keeping those rhythm elements, but it also in, in, in that way helped us define, uh, so you weren't, you, you couldn't be offbeat. We can make sure that it always worked right.

**1:00:11** · There was like a feeling of consistency regardless maybe of your input, which might go back to being more forgiving of the players, timing and so forth and yeah.

**1:00:20** · Awesome. Thank you. Thank you.

**1:00:23** · Hi, thank you for the talk. My question was you said that you planned as much as you could and then you started implementing early.

**1:00:31** · Did you ever find yourself in a situation where something that you had implemented early had to be revised?

**1:00:36** · And how did you deal with it if you had to?

**1:00:38** · Uh Yes, there was one stage. Um I think it's the stage uh right before you fight the Boss Corsica where you're climbing a tower where we realized that the stage is just way, way too long and we basically already finished it and we um had to figure out there was only one point in the level. We can, we can cut it to keep the music consistent.

**1:00:58** · So we uh it's we, we did it. So no one actually noticed this but we did it.

**1:01:03** · So it's, it's when you're like doing one of those rhythm jumps.

**1:01:06** · We, we actually secretly warp you to a, we skip an entire stage that we built and we finished and polished and everything like that and we skipped it.

**1:01:13** · But otherwise there were no other sections that could be cleanly cut. So we said that's the only, that's the only way we can do it and everything else. We just had, we just left it in. So some of the criticisms we got that the stages were a little bit too long, -- could have been worse. Really nothing we could do with -- it.

**1:01:28** · That's at the macro level.

**1:01:30** · Was there anything at the micro level that had the same experience at that point?

**1:01:34** · Certainly, no.

**1:01:35** · Um a lot of that stuff was figured out very early and I don't think anything later was cut just outside of or adjusted outside of just chunks of the game that can clearly be just sort of removed.

**1:01:46** · But um no features or gameplay features were kind of cut later in the game.

**1:01:50** · They were kind of locked in early. So, yeah.

**1:01:53** · All right. Thank you so much. Yeah, and I'm being like waved at so that our time is up.

**1:01:57** · But I can answer questions apparently uh in something called an alcove that's on the other side of the, the uh pavilion or West. What, what is it? West Pavilion somewhere over there? That's exactly correct.

**1:02:11** · So I will, I will proceed over there if, if, if you want to continue asking questions.

**1:02:14** · I'll, I'll stick around for a little bit, but thank you again for showing up.