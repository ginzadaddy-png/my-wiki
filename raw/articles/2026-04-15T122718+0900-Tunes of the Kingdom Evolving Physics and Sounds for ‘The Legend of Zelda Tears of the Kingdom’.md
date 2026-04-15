---
title: "Tunes of the Kingdom: Evolving Physics and Sounds for ‘The Legend of Zelda: Tears of the Kingdom’"
source: "https://www.youtube.com/watch?v=N-dPDsLTrTE&t=3240s"
author:
  - "[[GDC Festival of Gaming]]"
published: 2024-05-22
created: 2026-04-15
description: "At GDC 2024, developers of The Legend of Zelda: Tears of the Kingdom discuss structuring an expanded Hyrule around physics-based gameplay and evolved sound d..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=N-dPDsLTrTE)

## Transcript

**0:07** · K Yeah.

**0:22** · Hello everyone.

**0:23** · Thank you for coming to listen to Tunes of the Kingdom.

**0:28** · Our presentation about the Legend of the Here of the Kingdom.

**0:35** · This is a highly ensued.

**0:37** · It should be familiar to fans who have been playing the Legend of Zelda series for a long time.

**0:44** · But I doubt anyone imagine that you would be able to attach a piece of IC me to it and use it to serve at high speed in the latest game in the series.

**0:59** · This is a sequel to the Legends of the, the Breast of the Wild.

**1:03** · So you may have guessed their portable cooking pot.

**1:08** · But I doubt anyone predicted that cook import would also have excellent suspension even even we didn't predict that no matter how difficult the situation, sometimes you can just stick a bunch of logs together and figure something out rather than using only wisdom to find a solution.

**1:42** · Sometimes it is just as important to have a courage to power through a problem.

**1:59** · Hello everyone.

**2:01** · I am Takahiro dota.

**2:04** · I joined Nintendo in 2003.

**2:07** · I've been involved in many titles working on game programming, developing game engines and prototyping new games from a technological perspective.

**2:18** · I was a technical director for both breasts of the wild and tears of the Kingdom.

**2:25** · As you just saw, we introduced the ability to stick objects together as a distinctive game mechanic.

**2:32** · In tears of the kingdom.

**2:34** · We wanted to let players combine objects to make new discoveries and to write unexpected methods to start off.

**2:42** · Let me provide some background about how the idea of sticking objects together came about in tears of the kingdom.

**2:51** · First, let's return to the topic of the Breath of the Wild.

**2:57** · We had two major themes during development of Breath of the Wild.

**3:04** · The first was a fast and seamless high in breath of the wild.

**3:09** · We wanted prayers to see a place in the distance and be able to reach it simply going in that direction.

**3:18** · But at the same time, simply making the game field fast and the seamless doesn't necessarily make that game itself fun.

**3:27** · So we came up with the idea of multiplicative gameplay.

**3:32** · This was the second theme.

**3:35** · Now then what does that mean?

**3:39** · Multiplicative multiplicative gameplay is a game structure that lets players combine actions and objects to create many different ways to play?

**3:50** · This was one of the themes of our pres of the world presentation for G DC 2017.

**3:57** · This is a threat from that time.

**4:00** · All objects in the game are connected by same word rules such as physics and chemistry.

**4:09** · This allows actions and objects on the game field to interact on those basis.

**4:17** · These interactions cause many different things to happen automatically such as falling borders, damaging enemies.

**4:32** · And game designers use, use these rules as a basis for the design rather than creating something fun, create a system that makes fun things happen.

**4:45** · This is a concept behind the multiplicative gameplay.

**4:54** · We wanted to take the two development themes that were realized in rest of the world and expand on them even further.

**5:02** · For years of the kingdom.

**5:04** · First, we decided to expand hiro on the scope of players adventure.

**5:11** · Yeah, after developing Sky sword, we wanted to try seamlessly connecting the sky and surface in the future title, there have been many examples of a dark world that is the that is the counterpart of the surface in the series in this game. We created the tips based on this concept.

**5:44** · Our producer wanted to dig holes in the world ever since development of breath of the world started.

