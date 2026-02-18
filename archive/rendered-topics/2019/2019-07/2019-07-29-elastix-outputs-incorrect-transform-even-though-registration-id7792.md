# Elastix outputs incorrect transform even though registration is successful

**Topic ID**: 7792
**Date**: 2019-07-29
**URL**: https://discourse.slicer.org/t/elastix-outputs-incorrect-transform-even-though-registration-is-successful/7792

---

## Post #1 by @Prashant_Pandey (2019-07-29 01:28 UTC)

<p>I’m on the stable Windows release: 4.10.2</p>
<p>I’m using the Slicer Elastix module to perform rigid registration. I know the registration is successful because the output volume computed by elastix/transformix is correctly aligned with the reference volume.</p>
<p>However I’m getting a weird bug where the transform output by elastix is incorrect: the image not aligned and I’m also getting lots of scaling even though it’s a rigid transform. Moreover if I invert the transformation in the Transforms module, there are no visible changes in Slicer.</p>
<p>I have been using the same parameter file and images since Oct 2018, when everything was working fine. The only thing that has changed since then is the Slicer version and maybe the Slicer Elastix extension?</p>

---

## Post #2 by @Prashant_Pandey (2019-07-29 01:37 UTC)

<p>Actually I think the problem is in the volume rendering module. In slice view the output transformation aligns the images as expected, but when rendered through the volume rendering module the images don’t line up at all.</p>

---

## Post #3 by @lassoan (2019-07-29 03:18 UTC)

<p>Volume renderer does not support dynamic application of non-linear transforms. You need to harden the transform on the volume to make it appear correctly in volume rendering. I’ve added an <a href="https://issues.slicer.org/view.php?id=4701" rel="nofollow noopener">issue to the bugtracker</a> to communicate this limitation to users better.</p>

---

## Post #4 by @Prashant_Pandey (2019-07-29 18:10 UTC)

<p>I’m surprised I haven’t come across this issue before, I’ve been using slicer elastix transforms in Slicer for more than two years and I’m sure I must have used volume rendering at some point to visualize results</p>

---
