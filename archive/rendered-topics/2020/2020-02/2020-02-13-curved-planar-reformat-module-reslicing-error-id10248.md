---
topic_id: 10248
title: "Curved Planar Reformat Module Reslicing Error"
date: 2020-02-13
url: https://discourse.slicer.org/t/10248
---

# Curved Planar Reformat module reslicing error

**Topic ID**: 10248
**Date**: 2020-02-13
**URL**: https://discourse.slicer.org/t/curved-planar-reformat-module-reslicing-error/10248

---

## Post #1 by @mikebind (2020-02-13 22:19 UTC)

<p>Hello, I use SplineDrivenImageSlicer via the Curve Planar Reformat module of Slicer. However, I noticed that when I tried to reslice along a curve that the resliced images are not exactly centered on the supplied curve. This error could be grossly off if a transform had been applied to the image volume I was trying to reslice, but even with no transform applied, the resliced image was centered +0.5 mm off in the Right/I direction, and -0.5 mm off in the Anterior/J direction, with no error in the Superior/K direction (this is in a volume with zero origin and identity IJK to RAS matrix). At first I thought this could be due to a half-voxel shift somewhere (sometimes the origin is treated as the center of a voxel and sometimes it is treated as the corner of a voxel), but the error does not scale with the voxel size, instead it is always 0.5 mm regardless of whether this is half a voxel or two voxels or ten voxels. I have examined the Slicer module code (<a href="https://github.com/PerkLab/SlicerSandbox/blob/master/CurvedPlanarReformat/CurvedPlanarReformat.py" rel="nofollow noopener">https://github.com/PerkLab/SlicerSandbox/blob/master/CurvedPlanarReformat/CurvedPlanarReformat.py</a>) and can find nothing in that code which could explain this error.</p>
<p>My ability to read C++ code is much impaired relative to my ability to read Python, but I think I may have found the source of the bug in vtkSplineDrivenImageSlicer.cxx. On lines 112-114 of<br>
<a href="https://github.com/djelouze/SplineDrivenImageSlicer/blob/6b6cb42dbd5dd5df81eddf5cc0ecc6e5f75a4905/Filters/vtkSplineDrivenImageSlicer.cxx#L112-L114" rel="nofollow noopener">SplineDrivenImageSlicer/Filters/vtkSplineDrivenImageSlicer.cxx</a><br>
one is subtracted from the slice extent in the two slice directions. I don’t understand why this would be necessary or helpful. Furthermore, on <a href="https://github.com/djelouze/SplineDrivenImageSlicer/blob/6b6cb42dbd5dd5df81eddf5cc0ecc6e5f75a4905/Filters/vtkSplineDrivenImageSlicer.cxx#L211-L214" rel="nofollow noopener">lines 211-214</a><br>
the slice plane origin is set by using half the slice extent (without subtracting one). I think this could be how the center of the image ends of displaced by .5 mm in two dimensions (i.e. 1 mm shortened extent, divided by two, would lead to an error of .5 mm).</p>
<p>The larger and more complex errors I run into when there is a non-zero image origin and an applied rotation transform might be somehow related, but they might also be separate. I don’t understand those errors at this point.</p>
<p>I have been performing testing by constructing image volumes where the voxel value is it’s I, J, or K coordinate (3 separate volumes). Then I reslice along a straight line which is parallel to one of the axes and centered in the volume (for example, the K axis). In that case, I know exactly what the value of the center voxel should be, and can check it for errors. If it is wrong, then size of the error tells me how many voxels away from the correct voxel the sampled voxel is. By changing the voxel size, I was able to determine that the voxel error varied inversely with the voxel size, and that therefore the physical size of the error was actually constant (and equal to half a millimeter).</p>
<p>It is possible, but I can’t tell for sure, that just removing the -1 from lines 112 and 113 of<br>
vtkSplineDrivenImageSlicer.cxx will fix the problem. However, it is also possible that that subtraction was included for some other reason and this would introduce a different bug. I can’t follow the C++ code well enough to tell.</p>
<p>I don’t know how to modify C++ code and have the modified code used in Slicer (my impression is that it would involve rebuilding Slicer from source), and that’s a greater investment than I can make at the moment, so I don’t feel like this is something I can fix.  However, if I am correct, this error affects every straightened volume created for any user of the Curved Planar Reformat module, so perhaps someone with greater skill will take an interest? I’m happy to share my testing code if someone would find it helpful.  I also think that someone else constructing a test from scratch would be reassuring that I am not somehow creating this error in my own code. I am confident that I am not, however, because I can reproduce the error without using any of my own code, simply by carefully placing fiducials in a test volume and using the Curved Planar Reformat module’s GUI.</p>

---
