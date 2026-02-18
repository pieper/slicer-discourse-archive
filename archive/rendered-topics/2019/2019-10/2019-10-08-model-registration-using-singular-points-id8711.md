# Model Registration Using Singular Points

**Topic ID**: 8711
**Date**: 2019-10-08
**URL**: https://discourse.slicer.org/t/model-registration-using-singular-points/8711

---

## Post #1 by @David_Asgar-Deen (2019-10-08 19:44 UTC)

<p>Operating system: Windows 10 build 17763.775<br>
Slicer version: 4.10.2</p>
<p>Expected behavior: I currently have 2 main transforms within my scene: NeedleToReference and PhantomToReference. Within the NeedleToReference transform, I have another transformation that maps the NeedleTipToNeedle. I would like to place some spherical models inside the phantom. As I can locate the center of the sphere position within the phantom using the needle tip I was thinking of placing fiducial points in 3D space using the needle tip, finding the linear transform between the marker and my phantom tracker, and placing a spherical model in the Transform Hierarchy in the Data module.</p>
<p>Actual behavior: I am currently unsure about how to calculate the transformation between the fiducial point relative to the phantom position sensor.</p>
<p>Any help on the issue would be greatly appreciated!</p>

---

## Post #2 by @lassoan (2019-10-08 20:08 UTC)

<p>The process for landmark-based object registration using a tracked stylus is described in detail in <a href="http://www.slicerigt.org/wp/user-tutorial/" rel="nofollow noopener">SlicerIGT tutorials</a> (“Pivot calibration” and “Landmark registration”).</p>

---
