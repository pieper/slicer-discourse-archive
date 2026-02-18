# Circular ROI in MRI image

**Topic ID**: 26582
**Date**: 2022-12-05
**URL**: https://discourse.slicer.org/t/circular-roi-in-mri-image/26582

---

## Post #1 by @hanan (2022-12-05 17:35 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12f6293fcbc6828f6ff373615784d1adf1e69e40.jpeg" data-download-href="/uploads/short-url/2HJZweq0hAPatk0BAiW9oGHTgUU.jpeg?dl=1" title="Capture.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12f6293fcbc6828f6ff373615784d1adf1e69e40_2_536x500.jpeg" alt="Capture.PNG" data-base62-sha1="2HJZweq0hAPatk0BAiW9oGHTgUU" width="536" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12f6293fcbc6828f6ff373615784d1adf1e69e40_2_536x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12f6293fcbc6828f6ff373615784d1adf1e69e40_2_804x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12f6293fcbc6828f6ff373615784d1adf1e69e40_2_1072x1000.jpeg 2x" data-dominant-color="0C0C0C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture.PNG</span><span class="informations">1074×1001 41.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Hello,<br>
I do the segmentations on the MRI image but as shown in the figure I can’t get circular ROI. I use Segment Editor to segment. Is there any other method that gives circular shaped ROI?<br>
Thanks in advance</p>

---

## Post #2 by @pieper (2022-12-05 19:38 UTC)

<p>Binary labelmaps approximate the shape at a given resolution.  When you build a 3D representation it will look more spherical.  If it’s not high enough resolution you can increase the resolution of the segmentation (<a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough" class="inline-onebox">Segment editor — 3D Slicer documentation</a>).  If you really want precise spheres or circles you could try some kind of parametric technique but usually that isn’t the best approach.</p>

---

## Post #3 by @lassoan (2022-12-05 20:42 UTC)

<p>Also note that you can segment these spheres or tubes fully automatically by using</p>
<ul>
<li>Threshold effect, followed by</li>
<li>Islands effect → Split islands to segments</li>
</ul>

---

## Post #4 by @hanan (2022-12-06 16:52 UTC)

<p>Thanks for your help!</p>

---
