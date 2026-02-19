---
topic_id: 43450
title: "Endocast From Stl"
date: 2025-06-22
url: https://discourse.slicer.org/t/43450
---

# Endocast from STL

**Topic ID**: 43450
**Date**: 2025-06-22
**URL**: https://discourse.slicer.org/t/endocast-from-stl/43450

---

## Post #1 by @Samino (2025-06-22 11:58 UTC)

<p>Hi</p>
<p>Is there a way I can generate an endocast from an STL file?<br>
The cavity I want to use for generating the endocast has external openings.</p>
<p>Any help would be highly appreciated!</p>
<p>TIA</p>

---

## Post #2 by @muratmaga (2025-06-22 16:37 UTC)

<p>You can, but results may not be ideal.</p>
<p>You can convert your stl to a segmentation, and then use the WrapSurfaceSolidfy extension to fill the cavity. But sometimes conversion has artifacts that interfere with getting a good result, hence it is better practice to create the endocast from the original volume that the model was derived from.</p>

---

## Post #3 by @ThomasVanParys (2025-06-23 09:54 UTC)

<p><em>Endomaker</em> in R Studio works directly on the 3D meshes, in .STL, .PLY, or .OBJ format: <a href="https://search.r-project.org/CRAN/refmans/Arothron/html/endomaker.html" class="inline-onebox" rel="noopener nofollow ugc">R: endomaker</a>.<br>
For a segmentation in Slicer, there is the SegmentEndocast function, but this may be picking up more than just the intracranial volume, such as aspects of the brainstem and orbit.</p>

---

## Post #4 by @Samino (2025-06-25 09:31 UTC)

<p>Thank you <a class="mention" href="/u/muratmaga">@muratmaga</a>. I’ll look into this method!</p>

---

## Post #5 by @Samino (2025-06-25 09:33 UTC)

<p>Thank you <a class="mention" href="/u/thomasvanparys">@ThomasVanParys</a>. Unfortunately I have no experience using R…<br>
<img src="https://emoji.discourse-cdn.com/twitter/slightly_frowning_face.png?v=14" title=":slightly_frowning_face:" class="emoji only-emoji" alt=":slightly_frowning_face:" loading="lazy" width="20" height="20"></p>

---

## Post #6 by @Drnoor_fatima (2025-06-25 11:33 UTC)

<p>Hi! I saw your question and actually created a kit that solves exactly this problem using 3D Slicer.<br>
It includes a sample cavity STL, a ready-made endocast, and a step-by-step workflow using the Segment Editor + Smoothing/Logical Operators.<br>
Here’s the kit if you’re still working on this: <a href="https://noorfatima60.gumroad.com/l/hcdnqn" class="inline-onebox" rel="noopener nofollow ugc">STL Endocast Generation Kit – 3D Slicer Workflow for Open Cavity Models</a><br>
Happy to help if you run into issues!</p>

---

## Post #7 by @Samino (2025-07-05 08:34 UTC)

<p>Hi <a class="mention" href="/u/drnoor_fatima">@Drnoor_fatima</a><br>
DM sent. Please could you have a look when you have a moment <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=14" title=":slight_smile:" class="emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"></p>
<p>Cheers</p>
<p>Sam</p>

---

## Post #8 by @Samino (2025-08-12 12:35 UTC)

<p>Hi <a class="mention" href="/u/drnoor_fatima">@Drnoor_fatima</a></p>
<p>I’ve purchased and downloaded the STL Endocast Generation kit from your website.<br>
However I don’t understand how to use it. The Readme file is pretty basic. If you are able to assist me I’d be very grateful.</p>
<p>Cheers</p>
<p>Sam</p>

---
