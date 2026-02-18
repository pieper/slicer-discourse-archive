# Importing models for segmentation to fix

**Topic ID**: 2229
**Date**: 2018-03-02
**URL**: https://discourse.slicer.org/t/importing-models-for-segmentation-to-fix/2229

---

## Post #1 by @muratmaga (2018-03-02 19:38 UTC)

<p>I have these scalp models that have big gaps on top and a knot (before).I imported as segmentations into the segment editor, and used the scissors to trim the knot. Segment editor automatically stitched the gap at the top. which is good, except that the counter didn’t match very well (after). Any suggestions on how to improve this?</p>
<p>Thanks,<br>
M<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/488729ff2596a727042dabc9f3045d4a7a5cde3e.png" alt="before" data-base62-sha1="alBXRqJhFtO9HE3nh6jkB4G3ZRI" width="312" height="313"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/0/702cb341cfdf1648eaa0d8a37e9991d5a3859b82.png" alt="after" data-base62-sha1="g0lfhscFF3blpa8wsLRd5ZDDgZA" width="326" height="295"></p>

---

## Post #2 by @lassoan (2018-03-02 19:56 UTC)

<p>You can apply <a href="https://www.vtk.org/doc/nightly/html/classvtkFillHolesFilter.html">vtkFillHolesFilter</a> on the polydata in your model node before you import it into segmentation. It would be nice if you could add it as a step to SurfaceToolbox module.</p>

---

## Post #3 by @lassoan (2018-03-05 14:25 UTC)

<p><a class="mention" href="/u/muratmaga">@muratmaga</a> Do you plan to work on adding this filter to <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/SurfaceToolbox/SurfaceToolbox.py">SurfaceToolbox module</a>? It should be trivial, you can just clone and existing processing step and modify it to use vtkFillHolesFilter.</p>

---

## Post #4 by @muratmaga (2018-03-05 22:48 UTC)

<p>Sorry Andras, I do not. I took a look and I decided I will be beyond my depth.</p>

---

## Post #5 by @lassoan (2018-03-06 03:42 UTC)

<p>I’ve <a href="https://github.com/Slicer/Slicer/commit/f4a792d66b910edc54060566573d13264f3951fc">added “Hole filling” step</a> to Surface Toolbox. It should be available in the nightly build from tomorrow or the day after.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/062c3d1783138786d6190e337e3bf80ccbc4e031.jpeg" data-download-href="/uploads/short-url/SBE1XFucseWoGAAfUb6EgwsfV7.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/062c3d1783138786d6190e337e3bf80ccbc4e031_2_690x441.jpeg" alt="image" data-base62-sha1="SBE1XFucseWoGAAfUb6EgwsfV7" width="690" height="441" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/062c3d1783138786d6190e337e3bf80ccbc4e031_2_690x441.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/062c3d1783138786d6190e337e3bf80ccbc4e031_2_1035x661.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/062c3d1783138786d6190e337e3bf80ccbc4e031_2_1380x882.jpeg 2x" data-dominant-color="B7B8C6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3000×1920 478 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
