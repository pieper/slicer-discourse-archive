# Reslice perpendicular to center line?

**Topic ID**: 39622
**Date**: 2024-10-09
**URL**: https://discourse.slicer.org/t/reslice-perpendicular-to-center-line/39622

---

## Post #1 by @syafirasea (2024-10-09 23:23 UTC)

<p>How can I reslice my planes to always be perpendicular to the center line that I have defined? I have a vessel that bends and curves, and I want to convert all of my images of each cross-sectional slice to be orthogonal to that line (so the plane would move laterally but also rotate where needed so that that the image in that slice is perpendicular to the center line at that point).</p>
<p>I tried using the volume reslice driver in the IGT extension and set the driver as my center line and the mode to transverse, does this do what I described above? And if so, how would I export that stack of images where the planes have now been redefined?</p>

---

## Post #2 by @lassoan (2024-10-10 04:36 UTC)

<aside class="quote no-group" data-username="syafirasea" data-post="1" data-topic="39622">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/syafirasea/48/78187_2.png" class="avatar"> syafirasea:</div>
<blockquote>
<p>How can I reslice my planes to always be perpendicular to the center line that I have defined? I have a vessel that bends and curves, and I want to convert all of my images of each cross-sectional slice to be orthogonal to that line</p>
</blockquote>
</aside>
<p>This operation is called curved planar reformatting and it is implemented in the <a href="https://github.com/PerkLab/SlicerSandbox?tab=readme-ov-file#curved-planar-reformat">“Curved planar reformat” module</a> in Sandbox extension.</p>
<p>You can also find several vessel centerline exploration and analysis tools in <a href="https://github.com/vmtk/SlicerExtension-VMTK?tab=readme-ov-file#the-vmtk-extension-for-3d-slicer">VMTK extension</a>.</p>

---
