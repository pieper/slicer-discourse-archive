---
topic_id: 25054
title: "Ispointinroi And Getplanes Not Available"
date: 2022-09-02
url: https://discourse.slicer.org/t/25054
---

# IsPointInROI and GetPlanes not available

**Topic ID**: 25054
**Date**: 2022-09-02
**URL**: https://discourse.slicer.org/t/ispointinroi-and-getplanes-not-available/25054

---

## Post #1 by @Niels (2022-09-02 14:08 UTC)

<p>Hello Slicer users,</p>
<p>In my Python script I try to check if a voxel is inside a ROI. I searched the forum and found two options which are: IsPointInROI() and GetPlanes() on the vtkMRMLMarkupsROINode.</p>
<p>But on both I get an error that the attributes are not available. I use Slicer 4.11, maybe those methods are only available in newer versions of Slicer?</p>
<p>I use the new ROI node because that one has the possibility to rorate/place in the 3D window.</p>

---

## Post #2 by @lassoan (2022-09-03 12:43 UTC)

<p>Probably these methods are added in more recent Slicer versions.</p>

---

## Post #3 by @Niels (2022-09-05 11:39 UTC)

<p>I installed Slicer version 5.0.3 r30893 and tested with IsPointInROI. it works for the newer version</p>

---

## Post #4 by @Niels (2022-09-06 14:01 UTC)

<p>The functions are available, but I need some help with the usage.<br>
I have a volume and I want to check which voxels are inside the ROI area.<br>
I assume that the IsPointInROI accepts world space coordinates and not voxel space coords. I tried the transformation but I am not successful.</p>
<p>Do we have an example where we check voxels again a rotated ROI?</p>

---

## Post #5 by @lassoan (2022-09-06 15:28 UTC)

<p>With a few rare exceptions (when you access voxels by indices) all 3D coordinates in Slicer are in physical coordinate system. You can transform between them by multiplying the coordinates by the volumes IJK to RAS transformation matrix.</p>
<p>What would you like to achieve? Blank out voxels or compute statistics in a ROI?</p>

---

## Post #6 by @Niels (2022-09-06 19:25 UTC)

<p>My module is a tool to adjust a color volume (three scalars/rgb). I indeed would like to adjust the values within the region of interest. I iterate the voxels x,y,z and need to check if they are inside the roi.</p>
<p>If i understand you correctly, i can get the RAS value of each voxel like you described and use that on the rotated ROI using the IsInside function?</p>

---

## Post #7 by @lassoan (2022-09-06 20:41 UTC)

<p>Setting voxel values one by one would be extremely slow.</p>
<p>Instead, you can apply processing in a designated region very efficiently using numpy array indexing: Create a segment in Segment Editor to designate your region of interest (it can be a box shape but it can be a complex, free-form shape, too) and <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#read-and-write-a-segment-as-a-numpy-array">export that into a numpy array</a>. You can then <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#modify-voxels-in-a-volume">use this array as a mask for numpy operations</a>.</p>

---
