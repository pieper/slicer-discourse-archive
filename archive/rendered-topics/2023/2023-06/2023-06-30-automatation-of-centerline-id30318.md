---
topic_id: 30318
title: "Automatation of Centerline"
date: 2023-06-30
url: https://discourse.slicer.org/t/30318
last_bumped: 2026-05-25T13:40:13.919Z
---

# Automatation of Centerline

**Topic ID**: 30318
**Date**: 2023-06-30
**URL**: https://discourse.slicer.org/t/automatation-of-centerline/30318

---

## Post #1 by @Charlie_Hayward (2023-06-30 11:18 UTC)

<p>Hi all, I am looking to automate the vmtkcenterlines function in order to be able to run it on a server. It seems that my option is to have open profiles and use seed selector. This causes an issue because I need the entire processing to be automated, to open the profiles I would need to utilize something like vmtksurfaceclipper which requires a GUI. Is there any way to either automatically generate centerlines without open profiles or automatically clip ends to create open profiles?<br>
Thanks!</p>

---

## Post #2 by @lassoan (2023-07-21 14:10 UTC)

<p>You can have a look how it got fully automated in 3D Slicer’s Extract Centerline module. See source code <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py#L327">here</a>.</p>

---

## Post #3 by @lassoan (2023-10-26 02:55 UTC)

<p>3 posts were merged into an existing topic: <a href="/t/aneurysm-removal-and-reconstruct-the-parent-vessel/32304/6">aneurysm removal and reconstruct the parent vessel</a></p>

---

## Post #4 by @Thretent (2026-05-25 10:26 UTC)

<aside class="quote no-group" data-username="Charlie_Hayward" data-post="1" data-topic="30318">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/charlie_hayward/48/66528_2.png" class="avatar"> Charlie_Hayward:</div>
<blockquote>
<p>Hi all, I am looking to automate the vmtkcenterlines function in order to be able to run it on a server. It seems that my option is to have open profiles and use seed selector. This causes an issue because I need the entire processing to be automated, to open the profiles I would need to utilize something like vmtksurfaceclipper which requires a GUI. Is there any way to either automatically generate centerlines without open profiles or automatically clip ends to create open profiles?<br>
Thanks!</p>
</blockquote>
</aside>
<p>Yes, this is possible without manual GUI interaction, although the workflow in VMTK can be a bit unintuitive at first.</p>
<p>vmtkcenterlines fundamentally expects open surfaces because it computes paths between inlet/outlet boundaries. If your meshes are closed, you’ll usually need a preprocessing step to create openings automatically.</p>
<p>You don’t necessarily need vmtksurfaceclipper interactively though. A common server-side approach is:</p>
<p>detect vessel endpoints automatically,<br>
clip programmatically using VTK filters,<br>
then pass the resulting open surface into vmtkcenterlines.</p>
<p>A lot of people use combinations of:</p>
<p>vtkClipPolyData<br>
vtkCutter<br>
vmtksurfacecapper<br>
or custom scripts that identify terminal branches via curvature/radius analysis.</p>
<p>Another option is using pointlist or idlist seed selectors instead of openprofiles if you already know approximate inlet/outlet coordinates. That can sometimes avoid the need for interactive clipping entirely.</p>
<p>In practice, fully automated pipelines usually rely on custom Python/VTK preprocessing before invoking the VMTK scripts themselves.</p>

---

## Post #5 by @chir.set (2026-05-25 13:40 UTC)

<aside class="quote no-group" data-username="Thretent" data-post="4" data-topic="30318">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e480ec/48.png" class="avatar"> Thretent:</div>
<blockquote>
<p>Yes, this is possible without manual GUI interaction</p>
</blockquote>
</aside>
<p>Please post such an automation workflow here, with examples and code. Over the years, I could not achieve this, so I’m eager to learn from yours.</p>

---
