# STL files - centreline estimations

**Topic ID**: 4609
**Date**: 2018-10-31
**URL**: https://discourse.slicer.org/t/stl-files-centreline-estimations/4609

---

## Post #1 by @Jarka (2018-10-31 23:30 UTC)

<p>Dear Users/Slicer team,</p>
<p>I was wondering if 3D Slicer can be used to upload .STL files for the estimation of blood vessel centrelines?</p>
<p>Thank you,</p>
<p>Jarka</p>

---

## Post #2 by @pieper (2018-11-01 00:34 UTC)

<p>Yes, if you load the model and then <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/Segmentations">import it to a segmentation then you can export it again as a labelmap</a>.  From there you can use the <a href="https://www.slicer.org/wiki/Documentation/4.10/Modules/ExtractSkeleton">ExtractSkeleton</a> module on it.</p>

---

## Post #3 by @Jarka (2018-11-01 10:55 UTC)

<p>Dear Steve,</p>
<p>Many thanks for getting back to me. When I upload the .stl file, no image appears in the software. Do you know how I could go about troubleshooting this?</p>
<p>Kind regards,</p>
<p>Jarka</p>

---

## Post #4 by @pieper (2018-11-01 11:38 UTC)

<p>Hi -</p>
<p>I’d suggest starting with the segmentation tutorials so you can see how segments are created, exported and imported.  Once you see how other stl files are used you can see what’s up with your file.  Maybe you just need to center the camera on it (see <a href="https://www.slicer.org/wiki/Documentation/4.10/SlicerApplication/MainApplicationGUI#3D_Viewer">center the view</a>.  Or you can share your file and other people might be able to give suggestions.</p>

---
