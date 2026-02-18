# How to creat a plane by 3 fiducials and then used in "modelclip"?

**Topic ID**: 1722
**Date**: 2017-12-26
**URL**: https://discourse.slicer.org/t/how-to-creat-a-plane-by-3-fiducials-and-then-used-in-modelclip/1722

---

## Post #1 by @timeanddoctor (2017-12-26 09:26 UTC)

<p>Operating system:<br>
Slicer version:12-24<br>
Expected behavior:<br>
Actual behavior:<br>
I am going to creat a plane by 3 fiducials，and then cut a model like the module “modelclip”?</p>

---

## Post #2 by @lassoan (2017-12-26 15:41 UTC)

<p>You can copy-paste a few lines of Python code to the console to orient a slice plane using 3 fiducials: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Fit_slice_plane_to_markup_fiducials">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Fit_slice_plane_to_markup_fiducials</a></p>
<p>Alternatively, if you don’t want to use the Python console and you need to cut a closed surface, then you can use Segment editor module:</p>
<ul>
<li>Segmentations module (Import/export section): import your model into a Segmentation node</li>
<li>Segment editor module: cut the segment using Scissors tool in either 3D or slice views</li>
<li>Segmentations module (Import/export section): export segment to model</li>
</ul>

---