**5:51** · So we dug holes, we expanded the world over high, more and more going upwards downwards and even inside.

**6:06** · But let me repeat, simply making the JM field fast. Doesn't necessarily make the game fun.

**6:14** · How should players get around in the sky?

**6:18** · What kind of game play should exist in the depths?

**6:23** · We wanted to enhance the multiplicative game play too.

**6:27** · But how are we going to do that?

**6:33** · By the way, this is an article that was published on the Japanese Nintendo homepage.

**6:39** · After birth, Breath of the Wild was released, these oct balloons were special materials even in breath of the wild, they can make an object put when attached to it.

**6:51** · We implemented this functionality not to be used as a solution, but as a way to make the multiplicative gameplay even more plentiful because of this. It wasn't a major element, but we actually felt that the ability to stick one object to another.

**7:12** · it had a lot of potential.

**7:17** · So when development began on tear of the kingdom, Mr Fujii, the games director produced protype like this.

**7:27** · These were made the embrace of the wireless game engine by phosphorous sticking objects that appear in the game together by combining objects. He created something new by the way, the virus are actually co virus that Mr Fujii stole from a tang.

**7:52** · So we began proper prototyping to stick objects together freely.

**7:58** · The potential of sticking objects together that we felt with the balance and the new value gained by combining objects shown by the prototypes.

**8:08** · We thought that this could be a gameplay point for this expanded world.

**8:20** · In the end, Trahan and the fields were born.

**8:30** · What was once a simple ingredient can now be attached to an arrow to become a powerful way to defeat enemies.

**8:38** · The board on the ground over there can also become a carpet, a new game, new game design using this system was born, even if you aren't sure what to use these things to for at first you will come up with new ways to combine them to make something useful.

**9:09** · Mhm Sticking to things together, produces something new.

**9:20** · We used this as a guide when preparing this presentation which brings us to physics and sound by combining two technical fields that aren't usually spoken about together.

**9:35** · We thought that we might be able to create an interesting story.

**9:41** · Today, I invite the lead programmers from each field to discuss this game, from their perspectives.

**9:50** · And so I will pass the baton to the lead physics engineer Tak Ma.

**9:57** · Thank you very much.

**10:11** · Thank you Doan.

**10:16** · When I first saw the prototype, I was excited that this was going to be a great game, but I also knew this was going to be very, very difficult.

**10:33** · I said to myself, are we really doing this development is going to be chaos?

**10:46** · The more I thought, the more I worried, but in life, it's sometimes important to have the courage to push forward.

**10:59** · As expected, the world fell apart at this rate, the world will destroy itself before Ganon comes back and so began our against the true menace of hero.

**11:23** · Mhm Hello, everyone.

**11:27** · I'm Takahiro to, since I began at Nintendo, I've worked on many games as a programmer and now I developed the in-house F library and tools.

**11:44** · I was a physics programming lead on Press of the world and Tears of the Kingdom.

**11:50** · Thank you for having me today.

**11:54** · Before we start like breath of the wild tears of the kingdom use its havoc as the base for of his exa.

**12:04** · And on top of that, we have our in-house physics celebrity, which is the foundation for the physics in the of the Kingdom.

**12:17** · Please let me switch to Japanese now with the aim of expanding the world by enhancing the multiplicative gameplay.

**12:34** · There were two things we attempted and I'd like to touch on those.

**12:40** · The first was to create an entirely physics driven world.

**12:47** · So the second was to create a system where unique interactions occur without any dedicated implementation.

**12:56** · Ha ha I'll start out by explaining why we needed an entirely physics driven world to give up dynamic during development.

**13:23** · When we say physics driven, what we mean is objects have mass and moment of inertia and they can be controlled using things like velocity and acceleration.

**13:37** · So what would the opposite be? What is a non physics driven object?

**13:42** · So it's what we call a kinematic rigid body control.

**13:55** · It's forcibly moving a rigid body at a velocity calculated from the animation.

**14:09** · The implementation is easy and the results are also visually easy to understand.

**14:14** · So we used it quite a bit in the early stages of development for tears of the kingdom.

