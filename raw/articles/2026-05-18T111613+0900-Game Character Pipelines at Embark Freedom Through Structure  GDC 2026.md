---
title: "Game Character Pipelines at Embark: Freedom Through Structure | GDC 2026"
source: "https://www.youtube.com/watch?v=UFeC-VBbO90"
author:
  - "[[Houdini]]"
published: 2026-04-08
created: 2026-05-18
description: "Embark Studios' Erik Östsjö and Björn Arvidsson take you through the development journey of their character pipeline used for games like Arc Raiders and The ..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=UFeC-VBbO90)

## Transcript

**0:02** · Hello everyone, thank you all for coming to this talk.

**0:06** · And thanks to SideFX for bringing me here.

**0:09** · And my colleague, of course, to present to you about pipelines.

**0:14** · I'm Eric, a technical artist.

**0:16** · Yeah, and I'm Bjorn Avison, currently working as a senior character artist.

**0:22** · Both of us, of course, work at Embark Studios where we are responsible for the character pipeline.

**0:27** · Embark has released two games so far, the finals in 2023.

**0:32** · And of course, Arc Raiders last October.

**0:34** · Both of these projects actively used the pipeline we're gonna talk about today.

**0:40** · So a little bit of background on how we got to the stage where we're here.

**0:45** · We started very early with the pipeline.

**0:47** · Embark had a strong initiative at the start to find new ways of working and exploring new technologies.

**0:53** · And we started straight away, which meant we didn't really have a game in full production.

**0:57** · So whatever you came up with had to be quite flexible and be able to adapt to whatever our games turn out to be.

**1:04** · Starting out exploration, we tried to go with a black box approach from the start.

**1:08** · So we went all in on proceduralism.

**1:11** · We brought in high polys from C-Brush, random straight through, and then we got in-game assets to play with at the end.

**1:19** · This worked surprisingly well, but as most of you can probably guess, that sometimes it didn't fully work out.

**1:26** · And when that was the case, it was really hard for the artists to go in and refine stuff because of the whole black box approach.

**1:33** · So going to our second iteration, we tried to crack this issue.

**1:37** · We basically went to the box and split it into a collection of boxes instead.

**1:42** · And we also went to the character and split it into multiple, more kit-bashy pieces.

**1:47** · This allowed us to basically assign sequences of boxes to each individual piece that best fit that asset.

**1:54** · We did this for our own application.

**1:55** · We built our own Python app that allowed the character artists to set up projects, view characters, and set up procedural workflows.

**2:04** · This was great, and we found USD this way because when we were doing modular stuff, we realized that we probably need a modular way to store the data because having the full character be copy and pasted every box was a bit overkill.

**2:19** · So USD unlocked that modular capability for us.

**2:23** · This, unfortunately, wasn't really the path we ended up taking at that point because doing more with less people, which was kind of the initiative of Embark, didn't work out when we were building an entire application along with our normal tasks.

**2:37** · So the three of us that were working on this were at a loss to like, where do we go from here?

**2:42** · And we were in luck because SideFX had just released a new version of Houdini.

**2:47** · And with it, they're tech solaris, which is all in on USD, which was our new love at the point.

**2:53** · And we just brought that into Houdini, which is like the home of proceduralism.

**2:58** · So it became kind of our home as well for the pipeline.

**3:01** · And that's where we laid our foundation.

**3:05** · So we put up some mission statements after these learnings.

**3:11** · We try to treat characters as an assembly of separate pieces, having a kit bash mindset from the get-go.

**3:19** · We feel that game feedback should be decoupled from the asset feedback.

**3:23** · No need to lock things down until absolutely necessary.

**3:27** · And no blockers in the pipeline.

**3:29** · If there's any step that hasn't had a person look at it yet, procedural has your back.

**3:36** · And finally, we want tools and processes to handle the boring and tedious work for us, getting us 90% of the end result and have the artist come in and do artist things.

**3:45** · We don't want to lock artists out by the tools.

**3:51** · Oops, sorry.

**3:53** · So let's just revisit quickly what technologies will bring us to this point, like achieve the goals.

**3:59** · Firstly, Houdini, because it is our procedural core, basically, and it has great geometry processing.

**4:05** · It also has a very mature node editor.

**4:09** · And finally, customizable, because unfortunately, Houdini has a bit of a reputation of being scary, especially to artists, but it doesn't have to be.

