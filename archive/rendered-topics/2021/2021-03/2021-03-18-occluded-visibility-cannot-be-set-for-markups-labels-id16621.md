# Occluded visibility cannot be set for Markups labels

**Topic ID**: 16621
**Date**: 2021-03-18
**URL**: https://discourse.slicer.org/t/occluded-visibility-cannot-be-set-for-markups-labels/16621

---

## Post #1 by @muratmaga (2021-03-18 18:31 UTC)

<p>Occluded visibility does not seem to impact the markups label. Adjustment works fine for the fiducials, including making it invisible when they are occluded. But their text labels are always visible.</p>
<p>This seems to crowd the scene, and reduce the visibility. Is this intentional?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/9/2922d7d084134498e5dafa72225aada6593504a6.jpeg" data-download-href="/uploads/short-url/5RUe54wlwuk4oyc2zBS18qzssjc.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2922d7d084134498e5dafa72225aada6593504a6_2_553x500.jpeg" alt="image" data-base62-sha1="5RUe54wlwuk4oyc2zBS18qzssjc" width="553" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2922d7d084134498e5dafa72225aada6593504a6_2_553x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2922d7d084134498e5dafa72225aada6593504a6_2_829x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2922d7d084134498e5dafa72225aada6593504a6_2_1106x1000.jpeg 2x" data-dominant-color="8D7489"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1327×1198 244 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2021-03-18 18:33 UTC)

<p>Yes, I think it was intentional, but perhaps it should be optional.</p>

---

## Post #3 by @muratmaga (2021-03-18 18:41 UTC)

<p>If that’s intentional, the purpose is not clear (like being able to see their label without seeing the actual point). Is there a python code to block this for the time being? It is interfering my ability pickup the points I wanted to (text themselves can be highlighted and grabbed even though the point is not visible).</p>
<p>What we also need a field to offset labels a bit, so they are not centered on the point…</p>

---

## Post #4 by @lassoan (2021-03-18 19:03 UTC)

<p>Occluded labels are faded out the same way as the glyphs. So, occluded visibility works well.</p>
<p>What you see is the labels of the regular (non-occluded) markup labels. You can turn off occluded visibility and you will see that all labels are displayed. This is a technical limitation of the filter that determines visibility of a landmark. It relies on the Z buffer to be fast but it means that it ignores semitransparent surfaces and volume rendering.</p>
<p>As a workaround, you can quickly create an opaque model with thresholding (with some margin shrinking to make sure it does not peek out under the volume rendering anywhere) and that will take care of the proper occlusion.</p>
<p>Proper solution would be for VTK to take into account volume rendering when it creates the Z buffer (then it could be utilized in hardware pickers, etc.). If that is impossible then vtkSelectVisiblePoints and point pickers could use additional inputs from volume renderers (or potentially these information could be combined at Slicer level, too). All these options would be quite complex to implement.</p>

---

## Post #5 by @muratmaga (2021-03-18 19:17 UTC)

<p>Ok, extracting a 3D model does solve the issue for me (at least for the time being).</p>

---
