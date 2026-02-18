# Image construction

**Topic ID**: 2113
**Date**: 2018-02-19
**URL**: https://discourse.slicer.org/t/image-construction/2113

---

## Post #1 by @rayslicer (2018-02-19 04:37 UTC)

<p>Hello, am quite new on 3d slicer would like to know if numerical data’s can be transformed to images on this platform or something similar. Please i will highly appreciate recommendations of tutorial materials</p>

---

## Post #2 by @timeanddoctor (2018-02-19 05:10 UTC)

<aside class="quote no-group" data-username="rayslicer" data-post="1" data-topic="2113">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/r/ecae2f/48.png" class="avatar"> rayslicer:</div>
<blockquote>
<p>numerical data’s</p>
</blockquote>
</aside>
<p>What’s the numerical data’s? like OpenSCAD build a 3d model by code?</p>

---

## Post #3 by @lassoan (2018-02-19 05:16 UTC)

<p>Yes, it would be good to know what numerical data you have. Nevertheless, it should be easy to convert most data structures (arrays, meshes, contours, etc.) to images.</p>
<p>For example, you can directly convert a numpy array to an image node using slicer.util.updateVolumeFromArray (<a href="http://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.updateVolumeFromArray">http://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#slicer.util.updateVolumeFromArray</a>).</p>

---