**14:34** · However, rigid bodies controlled by kinematics have infinite mass and can be can break down a physics based calculation as seen in this footage, you normally wouldn't expect the metal object to get caught up like this.

**14:58** · Practically speaking, this meant chaos for us.

**15:01** · The clash between these non physics driven objects and ultra hand with its high degree of freedom caused daily problems all over the land of Hyrule.

**15:10** · It went something like this core masa to Mata, I would hear things like it broke or it went flying and I would respond. I know we'll deal with it later.

**15:27** · Just focus on getting the gameplay in there and trying it out.

**15:32** · We were in search of a solution.

**15:45** · The key to that solution was in our experience developing breath of the wild.

**15:49** · This is the cog wheel from earlier that was not functioning properly due to non physics driven controls.

**15:56** · I -- we connected the two fixed car -- wheels.

**16:03** · So with a constraint to transfer velocity Kao Mota de Ma and moved one of them with a motor sub sub because all calculations are now physics based.

**16:31** · All the issues we were facing were now resolved from this experience.

**16:35** · We realize removing all non physics driven objects and making everything physics driven would lead us to the solution we were looking for in tears of the kingdom gates were initially implemented as non physics driven objects.

**16:58** · And thus were one of many objects that proved problematic when using ultra hand you kinematic.

**17:14** · If the player were to place something underneath the gate, the physics calculation would fall apart because this was a kinematic controlled gate.

**17:27** · So to address this, we made the gate physics driven, this is now controlled by connecting the ground and the gate with a slider constraint.

**17:43** · We then add a motor to power it put the this and this removes all the breakdown.

**17:56** · So, but this shift from non physics driven to physics driven, brought many new discoveries for us to.

**18:17** · This particular shrine is one where you can weigh a switch down by reducing the size of a block of ice.

**18:40** · When we changed the gate to be physics driven to prevent the world from destroying itself.

**18:44** · It also resulted in an alternate solution to the shrine simply keeping the gate open.

**18:59** · This is precisely the kind of multiplicative gameplay we were seeking and a confirmation that making everything physics driven was the correct approach.

**19:17** · And this wasn't just limited to objects, player abilities like recall also needed to be physics driven.

**19:31** · While implementation is faster using a non physics driven control for a quick gut check, it can also lead to something like this in the end like everything else, we also changed. Recall to be physics driven.

**19:52** · So as a result, regardless of what the player does, we have a world free from self destruction.

**20:04** · As seen here, up until this point, I've spoken about how a world with a high degree of freedom requires everything to be physics driven.

**20:31** · Every single thing without exception is built with dynamic rigid bodies and constraints.

**20:43** · And this is what allowed us to create a world in which players can freely translate their creativity and imagination into action without destroying the world.

**21:03** · Next, I'd like to introduce the other important element necessary to bring this idea of enhanced multiplicative gameplay to life.

**21:11** · A system that allows unique interactions to occur without dedicated implementation.

**21:23** · OK.

**21:25** · Enhanced multiplicative gameplay aims to create a world in which a multitude of unique interactions can happen based on a player's creativity and imagination.

**21:42** · And so we thought a system that allows for unique interactions to occur without any dedicated implementation is what we needed dedicated implementation.

**21:59** · Here refers to having a dedicated program for each and every interaction we wanted to include.

**22:16** · For example, we wanted the player to be able to build vehicles to explore, but we didn't implement any sort of dedicated vehicle program.

**22:26** · A so, so, so so the things all we did was implement the individual elements like wheels, a steering stick and a wooden board.

**22:41** · So the player can combine them to create a vehicle themselves.

**22:47** · Matara Shina, -- the -- same goes for this gate, there was no dedicated programming.

**22:58** · This is just a combination of wheels, a stone slab and chains.

**23:05** · To me, the wheel is fixed down to the gate which opens up as the wheel rolls up. The chains, quino paddle bolts are yet another example, buoyancy and resistance acting on the paddle boats.

**23:30** · Individual elements like the wheels and wooden boards result in this unique interaction.

**23:43** · -- So -- far, I've touched on the interactions themselves.

