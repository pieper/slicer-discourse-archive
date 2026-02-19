---
topic_id: 14731
title: "Segmenting Using Smaller Images Then Applying Segmentation T"
date: 2020-11-22
url: https://discourse.slicer.org/t/14731
---

# Segmenting using smaller images then applying segmentation to the original

**Topic ID**: 14731
**Date**: 2020-11-22
**URL**: https://discourse.slicer.org/t/segmenting-using-smaller-images-then-applying-segmentation-to-the-original/14731

---

## Post #1 by @SteveJJ (2020-11-22 19:55 UTC)

<p>I am working on large datasets from the Visible Human Project and want to do some segmentations.  I had the idea of doing the segmentation using lower resolution images, then applying these segmentations to the higher res volume to save on processing time.  Please could you advise on how best to do this?<br>
Thanks<br>
Steve</p>

---

## Post #2 by @lassoan (2020-11-22 20:04 UTC)

<p>What do you mean by “applying” segmentations to a higher-resolution volume? What are you trying to achieve? Create a full-body anatomical atlas? Is the goal that you learn about anatomy as you are doing this, or you just want to have the segmentation result? Various parts of the visible human data set has been segmented before, so you may not need to start from scratch.</p>

---

## Post #3 by @SteveJJ (2020-11-22 20:15 UTC)

<p>I want to create my own segmentations of regions that have not been segmented already.  I have been trying to work with smaller files (that I reduced using a different program), and finding that it is much faster segmenting these.  However, I ultimately want to apply these segmentations to the full resolution dataset.</p>

---

## Post #4 by @lassoan (2020-11-22 20:36 UTC)

<p>By “applying the segmentation” do you just mean that you want to show the segmentation overlaid on an image? If yes, then it is automatic - everything is displayed in physical space, the resolution is properly taken into account.</p>

---

## Post #5 by @SteveJJ (2020-11-22 20:39 UTC)

<p>I want to load the set of smaller images (i.e. volume composed of images which are smaller versions of the originals), do a segmentation then load the set of full sized images and use the segmentation I created on this second full size volume if that makes sense?  Basically, I’m finding segmentation using the paint tool etc slow so am trying to speed things up.  I have switched off surface smoothing and am not using 3D view.</p>

---

## Post #6 by @lassoan (2020-11-22 20:52 UTC)

<aside class="quote no-group" data-username="SteveJJ" data-post="5" data-topic="14731">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/e99b99/48.png" class="avatar"> SteveJJ:</div>
<blockquote>
<p>use the segmentation I created on this second full size volume if that makes sense</p>
</blockquote>
</aside>
<p>It is still not clear what you mean by using. If by using you mean that you want to show the segmentation overlaid on an image then you don’t need to do anything, it will just work. You don’t even copy all the segments in to a single segmentation node, but you can load and overlay as many segmentations as you want over a single volume (you can store segmentation of brain, abdomen, extremities in separate nodes).</p>

---

## Post #7 by @SteveJJ (2020-11-22 20:59 UTC)

<p>I agree, this works fine using some of the sample data.  The segmentation just doesn’t seem to be transferring to the visible human image data</p>

---

## Post #8 by @lassoan (2020-11-22 21:07 UTC)

<p>It may be possible that the software that you used to crop/resample the visible human images did not preserve the physical location. You can use “Crop volume” module in Slicer to do cropping and resampling properly.</p>

---

## Post #9 by @SteveJJ (2020-11-22 21:17 UTC)

<p>Great, seems to be working well now thanks</p>

---
