# SlicerRT - VR visualization of Dose & Structures overlayed with CT

**Topic ID**: 6004
**Date**: 2019-03-04
**URL**: https://discourse.slicer.org/t/slicerrt-vr-visualization-of-dose-structures-overlayed-with-ct/6004

---

## Post #1 by @ahmad (2019-03-04 13:46 UTC)

<p>Operating system: Windows<br>
Slicer version: 4.10.1<br>
Expected behavior: To show dose color wash and structure using VR<br>
Actual behavior: I could not do it</p>
<p>I would like to know how SlicerRT can be used to accomplish the following functions:</p>
<ol>
<li>How can we use Virtual Reality to view the dose color wash (adjustable) or isodoce lines and structures overlaid over the CT cuts.<br>
I tried to use VR on DICOM-RT but it only showed structures, without showing the dose wash throughout slices.<br>
I hope it is possible to go through CT slices and see how dose distribution throughout slices in either color wash format or isodose lines.</li>
<li>Can I do segmentation (contouring) using the VR environment using the controllers, then save the contoured to the DICOM, and finally export them to be printed?</li>
</ol>
<p>Thank you<br>
Ahmad</p>

---

## Post #2 by @cpinter (2019-03-04 15:01 UTC)

<p>Hi Ahmad,</p>
<p>Thanks for posting your question here.</p>
<ol>
<li>This is more like three questions:<br>
a) You see in VR what you see in the 3D viewers of the Slicer window. So you need to set up the scene to show what you want to see in VR. After you generate isodose surfaces in the Isodose module (Radiotherapy category), then they will show up in VR as well.<br>
b) If you want to see volume rendering of the dose volume, you can visualize it in the Volume Rendering module. It will use the colors that you see in the 2D views. Here are some examples that you can see.<br>
c) You can do it. If you show the slice in 3D, and scroll it, then it will update in VR. You can also bind an object to the slice view to move the slice using the controller in VR. See this video: <a href="https://www.youtube.com/watch?v=F_UBoE4FaoY">https://www.youtube.com/watch?v=F_UBoE4FaoY</a></li>
<li>a) Not yet, but it will be the next major feature we add to VR, once we have time to work on it. You can see progress in this ticket <a href="https://github.com/KitwareMedical/SlicerVirtualReality/issues/43" class="inline-onebox">Add interactive Qt panel to VR scene · Issue #43 · KitwareMedical/SlicerVirtualReality · GitHub</a><br>
b) You can 3D print a segmentation. Just search on this forum, there were plenty of topics about this.</li>
</ol>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c70124be6d4f97237f36c4761740eedeb5d87cf.png" alt="image" data-base62-sha1="hKPjJKIGaePubHCq5uQfvnIEo2j" width="367" height="341"><br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7bb0a2cea0cf61f9600d839f5e23144a3a882f49.png" alt="image" data-base62-sha1="hEdawetNaAeMZ8uEb4TeRasJkeZ" width="371" height="341"></p>
<p>I hope this helps!</p>

---

## Post #3 by @lassoan (2023-03-21 03:09 UTC)



---