**23:45** · But I'd like to now talk about the various parts or components that trigger these interactions.

**23:51** · Ta take the wheel, it's comprised of three rigid bodies. The wheel motor and shaft, instead of the shaft connecting directly with the wheel, it holds up the motor, Morio Maati, the torque from the motor transfers to the wheel's rigid body causing it to -- rotate and the friction between the ground and the wheel creates the driving -- force chains are used to pull an object or change the direction of a moving force.

**24:52** · It's a series of capsule shaped, rigid bodies that vary in number based on length and are connected via ball socket constraints.

**25:08** · In order to simulate water resistance.

**25:10** · When an object enters the water, we use the projected area of the direction of velocity to calculate the resistance.

**25:32** · An easier way to simulate water resistance would be to simply apply velocity decay in all directions.

**25:38** · But in order for rafts and boats, boats to have a more convincing field and movement to them, we needed changes in velocity based on the contact surface.

**25:55** · The components of multiplicative gameplay were not limited to just objects and zona devices, the calculations pertaining to water are applied equally to all objects allowing us to create this unique, unique interaction also known as a paddle boat.

**26:30** · Since our goal was to create a system where unique interactions occur without dedicated implementation, we included many different components that can trigger these interactions.

**26:47** · And we've been so happy to see so many players combining these components in ways we hadn't thought about as they embark on their adventures.

**26:57** · It looks like the -- CACS are happy about it -- too.

**27:16** · I've shared the two concepts crucial in our efforts to create a world that expands through enhanced multiplicative gameplay, an entirely physics driven world in a system where unique interactions occur without dedicated implementation.

**27:39** · But is that enough?

**27:40** · The answer is no, not at all.

**27:42** · There's one more vital piece of the puzzle missing to that piece is working together as a team development consisted of each member of the team understanding the game play, they wanted to realize and understanding what they needed to do to achieve it.

**28:14** · I'd like to now share some of the team's efforts.

**28:26** · First, in order to create an entirely physics driven world, we worked with the artists and designers to set up the physics parameters correctly.

**28:39** · So when we assign a material property to an object such as wood, metal stone and so on that objects mass and moment of inertia are automatically calculated the volume necessary for that calculation is in turn automatically calculated based on the objects shape, not talking about.

**29:16** · But there are times when an automatic calculation doesn't fit our needs.

**29:20** · And in those cases, we work with the artists and game designers to make adjustments.

**29:36** · For example, objects like boards, slabs and plates in tears of the kingdom are actually thicker in those than those in the real world due to various reasons like the need to make them easier to see or control.

**29:58** · If the mass for these objects were to be calculated based on the shape as is they would become way too heavy.

**30:04** · So we corrected the mass and moment of inertia to match what the player would expect them to be.

**30:25** · Because all the puzzle elements for the shrines are physics driven.

**30:28** · Many of them required precise construction.

**30:31** · We created sort of a testing room so that we can check to make sure each and every one of them were functioning properly at any given time.

**30:40** · Sharia.

**30:43** · So I I mio complex objects such as wagons were created through close and careful communication between engineers and artists.

**31:02** · The size and position of the wheels were adjusted based on their physical physics behavior and the artist created the best possible look for them.

**31:12** · Tao Nori.

**31:16** · This is an example of using wheels for purposes other than driving a vehicle.

**31:29** · When a game designer is working on a shrine, they create content that maximizes multiple multiplicative gameplay and fun in this shrine. The key lies in changing the orientation of the boards.

**31:55** · This idea came up when we use the projected area of the direction of velocity in calculating the water resistance.

**32:05** · I personally like this idea very much as it leverages an intuitive interaction with the water.

**32:12** · The show Samo game design AO content Butin corroboration karate team, even the wheel as a component to trigger unique interactions is a result of the collaboration between game design, artistic perspective and physics because we were focused on making sure the experience of driving assembled vehicles felt right and enjoyable.

**32:45** · I vividly remember the team's excitement about how good the driving felt.

**32:49** · Once the suspension was attached a suspension, the artist in charge designed a wheel with built in suspension, which she mentioned was quite challenging.

