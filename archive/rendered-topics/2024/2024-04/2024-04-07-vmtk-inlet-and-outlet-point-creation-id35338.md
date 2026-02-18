# VMTK Inlet and Outlet Point Creation

**Topic ID**: 35338
**Date**: 2024-04-07
**URL**: https://discourse.slicer.org/t/vmtk-inlet-and-outlet-point-creation/35338

---

## Post #1 by @THartman (2024-04-07 20:45 UTC)

<p>I’m currently building an extension that uses VMTK to extract the centerlines of vessel trees in the lungs, and am looking to speed it up by adding some preprocessing to determine the inlet and outlet points of the blood vessels, as the auto-detect endpoints ends up taking quite a while to determine everything.  I was hoping that this process would speed that up a bit, but I cannot find any information on how to programmatically set the inlet vs outlet points within the MarkupNode.  Any information anyone has on this would be greatly appreciated!</p>

---

## Post #2 by @THartman (2024-04-08 16:30 UTC)

<p>I’m not sure if anyone else needs this information, but I found this comment on line 540 in the Github repo <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py" rel="noopener nofollow ugc">here</a>:</p>
<blockquote>
<p>“Return start point index from endpoint markups node. Endpoint is the first unselected control point. If none of them is unselected then the first control point.”</p>
</blockquote>
<p>Because of this, I believe that if I just add my start point and end point before running auto-detect (or maybe just before extracting the centerline?), then I will end up with a more accurate result.</p>

---

## Post #3 by @lassoan (2024-04-08 21:56 UTC)

<aside class="quote no-group" data-username="THartman" data-post="1" data-topic="35338">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/t/e47c2d/48.png" class="avatar"> THartman:</div>
<blockquote>
<p>’m currently building an extension that uses VMTK to extract the centerlines of vessel trees in the lungs</p>
</blockquote>
</aside>
<p>Quite a lot of people have been working on this topic recently, so I would recommend to search around a bit on the forum to learn what is feasible.</p>
<p>If segmentation is reasonable (you have removed all the irrelecant tiny vessel branches) then endpoint detection should be completed within a few seconds.</p>
<p>If you want to segment just specific branches then placing the endpoints manually can be useful. Inlet/outlet is indicated by the “selected” state of the control point.</p>

---

## Post #4 by @THartman (2024-04-09 00:13 UTC)

<p>I’m working with the vasculature in the lungs, so batch processing the 135 vessel trees right now is taking 3 hours or so, and the control point issue is the only place I can think to shave off some time.  How do I mark a control point as selected? Sorry, I’m pretty new to Slicer and am still figuring these details out.</p>

---

## Post #5 by @lassoan (2024-04-09 01:04 UTC)

<p>Tou can call methods of the markup node to set a control point selected/unselected.</p>
<p>What do you use the vessel tree for?</p>
<p>Usually you can get rid of the irrelevant small vessels as part of the segmentation procedure. Then rhe small vessels do not unnecessarily slow down any processing later.</p>

---

## Post #6 by @THartman (2024-04-10 21:07 UTC)

<p>I will have to ask the professor I’m doing this for about whether or not he wants us to drop the small vessels.  I’m just the software guy in this picture.  I know he’s working on research into the interplay between angiogenesis (I think that’s the right word) and cancerous tumors, but I’m unsure about the details of what he does and does not need from these files.</p>

---

## Post #7 by @lassoan (2024-04-10 22:09 UTC)

<p>Yes, it would be important to clarify what exactly is needed.</p>
<p>For example, if you go to smaller vessels then you may want to do network analysis (not centerline extraction).</p>

---
