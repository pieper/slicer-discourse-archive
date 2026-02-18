# Changing orientation of slices in DICOM files

**Topic ID**: 4820
**Date**: 2018-11-20
**URL**: https://discourse.slicer.org/t/changing-orientation-of-slices-in-dicom-files/4820

---

## Post #1 by @lambrosone (2018-11-20 17:43 UTC)

<p>Operating system:win 10<br>
Slicer version: 4.8<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Can slicer change the orientation of the 3 cardinal views of the dicom data, IE say to change the orientation of the views?  Say I want a view which changes the direction of the view of the orbit away from the normal?</p>
<p>thanks</p>
<p>V</p>

---

## Post #2 by @lassoan (2018-11-20 18:31 UTC)

<p>Yes you can modify DICOM files using Slicer. Import the DICOM file, apply a transform, then <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export">export to DICOM</a>.</p>
<p>Original metadata of the file is not preserved during this workflow. So, if you want to modify just a few tags while keeping all other metadata unchanged then you can use pydicom or DCMTK’s dcmodify tool instead.</p>

---

## Post #3 by @lambrosone (2018-11-20 18:45 UTC)

<p>thank you very much. The question is how do you apply the transform… I want to generate a plane and reformat the image along the new plane</p>
<p>V</p>

---

## Post #4 by @lassoan (2018-11-20 21:44 UTC)

<p>For now, you can just apply a transform and adjust the angles using sliders. Later, if everything works well then you can tune how you define the new image orientation.</p>

---

## Post #5 by @lambrosone (2018-11-20 23:13 UTC)

<p>I am grateful for your help, but I don’t know how to apply a transform or generate one or use the sliders. Is there an article you can refer me to?  What is a transformable node?  I want to alter the slices to a 3point defined plane.</p>
<p>thank you</p>
<p>V</p>

---

## Post #6 by @lassoan (2018-11-20 23:44 UTC)

<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms">Transforms module documentation</a> should help.</p>
<p>You can fit a plane to markup points as it is shown in this <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Fit_slice_plane_to_markup_fiducials">example in the script repository</a>. You can modify the script to not set the slice plane but instead set the transform</p>
<p>What would you like to align? There is a <a href="https://discourse.slicer.org/t/acpc-transform-question/3525">module and code snippets available</a> for brain AC-PC transformation.</p>

---

## Post #7 by @lambrosone (2018-11-21 00:20 UTC)

<p>Thanks, I’ll try that. I am just trying to align orbits to a plane.</p>
<p>V</p>

---
