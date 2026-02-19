---
topic_id: 717
title: "Dicom And Vtk File Orientation Issue"
date: 2017-07-19
url: https://discourse.slicer.org/t/717
---

# DICOM and VTK file orientation Issue

**Topic ID**: 717
**Date**: 2017-07-19
**URL**: https://discourse.slicer.org/t/dicom-and-vtk-file-orientation-issue/717

---

## Post #1 by @kanampalli_himaja (2017-07-19 12:23 UTC)

<p>I am trying to load nrrd as AXIAL, CORONAL, SAGITAL view and VTK file outside of the Slicer but the orientation is not matching as in slicer 3d Conventional view if we enable all three AXIAL, Sagital, and CORONAL views. There is some mismatch is there. Let me know how to solve this.</p>

---

## Post #2 by @pieper (2017-07-19 12:37 UTC)

<p>Probably the external code needs to take into account the coordinate systems:</p>
<p><a href="https://www.slicer.org/wiki/Coordinate_systems" class="onebox" target="_blank">https://www.slicer.org/wiki/Coordinate_systems</a></p>

---

## Post #3 by @fedorov (2017-07-19 15:36 UTC)

<p>A similar question came up in another context - does anyone know if there is a surface mesh format (other than DICOM!) that can specify the coordinate system?</p>

---

## Post #4 by @lassoan (2017-07-20 01:24 UTC)

<p>STL, PLY, VTK, VTP could all store the coordinate system (anatomical orientation), but there is no standard or commonly followed practice.<br>
<a href="https://itk.org/Wiki/MetaIO/Documentation">MetaIO</a> (supported by ITK, VTK, etc.) can store surface mesh (MetaSurface object) and anatomical orientation in a standard way, but this file format is rarely used for mesh storage.</p>

---

## Post #5 by @fedorov (2017-07-20 02:24 UTC)

<p>Thanks, I will forward this info to Christian Bauer who asked this question to me.</p>

---

## Post #6 by @kanampalli_himaja (2017-07-20 06:19 UTC)

<p>Hi Pieper, Andrey Fedorov, Andras Lasso,</p>
<p>I have gone through this link : <a href="https://www.slicer.org/wiki/" rel="nofollow noopener">https://www.slicer.org/wiki/</a><br>
Coordinate_systems but I am unable to find out how to make vtk model to<br>
load exactly on the bone structure on Slices(Axial,Sagital,Coronal) from<br>
backend without any adjustments from UI. Only in some cases it is matching<br>
because the bone structure is exactly at origin of the slice . If the bone<br>
structure is some where else like shifted to left or right or top/bottom,<br>
in these cases mismatch is there.</p>
<p>Able to read nrrd and get these details: (Letme know if we can use these<br>
details to load vtk model)<br>
type: int<br>
dimension: 3<br>
space: left-posterior-superior<br>
sizes: 512 512 182<br>
space directions: (0.41406199999999999,0,0) (0,0.41406199999999999,0)<br>
(0,0,0.625)<br>
kinds: domain domain domain<br>
endian: little<br>
encoding: gzip<br>
space origin: (-105.99999999999999,-127.30000305175778,-53.499999999999986)</p>
<p>It looks totally new for me ,  that’s why I am unable to findout. Can you<br>
please help me to sort out this?</p>

---

## Post #7 by @lassoan (2017-07-20 13:04 UTC)

<p>Most common issue is LPS/RAS coordinate system mismatch. So, may try to convert your data from LPS to RAS coordinate system by transforming it using Transforms module by a matrix that has [-1,-1,1,1] in the diagonal:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/9/b9faa9c7ce7284e3e97ef74d293d629977ec889f.png" data-download-href="/uploads/short-url/qxfnhjKtn18Ca9UWvsqvGZbCE4D.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9faa9c7ce7284e3e97ef74d293d629977ec889f_2_312x500.png" alt="image" data-base62-sha1="qxfnhjKtn18Ca9UWvsqvGZbCE4D" width="312" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9faa9c7ce7284e3e97ef74d293d629977ec889f_2_312x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9faa9c7ce7284e3e97ef74d293d629977ec889f_2_468x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/9/b9faa9c7ce7284e3e97ef74d293d629977ec889f_2_624x1000.png 2x" data-dominant-color="F4E4E4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">855×1367 84 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @pieper (2017-07-20 13:04 UTC)

<p>Hi -</p>
<p>The patient coordinate system (RAS in Slicer’s case) provides a frame of reference for the data.  When you have the data in Slicer you can explore this with the Data Probe.  Exported VTK models will be in this space with the vertices expressed in mm.  The nrrd header also tells how the volume data is positioned, scaled, and oriented in this space.</p>
<p>If the external code is using something like the pixel space of the image as the reference coordinate system, then you would need to apply the inverse of the volume’s transform to the vertices of the model.</p>
<p>HTH,<br>
Steve</p>

---

## Post #9 by @lassoan (2017-07-20 14:27 UTC)

<p>A post was split to a new topic: <a href="/t/specifying-coordinate-system-in-surface-mesh-file/724">Specifying coordinate system in surface mesh file</a></p>

---
