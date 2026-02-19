---
topic_id: 36141
title: "Customizing 3Dslicer For Video Stream Rendering Combining Sc"
date: 2024-05-14
url: https://discourse.slicer.org/t/36141
---

# Customizing 3DSlicer for Video Stream Rendering: Combining ScriptModule for GUI and LoadableModule for Stream Display Without GUI

**Topic ID**: 36141
**Date**: 2024-05-14
**URL**: https://discourse.slicer.org/t/customizing-3dslicer-for-video-stream-rendering-combining-scriptmodule-for-gui-and-loadablemodule-for-stream-display-without-gui/36141

---

## Post #1 by @herryliq (2024-05-14 11:20 UTC)

<p>Regarding custom development of 3DSlicer, I am still a newbie and constantly exploring and learning. From the official documentation of 3DSlicer, we can see that there are three types of Modules in 3DSlicer:</p>
<ul>
<li>LoadableModule</li>
<li>ScriptModule</li>
<li>CLIModule</li>
</ul>
<p>Currently, we want to read the video stream from a capture card and continuously render it in the SliceView of 3DSlicer in our customized version. This is similar to the SlicerOpenIGTLink module, but without the involvement of a GUI, where all node creation is done automatically.</p>
<p>Since the application itself also involves GUI development, we want to add two Modules to accomplish this:</p>
<ul>
<li>A ScriptModule to handle GUI development.</li>
<li>A LoadableModule to handle video stream display.</li>
</ul>
<p>After reviewing some LoadableModule codes, I found that they are all tied to the GUI. Therefore, I would like to ask:</p>
<ol>
<li>Is it possible to develop a LoadableModule without a GUI?</li>
<li>Are there any similar cases that we can refer to?</li>
</ol>

---

## Post #2 by @jcfr (2024-05-14 14:28 UTC)

<aside class="quote no-group" data-username="herryliq" data-post="1" data-topic="36141">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/3bc359/48.png" class="avatar"> herryliq:</div>
<blockquote>
<p>continuously render it in the SliceView of 3DSlicer in our customized version.</p>
</blockquote>
</aside>
<p>The two requirements “render it in the SliceView” and “develop a LoadableModule without a GUI” seems to be contradictory.</p>
<p>By  <em>develop a LoadableModule without a GUI</em>, do you mean a module in which you would customize the layout and hide unwanted element like default Slicer toolbars and alike ?</p>

---

## Post #3 by @herryliq (2024-05-15 01:31 UTC)

<p>Thank you very much for your response.</p>
<p>Although it may seem contradictory, this module will be developed in C++ to ensure processing efficiency, so it does not fall under the scope of ScriptModule. The current design idea is that reading the video stream is an automatic behavior, which means that the video stream is automatically read after the screen transition or when the application starts. Then, the screen refresh is triggered by the update of the node. This behavior indeed looks more like a Non-GUI Loadable Module.</p>
<p>Due to my limited experience with 3DSlicer development, I am currently conducting a feasibility study to ensure that the design plan can be consistent with the existing logic of 3DSlicer.</p>
<blockquote>
<blockquote>
<p>By <em>develop a LoadableModule without a GUI</em> , do you mean a module in which you would customize the layout and hide unwanted element like default Slicer toolbars and alike ?</p>
</blockquote>
</blockquote>
<p>Could you provide more specific information on the point you mentioned? Sorry, I have just started looking into 3DSlicer’s code, and it is indeed very large and complex.</p>

---

## Post #4 by @pieper (2024-05-15 11:57 UTC)

<p><a class="mention" href="/u/herryliq">@herryliq</a> you could start by looking into this feature that already exists.  It could simplify your work a lot:</p><aside class="quote quote-modified" data-post="1" data-topic="9194">
  <div class="title">
    <div class="quote-controls"></div>
    <img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar">
    <a href="https://discourse.slicer.org/t/compressed-video-support-in-slicer/9194">Compressed video support in Slicer</a> <a class="badge-category__wrapper " href="/c/support/11"><span data-category-id="11" style="--category-badge-color: #3AB54A; --category-badge-text-color: #FFFFFF;" data-drop-close="true" class="badge-category " title="The Support category is for all usage questions and general discussion of Slicer and extensions."><span class="badge-category__name">Support</span></span></a>
  </div>
  <blockquote>
    Compressed video support for 3D Slicer is available in both the 4.10.2 and 4.11.0 releases. 

For users: 

Requires Sequences, SlicerOpenIGTLink and SlicerIGSIO extensions
Video recording and playback
Save and load MKV files encoded with VP9
Stream compressed video through OpenIGTLink
Storage space for 60 sec, 10 fps, 640x480 video:

Before: ~222.6 MB, 30s
Now: ~37.1 MB, &lt;1s


Video sequences can be re-encoded with different settings/compression levels

For developers: 

Compressed video frames …
  </blockquote>
</aside>


---

## Post #5 by @herryliq (2024-05-18 01:22 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> We have also evaluated an implementation plan based on SlicerOpenIGTLink. Considering our requirement for low-latency display of captured video streams, our goal is to minimize the performance overhead in the transmission of video streams before rendering.</p>
<p>Therefore, we are currently inclined to directly embed a video stream reading module in 3DSlicer.By emulating the mechanism of SlicerOpenIGTLink, each captured video frame will be rendered into the window.</p>

---

## Post #6 by @pieper (2024-05-18 15:44 UTC)

<p>You can definitely write a custom module in C++ as a loadable module to be as efficient as possible but then do your GUI in Python.  I haven’t done it in a while, but you should just be able to set the <code>hidden</code> property to <code>true</code> in the loadable module.</p>
<p>As a general rule though, it’s good to start with the simplest solution and then optimize once you know what the bottlenecks are.  If you use OpenIGTLink on the same machine (not over the network) there may not be much overhead.</p>

---
