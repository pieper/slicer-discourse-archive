---
topic_id: 16035
title: "Nifti Problem With Reformatted Segmentations"
date: 2021-02-17
url: https://discourse.slicer.org/t/16035
---

# NIFTI Problem with Reformatted Segmentations

**Topic ID**: 16035
**Date**: 2021-02-17
**URL**: https://discourse.slicer.org/t/nifti-problem-with-reformatted-segmentations/16035

---

## Post #1 by @e25 (2021-02-17 17:11 UTC)

<p>I am reformatting segmentations, and I am able to save them without issue as an NRRD fiel. However, when I attempt to save them as a NIFTI file (the utilized form for our research group) and reload the file, they are a few slices off. This is not the situation when reloading the same file saved in an NRRD format . Does anyone have any suggestions on why there may be this issue with the NIFTI file format and how to address it?</p>

---

## Post #2 by @lassoan (2021-02-17 17:16 UTC)

<p>How did you reformat the segmentation? Can you share an example images in nrrd and nifti format?</p>
<p>Nifti has many issues. One of them is that image axes must be always converted to be orthogonal, which cause slight changes in the image geometry if your image axes were not exactly orthogonal. Unless you work with brain images, I would suggest not to use nifti, but use nrrd instead.</p>

---

## Post #3 by @e25 (2021-02-17 21:40 UTC)

<p>Thank you for the reply. This is what the same segmentation looks like when saved and reuploaded as the Nfiti file vs the NRRD file in the same position. With the Nifti file, it appears off by a few slides, and there seem to be gaps. How do you convert it to be orthogonal?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/f/7f9e321009bc205d93f2aa75b9058defaabc9e74.jpeg" data-download-href="/uploads/short-url/icXzpyFr5JkuuHfHr69aeprgFSI.jpeg?dl=1" title="Screen Shot 2021-02-17 at 4.38.22 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f9e321009bc205d93f2aa75b9058defaabc9e74_2_494x500.jpeg" alt="Screen Shot 2021-02-17 at 4.38.22 PM" data-base62-sha1="icXzpyFr5JkuuHfHr69aeprgFSI" width="494" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f9e321009bc205d93f2aa75b9058defaabc9e74_2_494x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f9e321009bc205d93f2aa75b9058defaabc9e74_2_741x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7f9e321009bc205d93f2aa75b9058defaabc9e74_2_988x1000.jpeg 2x" data-dominant-color="4B4D48"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-02-17 at 4.38.22 PM</span><span class="informations">1166×1180 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/8/6885c2fc7ab17779a3b54da78448b64f36694028.jpeg" data-download-href="/uploads/short-url/eUEeSs7Ao7Axf7czxtI1JEubU48.jpeg?dl=1" title="Screen Shot 2021-02-17 at 4.38.48 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6885c2fc7ab17779a3b54da78448b64f36694028_2_451x500.jpeg" alt="Screen Shot 2021-02-17 at 4.38.48 PM" data-base62-sha1="eUEeSs7Ao7Axf7czxtI1JEubU48" width="451" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6885c2fc7ab17779a3b54da78448b64f36694028_2_451x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6885c2fc7ab17779a3b54da78448b64f36694028_2_676x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6885c2fc7ab17779a3b54da78448b64f36694028_2_902x1000.jpeg 2x" data-dominant-color="454544"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-02-17 at 4.38.48 PM</span><span class="informations">1150×1274 127 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2021-02-17 23:38 UTC)

<p>How did you reformat the segmentation?</p>
<p>If you did it by applying a matrix that has non-orthogonal axes then make sure the top-left 3x3 submatrix of the transformation matrix is orthogonal.</p>

---

## Post #5 by @e25 (2021-02-18 22:54 UTC)

<p>Slicer was used to reformat the segmentation and output the segmentations as NIFTIs. Can you clarify what you mean by non-orthogonal axes?</p>

---

## Post #6 by @lassoan (2021-02-18 23:56 UTC)

<p>Where did you get the reference image from? Head CTs are often acquired with tilted gantry, which cannot be stored in a nifti image.</p>
<p>Can you share the segmentation in .seg.nrrd format (upload somewhere and post the link here)? If you can also share the complete scene (saved as .mrb) then it is even better.</p>
<aside class="quote no-group" data-username="e25" data-post="5" data-topic="16035">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/e/f0a364/48.png" class="avatar"> e25:</div>
<blockquote>
<p>Can you clarify what you mean by non-orthogonal axes?</p>
</blockquote>
</aside>
<p>Column vectors of the orientation matrix are orthogonal to each other (their dot product is zero).</p>

---
