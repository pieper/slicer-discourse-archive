---
topic_id: 7243
title: "Best Tools For Segmenting Cartilage In The Knee"
date: 2019-06-19
url: https://discourse.slicer.org/t/7243
---

# Best Tools for Segmenting Cartilage in the Knee

**Topic ID**: 7243
**Date**: 2019-06-19
**URL**: https://discourse.slicer.org/t/best-tools-for-segmenting-cartilage-in-the-knee/7243

---

## Post #1 by @paule18 (2019-06-19 14:56 UTC)

<p>Greetings,</p>
<p>I am working on a project which requires segmenting articular cartilage in the knee joint (specifically the femoral and tibial cartilage) from an MRI. It is a challenge to segment soft tissue like cartilage because a) thresholding does not distinguish it from other surrounding tissues and b) the tissue is so small and thin that it is easy to make errors in manual or even semi-autonomous segmentation.</p>
<p>Does anyone have suggestions for the best tools 3D Slicer has for going about this task? The major goals are accuracy and reproducibility. Thanks!</p>

---

## Post #2 by @paule18 (2019-06-19 21:08 UTC)

<p>Here is a screenshot of the MRI I am using for reference. One slice of the cartilage I am attempting to segment is visible in each view.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/6/7637500b51f31de1bf02a49075bfe638eb0550ea.jpeg" data-download-href="/uploads/short-url/gRMQB7Nb9HeRAs3QoFZy38noTQ6.jpeg?dl=1" title="PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7637500b51f31de1bf02a49075bfe638eb0550ea_2_690x371.jpeg" alt="PNG" data-base62-sha1="gRMQB7Nb9HeRAs3QoFZy38noTQ6" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7637500b51f31de1bf02a49075bfe638eb0550ea_2_690x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7637500b51f31de1bf02a49075bfe638eb0550ea_2_1035x556.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7637500b51f31de1bf02a49075bfe638eb0550ea_2_1380x742.jpeg 2x" data-dominant-color="8E8E95"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">PNG</span><span class="informations">1919×1034 377 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @pieper (2019-06-19 21:28 UTC)

<p>It’s true that the cartilage is thin and there’s not much contrast, but for what it’s worth, that’s a really nice scan compared to what was available years ago.  A lot depends on how much accuracy you need for your intended use, but it looks to me that if you supersample the segmentation (reduce the spacing by maybe half) and then use threshold paint and maybe the grow from seeds you have a chance.  Separating the tibia and femur cartilage will definitely be a challenge in a few spots.</p>

---

## Post #4 by @lassoan (2019-06-19 22:33 UTC)

<p>Make sure you use latest stable version of Slicer (currently 4.10.2), as we have made many very significant improvements and important fixes since 4.8.1.</p>

---

## Post #5 by @paule18 (2019-06-20 00:40 UTC)

<p>Thank you for the information! Are you aware of any new tools in the latest stable version which would help with this particular challenge? Or will the update simply offer an improvement of the same tools?</p>

---

## Post #6 by @lassoan (2019-06-20 00:48 UTC)

<p>There are both new features that you may find useful, such as masking in grow from seeds effect and ability to supersample segmentation by a few clicks; and many fixes to problems that you may run into if you use 4.8.1 version.</p>

---

## Post #7 by @three_wise_surgeons (2019-06-24 12:47 UTC)

<p>Hi Andreas, I’m exploring grow from seeds after applying threshoding and applying it for masking, and the result I get is a segmentation with two intensities in each segment. Then, when showing the 3D view, it only shows the initial slices painted… what am I doing wrong?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/9/39c1325ded2c36045eecdf8ca96ecb41c06b59c2.png" alt="17" data-base62-sha1="8eV8ydBf9D0n3qRGHyJaYcqZ2v0" width="319" height="284"></p>

---

## Post #8 by @lassoan (2019-06-24 14:48 UTC)

<p>“Show 3D” button near the top of Segment Editor widget shows current segment content, which are the seed regions. Click “Show 3D” button in Display row in “Grow from seeds” effect settings to preview segmentation results in 3D.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fba8e155ab63ee893a05b0f132b041c1d8a07f59.png" data-download-href="/uploads/short-url/zUhFuG6cVVIeQ97imyg35OemlOV.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/b/fba8e155ab63ee893a05b0f132b041c1d8a07f59.png" alt="image" data-base62-sha1="zUhFuG6cVVIeQ97imyg35OemlOV" width="690" height="302" data-dominant-color="F0F1F0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1071×470 25 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This feature is available in latest stable release (currently Slicer-4.10.2) or preview releases.</p>

---

## Post #9 by @three_wise_surgeons (2019-07-17 20:50 UTC)

<p>Hi<br>
Can you explain me what supersample is and where can i find a tutorial?<br>
Is it useful when the source ie. ct scan had not overlap?</p>
<p>Thanks</p>
<p>F F</p>

---

## Post #10 by @lassoan (2019-07-26 02:56 UTC)

<p>By supersampling we mean that sample the input volume at higher resolution than its original resolution, which allows representing thinner structures, finer details. The simplest is to crop and resample the input volume before segmentation using Crop volume module.</p>

---

## Post #11 by @lassoan (2020-12-27 19:58 UTC)

<p>2 posts were merged into an existing topic: <a href="/t/where-can-i-find-dicom-files/15243/2">where can i find DICOM files</a></p>

---
