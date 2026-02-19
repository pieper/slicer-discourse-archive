---
topic_id: 12378
title: "Segmentation Transform"
date: 2020-07-05
url: https://discourse.slicer.org/t/12378
---

# Segmentation Transform

**Topic ID**: 12378
**Date**: 2020-07-05
**URL**: https://discourse.slicer.org/t/segmentation-transform/12378

---

## Post #1 by @FatihSogukpinar (2020-07-05 08:24 UTC)

<p>Hi all,</p>
<p>I have a segmentation (similar to an atlas but includes only specific anatomical regions) and an MRI and I need to figure out how Slicer aligns them. When I open and plot them in Matlab, they are not aligned. Basically it seems like their origins are different. Slicer somehow apples the correct transformation and I need to figure out what it is.</p>
<p>When I check the Transforms module, I don’t see any transforms applied to the Segmentation. I don’t understand why…</p>
<p>Any suggestions ?</p>
<p>Thank you !</p>

---

## Post #2 by @manjula (2020-07-05 09:50 UTC)

<p>When you export the segmentation have you select the correct coordination system ? Both RAS and LPS is available and by default it is set to RAS.</p>

---

## Post #3 by @lassoan (2020-07-06 05:39 UTC)

<aside class="quote no-group" data-username="FatihSogukpinar" data-post="1" data-topic="12378">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/fatihsogukpinar/48/7257_2.png" class="avatar"> FatihSogukpinar:</div>
<blockquote>
<p>When I open and plot them in Matlab, they are not aligned. Basically it seems like their origins are different. Slicer somehow apples the correct transformation and I need to figure out what it is.</p>
</blockquote>
</aside>
<p>You have two options:</p>
<ul>
<li>take into account pixel&lt;-&gt;physical coordinate system mapping that is saved into the segmented image (it is available in <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/934a1eff4db11b16af7d3de31357d08515dd05cd/MatlabCommander/commandserver/nrrdread.m#L6-L7">IJK to LPS transformation matrix</a> provided by the nrrd reader)</li>
<li>export the labelmap into the same image geometry as the input image (this is the default behavior in recent Slicer-4.11 versions, but if you use an older Slicer version then you may need to select the input image as reference volume manually when you export the segmentation to labelmap)</li>
</ul>
<p>I would recommend to move on from Matlab to Python, as Python has so many more and much better tools for medical image computing, you can implement complete application workflows (from server-side processing to end-user GUI), there are no licensing hassles, etc. I’ve implemented Slicer’s MatlabBridge extension because 5-10 years ago it still made sense to use Matlab for some problems, but nowadays it is very hard to justify choosing Matlab over Python.</p>

---
