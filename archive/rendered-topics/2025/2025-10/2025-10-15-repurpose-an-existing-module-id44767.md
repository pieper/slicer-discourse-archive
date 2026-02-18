# Repurpose an existing module

**Topic ID**: 44767
**Date**: 2025-10-15
**URL**: https://discourse.slicer.org/t/repurpose-an-existing-module/44767

---

## Post #1 by @mohammed_alshakhas (2025-10-15 12:01 UTC)

<p>Im completely novice and have zero coding skills .</p>
<p>I’m  planning to start  coding a module . One for TMj viewer and possibly another one dedicated for Clipping segmentation.</p>
<p>It’s partially a need and partially a fun project .</p>
<p>I’m gonna use spec kit / GitHub copilot / gpt codex . for vibe coding</p>
<p>Im thinking that it would be much easier to build on an existing module and down extras . Is that possible that I get the code for segmentation is editor for example and delete all the code for editing and only make the part for viewing then edit it to my purpose</p>
<p>Or do I have start something from scratch ?</p>
<p>Any advise is highly appreciated</p>

---

## Post #2 by @pieper (2025-10-15 13:36 UTC)

<p>Something like copilot or gemini should be able to give you a good description of how Slicer’s codebase works and even get you started with templates and working examples.  Be aware that it can also be difficult or impossible to debug vibe code, so take very small steps and test as you go.</p>

---

## Post #3 by @muratmaga (2025-10-15 17:12 UTC)

<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="1" data-topic="44767">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>Im thinking that it would be much easier to build on an existing module and down extras . Is that possible that I get the code for segmentation is editor for example and delete all the code for editing and only make the part for viewing then edit it to my purpose</p>
</blockquote>
</aside>
<p>This tells me you are not ready for vibe coding, not just yet. A module like Segment Editor is not something you can easily strip down and make it work for your purposes. There are different types of modules with Slicer (CLI, C++, Python scripted) that work differently (structure wise) and have different levels of complexities. So you really want to read the developer guide a bit more carefully, and then probably through python scripting develop what you want to do (as opposed to building a module). Script is much easier to debug and iterate over, and once you figure out the workflow for a specific dataset, then you can start the designing and writing the logic that you will need for the module development and the UI (which can get complex very easily and quickly).</p>
<p>As someone who is sort of slightly ahead of you on this, I gave up on having agent build a module. I am perfectly happy if they can help me create the workflow as a script, and then ask them to convert to a simple module.</p>
<p>It is fun, but first you need to get familiar with Slicer developer guide. (also LLMs make mistakes, like looking at older documentation etc. To be able to hold their hands, you need to know where the things are and point specifically those in your prompts).</p>

---

## Post #4 by @mohammed_alshakhas (2025-10-25 14:52 UTC)

<p>im of course not ready for and probably will never be properly trained for it . howver i started and im halfway into small module project .</p>
<p>the way im using it now is using the codes from other extensino as reference. im making progress so far and did one thing i really liked but i want to add more .</p>

---

## Post #5 by @mohammed_alshakhas (2025-10-25 14:53 UTC)

<p>using specs files and iterating small steps is keeping me sane , otherwise you are right those are terribel to debug</p>

---
