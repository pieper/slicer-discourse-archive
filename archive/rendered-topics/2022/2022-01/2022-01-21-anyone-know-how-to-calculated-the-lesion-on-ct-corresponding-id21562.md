---
topic_id: 21562
title: "Anyone Know How To Calculated The Lesion On Ct Corresponding"
date: 2022-01-21
url: https://discourse.slicer.org/t/21562
---

# Anyone know how to calculated the lesion on CT corresponding on SPECT images?

**Topic ID**: 21562
**Date**: 2022-01-21
**URL**: https://discourse.slicer.org/t/anyone-know-how-to-calculated-the-lesion-on-ct-corresponding-on-spect-images/21562

---

## Post #1 by @akmal871026 (2022-01-21 16:22 UTC)

<p>Hi All, I have SPECT image with lesion 1 and lesion 2. (as attached picture)</p>
<p>I also have CT from the PET machine that also have the same lesion 1 and lesion 2. (as attached picture)</p>
<p>My problem is how to calculate the lesion on the CT image?</p>
<p>Anyone can help me?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b33f0038ee238f7bda6b7ca6d666fa62babc50f.jpeg" data-download-href="/uploads/short-url/fimmDc2FXfhhIvpr86ftJUZnOmr.jpeg?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b33f0038ee238f7bda6b7ca6d666fa62babc50f_2_690x308.jpeg" alt="2" data-base62-sha1="fimmDc2FXfhhIvpr86ftJUZnOmr" width="690" height="308" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6b33f0038ee238f7bda6b7ca6d666fa62babc50f_2_690x308.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b33f0038ee238f7bda6b7ca6d666fa62babc50f.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b33f0038ee238f7bda6b7ca6d666fa62babc50f.jpeg 2x" data-dominant-color="110D0F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">782×350 32.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2022-01-21 17:58 UTC)

<p>I’ve never worked with SPECT data so it’s not clear I can help, but could you elaborate on what you mean by “calculate the lesion on the CT image”?  It might be that you can create a segmentation with thresholding on the SPECT and then run segment statistics with the CT as the target volume.</p>

---
