# Pad volume to match reference image

**Topic ID**: 14772
**Date**: 2020-11-25
**URL**: https://discourse.slicer.org/t/pad-volume-to-match-reference-image/14772

---

## Post #1 by @Carlp (2020-11-25 19:05 UTC)

<p>Operating system: Win10<br>
Slicer version: 4.11.20200930</p>
<p>Basically, I have a set of abdominal CTs, all of which have a full volume and one that is cropped to a VOI (volume of interest), see below screenshot of compared volumes.</p>
<p>What I want to do is to pad the VOI volume so that it corresponds exactly to the size of the full volume, adding zeros in the superior and inferior of the VOI. I have found how to to this with segmentations, but not with grey-scale volumes. … Is there such a feature in Slicer?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/572ba3f8ae38752237fea2741d9ff44be9bc9c55.jpeg" data-download-href="/uploads/short-url/cr92r3IXF2P3gAzwyGmhDLfpNxb.jpeg?dl=1" title="0" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/572ba3f8ae38752237fea2741d9ff44be9bc9c55_2_690x415.jpeg" alt="0" data-base62-sha1="cr92r3IXF2P3gAzwyGmhDLfpNxb" width="690" height="415" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/572ba3f8ae38752237fea2741d9ff44be9bc9c55_2_690x415.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/572ba3f8ae38752237fea2741d9ff44be9bc9c55_2_1035x622.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/572ba3f8ae38752237fea2741d9ff44be9bc9c55_2_1380x830.jpeg 2x" data-dominant-color="565656"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">0</span><span class="informations">1482×892 235 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-11-25 19:45 UTC)

<p>You can resample (including any padding or cropping) an image using one of the image resampling modules. For example, using “Resample Scalar/Vector/DWI Volume”. Choose the full volume as “Reference volume”. You can set background voxel value in Advanced resampling parameters / Default pixel value.</p>

---

## Post #3 by @Carlp (2020-11-25 19:48 UTC)

<p>It worked straight away. Thank you!</p>

---
