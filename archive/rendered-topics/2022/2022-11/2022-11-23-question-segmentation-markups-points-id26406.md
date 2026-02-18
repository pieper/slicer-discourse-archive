# Question: Segmentation + Markups(Points)

**Topic ID**: 26406
**Date**: 2022-11-23
**URL**: https://discourse.slicer.org/t/question-segmentation-markups-points/26406

---

## Post #1 by @lucas_sd (2022-11-23 13:00 UTC)

<p>Hi everybody,</p>
<p>Im working doing some segmentations, and I wonder if its possible to use markups point in order to guide the segmentation process (e.g., use points to indicate start and end for obtain the segmentation of a specific artery). There is a extension/module/method/idea for do that?</p>
<p>Thanks! Lucas.</p>

---

## Post #2 by @chir.set (2022-11-23 14:16 UTC)

<p>You may install <a href="https://github.com/vmtk/SlicerExtension-VMTK" rel="noopener nofollow ugc">SlicerVMTK</a> via the ‘Extensions manager’. Depending on your version of Slicer, you’ll find 2 modules that may fit your requirements :</p>
<ul>
<li>Formerly ‘Curve centerline extraction’, renamed now to 'Guided artery segmentation ’</li>
<li>Formerly ‘Fiducial centerline extraction’, renamed now to 'Quick artery segmentation ’</li>
</ul>
<p>They use markups points, targeting different kind of tasks, the second module having as assumption good quality contrasted CT scans.</p>

---
