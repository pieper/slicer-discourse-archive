# Changing hounsfield units after painting with a different range of masking

**Topic ID**: 11854
**Date**: 2020-06-03
**URL**: https://discourse.slicer.org/t/changing-hounsfield-units-after-painting-with-a-different-range-of-masking/11854

---

## Post #1 by @Mark_Brahier (2020-06-03 21:30 UTC)

<p>Hello. I am using Slicer for contrast-enhanced cardiac CT analysis. After a substantial amount of work painting axial views to determine pericardial fat volume under a certain range of HU, I would like to reanalyze by saved files using a different range of HU. Is there a way to change HU for all previously painted slices? Thanks!</p>

---

## Post #2 by @lassoan (2020-06-03 21:56 UTC)

<p>Would you like to modify the input volume’s voxel values? Or, would you like to adjust the painted regions (e.g, remove regions that are in a certain value range)? Maybe you could explain it better by attaching a screenshot with your annotations.</p>

---

## Post #3 by @Mark_Brahier (2020-06-03 23:25 UTC)

<p>Hi Andras, thanks for your reply. I have included a photo below that I hope will help. I used the Paint feature Masked to -30 to -190 HU and encircled the left atrium for every axial view of the cardiac CT to arrive at a periatrial fat volume. Now, I would like to change the Masking to -50 to -200 HU for every axial slice without re-doing the manual encircling of the entire left atrium. In other words, I want to “re-analyze” the pericardial fat volume for a slightly different range of masking without manually re-doing the whole thing. Is there a way to change that masking range for painting that has already been done?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/0/40e0a4abdf1e736463f49f05bacb225664d9fda8.jpeg" data-download-href="/uploads/short-url/9fVQWXi2Pfwijk4hf2JGH9cbH3W.jpeg?dl=1" title="Screen Shot 2020-06-03 at 7.21.08 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40e0a4abdf1e736463f49f05bacb225664d9fda8_2_690x390.jpeg" alt="Screen Shot 2020-06-03 at 7.21.08 PM" data-base62-sha1="9fVQWXi2Pfwijk4hf2JGH9cbH3W" width="690" height="390" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40e0a4abdf1e736463f49f05bacb225664d9fda8_2_690x390.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40e0a4abdf1e736463f49f05bacb225664d9fda8_2_1035x585.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/40e0a4abdf1e736463f49f05bacb225664d9fda8_2_1380x780.jpeg 2x" data-dominant-color="9C9B9B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-06-03 at 7.21.08 PM</span><span class="informations">2046×1158 349 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2020-06-04 01:11 UTC)

<p>If you just want to change the segmentation in the nerighborhood of the original segmentation with a different intensity range then set “Editable intensity range” to the new range, select “Margin” effect, and set up to how far the segmentation can be expanded in “Margin size”, and click Apply. You can then use “Smoothing” effect to even out the result (remove small speckles, fill small holes).</p>

---

## Post #5 by @Mark_Brahier (2020-06-04 12:01 UTC)

<p>Thank you. Just to make sure I understand what this is doing, does Margin extend all of the “edges” of every slice in the segmentation by the specified amount (i.e. 3mm)? And in doing so, it re-calculates both the original areas for each slice and the new area margins using the new range of HU that I have specified?</p>

---

## Post #6 by @lassoan (2020-06-04 15:21 UTC)

<p>Everything is done fully in 3D, nothing is limited to specific slices, but otherwise what you described is accurate.</p>

---

## Post #7 by @lassoan (2020-06-10 18:56 UTC)

<p>A post was split to a new topic: <a href="/t/why-growing-segment-by-10mm-margin-is-different-from-growing-by-5mm-margin-twice/11985">Why growing segment by 10mm margin is different from growing by 5mm margin twice</a></p>

---
