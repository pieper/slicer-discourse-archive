# Coordinate transformations? 

**Topic ID**: 30682
**Date**: 2023-07-19
**URL**: https://discourse.slicer.org/t/coordinate-transformations/30682

---

## Post #1 by @Charlie_Hayward (2023-07-19 15:52 UTC)

<p>Hello, I am attempting to fully automate the vmtkcenterline function by specifying seed points like this: vmtkcenterlines -seedselector pointlist -sourcepoints 0 0 0 -targetpoints 1 1 1 2 2 2. To find the source and target points I have a function that utilizes gradient data and the mask as nifti files, it then finds the end points. I have checked its functionality by looking at the output points on the mask file using itk snap. Unfortunately, I have found that after segmentation and level sets, and smoothing my .vtp file has a different coordinate system. For reference the endpoints from the .nii file are: (131.15801614763552, 80.82237600922723, 17)<br>
(47.65384615384615, 137.34615384615384, 644)<br>
(97.26470588235294, 75.5672268907563, 678)<br>
and the .vtp file are (roughly):<br>
(159, 55, -113)<br>
(129, 75, 105)<br>
(147, 54, 117)<br>
How are the coordinates transformed using the vmtk pipeline? Any info on how to convert my scripts .nii endpoints to the .vtp endpoints would be greatly appreciated</p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2023-07-21 14:11 UTC)

<p>You can have a look how it got fully automated in 3D Slicer’s Extract Centerline module. See source code <a href="https://github.com/vmtk/SlicerExtension-VMTK/blob/master/ExtractCenterline/ExtractCenterline.py#L327">here</a>.</p>

---