**33:05** · Given it's not something you really see out in the real world.

**33:12** · Sha the shaft holds up the motor via the suspension and the motor provides driving power to the wheel.

**33:32** · The length of time the wheel makes contact with the ground is increased by having the wheels along with the motor shift up and down and left to right.

**33:47** · There's also a range limit constraint and a plane constraint to control the range of movement.

**33:56** · Lastly, I'd like to talk about the portable pot since they can be placed anywhere.

**34:10** · Now, there's no guarantee the pot will be placed on a flat level surface, meaning your dish could spill out.

**34:21** · No, as a countermeasure to this critical problem, an artist proposed adding telescopic legs to the pod.

**34:42** · But in the end, we decided to put a joint at the bottom of the pot for stability.

**34:46** · I'm happy to say your soup is now safe.

**35:00** · And furthermore, we were so happy to see that the joint on the portable pot has seen a whole range of other uses.

**35:07** · Thanks to the creative imagination of so many players

**35:28** · as you can see from the examples I've shared in order to bring the vast world of tears of the kingdom to life without it falling apart.

**35:35** · It was essential that we worked intimately with designers and artists that had a deep understanding of the world we wanted to create.

**35:45** · To car.

**35:50** · This concludes the physics portion of the presentation. I'll now pass it along to Osada San to talk about the sound. Thank you very much.

**36:01** · Yes.

**36:09** · Thank you. That I A song.

**36:10** · But aren't you forgetting something?

**36:13** · You forgot that sound there.

**36:18** · That's better.

**36:21** · No.

**36:25** · Hello, everyone.

**36:26** · My name is Julian Osada for several years after I joined the company, I was a sound designer in charge of creating sound effects, studying of this uh development of Breath of the Wild.

**36:41** · I became the programming reed and I developed uh in house sound rivalry and tools.

**36:48** · Thank you very much for having me here today.

**36:52** · I'm going to switch to Japanese now.

**37:12** · Now then you've seen how the vast and seamless world of Breath of the Wild was further expanded for Tears of the Kingdom.

**37:18** · But this wasn't just limited to physical space with the ability to combine various objects.

**37:23** · The freedom within the gameplay itself also expanded because of this many different kinds of spaces now appear within the game.

**37:45** · We wanted to depict how sound spreads and naturally echoes in every corner of this expanded high rule.

**37:50** · Whether in open air places, complicated terrain in closed spaces and so on to do this, it seemed we would need some rules that could act as the focal point of our sound design.

**38:16** · We thought perhaps that real world acoustic characteristics could be those rules.

**38:20** · And so we decided to go back to the basics of what it means to make sound in a 3d space.

**38:33** · But before we get into that, did you know that we've worked on various types of interactive music in the Legend of Zelda series?

**38:43** · Here are just a few examples from past games.

**38:58** · Yes,

**39:32** · pretty nostalgic, right times have changed.

**39:44** · But even now in an era where an orchestrated recordings are more prominent, we pour our energy into interactive musical expression.

**40:00** · Yeah.

**40:02** · OK.

**40:15** · For me, clip, clip, OK.

**40:51** · As games grew larger in scale and freer in gameplay so grew the demand for an even more complex musical expression.

**41:02** · -- We -- developed this tool in order to meet those demands.

**41:18** · Now we can graphically edit the way music transitions by connecting notes.

**41:22** · You could say that this is an indispensable tool for designing interactive music as it's being composed.

**41:29** · So -- speaking -- of which we got to see the musical troupe in one of the earlier videos, we tend to notice that their performances and animations are synchronized.

**41:49** · But another distinctive factor is that their music actually plays in the game space in the same way, sound effects do most interactive.

**42:12** · What if we were to expect express some of the bold changes much like the interactive music we spoke about.

**42:18** · But in sound effects, this means rather than just playing an audio file as is manipulating it so that the sound plays naturally within a 3d game space,

**42:44** · we can define making sounds in a 3d space to mean reproducing changes in sounds within the game such as how sounds coming from far away, sound quieter sounds coming from the right side of the screen can be heard from the right speaker and sounds echo.

