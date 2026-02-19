---
topic_id: 4290
title: "Seemingly Distorting Images From Input Images Mprs"
date: 2018-10-04
url: https://discourse.slicer.org/t/4290
---

# Seemingly distorting images from input images (MPRs)

**Topic ID**: 4290
**Date**: 2018-10-04
**URL**: https://discourse.slicer.org/t/seemingly-distorting-images-from-input-images-mprs/4290

---

## Post #1 by @F_Karl (2018-10-04 22:40 UTC)

<p>Hello everyone,</p>
<p>I was once helped greatly, when I was getting started with Slicer here, so I am giving it one more shot, as I have been stuck for a while now. I am having trouble with images I have been given; these are MPRs (Multi Planar Reconstruction) to get a view of the transverse plane. Slicer always seemed to distort them a little, to get its own " transverse plane" so to speak. But with one image in particular, it was so bad, that it cut a part off.</p>
<p>This is what I mean by distortion:</p>
<p>This is the original:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64010292e701b44f7dd06fefc4da31e14220d619.jpeg" data-download-href="/uploads/short-url/egFUuaR8pvPG1wAmr3rKt7A8IJz.jpeg?dl=1" title="Org" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64010292e701b44f7dd06fefc4da31e14220d619_2_555x500.jpeg" alt="Org" data-base62-sha1="egFUuaR8pvPG1wAmr3rKt7A8IJz" width="555" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/64010292e701b44f7dd06fefc4da31e14220d619_2_555x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64010292e701b44f7dd06fefc4da31e14220d619.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/64010292e701b44f7dd06fefc4da31e14220d619.jpeg 2x" data-dominant-color="474747"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Org</span><span class="informations">787×709 60.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>This is what I get from Slicer:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a921891f72425c2a2acf362af464961e356e9bc.jpeg" alt="Slicer" data-base62-sha1="aDGlcEorWQ79Odf1ePhlahBVcSg" width="375" height="315"></p>
<p>The same tumor is visible in both images on the right hand side in the middle. But where it is much above eye level in the original, it is on eye level in the Slicer version.</p>
<p>Ultimately, on top, a part of the image gets cut off in Slicer:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/2/620024b5094dffcee935243707e16d7f839ed902.jpeg" alt="Cut" data-base62-sha1="dYX69KnbsWQGYFJSUl283APIT4u" width="355" height="317"></p>
<p>This prevents me from making proper segmentation to measure volume. I assume it has something to do with the image already being an MPR, but I really don’t know. I would love all kinds of help and tips, I could try.</p>
<p>Thank you very much in advance!<br>
Florian</p>

---

## Post #2 by @lassoan (2018-10-05 03:43 UTC)

<p>What you described is the expected behavior, since Slicer by default shows image slices aligned to anatomical axes (and not to the image axes). <a href="https://discourse.slicer.org/t/read-prostate-mr-image-failed/3423/2?u=lassoan">Click rotate to volume plane button</a> to align slice views to image axes.</p>
<p>If you use a recent nightly version of Slicer (I would recommend it) then in Segment Editor module you can see a warning button next to the master volume selector in case of non-image-axis-aligned slice views during segmentation - clicking the button aligns the slice views.</p>

---

## Post #3 by @F_Karl (2018-10-05 13:42 UTC)

<p>Thank you so much! My thinking was (because of confusing naming of the files), that the MPR was made to exactly capture the tra-plane, when in fact this was not the case! Your comment made me finally realize that. Thank you!</p>

---
