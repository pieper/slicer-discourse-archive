---
topic_id: 17199
title: "Virtual Reality"
date: 2021-04-20
url: https://discourse.slicer.org/t/17199
---

# Virtual reality

**Topic ID**: 17199
**Date**: 2021-04-20
**URL**: https://discourse.slicer.org/t/virtual-reality/17199

---

## Post #1 by @Honza_Hecko (2021-04-20 11:08 UTC)

<p>Hello,</p>
<p>I would like to ask about the possibility of a problem with Virtual Reality in Slicer. The moment I press “Show scene in Virtual Reality”, everything seems ok. SteamVR starts, announcing that there is a Slicer-real app in the game, but it is dark in the glasses.<br>
Obviously, space responds to movement, but I don’t see anything. No need to install something, or don’t know what it could be?</p>
<p>thank you for your helpfulness<br>
With respect<br>
Honza Hečko<br>
Podlesí Hospital</p>

---

## Post #2 by @cpinter (2021-04-20 11:11 UTC)

<p>Thinking about this, I had the same issue after my cat chew on the VR cable (three times). However, I suppose it is not the same issue for you… Maybe it is simply the connection of the cable? Sorry for the obvious suggestion, I don’t have much experience with hardware issues.</p>

---

## Post #3 by @Honza_Hecko (2021-04-20 11:19 UTC)

<p>Do you think it could only do that with the SlicerVirtualReality extension?<br>
Because other VR software runs normally. I personally don’t think so because I’m able to get into the SteamVR menu. Does anyone have any idea?<br>
Honza</p>

---

## Post #4 by @Honza_Hecko (2021-04-20 14:36 UTC)

<p>would screens help? we’ll really use it in the hospital. Do you have any tips? (reinstall, cache, temporary file, other extension?) i have hp create z book g7. please help</p>

---

## Post #5 by @lassoan (2021-05-02 13:20 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> have you tried Slicer VR with latest Steam version?<br>
<a class="mention" href="/u/honza_hecko">@Honza_Hecko</a> what is your Steam &amp; SteamVR versions?</p>

---

## Post #6 by @cpinter (2021-05-02 14:52 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> I haven’t. I wanted to do minor work on VR until the VTK upgrade, but one of my controllers apparently broke and it is impossible to do anything meaningful like that so I’ve been postponing getting started…</p>

---

## Post #7 by @Honza_Hecko (2021-05-02 16:00 UTC)

<p>Hi to all,<br>
in the end, it was necessary to strictly set up the launch of the entire Slicer via non-integrated NVIDIA graphics. In my head, I thought that Slicer would switch it automatically, but it probably took it integrated during processing.<br>
After switching, the display no longer works. Now I still have to figure out the possibility of displaying the pointer and Cut Plane.<br>
Thank you all.<br>
Honza H</p>

---

## Post #8 by @lassoan (2021-05-02 17:45 UTC)

<p>Probably you need to set Slicer to use the same graphics system that SteamVR is using.</p>
<p>Applications can use some NVidia-specific API to force using a specific graphics system, but this has two issues:</p>
<ol>
<li>We do not know if the user wants to use integrated or discrete GPU (discrete GPU is faster but consumes more power; requires the GPU to remain connected, which may not be desirable when you use an eGPU or systems like the Surface Book, which has the GPU in the base).</li>
<li>It would require Slicer to use a closed-source third-party library (we try to minimize these kind of dependencies).</li>
</ol>
<aside class="quote no-group" data-username="Honza_Hecko" data-post="7" data-topic="17199">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/honza_hecko/48/5303_2.png" class="avatar"> Honza_Hecko:</div>
<blockquote>
<p>Now I still have to figure out the possibility of displaying the pointer and Cut Plane.</p>
</blockquote>
</aside>
<p>You can use any MRML node (a model, markup, volume, etc.) as pointer, just enable controller transforms and apply that transform to the node.</p>
<p>See instructions for model clipping in virtual reality  <a href="https://github.com/KitwareMedical/SlicerVirtualReality/blob/master/README.md#how-to-clip-models">here</a>.</p>

---
