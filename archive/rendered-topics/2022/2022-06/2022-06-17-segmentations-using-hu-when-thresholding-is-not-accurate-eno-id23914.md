---
topic_id: 23914
title: "Segmentations Using Hu When Thresholding Is Not Accurate Eno"
date: 2022-06-17
url: https://discourse.slicer.org/t/23914
---

# Segmentations using HU when Thresholding is not accurate enough

**Topic ID**: 23914
**Date**: 2022-06-17
**URL**: https://discourse.slicer.org/t/segmentations-using-hu-when-thresholding-is-not-accurate-enough/23914

---

## Post #1 by @zells (2022-06-17 14:07 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a657ce5ac10a48b1a8c27a56172027184455bf6.png" data-download-href="/uploads/short-url/cTGpmECPPIbuAnKMruMinijv6FU.png?dl=1" title="Screen Shot 2022-06-16 at 10.29.29 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a657ce5ac10a48b1a8c27a56172027184455bf6_2_690x335.png" alt="Screen Shot 2022-06-16 at 10.29.29 AM" data-base62-sha1="cTGpmECPPIbuAnKMruMinijv6FU" width="690" height="335" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a657ce5ac10a48b1a8c27a56172027184455bf6_2_690x335.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5a657ce5ac10a48b1a8c27a56172027184455bf6_2_1035x502.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5a657ce5ac10a48b1a8c27a56172027184455bf6.png 2x" data-dominant-color="B7B9AC"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-06-16 at 10.29.29 AM</span><span class="informations">1200×584 67.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/7/67cde2ee826ae547aade4619cb74da5d6b6aa2ce.png" alt="Screen Shot 2022-06-16 at 10.19.03 AM" data-base62-sha1="eOihVtlDFxObXi1FF6W3kxYcrzE" width="384" height="324"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a53b428959ea367a701cbc5416f1f83657d0c97.png" alt="Screen Shot 2022-06-16 at 10.19.16 AM" data-base62-sha1="aBwFmWk2vTqLACUia842Jx6HhtB" width="260" height="248"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba51743471d11811a62edd5cde19d8d062e6faf7.png" data-download-href="/uploads/short-url/qAfk4qKZMRztLc59z2TmW7csBoj.png?dl=1" title="Screen Shot 2022-06-16 at 10.29.40 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba51743471d11811a62edd5cde19d8d062e6faf7_2_690x311.png" alt="Screen Shot 2022-06-16 at 10.29.40 AM" data-base62-sha1="qAfk4qKZMRztLc59z2TmW7csBoj" width="690" height="311" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba51743471d11811a62edd5cde19d8d062e6faf7_2_690x311.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/ba51743471d11811a62edd5cde19d8d062e6faf7_2_1035x466.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba51743471d11811a62edd5cde19d8d062e6faf7.png 2x" data-dominant-color="ACADA0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2022-06-16 at 10.29.40 AM</span><span class="informations">1300×587 68.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Hi All,</p>
<p>I have a “heat map” DICOM here that I brought into slicer and I need each different color (see images) to be a different segmentation. I cannot use the threshold effect though as each color corresponds to a single HU (ie. 1,2,3,4,5 etc. see images attached in bottom left with green circle).</p>
<p>Is the best way to do this to break it down into a numpy array and then assign a segmentation to a particular value? Is that even possible? Does anyone else have any ideas on how to solve this problem?</p>
<p>Thanks,<br>
Zach</p>

---

## Post #2 by @mau_igna_06 (2022-06-17 17:59 UTC)

<p>I would try using a module to convert it to a gray scale image.<br>
It is called RGB to scalar or something like it.<br>
Then you’d be able to threshold I think</p>

---

## Post #3 by @lassoan (2022-06-17 18:35 UTC)

<aside class="quote no-group" data-username="zells" data-post="1" data-topic="23914">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/z/6de8d8/48.png" class="avatar"> zells:</div>
<blockquote>
<p>I have a “heat map” DICOM here that I brought into slicer and I need each different color (see images) to be a different segmentation.</p>
</blockquote>
</aside>
<p>You can do this by loading this image as a segmentation as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentations.html#import-an-existing-segmentation-from-volume-file">here</a>. It is unnecessary to load each label as a separate segmentation, it is sufficient to load it as a separate segment.</p>
<p>However, you can display much nicer colormaps by loading the image as a scalar volume and then choosing an appropriate color lookup table in volumes module. See for example how dose maps are rendered in <a href="http://slicerrt.github.io/">SlicerRT extension</a>.</p>

---