**4:17** · And since it's so customizable, we made an interface that eases people into the workflow and now all the artists are working in Houdini.

**4:25** · USD, I don't have the time to do a full USD deep down.

**4:30** · We love it, but the short of it is, and crudely, it's the PSD of 3D.

**4:36** · So if you were working in Photoshop and you made an image out of layers, that's kind of what you're doing with USD, but for 3D.

**4:42** · So think of going from a JPEG to a PSD and an OBJ2 at USD.

**4:48** · A second benefit is it supports single source of truth.

**4:53** · Since when we do a process, it only needs to save what it cares about, for example, colors.

**4:58** · That means that there is no more second guessing and artists don't have to be like, I wonder if the geometry is updated from the previous stuff or if it's a duplicate since a prior run.

**5:09** · You always only get the relevant data through this layer composition.

**5:14** · Finally, unified Python API.

**5:16** · This was great if you have a Python interpreter in your application, you can leverage USD.

**5:21** · So if we needed an integration, we just built it.

**5:24** · If it didn't exist, if it existed, we basically enhanced it if we needed to, fantastic.

**5:30** · And then, thirdly, we think there is no tool that is a one in all solution.

**5:35** · So it would be a shame to throw away all the existing specialized tools and workflows.

**5:39** · So we try really hard to integrate external DCC into our pipeline.

**5:43** · Okay, just like Eric hinted in the previous slide, Houdini is our main hub and connection point to all of our other software.

**5:52** · This means that all the character artists at embark use it as their central point of reference.

**5:57** · And thanks to its node-based interface, we can get a really clear overview of the character, all of its processes, and exactly what parts go into it.

**6:06** · We also made sure that all the source files, so C tools, marvelous files, and so on, are all easily accessible from the hip file.

**6:14** · Everything you need is in one place, so it's very easy for anyone to jump in and work on any part of the project.

**6:20** · So, how do you start?

**6:22** · Where is everything?

**6:23** · And how do we start building?

**6:25** · Well, we start by launching via our own custom launcher that automatically installs Houdini and all the necessary packages.

**6:35** · Artists also doesn't have to install any other software.

**6:37** · Everything is run from our version control, making it super easy for both developers and artists alike.

**6:43** · Once inside, a project browser lists all the characters in the entire project.

**6:49** · You just double-click on the one you like, or you start a new one.

**6:52** · And now we're actually in Houdini, all ready to work.

**6:57** · So, once inside Houdini, we build an outfit one at a time from the ground up, or we drop an entire working structure with a template.

**7:08** · And we work a lot with templates to speed up the creation process, both in the network stage and on an individual node base.

**7:18** · So, there's a template for building an outfit, different assets, and so on.

**7:23** · And because the network is entirely modular, the size of a project can vary a lot depending on the type of outfit, if it's a different asset entirely, like a backpack, or if you're on a completely different project, like Arc Raiders or the Finals, they both have their unique nodes.

**7:41** · And in this example, it's a backpack.

**7:45** · They don't require skinning or joints.

**7:47** · So, we just skip those processes and nodes entirely.

**7:51** · And here's a more typical character example, where we add some joints for skinning, and we add a node for skinning and joints, and a project-specific node that handles the way we set up first-person arms.

**8:06** · And finally, even more complex character outfits.

**8:11** · Now we added even more nodes, some nodes for kit bashing, some nodes for marvelous up there at the top.

**8:18** · And you can clearly see how the network grows when the need arises.

**8:22** · Then we can combine this entire network, all of these layers stacked together on top of each other, and export it into Unreal.

**8:32** · So, we started our project.

**8:35** · Now it's time to start creating something.

**8:38** · With the first node type we wanna talk about today is the Origins node.

**8:41** · That's how we connect Houdini to our outside DCCs.

**8:45** · This is also where we tie the source files from those DCCs and their respective outputs directly into our hip file, and how we keep the workflow centralized in Houdini.

**8:58** · Even though the artists work in programs like ZBrush, Marvelous, and so on, Houdini handles all the processing, all the procedural stuff, and the overlying hierarchy for the project.

**9:09** · And just as a side note, we won't go into the mesh creation part today because that's another topic.

**9:14** · We have a bunch of automatic processes for that, and a more traditional workflow as well.

