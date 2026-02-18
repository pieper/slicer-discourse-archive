# Get ROI size in pixels

**Topic ID**: 18665
**Date**: 2021-07-13
**URL**: https://discourse.slicer.org/t/get-roi-size-in-pixels/18665

---

## Post #1 by @xackey (2021-07-13 07:38 UTC)

<p>Dear lassoan</p>
<p>Could you teach me how to determine the ROI size by number of pixels, not millimeter?<br>
My goal is to set both L-R and P-A ranges into 100 pixels, and make a cropped volume with x and y lengths = 100 pixels.</p>

---

## Post #2 by @lassoan (2021-07-13 13:58 UTC)

<p>Spacing of a volume may be anisotropic (different voxel size in different directions) and even be different in different parts of the volume (if a warping transform is applied to the volume). Therefore, the only thing that you can easily and reliably compute is correspondence between physical (RAS) coordinates and voxel coordinates (IJK) as shown in <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-volume-voxel-coordinates-from-markup-fiducial-ras-coordinates">this example</a>.</p>

---

## Post #3 by @lassoan (2021-07-13 13:59 UTC)



---
