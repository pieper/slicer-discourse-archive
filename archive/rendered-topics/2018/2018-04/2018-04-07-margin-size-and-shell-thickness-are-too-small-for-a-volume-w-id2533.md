# "Margin size" and "Shell thickness" are too small for a volume with 0.05 0.05 0.05 spacing

**Topic ID**: 2533
**Date**: 2018-04-07
**URL**: https://discourse.slicer.org/t/margin-size-and-shell-thickness-are-too-small-for-a-volume-with-0-05-0-05-0-05-spacing/2533

---

## Post #1 by @brhoom (2018-04-07 17:02 UTC)

<p>I tried the new Segment Editor Hollow effect and the old Margin effect. I can not get good result because the smallest acceptable size and thinness is 0.8 mm (3x3x1 pixels). Why is that?</p>

---

## Post #2 by @lassoan (2018-04-07 17:31 UTC)

<p>Voxel size of the binary labelmap representation in the segmentation limits the minimum wall thickness. To reduce the voxel size, use Crop volume module on the original input volume and use a scale of &lt; 1.0 (for example, 0.5). It is also recommended to enable isotropic spacing option. If you reduce the voxel size, the number of voxels may increase significantly (thus increasing memory use and computation time). To compensate that, set the cropping region to as small as possible.</p>

---

## Post #3 by @brhoom (2018-04-07 18:18 UTC)

<p>Thanks Andras, I think the segmentation file has a problem. I created a new segmentation and I could reduce the size to 0.2mm (3x3x3 pixels).</p>

---