**9:20** · It all depends on what's the fastest and how the artist wants to work.

**9:24** · So, how do you actually get into ZBrush and start working?

**9:28** · Well, you drop the ZBrush node.

**9:32** · And then you click on Edit, and the user is launched into the program.

**9:38** · And upon launch, the node has the responsibility to make sure that all the required dependencies are there, all the software updates, all the template files, everything you need to work and stay updated will be automatically synced from our version control.

**9:54** · Once inside, you can work just as you normally would.

**9:58** · And on top of that, we also include a custom plugin and all of our connected software that handles import and export to the pipeline, and a bunch of program-specific tasks.

**10:08** · For example, we have cleanup procedures that make sure the inbound meshes doesn't contain any errors.

**10:14** · We have a custom outliner for our USD hierarchy and a bunch of other things.

**10:20** · And we do this for all of our connected software.

**10:23** · So, there's custom plugging in everything.

**10:28** · And here is our example.

**10:31** · It was jumping into ZBrush by pressing on Edit.

**10:36** · In ZBrush, it quickly becomes a lot of folders to represent to what we see in Houdini.

**10:42** · Fortunately, we can extend Houdini's scene graph into ZBrush by controlling it, and thus allowing the artists to set up their assets inside of Houdini.

**10:55** · And then finally, the plugin does some housekeeping, cleaning up both the origin, in this case ZBrush and Houdini to be in sync.

**11:10** · So, why is this any good, especially compared to a more traditional approach?

**11:16** · There are several reasons, but the two main ones are, everything is a layer, which means no unnecessary exporting importing, because everyone is looking at the same thing.

**11:30** · As soon as that file is updated, everyone gets updated.

**11:34** · This way you can work in several software at once and always be synced with your changes.

**11:40** · Very much like live linking works.

**11:43** · So, in this example, our scene graph in Houdini tells us the truth, and all the other software are aware of that truth.

**11:50** · The hierarchy also gives you a way to add or modify the underlying meshes without breaking anything, like the Photoshop example Eric had.

**12:00** · Changing one layer in the stack doesn't change the others.

**12:03** · It alters the output, but the procedural parts stay the same.

**12:09** · So, as an example, say you want to create a helmet.

**12:14** · We start with a box, we run it all the way through the pipeline into the game, and then we can do maybe a rough block out of that helmet, run that into the game, and then we can come back once again, and then we make the actual helmet, all without breaking the hierarchy.

**12:32** · And we call these placeholder items subcomponents, and these have to match up between our different software, but everything that happens underneath, so the meshes can be anything they want, they can have any name, you're free to change them as you want.

**12:49** · This means that we can build fully complex, fully functional node networks around a placeholder object, and update that whenever.

**12:58** · This creates a lot of flexibility, concepting new ideas, sending new meshes between programs, and handling feedback.

**13:05** · You're not bound by any decision here at all.

**13:10** · Oh, sorry, that was the...

**13:11** · Good.

**13:14** · Yes, so now we're moving on to the next node, which is a fully procedural node, the UV layout node.

**13:21** · And what it does is it ensures that every asset has unified text density within the asset.

**13:28** · Usually the pipeline handles all of the layouts, so we don't do any manual layouting.

**13:32** · It provides the best layout for the task, for the node.

**13:36** · But it's a good example to dive into what makes an embarked pipeline node.

**13:40** · It utilizes mainly three technologies from Houdini, Solaris, which we talked about before, procedural dependency graph, commonly known as PDG, and surface operator, also known as SOPS.

**13:53** · So let's talk about the top layer.

**13:55** · And this is where some people may be like questioning why we use Solaris, because when you talk about geometry in Houdini, you usually think of SOPS.

**14:03** · And it's mostly about finding a way to glue together artistry and tool creation.

**14:08** · And we think that selection is showing intent, so let's compare some selections.

**14:13** · Here to the right, we're selecting some faces on the top.

**14:17** · This is just indice ranges, and if someone were to change the topology, this will quickly break.

**14:23** · So there are some other alternatives in Houdini.

**14:26** · You can use groups.

**14:27** · These are great, but it's essentially just moving the face selection elsewhere.

**14:32** · And it's also flat, so we can't use our beautiful hierarchy.

**14:35** · There is a third option, where you can use path attributes.

