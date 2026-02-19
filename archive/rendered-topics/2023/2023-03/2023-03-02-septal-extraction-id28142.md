---
topic_id: 28142
title: "Septal Extraction"
date: 2023-03-02
url: https://discourse.slicer.org/t/28142
---

# Septal extraction

**Topic ID**: 28142
**Date**: 2023-03-02
**URL**: https://discourse.slicer.org/t/septal-extraction/28142

---

## Post #1 by @soukup.la (2023-03-02 12:28 UTC)

<p>Hello,<br>
I’d like to extract septal surface from left (LV) or right (RV) ventricle model. I am able to convert models points to numpy arrays and get its distance using numpy.linalg.norm. Then I can select part of points with minimal distance. However I don’t know how to create new model based on selected points - see picture.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/869e22cc190ad2df420d4ed9bc203284f270f047.png" data-download-href="/uploads/short-url/jcSMIeurczbYa3l2gk9S9AiAWDJ.png?dl=1" title="rv" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/869e22cc190ad2df420d4ed9bc203284f270f047_2_473x500.png" alt="rv" data-base62-sha1="jcSMIeurczbYa3l2gk9S9AiAWDJ" width="473" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/6/869e22cc190ad2df420d4ed9bc203284f270f047_2_473x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/869e22cc190ad2df420d4ed9bc203284f270f047.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/6/869e22cc190ad2df420d4ed9bc203284f270f047.png 2x" data-dominant-color="916A85"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">rv</span><span class="informations">566×598 88 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>thank you fro your help<br>
Ladislav</p>

---

## Post #2 by @lassoan (2023-03-03 05:40 UTC)

<p>You don’t need to mess with computing distances in numpy, but instead use vtkDistancePolyDataFilter. You can then use vtkThreshold to extract a piece of a mesh based on the computed distance that is stored in point scalars.</p>
<p>An alternative, potentially simpler and more robust method is to use the Segment Editor:</p>
<ol>
<li>Create a segment “septum” that contains LV RV and septal wall, by combining LV and RV into one segment using Logical operators effect (allow overlap in masking settings to be able to preserve the original LV and RB segments).</li>
<li>Fill the gap between the LV and RV in the “septum” segment by using Smoothing effect (Closing operation, with a sufficiently large kernel).</li>
<li>Subtract the original LV and RV segments from the “septum” segment using Logical operators. What remains is the septal wall.</li>
</ol>

---

## Post #3 by @soukup.la (2023-03-06 08:55 UTC)

<p>Hello,<br>
thank you very much! The segmentation method looks great. However, I am not sure if I make it correctly - smoothing takes more than 15 minutes.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fb631e4ae20743cf17f8bb7c61db310dfa43d9b.png" data-download-href="/uploads/short-url/fWflHkRbRZOTpjrlWgJiXcci0pt.png?dl=1" title="smoothing" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fb631e4ae20743cf17f8bb7c61db310dfa43d9b_2_690x211.png" alt="smoothing" data-base62-sha1="fWflHkRbRZOTpjrlWgJiXcci0pt" width="690" height="211" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fb631e4ae20743cf17f8bb7c61db310dfa43d9b_2_690x211.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fb631e4ae20743cf17f8bb7c61db310dfa43d9b_2_1035x316.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fb631e4ae20743cf17f8bb7c61db310dfa43d9b_2_1380x422.png 2x" data-dominant-color="B2B5C5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">smoothing</span><span class="informations">1509×462 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2023-03-06 11:47 UTC)

<p>If the serial wall can be up to 15mm and voxel size is about 0.5mm then indeed the smoothing may take long. You can try Margin effect instead (grow then shrink by 15mm), or use Wrap Solidify effect (provided by SurfaceWrapSolidify extension).</p>

---

## Post #5 by @soukup.la (2023-03-07 09:50 UTC)

<p>Hello,<br>
thank you very much! The Margin effect works good for my purposes.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/0/206cdb037612c8eef27b5e39f6a3e34cb5dc6715.png" alt="septum" data-base62-sha1="4CQv3AwR7FO9yQrBBEQXL3RGAzH" width="476" height="455"></p>

---

## Post #6 by @soukup.la (2023-03-07 13:07 UTC)

<p>I have problem with saturation after Margin operation in some cases. Do you have any idea why?<br>
Thank you.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c08a03403354f9dfba18857e2826be8a1ba2020a.png" data-download-href="/uploads/short-url/rthmDHWqoQoSA69r4aLATRloc4O.png?dl=1" title="saturation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c08a03403354f9dfba18857e2826be8a1ba2020a_2_580x500.png" alt="saturation" data-base62-sha1="rthmDHWqoQoSA69r4aLATRloc4O" width="580" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/0/c08a03403354f9dfba18857e2826be8a1ba2020a_2_580x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c08a03403354f9dfba18857e2826be8a1ba2020a.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/0/c08a03403354f9dfba18857e2826be8a1ba2020a.png 2x" data-dominant-color="9496A5"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">saturation</span><span class="informations">782×673 58.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2023-03-10 22:03 UTC)

<p>You can increase the extent of the segmentation by creating an ROI markup and use it in “Specify geometry” in Segment Editor.</p>

---
