---
topic_id: 28293
title: "How To Get Image Like This In Slicer"
date: 2023-03-10
url: https://discourse.slicer.org/t/28293
---

# How to get image like this in slicer

**Topic ID**: 28293
**Date**: 2023-03-10
**URL**: https://discourse.slicer.org/t/how-to-get-image-like-this-in-slicer/28293

---

## Post #1 by @mukund_shah (2023-03-10 20:19 UTC)

<p>I have a T1 volume and a segmented volume with ventricles , tumor and blood vessels ,I am trying to get a figure like this one ,this is taken from a paper.<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37966bd7458dd09897a96f5fef0d20cf8aa10521.png" alt="Screenshot 2023-03-10 120725" data-base62-sha1="7VKxhW2yzO3rBEswXf8ErKPDT5n" width="336" height="299"></p>

---

## Post #2 by @muratmaga (2023-03-10 20:40 UTC)

<p>This is a feature that hasn’t been merged into Slicer yet (<a href="https://github.com/Slicer/Slicer/pull/6809" class="inline-onebox">ENH: Add connector line for fiducial markup label texts by lassoan · Pull Request #6809 · Slicer/Slicer · GitHub</a>).</p>
<p>When functional, you can generate figures like this;<br>
          <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/a/a75d9c6e8e8a1ee933ca3bd472ff7edc885418a3.jpeg" target="_blank" rel="noopener" class="onebox">
            <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/2X/a/a75d9c6e8e8a1ee933ca3bd472ff7edc885418a3.jpeg" width="690" height="257">
          </a>
</p>
<p>Until then, I think your best option is to get screenshot and add those texts and lines in Illustrator and/or powerpoint. That will give you more flexibility in terms of colors/font choices as well…</p>

---

## Post #3 by @lassoan (2023-03-10 22:10 UTC)

<p><a class="mention" href="/u/mukund_shah">@mukund_shah</a> if you want to display the ventricle, tumor, and blood vessels then you can use the Segment Editor. The <a href="https://spujol.github.io/NeurosurgicalPlanningTutorial/WhiteMatterExplorationTutorial_SoniaPujol-RonKikinis.pdf">Neurosurgical planning tutorial</a> is a good starting point.</p>

---

## Post #4 by @mukund_shah (2023-03-11 06:07 UTC)

<p>But i already have a segmented label volume with ventricles,tumor and blood vessels along with  T1 volume do I still need segment editor?</p>

---

## Post #5 by @lassoan (2023-03-11 06:25 UTC)

<p>Not at all, then you are done. You can segment the brain surface using HDBet or SwissSkullStripper and display the structures that you already segmented. You can adjust the transparency of both the brain and the segmentations. You can draw the trajectories as curves in Markups module.</p>

---

## Post #6 by @mukund_shah (2023-03-11 06:37 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> will try this</p>

---

## Post #7 by @mukund_shah (2023-03-11 07:05 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> i am getting brain output  after skull striping ,how do I change opacity of this? i cant see any option here for changing that<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b35bc2d04185c07dca5645656a8d450224dbdc29.png" alt="Screenshot 2023-03-11 123410" data-base62-sha1="pAG3YSG1uG5Ux9MAVd1bWTKOjXz" width="447" height="231"></p>

---

## Post #8 by @lassoan (2023-03-11 07:10 UTC)

<p>You have rendered the mask. Instead, render the skull-stripped image instead. You can adjust opacity of volume rendering by decreasing the opacity values in the Scalar Opacity Mapping function.</p>

---

## Post #9 by @mukund_shah (2023-03-11 11:31 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>  thanks to you i am able to make this figure now, one last thing how can I make these blood vessels etc more smooth looking as in the first image? mine look granular<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/0/d08db243eae9b7127193ab5d8cd152aaed1ff1f1.png" alt="Screenshot 2023-03-11 170051" data-base62-sha1="tKWTBBMlpqls8pZsteidO99BF4d" width="613" height="345"></p>

---

## Post #10 by @lassoan (2023-03-11 16:16 UTC)

<p>If you load your image as a segmentation (in “Add data” popup window, choose “Segmentation” in the description column) then you get a lot more visualization options - smoothing, opacity, etc. You can also apply further smoothing, thickening, etc. in Segment Editor module.</p>
<p>For additional improvements in appearance, you can use Lights module in Sandbox extension. Especially <a href="https://discourse.slicer.org/t/new-feature-surface-rendering-with-ambient-shadows-for-improved-depth-perception/16903">“ambient shadows”</a> may make a big difference.</p>

---