**14:39** · And this is very good for setting up procedural setups, but for artists, it's not very nice when it comes to how it actually looks with the at path equals prefix.

**14:49** · If we look at something similar here in Solaris, we can see our graph from before, from our helmet.

**14:55** · And we can see that we can select either just the helmet and everything underneath it gets selected, since Solaris supports selecting at every level of the hierarchy.

**15:03** · We can also select a combination of levels.

**15:05** · Or finally, we can use something very powerful, which is prim patterns.

**15:10** · This is ways to make generalized selections that can just include anything that matches the pattern.

**15:16** · So in this case, we use everything that's at the top and then expand the star.

**15:21** · So we can select, in this case, just helmet, but it could be a lot of assets.

**15:26** · Secondly, the task distribution.

**15:29** · This is what allows us to be quick when we iterate.

**15:31** · Normally, if you would do a native loop, if you change one of the assets, you would still have to wait for all the assets to be reprocessed.

**15:38** · And that can take a lot of time when you do that for each node.

**15:41** · So by using PDG, we can be parallel instead.

**15:45** · PDG also allows us to do custom validation.

**15:47** · What this means is that we can decide when an item needs to be rerun.

**15:51** · And if we don't deem it necessary, we just skip it.

**15:54** · The fastest way to do something is to not have to do it at all.

**15:58** · So we can see here that each little asset becomes a dot.

**16:01** · And then the color shows its status to the user.

**16:04** · We can also see here that for this asset, we care about topology and UVs, because that's what would change our layout.

**16:11** · If the colors change, for example, we don't redo any work.

**16:15** · And finally, we have a good way to indicate warnings to users.

**16:19** · Finally, it's a bit of a lie.

**16:21** · We use much more than soaps, but usually soaps.

**16:23** · We can also use other contexts, like Copernicus for 2D, or other external DCCs like before, Blender and CBrush, in that case, acted as our engine of the node, or command line tools.

**16:36** · Here is a little video to showcase it all in action.

**16:38** · We can see the user both getting a preview, a viewer state, as it's called, to see the UVs.

**16:44** · They can also iteratively refine their selectments.

**16:46** · So they work from a slash star approach, where everything is caught, and then they can refine their selection further down in the parameter view.

**16:53** · You can also see only some dots get triggered.

**16:57** · And you could see the single item at the very end.

**17:02** · All right.

**17:02** · So we modeled together a few pieces.

**17:05** · We have our UVs.

**17:07** · Now it's time for some baking and putting some color on this outfit.

**17:11** · We always had the philosophy of trying to put the artist first.

**17:15** · And we liked that with Substance Painter.

**17:18** · We could embrace proceduralism and, at the same time, blend in manual work, which is a core pillar of our pipeline.

**17:26** · Now, we do have the flexibility to create procedural materials in Painter, or a layered approach in Unreal, which is what we finally set apart for both games.

**17:37** · But before we go into the steps in Painter, I wanted to show another example of what we discussed earlier, how everyone is looking at the same file, and it's one source of truth.

**17:48** · So updating our meshes in Blender will automatically trigger Substance Painter import, and keeping that live link alive in all of our software in the pipeline.

**18:01** · So first step, we go through our auto-matching system, which pairs incoming high poly meshes to low poly meshes.

**18:10** · With a click of the button, the meshes are paired to each other by looking in world space, and then guessing which pieces fit the best together.

**18:19** · If, for any reason, this system matched something that shouldn't belong together, there's always a manual override available as a viewer state, where you can easily click and assign different pieces to each other.

**18:31** · So it's proceduralism, but with manual override.

**18:36** · Once inside Painter, now you have essentially two choices.

**18:40** · Either you just run the node, and Painter will automatically bake everything for you, allowing you to go down to the next node or step in the pipeline.

**18:49** · Or you decide you want to do some manual refinement.

**18:52** · And in that case, we want to do some edits.

**18:55** · But how does that work for us specifically?

**18:58** · Well, it isn't that much manual work at all.

**19:01** · The only thing the user needs to do is assign what pieces you want to be the same material in Unreal.

**19:07** · That's the only work you do in here.

**19:10** · Now, aren't you wondering, isn't it hard to go through this network now that we have so many nodes?

**19:16** · Not really.

**19:17** · Nodes can find their dependencies further up the network, but they can also find their endpoints down the network.

