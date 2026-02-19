---
topic_id: 2757
title: "Export Ct Aaa2 From 3D Slicer"
date: 2018-05-03
url: https://discourse.slicer.org/t/2757
---

# Export CT-AAA2 from 3d Slicer

**Topic ID**: 2757
**Date**: 2018-05-03
**URL**: https://discourse.slicer.org/t/export-ct-aaa2-from-3d-slicer/2757

---

## Post #1 by @ghoulfool (2018-05-03 19:56 UTC)

<p>Operating system: Win 7<br>
Slicer version:4.8.1<br>
Expected behavior: Export an OBJ (as seen on screen)<br>
Actual behavior:No option to export (or in one case a 0 byes .OBJ)</p>
<p>Hi, first time caller and I’m having problems exporting an .OBJ from a CT scan. I have no medical background and all this is very new to me, maybe someone will be kind enough to point out where I’m going wrong.</p>
<p>Here’s my method:<br>
I got the CT scan from <a href="https://osf.io/6zamj/" rel="noopener nofollow ugc">here</a>, I had to convert it to a nii.gz file with dcm2niigui that comes with mricron.</p>
<p>Drop the nii.gz file into 3D Slicer<br>
Add Volume Rendering with the input set to the new file, click the eye open, choose the preset Bones (say, CT AAA2 or CT-Fat) I basically want to export out three obj files, skin, bones and fat respectively.</p>
<p>And this is where things get fuzzy:<br>
Click Editor, add generic anatomy colours.<br>
Click Make Model Effect, click apply (wait a moment)<br>
click Go To Model Maker<br>
in Models click create new Model Hierarchy<br>
in model Maker parameters<br>
uncheck generate all models<br>
check filter type to Laplacian<br>
That should allow me to save polydata that I want. Only it doesn’t and I’ve tried for several hours now and I’m not getting any closer to what I want. Which is essentially exporting what I see on the screen (bones, fat) as an obj. I’ve managed to do the skin layer by using ThresholdEffect, but that’s about it</p>
<p>Can anyone help me out?</p>

---

## Post #2 by @pieper (2018-05-03 21:26 UTC)

<p>You can start with this tutorial and video:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Training#Segmentation_for_3D_printing" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Training#Segmentation_for_3D_printing</a></p>

---

## Post #3 by @lassoan (2018-05-04 01:33 UTC)

<p>Note that what you visualize with volume rendering may appear as a surface when viewed on a 2D screen, but it is actually a surface-like rendering of a semi-transparent point cloud, and therefore it cannot be “saved” as a surface mesh. You must segment it if you need it as .obj or .stl, as Steve described above. See this post for more detailed explanation: <a href="https://discourse.slicer.org/t/save-volume-rendering-as-stl-file/524">Save volume rendering as STL file</a>.</p>

---