**42:58** · When the player enters a cave, it is common to depict sounds moving farther away by using a distance attenuation curve for volume with distance taken on the horizontal axis.

**43:19** · But that doesn't mean just lowering the volume is enough, not only do we lower the volume, but we also apply filters that muffle the sound and reverb to blend it with the ambient sounds of the environment.

**43:43** · In doing so we can make it feel like the sound is realistically moving farther away -- rather -- than adjusting the parameters.

**43:58** · Another method that works well is preparing both short and long distance sounds and cross fitting them according to distance.

**44:09** · These methods are well known and have been used on many existing titles.

**44:42** · However, there are many different kinds of spaces in high.

**44:45** · So simply changing the sounds isn't enough.

**44:47** · We want players to be able to tell which direction the sound is coming from how far away it is.

**44:52** · Whether it's inside a cave or a forest and so on. Just by hearing it to do this all sounds really must be controlled by the same rules.

**45:19** · For example, it is a well known property of sound that when distance is doubled volume is halved, this represents the fact that in point sources sound pressure per unit area attenuates with distance and can be determined with a calculation.

**45:39** · Put in simple terms, this means that loud sounds can be heard at a distance while quiet sounds cannot.

**45:50** · In other words, if you want a sound to be heard from far away, then it needs to be loud.

**46:02** · A simple logarithmic graph like this shows the change in volume decreasing by half as distance doubles.

**46:21** · But is that all it takes, for example, a rooster's pro is reportedly about 100 decibels.

**46:27** · It would appear to take 100,000 m before its sound would attenuate, converted to miles. That's about 62 miles in Japan. The distance from Tokyo to Mount Fuji is about 62 miles.

**46:50** · While roosters certainly are loud, I have a hard time believing a rooster crowing in Sacramento could be heard from this stage.

**47:03** · Basically, it's very difficult to represent direct sound attenuation using only the phenomenon of sound diffusion.

**47:15** · -- This -- is where excess attenuation or in this case, air absorption in particular comes into play with air absorption experiments have shown that the higher the frequency, the stronger the attenuation since air absorption decays in proportion to distance, it becomes a curve on a logarithmic graph.

**47:46** · With this the audible range for a rooster's crow becomes a much more realistic distance.

**48:05** · Here too, we use filters to depict stronger attenuation.

**48:08** · For higher frequencies, we take excess attenuation into account and make adjustments to find the right balance for things like what characteristics we need filters for and the distance at which those filters should be applied.

**48:26** · -- Here -- are some examples of sounds that have been designed in such a way.

**48:29** · Can you sense the change in the way the arrow sounds when it impacts?

**49:09** · Did you hear the sound?

**49:10** · Did you hear the way the sound of the vehicle blends into the environment as it gets farther away

**49:32** · when depicting sounds within a game space, it's important to factor in not just distance but also indirect sound.

**49:38** · Whether it's the inside of a house or within a rock cave, you can represent the characteristics of that space with sound by correctly setting how the sounds reverberate or how long their echoes last.

**49:56** · We've used reverb effects on other Zelda Games in the past as well, but there were too many parameters to adjust and it ended up being a lot of work to address.

**50:05** · So, so we made it so the reverb parameters would be automatically calculated information such as room capacity based on the direction and distance of nearby walls and sound absorption rate based on the material of the walls is collected and used to calculate parameters using a formula called I R's reverberation time equation.

**50:45** · This is what echoes sound like when based on the reverberation equation.

**51:33** · Taking it a step further.

**51:34** · This game has a much larger amount of complicated terrain such as caves, sound obstruction and inclusion are also important when creating even more realistic sounds for high roll in this game.

**51:52** · In order to depict a three dimensional world, the terrain contains voxel information.

**52:04** · Each vel stores terrain information such as whether its coordinates are located indoors or whether they are near the water's surface.

**52:17** · They also contain information vital to level design such as whether it's possible to use ascend sound uses these voxels too to search for sound paths using an informed search Algo algorithm to give a bit of extra information. In this game.

**52:48** · The sound system performs calculations for the audio listener based on the camera's position, but searches for sound pass between the sound force and links position.