**19:24** · So this way, we can keep Unreal up to date as we update iterating in Substance Painter.

**19:31** · So nodes in our network are allowed to notify other nodes.

**19:35** · The moment the texture is saved here from Painter, the network detects the change, cooks the necessary logic all the way through the graph on any one node that needs it, and then automatically pushes it into Unreal.

**19:49** · Looking at other cases of manual edits for artists, so in this case, we have two assets.

**19:54** · Maybe they were kit-bashed together.

**19:56** · Both assets look good on their own, but together, they unfortunately clip a little bit.

**20:00** · So now comes the question, how do we solve this, and how do we stay procedural?

**20:04** · So we try to use an edit-in-place approach, where we basically add a node in the case where the collision occurs.

**20:13** · Because if we were to go back up and start editing the source assets, then the high poly and low poly might be misaligned.

**20:20** · Or we actually might ruin a perfectly good asset that on its own was already done and baked.

**20:27** · This way, we don't really touch the source data, which is great.

**20:30** · And if we don't like the result or someone decides we shouldn't pair these items, we can just disconnect the node, and then nothing happened.

**20:38** · So here is a showcase of creating the node, selecting what we want to edit, and then diving in.

**20:44** · And inside, you can use pretty much whatever soap you want.

**20:48** · In this case, we use a sculpt to mimic the feel of ZBrush, a node that ships with Houdini.

**20:55** · But it's much more than that.

**20:56** · So a node is also like the glue between proceduralism and manual edits.

**21:00** · So here we can see the first change that represents just moving stuff about.

**21:04** · But we also treat all our manual changes as sort of deformers.

**21:08** · So any new input gets automatically repurposed to fit with our edit.

**21:13** · So it's resistant to topology changes and transforms.

**21:18** · Now let's skin the asset and get it moving.

**21:21** · So like all other processes, we start with just filling in a base procedural pass.

**21:25** · Then we have an internal network, just like Adjust, where we can refine stuff.

**21:29** · And in this case, we can create custom networks because Houdini is procedural, which allows tech anim and tech art to make one-off solutions that still fits with our procedural workflows.

**21:40** · And we can also use caches and just transfer the result.

**21:43** · So if you have a full pipeline in Maya, you can use it as an origin and then transfer your results procedurally.

**21:52** · And this is just to reiterate.

**21:53** · So here we have a viewer state.

**21:55** · And we have done a selection on these left items here.

**21:59** · Then we have iterated upon them.

**22:01** · And the core thing to notice is that it looks completely different.

**22:04** · But our selection hasn't changed at all.

**22:07** · So the user said all the subcomponents inside left items should be rigid and not bend.

**22:13** · And then we just added more components as we went along.

**22:18** · Then the second part is, if we want to expand the boxes I touched upon earlier, we can add custom networks.

**22:24** · But this is also a space for artists and tech to meet.

**22:27** · So it doesn't necessarily have to be a tech person that builds these networks.

**22:31** · They can wrap them up into custom HDAs that are very easily accessible by artists.

**22:36** · So if we have those cases where it's not something that we really want to be part of the node always, we can build a node for it.

**22:42** · We can have the artists use it.

**22:44** · And then when it's mature enough and seems to be something we want to integrate, we can move it to the top interface.

**22:51** · And the artist has an option to select what system they want to use.

**22:54** · And they all layer upon each other.

**22:58** · And one of the most-- usually the end nodes, pretty much, we do some wrapping.

**23:04** · What this means is we basically refit our outfits to fit all our body types.

**23:09** · This was something that was prototyping created for the finals when they wanted to use a lot of customization.

**23:14** · They required six different body types for each clothing item.

**23:18** · And since that seemed like a procedural task, we decided to do it procedurally and let Houdini do the heavy lifting.

**23:24** · Prototyping was easy.

**23:25** · We just made a new node, slotted it into some projects, and started refining.

**23:30** · This meant that nothing had to change for the other pipelines.

**23:34** · Our creators didn't even have to notice the existence of this new RNG workflow.

**23:39** · But when it was matured-- and here are the characters, by the way, from the finals to different bodies-- when the node was mature enough to work and it sold the purpose, we could then simply use it on our creators as well in the future.

**23:52** · It's just a couple of different templates that's required to refit it to a new project.

