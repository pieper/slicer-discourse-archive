---
topic_id: 9110
title: "Segmentation Resolution Problem"
date: 2019-11-12
url: https://discourse.slicer.org/t/9110
---

# Segmentation resolution... problem

**Topic ID**: 9110
**Date**: 2019-11-12
**URL**: https://discourse.slicer.org/t/segmentation-resolution-problem/9110

---

## Post #1 by @NoobForSlicer (2019-11-12 02:02 UTC)

<p>So I have a volume with horrible resolution to work with… Fine…</p>
<p>I want to segment it manually so it looks somewhat better in 3D.</p>
<p>Well, I crop the volume and whether I reduce the spacing scale or increase it, nothing changes…<br>
New cropped volume with new segmentation created for it, still paints exact same pixes and it is so ugly…it looks like minecraft.</p>
<p>How to solve this?</p>

---

## Post #2 by @lassoan (2019-11-12 02:38 UTC)

<p>Make sure you create a new segmentation (or update the segmentation geometry) after you create the higher-resolution volumes. After thresholding you need to apply smoothing. Or, you can segment on a number of slices and use Fill between slices to interpolate smoothly between them.</p>
<p>If you can post a few screenshots then we may be able to give more specific advice.</p>

---

## Post #3 by @NoobForSlicer (2019-11-12 03:59 UTC)

<p>Nothing helps…<br>
I actually didn’t create any segmentation until first cropping file</p>
<p>here is screenshot<br>
hhmm how do I add screenshot to reply…</p>

---

## Post #4 by @NoobForSlicer (2019-11-12 04:00 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/9037e62e9005006b3bd6fb86fa519a9f29fe03dc.jpeg" data-download-href="/uploads/short-url/kzOwbu5xb47Rp97JSOkVBKmFo5K.jpeg?dl=1" title="what%20i%20had%20enabled" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9037e62e9005006b3bd6fb86fa519a9f29fe03dc_2_412x500.jpeg" alt="what%20i%20had%20enabled" data-base62-sha1="kzOwbu5xb47Rp97JSOkVBKmFo5K" width="412" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9037e62e9005006b3bd6fb86fa519a9f29fe03dc_2_412x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9037e62e9005006b3bd6fb86fa519a9f29fe03dc_2_618x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/9037e62e9005006b3bd6fb86fa519a9f29fe03dc_2_824x1000.jpeg 2x" data-dominant-color="F9F9F9"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">what%20i%20had%20enabled</span><span class="informations">1269×1540 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>here it is… this is how i cropped it</p>

---

## Post #5 by @NoobForSlicer (2019-11-12 04:04 UTC)

<p>just closed slicer and opened new slicer, loaded in the new file… nothing happens, still<br>
each pixel on images&gt;&gt; corresponds pixels on segmentations</p>

---

## Post #6 by @lassoan (2019-11-12 04:14 UTC)

<p>The new volume that “Crop volume” module creates has much higher resolution than the original, so you can create segmentation with smooth edges. Make sure you click on Apply in Crop volume and when you go to Segment Editor module, choose the high-resolution volume to define the segmentation geometry (see instructions <a href="https://discourse.slicer.org/t/cannot-apply-threshold-on-roi/7269/2">here</a>).</p>

---

## Post #7 by @NoobForSlicer (2019-11-12 04:42 UTC)

<p>why do I have to crop at all, I just loaded in the normal nrrd and just enabled high resolution by splitting voxels… hmm</p>

---

## Post #8 by @lassoan (2019-11-12 04:49 UTC)

<p>Crop volume can do cropping and resampling at once because typically you need to do both (without cropping, the supersampled volume can be come too big - too many voxels). If the original volume had very low resolution and/or you have enough memory space then you can use the full image region.</p>

---

## Post #9 by @NoobForSlicer (2019-11-12 04:52 UTC)

<p>hmm I understand but croping does nothing for me… <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=9" title=":frowning:" class="emoji" alt=":frowning:"></p>

---

## Post #10 by @NoobForSlicer (2019-11-12 04:53 UTC)

<p>tried it many times… of course i clicked apply as well</p>

---

## Post #11 by @muratmaga (2019-11-12 05:06 UTC)

<p>And you are sure when you open the segment editor and start segmenting after cropping, you are using the “Output Volume” not the “3 Standard Full” as the master volume.</p>
<p>You might want to look at the log file and see if you are running out of memory. Your scale implies 125 fold increase in the volume of the data.</p>

---

## Post #12 by @NoobForSlicer (2019-11-12 16:29 UTC)

<p>YEP! I cropped the file indeed I clicked apply but it never cropped because I selected the entire volume which was already quite huge and I added 0.2 spacing… this multiplied the amount of voxels A LOT!</p>
<p>Even though I have over 60 gb of ram, it failed…</p>
<p>Cropping smaller file worked good now</p>

---
