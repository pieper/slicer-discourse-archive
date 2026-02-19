---
topic_id: 12249
title: "Transform Matrix And Image Coordinates For Fcsv Files"
date: 2020-06-27
url: https://discourse.slicer.org/t/12249
---

# Transform matrix and image coordinates for .fcsv files

**Topic ID**: 12249
**Date**: 2020-06-27
**URL**: https://discourse.slicer.org/t/transform-matrix-and-image-coordinates-for-fcsv-files/12249

---

## Post #1 by @FatihSogukpinar (2020-06-27 23:53 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.10.2</p>
<p>Hi all,</p>
<p>In Slicer I have an atlas and a .fcsv file. I need to get coordinates of .fcsv file in the image coordinates from Slicer to Matlab (and also the anatomical regions to which these points correspond). So basically I need the transform matrix for the .fcsv file, so that I can also transform the coordinates in Matlab and explore the locations.</p>
<p>How can I get the matrix from Slicer ?</p>
<p>And also, is there a way to get the anatomical locations directly from Slicer to Matlab ?</p>
<p>Thank you so much !</p>
<p>PS: I am new to Slicer …</p>

---

## Post #2 by @lassoan (2020-06-28 00:02 UTC)

<p>You can get voxel coordinates from physical (RAS) coordinates from the volume’s IJK to RAS matrix, as shown in this example:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Get_volume_voxel_coordinates_from_markup_fiducial_RAS_coordinates</a></p>
<p>You can get IJK to RAS matrix in Matlab by reading the exported nrrd file using this reader: <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdread.m">https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdread.m</a></p>
<p>However, I would strongly recommend to move on from Matlab to Python. Python has so much more libraries, several magnitudes more developers, it is also a generic programming language that you can use to implement complete solutions. Python is also free, so you can use it after you finish your studies (Matlab commercial licenses are so expensive that companies rarely use it). Whatever you develop you can easily deploy it to end users if you use Python, as there are no licensing issues. You also have a full Python environment within 3D Slicer, so you can do all your processing within one application. You can also run all Slicer features in Python, customize the application and add new modules using Python scripting.</p>

---

## Post #3 by @FatihSogukpinar (2020-07-01 06:12 UTC)

<p>Thank you so much Andras ! This was really helpful and I was able to solve most of my problems by the Python interface.<br>
Now I have further questions about Python scripting. For example, I want to load fiducial lists, use more python libraries, etc. Is there a detailed documentation which you can recommend me for all these python features ?</p>
<p>Thank you so much.</p>

---

## Post #4 by @lassoan (2020-07-01 13:11 UTC)

<p>Yes, everything is quite thoroughly documented. The only caveat is that you need to look for documentation of each library (Slicer core, VTK, CTK, Qt, ITK, …) at a different location. You can find a link to each library in this <a href="https://github.com/PerkLab/PerkLabBootcamp/blob/master/Doc/day3_2_SlicerProgramming.pptx?raw=true">programming tutorial</a> (slide 48).</p>
<p>There are also lots of examples to learn from: <a href="https://github.com/Slicer/Slicer">Slicer core</a>, all the <a href="https://github.com/Slicer/ExtensionsIndex">extensions</a>, and the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository">script repository</a>.</p>

---