**23:58** · Finally, batching.

**24:00** · So just like we basically batch process all our assets, we can also batch process all our projects.

**24:06** · In season-- I think it was season six of the finals, we got requests to add more body types.

**24:12** · So we used our batching tool and said, please rerun the wrap and the Unreal export for all the different projects.

**24:19** · And we got them wrapped up here as a nice little UI, which showed each point being a project and the state of it.

**24:26** · This came with a great benefit.

**24:28** · We hadn't just idled and twiddled our thumbs during this time.

**24:31** · We had actually improved all our nodes.

**24:33** · So that meant all the other body types also got a big quality boost for minimal effort, which was great.

**24:40** · And here you can see it going from the old version to the new one.

**24:46** · All right.

**24:47** · We finally arrived at a place where we were ready to export our entire layered structure into the game.

**24:54** · And with that, our final node, the exported node.

**24:57** · We'll also look at some kit-bashing examples, since it's heavily intertwined with the concept of exporting for us, especially assets that have a network.

**25:08** · And lastly, the concept of delayed decision making and setting up the asset for send-off before pressing export.

**25:16** · So we try to keep up more of a publishing mindset, more than just straight exporting to the game engine.

**25:23** · Our assets are our assets.

**25:26** · They can be mixed and matched in different degrees and be set up to be used somewhere else entirely.

**25:32** · So in this example here, what we're doing is we're taking some cords.

**25:36** · We're combining them with a watch, removing some parts we don't like, adding a glove.

**25:41** · All of this is from different projects, different outfits, and then adjusting the parts that intersect in.

**25:47** · And we got ourselves a completely new glove.

**25:50** · And I think what's really important to note here is that we're not only kit-bashing together low-poly pieces, but since our USDs contain everything layered in their networks, you are actually getting the high-poly, the textures, and even skinning, and the source files.

**26:08** · And this is an example of that, like the opposite side of the kit-bashing spectrum.

**26:14** · So like I said, you actually get the source files as well.

**26:18** · So in this case, the marvelous files.

**26:21** · But you can do this for ZBrush, Blender, anything.

**26:25** · They all come along with the network.

**26:26** · And here you can combine different marvelous files to new marvelous clothing.

**26:36** · So this delayed decision-making, what does that give us?

**26:40** · Well, the ability to decide a bit more on the actual in-game asset at the very last stage.

**26:47** · It's not until this step we actually decide on things like texture resolution, UV packing, and what pieces should be combined with what.

**26:55** · Our core idea is always to keep things as fluid and as flexible as possible for as long as possible.

**27:02** · And again, looking back to that flexible iteration we touched upon earlier.

**27:07** · So in this example, we have Celeste.

**27:10** · You can up-press the texture size to maybe fit for an in-game cutscene or something.

**27:16** · And then you can just export that, come back, lower it, and use that for the in-game asset instead.

**27:23** · And now we've actually gone through the entire pipeline.

**27:26** · We'll start to finish.

**27:27** · And we export this on real.

**27:29** · And with that, we finish up this presentation.

**27:32** · So firstly, thanks to all of you who came here to listen.

**27:38** · We greatly appreciate it.

**27:39** · And then secondly, thanks to-- thank you to Ivar, who is responsible for all the cool, unreal stuff and is the third person in our little pipeline team, and also our technical director.

**27:51** · And a final thank you to the character team as well, who have all joined along and created more nodes and debug everything for us.

**28:03** · And also a traitor.

**28:05** · And this is what it looks like when they're in the game.

**28:08** · \[VIDEO PLAYBACK\] \[MUSIC PLAYING\] \[SHOUTING\] \[MUSIC PLAYING\] \[SHOUTING\] \[MUSIC PLAYING\] \[MUSIC PLAYING\] \[MUSIC PLAYING\] \[MUSIC PLAYING\] \[MUSIC PLAYING\] \[MUSIC PLAYING\] \[MUSIC PLAYING\] \[MUSIC PLAYING\] \[MUSIC PLAYING\] They said the world above had ended.

**28:26** · But endings are only for those who forgot how to begin again.

**28:29** · \[MUSIC PLAYING\] \[MUSIC PLAYING\] \[MUSIC PLAYING\] So you learn to listen, to move quiet, think fast.

