---
topic_id: 3706
title: "Calculate The Geometric Volume Of The Heart In Radiation Fie"
date: 2018-08-08
url: https://discourse.slicer.org/t/3706
---

# Calculate the geometric volume of the heart in radiation field

**Topic ID**: 3706
**Date**: 2018-08-08
**URL**: https://discourse.slicer.org/t/calculate-the-geometric-volume-of-the-heart-in-radiation-field/3706

---

## Post #1 by @aseman (2018-08-08 12:19 UTC)

<p>Slicer version:4.8.1<br>
Hi 3d slicer experts<br>
I am working with some modules in slicer RT extension ; and I have radiation fields and some organs such as heart and lungs. I want to calculate the the geometric volume of heart (mm3) wich is located in the radiation field . Is there a module or another software wich calculates this geometric volume for me?<br>
thanks a lot</p>

---

## Post #2 by @lassoan (2018-08-08 18:16 UTC)

<p>You can segment the heart using Segment Editor module and compute its volume using Segment statistics module.</p>

---

## Post #3 by @jcfr (2018-08-08 21:16 UTC)

<p>This video from <a class="mention" href="/u/lassoan">@lassoan</a> should be helpful:</p>
<div class="lazyYT" data-youtube-id="BJoIexIvtGo" data-youtube-title="Whole heart segmentation from cardiac CT in 10 minutes" data-width="480" data-height="270" data-parameters="feature=oembed&amp;wmode=opaque"></div>

---

## Post #4 by @aseman (2018-08-12 19:04 UTC)

<p>Hi 3D slicer experts<br>
Thanks for your response. My images have already been contoured by an oncologist . In some slices a part of the heart lies in the radiation fields (red area in following figure) . The sum of these slices is the volume of the heart located in the radiation fields  and I just want to calculate the geometric volume of these areas(red areas in multiple  slices).<br>
1-wich module should I use?<br>
2- If there is a need to re-segment for the the red areas, is there any possibility of automatic segmentation?<br>
thanks a lot<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bca7649c749fb9fb25ceb12001b4e743b74c4243.png" alt="Picture1" data-base62-sha1="qUUoWvXc3ylspKZmtEpwDXojuHp" width="265" height="289"></p>

---

## Post #5 by @lassoan (2018-08-12 21:55 UTC)

<p><a class="mention" href="/u/cpinter">@cpinter</a> Can we import beam models into segmentation node?</p>

---

## Post #6 by @cpinter (2018-08-13 01:31 UTC)

<p>Yes, you can import beam models as any other models to segmentations in the Segmentations module, copy the beam segment into the segmentation that contains the heart. Then use Segment Editor’s Logical operator effect to get their intersection, then the Segment statistics module to calculate volume etc.</p>

---
