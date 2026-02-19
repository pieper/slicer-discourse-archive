---
topic_id: 301
title: "Stl File Created From Segmentation Is Not Smooth Enough"
date: 2017-05-12
url: https://discourse.slicer.org/t/301
---

# STL file created from segmentation is not smooth enough

**Topic ID**: 301
**Date**: 2017-05-12
**URL**: https://discourse.slicer.org/t/stl-file-created-from-segmentation-is-not-smooth-enough/301

---

## Post #1 by @Sarvraj_Kohli (2017-05-12 07:52 UTC)

<p>Thanks Andras. Your suggestion helped a lot and we were able to generate a 3D stl file. However a new issue has arisen.</p>
<p>The stl file so obtained does not have a smooth surface. It is composed of blocks (like a pixelated image) and is therefore unsuitable for printing. Can you tell us how to overcome this problem.</p>
<p>Thanks<br>
Sarvraj</p>

---

## Post #2 by @lassoan (2017-05-12 11:35 UTC)

<p>You have three options, you can use all, but the first one is the most important:</p>
<ul>
<li>crop your input volume to the region of interest &amp; resample to have sufficiently high resolution using the <code>Crop volume</code> module: specify your ROI, select <code>Isotropic spacing</code>, select sufficiently low <code>spacing scale</code> value (the lower the value, the more details you can preserve during segmentation, but more memory and processing time you will need; typically 0.5 … 0.2 should work), select bspline interpolator</li>
<li>smooth the labelmap representation using <code>Smoothing</code> effect in Segment editor module</li>
<li>smooth the generated surface: in Segment editor module, click on the small arrow on the “Show 3D” button, choose <code>Set surface smoothing</code>, and increase the smoothing value. (in older Slicer versions, this setting was only available in Segmentations module: click <code>Update</code> button in the row of <code>Closed surface</code> representation in <code>Representations</code> section, click on <code>Binary labelmap -&gt; Closed surface</code> rule, increase <code>Smoothing factor</code> value)</li>
</ul>

---
