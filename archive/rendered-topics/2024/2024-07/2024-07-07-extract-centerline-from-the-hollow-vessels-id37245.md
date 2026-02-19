---
topic_id: 37245
title: "Extract Centerline From The Hollow Vessels"
date: 2024-07-07
url: https://discourse.slicer.org/t/37245
---

# Extract centerline from the hollow vessels

**Topic ID**: 37245
**Date**: 2024-07-07
**URL**: https://discourse.slicer.org/t/extract-centerline-from-the-hollow-vessels/37245

---

## Post #1 by @Djoumessi (2024-07-07 21:09 UTC)

<p>Dear all,</p>
<p>I don’t know if this subject has already been dealt with here, but I’ve read a lot of answers and haven’t found one that satisfies me.</p>
<p>In fact I want to extract the centerline of a deformed hollow tube. but the tube does not come from an image segmentation. I drew it in a CAD program and imported it into slicer as an stl file. but it seems to me that slicer’s algorithm (extractcenterline) is not able to handle this case. it seems that the geometry must be full.<br>
But when I try to do a solidify wrap to get a full geometry it fails after the Labelmap is created, because after that the geometry looks like nothing.<br>
I’d like to know if anyone has solved a similar problem. Can you recommend a python code that does the job, thanks in advance.<br>
The mesh I’m using comes mainly from Gmsh.</p>
<p>Thank you for your understanding.</p>
<p>Operating system: window<br>
Slicer version: 5.4.0</p>

---

## Post #2 by @chir.set (2024-07-31 20:59 UTC)

<aside class="quote no-group" data-username="Djoumessi" data-post="1" data-topic="37245">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/d/da6949/48.png" class="avatar"> Djoumessi:</div>
<blockquote>
<p>it seems that the geometry must be full.</p>
</blockquote>
</aside>
<p>I don’t know how your tube looks like, I just point out that centerline extraction always failed with a perfect polydata cylinder as a Model.</p>
<p>If you make a Segmentation from the Model in the ‘Data’ module, then uncheck/check the ‘Show 3D’ button in the ‘Segment editor’, the resulting segment will have a slightly rough surface. If you use it an input of the ‘Extract centerline’ module, centerline extraction is successful.</p>
<p>If you give it a try, please keep us updated. It’s doubtful the reason would be because your tube is open, I could extract centerlines with open tubes of varying radius.</p>

---

## Post #3 by @lassoan (2024-08-04 04:49 UTC)

<p>The easiest may be to save the centerline when you generate the synthetic vessel tree (before you generate the tube) but if you find that harsld then do it before you make it a thin shell.</p>
<p>The problem with specifying the vessel by a volumetric mesh of thin wall is that the labelmap representation may require very high resolution, which may require a lot of memory and long processing if your vessel of interest has a large extent. Finite element simulations may also be very slow and the  vessel wall will be hard to deform because the mesh consists of too many very small elements.</p>
<p>If you represent your vessel wall by a surface mesh and specify the shell thickness at each point then your finite element solver will be happier and you won’t have problems with processing and all processing will be very sinple and fast (including centerline extraction).</p>

---
