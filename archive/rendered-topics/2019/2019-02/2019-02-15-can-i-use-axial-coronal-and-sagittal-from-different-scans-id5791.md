---
topic_id: 5791
title: "Can I Use Axial Coronal And Sagittal From Different Scans"
date: 2019-02-15
url: https://discourse.slicer.org/t/5791
---

# Can I Use Axial Coronal and Sagittal from Different Scans?

**Topic ID**: 5791
**Date**: 2019-02-15
**URL**: https://discourse.slicer.org/t/can-i-use-axial-coronal-and-sagittal-from-different-scans/5791

---

## Post #1 by @nate (2019-02-15 15:21 UTC)

<p>I have loaded a DICOM file into Slicer. When I look at the Data module, I can see the separate scans done for each plane (a scan for axial, sagittal, and coronal) and each is listed as a volume. When looking at one of these volumes - axial for example - it shows the red, yellow, and green slices, and if I turn on the sight for the volume in Volume Rendering, I can see it there as a 3D rendering. The red slice window is the axial window, and in it shows the master information that the green and yellow window’s information is derived from. In other words, the red/axial window is showing me slices(images) that were actually captured from the scanner. While the yellow and green windows are calculated from the information in the red window. [This is how I assume Slicer works, and if I’m wrong here, please correct this assumption first.]</p>
<p>As a result of this, the red window has better resolution and the other two windows have less. This is due to the spacing between the actual images captured from the scanning done in the axial plane. If the slices are 1 mm apart from each other when scrolling through them in the red window, then one of the dimensions for the yellow and green is going to be that 1 mm. This results in rectangular prism voxels instead of cubic, which I know I can fix by cropping the volume using isotropic spacing. Important to note here is that the space between the slices causes a stair case look when looking at he rendered volume.</p>
<p>Let’s say I have the volume in a given orientation where I can see the staircases really well…  …If I close that axial volume and open up a different volume, the staircases go away for the same view orientation that I was on.  Where the stairs were is now a very clear continuous volume surface with no staircase appearance. This is because this volume was taken in a different plane. I can - for this second volume - rotate the view to find where it’s own staircases are visible.</p>
<p>My question is a result of me recognizing that each scan’s images are used to each create their own volumes in Slicer- leading to lost information in the staircases. Is it possible to use the slices that were only taken by the scanner (not calculated by Slicer) to make a volume: To have the red window be the original axial images taken by the scanner, to have the yellow window be the original sagittal images taken by the scanner, and have the green window be the original coronal images taken by the scanner? In theory, the rendered volume would have no staircases seen, no matter the orientation.</p>
<p>I have a feeling this might require lots of work because each window would be taken from separate scans, and I don’t know how Slicer would know what pixel in one window is the same pixel in a different window…</p>
<p>Anyway, thank you for reading this long entry.</p>
<p>Operating system: Win 10<br>
Slicer version: 4.10.0</p>

---

## Post #2 by @jcfr (2019-02-15 15:25 UTC)

<p>Look like you have 3 anisotropic scans with high resolution in only one axis and you would like to combine them ?</p>
<p>If this is the case, I suggest you read <a href="https://discourse.slicer.org/t/3d-model-from-dicoms/5478/2?u=jcfr" class="inline-onebox">3D model from dicoms</a></p>

---
