# VolumePropertyAction Animator Problem

**Topic ID**: 40531
**Date**: 2024-12-05
**URL**: https://discourse.slicer.org/t/volumepropertyaction-animator-problem/40531

---

## Post #1 by @Ellie_In (2024-12-05 14:37 UTC)

<p>Hello,</p>
<p>I’m new to Slicer so I’m not sure if this issue is my fault or not, so any insight would be appreciated. I am trying to create an animation using the VolumePropertyAction and I set my start property and end property and I can successfully see that being animated, however after it plays once, it suddenly disappears and the start and end volume properties becomes blank and the volume rendering can’t be seen anymore. Any ideas on what could be the issue?</p>
<p>Thanks in advance,<br>
Ellie In</p>

---

## Post #2 by @pieper (2024-12-05 15:45 UTC)

<p>Hard to say, but probably you don’t have the volume properties set up correctly.  I recently went through the SlicerMorph Animator tutorial and if you follow it carefully it works well.  Be sure to make three volume properties, two for the start and end states of the animation and a third that will be interpolated in the animation process.  It’s a bit clunky but it works.  We’re hoping to get some funding for a more streamlined interface in the future.</p>

---

## Post #3 by @muratmaga (2024-12-05 22:46 UTC)

<aside class="quote no-group" data-username="Ellie_In" data-post="1" data-topic="40531">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/ellie_in/48/78741_2.png" class="avatar"> Ellie_In:</div>
<blockquote>
<p>art and end volume properties becomes blank and the volume rendering can’t be seen anymore. Any ideas on what could be the issue?</p>
</blockquote>
</aside>
<p>What happens when you rerun the animator (click the play button)? Does it stay invisible or the animation work correctly. If it is the latter, at the end it might simply going to a state where nothing is visible so there wouldn’t be anything to concern.</p>

---
