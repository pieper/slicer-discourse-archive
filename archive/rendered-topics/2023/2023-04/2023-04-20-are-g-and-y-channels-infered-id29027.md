---
topic_id: 29027
title: "Are G And Y Channels Infered"
date: 2023-04-20
url: https://discourse.slicer.org/t/29027
---

# Are G and Y channels infered?

**Topic ID**: 29027
**Date**: 2023-04-20
**URL**: https://discourse.slicer.org/t/are-g-and-y-channels-infered/29027

---

## Post #1 by @Ilias_P (2023-04-20 11:46 UTC)

<p>I have some nii.gz files which, when I open using imajeJ , or any python library such as SimpleITK or Monai I get a stack of MRI images, as if taken from top to bottom. That being said, when I open the same file with slicer, I also get a stack of images, taken from the side and from the front, the G and Y channels. My question is, do the images from the different angles exist inside the file, or is 3D slicer inferring how these channels would look like based on the R channel. I am asking this because the other methods don’t seem to be able to find the other views.<br>
Thank you.</p>

---

## Post #2 by @lassoan (2023-04-20 11:50 UTC)

<p>You can interpret a 3D voxel array many ways (a 3-slice scalar image, an RGB color image, a displacement field transform, etc.). What does your data contain?</p>
<p>The memory layout (order of slices in the stack) is typically chosen so that the data does not need any reordering when the file is read, but it is ultimately the choice of each application. For example, if the image uses a left-handed IJK voxel coordinate system then it can make sense to reorder one axis to avoid IJKToLPS transformation matrix with a negative determinant. What matters is that the after the image is read, the IJKToLPS transform correctly maps the voxels in memory to physical space.</p>

---
