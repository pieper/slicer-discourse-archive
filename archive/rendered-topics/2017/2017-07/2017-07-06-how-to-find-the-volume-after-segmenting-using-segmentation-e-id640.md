---
topic_id: 640
title: "How To Find The Volume After Segmenting Using Segmentation E"
date: 2017-07-06
url: https://discourse.slicer.org/t/640
---

# How to find the volume after segmenting using "Segmentation Editor"

**Topic ID**: 640
**Date**: 2017-07-06
**URL**: https://discourse.slicer.org/t/how-to-find-the-volume-after-segmenting-using-segmentation-editor/640

---

## Post #1 by @kanga_ruu (2017-07-06 18:36 UTC)

<p>Hi,</p>
<p>I have already segmented my model, I am just looking for the volume (an actual number). Someone directed me to “Segment Statistics” module, but I cannot find that module. Is this an extension of some sort?</p>

---

## Post #2 by @lassoan (2017-07-06 18:36 UTC)

<p>It’s in the nightly version.</p>

---

## Post #3 by @kanga_ruu (2017-07-06 18:57 UTC)

<p>Thank you!! If I download the nightly version, will I have to re-segment it all over again?</p>

---

## Post #4 by @lassoan (2017-07-06 19:15 UTC)

<p>You don’t need to re-segment.</p>
<p>If you used the Segment Editor in an earlier Slicer version then you should be able to just load those segmentations.</p>
<p>If you used the Editor module then you need to import the labelmap into a segmentation node using Segmentations module.</p>

---

## Post #5 by @kanga_ruu (2017-07-06 20:06 UTC)

<p>Great! So I am now in the Segment Statistics module with my previously segmented model up. Which option do I click to get the volume?</p>

---

## Post #6 by @lassoan (2017-07-06 21:59 UTC)

<p>Volume is always included in the computed quantities.</p>

---

## Post #7 by @kanga_ruu (2017-07-06 22:58 UTC)

<p>The computed quantities are the ones that show up in the boxes on the bottom right hand of the screen, correct?</p>

---

## Post #8 by @lassoan (2017-07-06 23:08 UTC)

<p>You should see something like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/3/737bdaa64928383d518b029e54b851e01863f6cd.png" data-download-href="/uploads/short-url/gtCgrLfkWw7g8vTBGkwtgzpapcx.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/737bdaa64928383d518b029e54b851e01863f6cd_2_690x458.png" alt="image" data-base62-sha1="gtCgrLfkWw7g8vTBGkwtgzpapcx" width="690" height="458" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/737bdaa64928383d518b029e54b851e01863f6cd_2_690x458.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/737bdaa64928383d518b029e54b851e01863f6cd_2_1035x687.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/3/737bdaa64928383d518b029e54b851e01863f6cd_2_1380x916.png 2x" data-dominant-color="A6A6A8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1388×923 244 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Volume computed from the labelmap representation, in cubic cm is the “LM volume mm3” column. See more information in the module help.</p>

---

## Post #9 by @kanga_ruu (2017-07-06 23:12 UTC)

<p>Wonderful. You have been so helpful. Thank you!</p>

---
