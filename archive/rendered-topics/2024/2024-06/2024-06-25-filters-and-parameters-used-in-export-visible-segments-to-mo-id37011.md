---
topic_id: 37011
title: "Filters And Parameters Used In Export Visible Segments To Mo"
date: 2024-06-25
url: https://discourse.slicer.org/t/37011
---

# Filters and parameters used in "export visible segments to model"

**Topic ID**: 37011
**Date**: 2024-06-25
**URL**: https://discourse.slicer.org/t/filters-and-parameters-used-in-export-visible-segments-to-model/37011

---

## Post #1 by @ckolluru (2024-06-25 18:51 UTC)

<p>Is there a way to figure out which vtk filters, parameters and processing steps are run in Slicer, when one clicks the “export visible segments to models” button? Since it takes a binary voxel mask and converts it to a mesh, I assume vtkContourFilter is used?</p>
<p>I would like to replicate this functionality outside of Slicer, in python. I looked in the Slicer source code, but couldn’t get far. In addition, would also like to understand the methods for the opposite “Convert model to segmentation node”.</p>
<p>Any help would be appreciated! If this is documented somewhere, please let me know.</p>
<p>Thanks,<br>
Chaitanya</p>

---

## Post #2 by @ckolluru (2024-06-28 17:57 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/pieper">@pieper</a>,</p>
<p>Do you have some pointers here?</p>
<p>Thanks,<br>
Chaitanya</p>

---

## Post #3 by @lassoan (2024-06-28 21:05 UTC)

<p>This is all implemented in a standalone library (vtkSegmentationCore, a.k.a. PolySeg). It has been also compiled with webassembly and used in JavaScript (in OHIF) and will be avilable as a standalone pip-installable Python package.</p>
<p>The Python work takes time, as we want to implement it properly, by developing a solid infrastructure for it in VTK (that can be used for many other VTK-based libraries). <a class="mention" href="/u/jcfr">@jcfr</a> might be able to give more details.</p>

---
