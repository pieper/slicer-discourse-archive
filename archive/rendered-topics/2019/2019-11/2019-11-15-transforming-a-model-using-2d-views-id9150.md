# Transforming a model using 2D views

**Topic ID**: 9150
**Date**: 2019-11-15
**URL**: https://discourse.slicer.org/t/transforming-a-model-using-2d-views/9150

---

## Post #1 by @heidi (2019-11-15 00:41 UTC)

<p>Is it possible to show (and manipulate) the transform white cube in the 2D views? I would like to move my part within the plane of the 2D view. My application is placing an orthopaedic implant in a ct data set.<br>
Thank you in advance for your help.</p>

---

## Post #2 by @lassoan (2019-11-15 01:20 UTC)

<p>We plan to add transform widget to slice views at some point, but since there are more direct and more accurate (semi)automatic registration methods, adding a fully manual adjustment option has not been a priority.</p>
<p>You can adjust transforms in slice views by moving markup fiducial points if you use Fiducial registration wizard module (in SlicerIGT extension).</p>
<p>You can write a short Python script that adjust transforms based on markup fiducial point positions (see examples in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a>).</p>

---
