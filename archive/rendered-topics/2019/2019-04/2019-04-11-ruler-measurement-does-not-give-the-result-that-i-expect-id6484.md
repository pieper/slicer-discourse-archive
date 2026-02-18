# Ruler measurement does not give the result that I expect

**Topic ID**: 6484
**Date**: 2019-04-11
**URL**: https://discourse.slicer.org/t/ruler-measurement-does-not-give-the-result-that-i-expect/6484

---

## Post #1 by @arcus (2019-04-11 22:23 UTC)

<p>Hello, I have been using slicer and am comfortable with a few of the modules. When I use the measuring tool (ruler) point to point, on an area that know would be approximately 1mm in length, it shows a number of :55.5?  I have the ruler set to measure at mm increments.  What am I doing wrong?</p>

---

## Post #2 by @pieper (2019-04-12 11:40 UTC)

<p>Hi -</p>
<p>What kind of data are you measuring?  If it’s from something like a jpg or tiff file, then you need to set the pixel spacing so that the measurement tools are calibrated.  You can do this in the <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/Volumes#Panels_and_their_use" rel="nofollow noopener">Volumes module</a>.</p>

---

## Post #3 by @arcus (2019-04-12 15:42 UTC)

<p>It’s an nrrd file.  Thanks.  I’ll check the volumes module.</p>
<p>Steve</p>

---
