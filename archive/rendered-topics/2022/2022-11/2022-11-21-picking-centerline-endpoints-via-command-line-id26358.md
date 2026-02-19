---
topic_id: 26358
title: "Picking Centerline Endpoints Via Command Line"
date: 2022-11-21
url: https://discourse.slicer.org/t/26358
---

# Picking centerline endpoints via command line

**Topic ID**: 26358
**Date**: 2022-11-21
**URL**: https://discourse.slicer.org/t/picking-centerline-endpoints-via-command-line/26358

---

## Post #1 by @nlbrown62 (2022-11-21 20:30 UTC)

<p>Hello,</p>
<p>I have been using centerline and network extraction in VMTK through the Python interface. For centerlines, I have been using the pickpoint GUI to set the start and endpoints for vessels, and I want to switch to specifying these points on the command line. I have tried passing in coordinates (in voxels and millimeters) to points in the vessel via the “pointlist” option, but the centerline fails to generate. Is there another option I should be using, or is there a specific format that the seeds need to be in?</p>
<p>If the seeds are required to be on the vessel surface and not just anywhere in/on the vessel, is there a way to get the closest point to the specified seed on the surface?</p>
<p>Thank you in advance!<br>
Nicole</p>

---

## Post #2 by @chir.set (2022-11-21 21:10 UTC)

<aside class="quote no-group" data-username="nlbrown62" data-post="1" data-topic="26358">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nlbrown62/48/17415_2.png" class="avatar"> nlbrown62:</div>
<blockquote>
<p>command line</p>
</blockquote>
</aside>
<p>What do you mean by ‘command line’ here ? Is it system console command line interface ? Python console inside Slicer ?<br>
And how do you determine the endpoint coordinates ?</p>

---

## Post #3 by @nlbrown62 (2022-11-22 15:28 UTC)

<p>The command line would be a system console (Git Bash on Windows in my case); I am running the centerline extraction from a Python script using functions from vmtkscripts. The endpoint coordinates were landmarks labeled in advance using Slicer fiducials.</p>

---

## Post #4 by @chir.set (2022-11-22 16:44 UTC)

<aside class="quote no-group" data-username="nlbrown62" data-post="3" data-topic="26358">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nlbrown62/48/17415_2.png" class="avatar"> nlbrown62:</div>
<blockquote>
<p>a system console</p>
</blockquote>
</aside>
<p>Ok, I won’t be of help here,</p>
<aside class="quote no-group" data-username="nlbrown62" data-post="3" data-topic="26358">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/nlbrown62/48/17415_2.png" class="avatar"> nlbrown62:</div>
<blockquote>
<p>on Windows</p>
</blockquote>
</aside>
<p>and even less here, sorry.</p>

---
