---
topic_id: 8696
title: "Leaflet Mold Generator"
date: 2019-10-07
url: https://discourse.slicer.org/t/8696
---

# Leaflet mold generator

**Topic ID**: 8696
**Date**: 2019-10-07
**URL**: https://discourse.slicer.org/t/leaflet-mold-generator/8696

---

## Post #1 by @Rodrigo_Visconti (2019-10-07 17:00 UTC)

<p>I read a text that shows valve building and uses a valve mold generator module. But i can’t find that module. I’m trying to start a research in my institution in brazil with 3d printed valves filled with silicone. Where i can find this module? Can you help anyway?</p>

---

## Post #2 by @lassoan (2019-10-07 17:44 UTC)

<p>Some parts of the workflow (importing 4D US image, define annulus contour, segment leaflets, generate 3D-printable mold) are not yet publicly released. Do you already have a solution for segmenting the valve leaflets from images or you are building the complete workflow from scratch? Do you plan to do other cardiac simulation or analysis?</p>

---

## Post #3 by @Rodrigo_Visconti (2019-10-07 18:12 UTC)

<p>I 'm already segmenting valves using traditional tools and other cardiac structures too. My main project is to plan mitral valve surgery but i have other projects that i plan to use molds. My workflow is being built from scratch…</p>

---

## Post #4 by @Rodrigo_Visconti (2019-10-07 18:13 UTC)

<p>I plan to use other cardiac structures… any solution or advice?</p>

---

## Post #5 by @lassoan (2019-10-07 19:18 UTC)

<aside class="quote no-group" data-username="Rodrigo_Visconti" data-post="3" data-topic="8696">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rodrigo_visconti/48/3436_2.png" class="avatar"> Rodrigo_Visconti:</div>
<blockquote>
<p>I 'm already segmenting valves using traditional tools</p>
</blockquote>
</aside>
<p>How do you segment the leaflets? What software, what segmentation tools?</p>
<p>What is the result of your segmentation: 3D segmentation (closed surface or binary labelmap representation) or the leaflet surface (open surface)?</p>

---

## Post #6 by @Rodrigo_Visconti (2019-10-07 20:48 UTC)

<p>I’m doing all manually… using segment editor and separating leaflets using different color maps. It’s not so easy but works. Actually I’m printing in PLA and flexible filaments but I think silicone mimics better the tissue.</p>

---

## Post #7 by @Rodrigo_Visconti (2019-10-07 21:45 UTC)

<p>If you want i can send one segmentation I’ve done so you can give me some advice.</p>

---

## Post #8 by @lassoan (2019-10-07 23:43 UTC)

<p>Currently, the leaflet mold generator module requires a leaflet surface (proximal surface of the segmented leaflet) as input, which is generated from the segmentation node using a tool that is not yet publicly released. We hope that we can publish it in SlicerHeart extension within a couple of months. While the module is convenient because it can create a mold fully automatically, including add labels, breathing holes, etc., with a bit of extra effort, you can do this operations manually, too - using Segment editor.</p>
<p>For now, you can create a mold manually by creating a “box” segment and subtracting all the leaflet segments. Then cut the mold into two segments using Scissors or other effects. You can make breathing holes in the top segment using scissors effect.</p>

---

## Post #9 by @Rodrigo_Visconti (2019-10-08 00:02 UTC)

<p>Thanks for the tips. I look forward to seeing the module active for the general public. Until then I will continue to work manually. In fact this helps me to get used to the software. I hope i can get the results i expect soon…</p>

---

## Post #10 by @Rodrigo_Visconti (2019-11-09 18:27 UTC)

<p>I’m having troubles when creating box in some models when the volume is too small. How can i enhance the extent of the volume?</p>

---

## Post #11 by @lassoan (2019-11-25 16:24 UTC)

<p>You can change extent and resolution of a volume using Crop volume module.</p>

---

## Post #12 by @Rodrigo_Visconti (2019-11-30 20:36 UTC)

<p>Thanks. Please tell us when the leaflet mold generator module is ready to public.</p>

---

## Post #13 by @Rodrigo_Visconti (2020-04-23 02:28 UTC)

<p>Any evolution in the release of the module?</p>

---

## Post #14 by @aptirumalai (2020-06-03 19:39 UTC)

<p>Are 3D TEE data sets publicly available that can be used to understand the SlicerHeart module?</p>

---

## Post #15 by @Rodrigo_Visconti (2020-06-04 00:15 UTC)

<p>Sure. How can i send to you?</p>

---

## Post #16 by @lassoan (2020-06-04 01:01 UTC)

<p>You can upload it to any cloud hosting service (dropbox, onedrive, google drive, …) and post the link here. Once you share it, I can also add it as a sample data set to SlicerHeart extension so that it can be downloaded by a single click from Sample Data module.</p>

---

## Post #17 by @aptirumalai (2020-06-06 09:10 UTC)

<p>Could you upload some 3D TEE datasets to a cloud hosting service (dropbox, onedrive, google drive, …) and post the link here - as Andras suggested? Thanks!</p>

---

## Post #18 by @Rodrigo_Visconti (2020-06-26 12:47 UTC)

<p>Thanks. It would help a lot. Any news about the launch of the leaflet mold generation module?</p>

---

## Post #19 by @lassoan (2020-06-26 15:35 UTC)

<p>We still have not published the leaflet analysis modules that the leaflet generator module depends on. We would need to first finish the corresponding journal paper and get it accepted, which could take minimum 3 months, but potentially a year or more. That’s a long time and the principal investigator of the project may decide to make the leaflet analysis modules public before the work is published, but it is really up to him.</p>

---

## Post #20 by @Rodrigo_Visconti (2020-06-29 02:49 UTC)

<p>Thanks for the reply. I didn’t know about this issue. I hope you can release the application cause it seems to be faster to generate the model.</p>

---
