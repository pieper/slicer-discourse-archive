# I want to modify the nrrd file with the segmented Labelmaps

**Topic ID**: 8079
**Date**: 2019-08-19
**URL**: https://discourse.slicer.org/t/i-want-to-modify-the-nrrd-file-with-the-segmented-labelmaps/8079

---

## Post #1 by @kscript (2019-08-19 01:50 UTC)

<p>I want to save the segmented Labelmpas as nrrd and open this file again to add, delete or smooth the Labelmap.</p>
<p>I tried opening the saved nrrd file but couldn’t find the function I wanted.</p>
<p>Doesn’t the 3D Slicer provide that feature?</p>

---

## Post #2 by @lassoan (2019-08-19 02:30 UTC)

<p>By default, Slicer saves segmentation as a 4D nrrd file that you can reload and continue to edit. Is this not what you would need?</p>
<p>If you need a 3D (merged) labelmap then you need to export the segmentation to a labelmap before saving it. When you load the merged labelmap, make sure to select “Labelmap” option in “Add data” and import it into segmentation for editing.</p>

---

## Post #3 by @kscript (2019-08-19 02:48 UTC)

<p>4D labelmaps are not available because I don’t know how to open them using vtk. But I decided to save the seg.nrrd file, reload it, modify it, and save it as an nrrd file using the method you mentioned.</p>

---

## Post #4 by @aldoSanchez (2020-12-16 17:39 UTC)

<p>how can I do this by code, I don’t find some code for labelmap</p>

---
