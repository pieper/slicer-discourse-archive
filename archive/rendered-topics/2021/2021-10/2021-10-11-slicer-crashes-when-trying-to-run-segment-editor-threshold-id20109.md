---
topic_id: 20109
title: "Slicer Crashes When Trying To Run Segment Editor Threshold"
date: 2021-10-11
url: https://discourse.slicer.org/t/20109
---

# Slicer crashes when trying to run segment editor threshold

**Topic ID**: 20109
**Date**: 2021-10-11
**URL**: https://discourse.slicer.org/t/slicer-crashes-when-trying-to-run-segment-editor-threshold/20109

---

## Post #1 by @Saima (2021-10-11 23:17 UTC)

<p>Hi,<br>
Any support in this<br>
Switch to module:  “SegmentEditor”<br>
QLayout::addChildLayout: layout “” already has a parent<br>
ctkSliderWidget::setSingleStep()  0 is out of bounds. 0 10 1<br>
error: [/home/saima/Downloads/Downloads/slicer/bin/SlicerApp-real] exit abnormally - Report the problem.</p>
<p>Slicer version is 4.11.20210226<br>
volume used<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/f/af9a6723ab8921e51fc2d0603e68858344522d8e.png" alt="image" data-base62-sha1="p3smzb8lUe12IIKqIFYVWSrNt70" width="523" height="280"></p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #2 by @muratmaga (2021-10-11 23:21 UTC)

<p>After the crash, open slicer one more time, go to Help-&gt;Report a bug, and pull the second from the top log file and post it here (the topmost one will be the log from the current session).</p>

---

## Post #3 by @lassoan (2021-10-12 00:24 UTC)

<p>The problem has been probably fixed in the Slicer Preview Release. Please test and let us know if you can reproduce the problem using the very latest Slicer Preview Release.</p>

---

## Post #4 by @Saima (2021-10-13 07:55 UTC)

<p>Hi Andras,<br>
when I am loading a .vtk file I have this</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5b40e9953f41ad34fc8b3cbfeeaf67992586b609.png" alt="image" data-base62-sha1="d1gwutN4ZKoyN8BNNYTcGuQ2urn" width="518" height="288"></p>
<p>there is no polys? why it is not recognizing polys in the data vtk</p>
<p>it is showing me the model  in 3d view.</p>
<p>Regards,<br>
Saima Safdar</p>

---

## Post #5 by @lassoan (2021-10-13 12:17 UTC)

<p>A .VTK file can contain pretty much anything - image, surface mesh, volumetric mesh,… The one that you loaded contains an unstructured grid, which is typically a volumetric mesh and so it does not contain polygons, only volumetric cells, such as tetrahedra and wedges.</p>

---