**28:40** · \[MUSIC PLAYING\] \[MUSIC PLAYING\] \[MUSIC PLAYING\] \[MUSIC PLAYING\] \[MUSIC PLAYING\] Be ready to change your mind.

**28:47** · \[MUSIC PLAYING\] \[MUSIC PLAYING\] \[MUSIC PLAYING\] Up there, the roads are twisted.

**28:52** · The rules are gone.

**28:53** · \[MUSIC PLAYING\] But if you were brave enough to wander and seek, who knows what you might find?

**29:07** · Hey, don't shoot.

**29:09** · Fucking-- \[MUSIC PLAYING\] \[MUSIC PLAYING\] Come on!

**29:19** · \[MUSIC PLAYING\] Come on!

**29:23** · \[MUSIC PLAYING\] Come on!

**29:24** · \[MUSIC PLAYING\] Come on! \[MUSIC PLAYING\] Come on! \[MUSIC PLAYING\] Come on! \[MUSIC PLAYING\] Thank you.

**29:55** · And that is the true end.

**29:58** · But thank you.

**30:01** · We've been asked to remind you to...

**30:04** · Oh, a little epilogue here.

**30:08** · We've been asked to remind you to fill in the survey, the speaker survey.

**30:12** · And since we're done, I don't know if there is any Q&amp;A format, otherwise that's it.

**30:19** · Okay, we're done.

**30:20** · No? No?

**30:23** · Okay, yeah, sure. Any questions?

**30:31** · Oh, one.

**30:37** · When you hire new artists, is there like an onboarding process to learn this Houdini workflow?

**30:45** · There sort of is, but we're very much like just a collective, so we all help each other.

**30:51** · So usually, and since it's one note at a time, you get onboarded slowly and usually start working with one or two of them.

**30:58** · Okay. Super cool, by the way.

**31:00** · Thank you.

**31:01** · Hey, thanks for the talk, guys.

**31:02** · I was just curious on the rigging side, like working with the rigging team on skinning and kind of that back and forth, is that all set on the Houdini side with the skinning and all that kind of stuff?

**31:14** · So if you're asking about how the rigging works, it's very much a combination.

**31:19** · So initially, they had a full pipeline in Maya.

**31:21** · So what we did was we built an origin, similar to ZBrush and Blender, where they could just access the latest data at all times.

**31:29** · And whenever the artist did updates, their cache basically got re-projected.

**31:34** · So if there was a new piece that they hadn't touched, it got procedurally skinned and folded in.

**31:38** · And then they could go and retouch it.

**31:41** · But since then, a lot have changed.

**31:42** · So they have made a bunch of custom notes for procedural clothing, like animation and joint orientation and stuff.

**31:51** · And we're currently working actively on this part that we were showing here, where we basically allowed them to build their own Houdini networks inside of the pipeline.

**32:02** · So we're slowly moving over to being Houdini only while still having access to Maya.

**32:08** · Cool. And like real-time cloth or things like that, like Havoc setups or whatever, are those joints set up on the Houdini side as well?

**32:20** · Not currently. Not currently they're being set up in Maya.

**32:22** · But we are looking at that.

**32:24** · Cool. Thank you.

**32:27** · Hello, everybody. We have time for one more question because it's pretty quick.

**32:30** · But afterwards, we're going to have to have everyone go out and around the corner to a little breakout area.

**32:35** · You guys can definitely keep talking as long as the speakers are available.

**32:39** · But that's all we have time for because we have another line forming outside for the next talk.

**32:43** · Thank you. Cool.

**32:45** · Hi, it's a really quick question. It seems like you guys use a lot of similarities as the fanals.

**32:50** · So I just want to ask how much similarity, how much similar tools you are using between the Arc readers and the fanals in those two games.

**32:59** · It's a lot. It's a lot. Yeah, both projects use the same pipeline.

**33:02** · It's just a few individual nodes per project pretty much.

**33:05** · So you mentioned all the execution process and that kind of joint system, they're all the same in between two games?

**33:14** · Mostly the same?

**33:16** · It's pretty much the wrap system that's different.

**33:18** · Awesome.

**33:20** · And then the customization as well.

**33:22** · Awesome. Thank you so much.

**33:24** · Yeah, it's usually unreal that has some differences. But we do share the engine as well. So a lot is the same.

**33:31** · OK, great. Thanks, everybody.

**33:33** · If you.