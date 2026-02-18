# Automatically create labelmaps for all values of the custom LUT

**Topic ID**: 2534
**Date**: 2018-04-07
**URL**: https://discourse.slicer.org/t/automatically-create-labelmaps-for-all-values-of-the-custom-lut/2534

---

## Post #1 by @NaglisR (2018-04-07 17:09 UTC)

<p>Hi,</p>
<p>I have a volume that contains only values that are listed in my custom LUT (~70 different values representing anatomical structures):<br>
Example:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/1/e1c71782041056bfa80df6a3a66d20b7bfea86d1.png" data-download-href="/uploads/short-url/wdjYX862kx0RLZVBCtWf3i6azOp.png?dl=1" title="image%20(2)" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1c71782041056bfa80df6a3a66d20b7bfea86d1_2_690x373.png" alt="image%20(2)" data-base62-sha1="wdjYX862kx0RLZVBCtWf3i6azOp" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1c71782041056bfa80df6a3a66d20b7bfea86d1_2_690x373.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1c71782041056bfa80df6a3a66d20b7bfea86d1_2_1035x559.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/1/e1c71782041056bfa80df6a3a66d20b7bfea86d1_2_1380x746.png 2x" data-dominant-color="636262"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image%20(2)</span><span class="informations">1914×1035 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I want to automatically create a labelmap, that would assign the values of the volume to the corresponding values of the LUT. Therefore I would be able to visualize the structures with their assigned colors, modify them or for example create a 3D model of all the structures. If I was to do this by hand I would have to manually apply thresholds and create a label map for each structure individually and of course I don’t want to do that. Is it possible?<br>
Thanks in advance!</p>

---

## Post #2 by @lassoan (2018-04-07 17:33 UTC)

<p>In Volumes module, convert the volume to labelmap and select your custom LUT. If you import this labelmap to a segmentation node (using Segmentations module) then colors and segment names should be automatically set based on your LUT.</p>

---

## Post #3 by @pieper (2018-04-07 17:39 UTC)

<p>You can create a custom color table as describe here: <a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/Colors">https://www.slicer.org/wiki/Documentation/4.8/Modules/Colors</a></p>

---
