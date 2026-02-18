# Volume size - labelmap vs closed surface

**Topic ID**: 31889
**Date**: 2023-09-25
**URL**: https://discourse.slicer.org/t/volume-size-labelmap-vs-closed-surface/31889

---

## Post #1 by @Inka_Saraswati (2023-09-25 14:50 UTC)

<p>Hi, I’m using Slicer for research in which I segment and determine volume of a bone defect from a CT image, for the purpose of determining how much graft material is needed. What is the difference between labelmap vs closed surface volume, and which one is best suited for my needs?</p>
<p>The difference is not big, less than 2% but this being a research obviously I want to be as accurate as possible, and also I want to be able to explain <em>why</em> I’m choosing one over the other. I’m new to Slicer and 3D stuff, and am a clinician by trade so all of this is new to me.</p>
<p>Thank you !</p>

---

## Post #2 by @pieper (2023-09-25 15:03 UTC)

<aside class="quote no-group" data-username="Inka_Saraswati" data-post="1" data-topic="31889">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/inka_saraswati/48/67631_2.png" class="avatar"> Inka_Saraswati:</div>
<blockquote>
<p>What is the difference between labelmap vs closed surface volume, and which one is best suited for my needs?</p>
</blockquote>
</aside>
<p>They use slightly different approaches.  Labelmap volume just counts the number of ‘on’ voxels and multiplies by the voxel size.  Closed surface volume uses the smoothed surface model and an <a href="https://vtk.org/doc/nightly/html/classvtkMassProperties.html#details">integration of the volume based on the triangulated surface</a>.  Typically the closed surface more closely matches the real contours of the anatomy.</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/modules/segmentstatistics.html</a></p>

---

## Post #3 by @Inka_Saraswati (2023-09-26 02:08 UTC)

<p>Thank you! I wasn’t sure what labelmap means, that’s helpful.</p>

---
