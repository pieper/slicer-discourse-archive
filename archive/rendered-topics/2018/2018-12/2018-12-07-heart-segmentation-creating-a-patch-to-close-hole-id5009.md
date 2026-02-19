---
topic_id: 5009
title: "Heart Segmentation Creating A Patch To Close Hole"
date: 2018-12-07
url: https://discourse.slicer.org/t/5009
---

# Heart segmentation: Creating a Patch to close hole

**Topic ID**: 5009
**Date**: 2018-12-07
**URL**: https://discourse.slicer.org/t/heart-segmentation-creating-a-patch-to-close-hole/5009

---

## Post #1 by @sarvpriya1985 (2018-12-07 16:28 UTC)

<p>Operating system: windows 10<br>
Slicer version:4.11<br>
Expected behavior:<br>
Actual behaviour:<br>
Hi all,<br>
Is there a way to design a patch to close a hole inside heart. I am attaching few screenshots of what I mean. These are taken from 3D matic software.<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/1/71afb326257311903db6fdd2415cadfc1bdfc900.jpeg" alt="Capture2" data-base62-sha1="gdIo8gFDggZpUQ6ilFMIhBmrRNC" width="600" height="491"> <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56e1fc15a6a0ab7e88c47de915a041e6522f8f7a.jpeg" alt="Capture3" data-base62-sha1="coBepyZeaSrbWL4bESRmPRubVkm" width="425" height="407"> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3d4d905dc11ee90f64aff56da12407d96c1d24a.jpeg" data-download-href="/uploads/short-url/rWp87ia2ktrMImrHnQnWMdkr55U.jpeg?dl=1" title="Capture4" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c3d4d905dc11ee90f64aff56da12407d96c1d24a.jpeg" alt="Capture4" data-base62-sha1="rWp87ia2ktrMImrHnQnWMdkr55U" width="526" height="500" data-dominant-color="81A5BF"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture4</span><span class="informations">555×527 48.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks,<br>
Sarv</p>

---

## Post #2 by @lassoan (2018-12-07 18:19 UTC)

<p>You can use the Paint, Scissors, or Surface cut effects for this. Surface cut is provided by SegmentEditorExtraEffects extension. Scissors need two steps: first fill the hole (it will not just fill the whole but will create an entire extruded beam) then rotate the view to see the remove the excess region from both sides of the whole.</p>
<p>You can also create a ASD closure device model in a 3D drawing software, import the STL model, and position it with a transform to see how it would fit.</p>

---

## Post #3 by @sarvpriya1985 (2018-12-07 18:36 UTC)

<p>Thanks.</p>
<p>Will try so and see if I can do it.</p>
<p>Sarv</p>

---
