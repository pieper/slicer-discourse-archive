# Embed 3DSlicer in a web GUI

**Topic ID**: 3167
**Date**: 2018-06-13
**URL**: https://discourse.slicer.org/t/embed-3dslicer-in-a-web-gui/3167

---

## Post #1 by @Raccoon5031 (2018-06-13 13:19 UTC)

<p>Hi,</p>
<p>As seen in <a href="https://data.kitware.com/api/v1/item/5b101f958d777f15ebe1fd59/download?contentDisposition=inline" rel="nofollow noopener">this powerpoint</a> (p. 134), 3D Slicer can be exposed via Girder or HTML/JS, as I don’t use Docker, Girder is not an option.</p>
<p>So my question is, how can I proceed to embed my 3D-Slicer in a web GUI? Is there any guideline somewhere? I can’t find anything</p>

---

## Post #2 by @lassoan (2018-06-13 21:03 UTC)

<aside class="quote no-group" data-username="Raccoon5031" data-post="1" data-topic="3167">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/raccoon5031/48/1691_2.png" class="avatar"> Raccoon5031:</div>
<blockquote>
<p>I don’t use Docker</p>
</blockquote>
</aside>
<p>What prevents you from using Docker? Anyway, you can run Slicer on Windows/Linux/MacOS directly on the host without a container.</p>
<p>Then, you can either set up a VNC server and expose that through a web server (that’s what some of the Slicer docker containers do); or access selected functions (such as slice browsing) using <a class="mention" href="/u/pieper">@pieper</a>’s <a href="https://github.com/pieper/SlicerWeb">SlicerWeb</a>.</p>

---

## Post #3 by @pieper (2018-06-13 22:45 UTC)

<p>Note also that if you don’t use Docker you can still do all the VNC or SlicerWeb stuff, it just requires running the same code natively on your computer and that may mean you cannot do anything else useful with the computer at the same time.  The Docker approach basically just turns it into a background service.</p>

---

## Post #4 by @timeanddoctor (2018-06-14 13:45 UTC)

<p>very usfull in the timing of 5G</p>

---
