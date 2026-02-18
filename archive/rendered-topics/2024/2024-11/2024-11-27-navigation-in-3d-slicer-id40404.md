# Navigation in 3D slicer

**Topic ID**: 40404
**Date**: 2024-11-27
**URL**: https://discourse.slicer.org/t/navigation-in-3d-slicer/40404

---

## Post #1 by @mayaambar (2024-11-27 12:54 UTC)

<p>Hello, I’m trying for weeks to do registration to a heart model… and its never seems to be accurate enough.<br>
here is the process in which Im doing the registration:</p>
<ol>
<li>Im making a pivot and spin caliberation, usually Im not able to get a RMS smaller than 1, I apply the transformation to the needle</li>
<li>I move the needle to a specific points on the model or making a route with the sensor on a specific vein then those point I collected is a point list called NP1</li>
<li>then im making a new point list called LA(left artium) and put the point on the same locations that the needle was on the model</li>
<li>Im using registration=&gt; fiducial registration to make a transformation and choosing a linear transformation.</li>
<li>I apply the linear transformation to the needle…</li>
</ol>
<p>after this the needle is closed to where it suppost to be but there are some error- for instance - sometimes it goes out of the model when it is still suppost to be in the model<br>
our model is elastic so we think this may be an issue - the model is moving sometimes - we are thinking of printing a harden model.<br>
before we do that- is the process I describe seems ok? how can I improve it?</p>
<p>thank you for reading this and for all your help<br>
Maya</p>

---
