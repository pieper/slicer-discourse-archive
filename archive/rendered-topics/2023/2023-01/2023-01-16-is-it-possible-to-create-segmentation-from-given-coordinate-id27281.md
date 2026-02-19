---
topic_id: 27281
title: "Is It Possible To Create Segmentation From Given Coordinate"
date: 2023-01-16
url: https://discourse.slicer.org/t/27281
---

# Is it possible to create segmentation from given coordinate information (x,y,z)?

**Topic ID**: 27281
**Date**: 2023-01-16
**URL**: https://discourse.slicer.org/t/is-it-possible-to-create-segmentation-from-given-coordinate-information-x-y-z/27281

---

## Post #1 by @aysegul_sayin (2023-01-16 22:39 UTC)

<p>Is it possible to segment the x, y, z points that I entered manually? I found that polygons or cubes are drawn with python using vtk, but what I want is to segment the coordinate points I have given by painting. For example, when I enter the point (170,100,150), this point is automatically segmented.</p>

---

## Post #2 by @lassoan (2023-01-16 23:14 UTC)

<p>Do you mean you would want to set each voxel in the segmentation using a method call? That would mean hundreds of thousands, maybe millions of calls for a single segment. That could take dozens of seconds or more.</p>
<p>Python is generally not meant to be used for voxel-bygvixel processing. Can you work with higher-level objects than voxels?</p>
<p>What is your overall goal, clinical problem to solve?</p>

---

## Post #3 by @aysegul_sayin (2023-01-17 08:25 UTC)

<p>thanks for answer,<br>
Actually I want to make this one. I want to turn the coordinates I entered into a segmentation mask on the image.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95fa927802a7ff860b5994e6dd6b01de72f4e8c5.jpeg" data-download-href="/uploads/short-url/loLZt5EfzbtwDYFC41uV0OFsiLH.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95fa927802a7ff860b5994e6dd6b01de72f4e8c5_2_690x314.jpeg" alt="image" data-base62-sha1="loLZt5EfzbtwDYFC41uV0OFsiLH" width="690" height="314" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95fa927802a7ff860b5994e6dd6b01de72f4e8c5_2_690x314.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/5/95fa927802a7ff860b5994e6dd6b01de72f4e8c5_2_1035x471.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/5/95fa927802a7ff860b5994e6dd6b01de72f4e8c5.jpeg 2x" data-dominant-color="A09F9F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1168×532 37.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2023-01-17 19:50 UTC)

<p>You can convert your list of coordinates to a numpy array (see for example <a href="https://stackoverflow.com/questions/56660387/fastest-way-to-convert-a-list-of-indices-to-2d-numpy-array-of-ones">here</a>) and then <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#read-and-write-a-segment-as-a-numpy-array">import that numpy array into a segmentation</a>.</p>
<p>However, this whole idea of representing binary labelmaps as list of coordinate values is much more complicated than needed and extremely inefficient. What software generates point list positions instead of a labelmap image? Does that software have an option to save a binary image instead? If not, then suggest to the developer to implement saving of the result into a numpy array and write that array to a standard 3D image file using pynrrd. You can load the nrrd file into Slicer directly as a segmentation.</p>

---
