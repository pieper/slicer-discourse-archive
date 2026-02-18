# Bug? Segmentation opacity not updated in panel

**Topic ID**: 22771
**Date**: 2022-03-31
**URL**: https://discourse.slicer.org/t/bug-segmentation-opacity-not-updated-in-panel/22771

---

## Post #1 by @DIV (2022-03-31 03:50 UTC)

<p>I opened several <code>Segmentation</code>s (by loading previously saved STL files.</p>
<p>In the <strong>Segmentations</strong> module, with one <code>Segmentation</code> active I set the <code>Overall opacity</code> from 1.00 to 0.50.  Its rendering in the 3D window was correspondingly adjusted, but the other <code>Segmentation</code>s appeared visually unchanged.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/d/cdaaf4273e95e515d7a291e12f7c3fd5e35a1f9e.png" alt="image" data-base62-sha1="tlq9bjQ8r5rK7rRdowky8Y9YCjY" width="681" height="178"></p>
<p>When I then choose a different <code>Segmentation</code> as active, its <code>Overall opacity</code> is erroneously still shown as 0.50, even though what’s actually rendered is the original default of 1.00.  This is obvious if a further adjustment is made in the <em>Display</em> panel to increase the <code>Overall opacity</code> to 0.60, resulting in an obvious decrease in opacity in the 3D view (<em>i.e.</em> from 1.00 down to 0.60).</p>
<p>Version 4.13.0-2022-01-19</p>
<p>—DIV</p>

---

## Post #2 by @cpinter (2022-03-31 09:13 UTC)

<p>Good catch. I fixed this in <a href="https://github.com/Slicer/Slicer/pull/6289" class="inline-onebox">BUG: Fix update of overall opacity slider in Segmentations module by cpinter · Pull Request #6289 · Slicer/Slicer · GitHub</a></p>
<p>Once approved and integrated it will be fixed in the next preview release.</p>

---