**53:01** · This is why sound changes when you go behind a wall like this.

**53:30** · This also addresses cases when the sound path is changed dynamically by a door P as you can see, expanding the degree of freedom and the world itself paints the world with a diverse palate of sound.

**54:11** · -- The -- important thing here is that all sounds follow the same rules and among those rules, loudness is particularly important.

**54:34** · Basically, if you create acoustic characteristics based on the loudness of a sound such as how loud it is and how far it can be heard.

**54:41** · All that's left is to assign a loudness to each sound and you'll be able to hear them within the game space properly.

**55:01** · This is how sounds can now be heard in high roll from quiet.

**55:05** · Sounds like the heart container to loud. Sounds like the storm cloud.

**55:35** · And what's more instrumental music that isn't a sound effect can also sound as if it's echoing off of nearby walls or coming from the bottom of the cliff.

**55:49** · Ok.

**55:52** · But

**56:25** · -- each -- and every sound now plays naturally within the game space.

**56:29** · But now that I mention it, there is an incredible amount of freedom in this world.

**56:33** · It would not be possible to prepare dedicated audio files for all of the many different things that can be created with ultra hand.

**56:45** · -- And -- so like with physics, the sound team also thought of a system where sounds would play without dedicated implementation.

**57:05** · Take a look at this wagon. For example, this is just a combination of the sound of wheels rolling, the short repeated shaking of the wooden bed, the chains connected to the bed and so on.

**57:14** · We did not use any recordings of actual wagon sounds.

**57:27** · Even this paddle board, paddle boat sound is a combination of the sound the water makes when wheels rotate through it and the sound of wooden boards fighting water resistance as they splash through the water.

**57:47** · We made a system that analyzes the way rigid bodies controlled by the physics system will move then bases the sound on their size and material.

**58:03** · As a result, various sounds will now play without needing to have a dedicated program set up to play them.

**58:11** · -- Whether -- it's the flux constructs geometric movements or sliding down a rail on a hook.

**58:29** · The suspension bridges are also held together just with physics without any kind of special suspension bridge program at all.

**58:35** · And their wobbling and creaking sounds play automatically.

**58:46** · Of course, these sounds are also based on the sound loudness rules.

**58:49** · I explained earlier and they play naturally within the game space.

**59:08** · Having come up with this form of implementation, makes it feel like we have in a sense built a rule system for how sounds are made in the world of high rule.

**59:16** · Many of the sound designers were surprised at the high quality sounds that were created with the system sounds which they had no memory of creating even the director told us. So this is basically a physics engine for sound, isn't it?

**59:47** · We didn't start out with the goal of building such a system, but it was the result of our efforts to use sound to make the expanded high rule more dynamic.

**59:54** · That's all for me. Thank you very much.

**1:00:08** · Thank you. The guy has.

**1:00:10** · So also the song physics and sound are two different fields. But I think they have some things in common when it comes to how they evolved in this game, first, both steer towards a more rules based system design to allow for greater prayer freedom.

**1:00:31** · And these designs added another layer of complexity to interactions that occur within the game.

**1:00:41** · And this is as a result, they each created a system that brings new discoveries, not only to players but also as developers.

**1:00:55** · As I explained at the beginning, the concept for multiple multiplicative game play was rather than creating something fun, create a system that makes fun. Things happen with scars of the kingdom.

**1:01:10** · We aim to achieve an even higher level of freedom as a result.

**1:01:17** · Rather than determining each object movement.

**1:01:20** · The physics team focused on creating a system that makes the objects move.

**1:01:27** · And rather than creating every sound you heard in the game, the sound team created a system that makes it sound that way.

**1:01:37** · The fact that they focused on and worked hard to tune this system is fascinating to me rather than creating unique interactions, create a system that causes unique interactions to occur.

**1:01:57** · I believe this was the essence of the evolution of physics and sound in tears of the kingdom.

**1:02:06** · That's all for our presentation.

**1:02:11** · Thank you for your kind attention.

**1:02:20** · And the interpreters you have heard today are from Nintendo of America.

**1:02:25** · Let's have a big iron of app for them too.