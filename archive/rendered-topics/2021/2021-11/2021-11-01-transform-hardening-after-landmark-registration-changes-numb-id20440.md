# Transform hardening after landmark registration changes number of slices

**Topic ID**: 20440
**Date**: 2021-11-01
**URL**: https://discourse.slicer.org/t/transform-hardening-after-landmark-registration-changes-number-of-slices/20440

---

## Post #1 by @giovform (2021-11-01 16:51 UTC)

<p>Hello. I found a strange behavior after hardening a transform that was created using the Landmark Registration module.</p>
<p>After using the Landmark Registration module to register (using ThinPlate Registration) any 2D color images (vector volumes with one slice in the axial direction), the resulting image will still have one slice in the axial direction (as expected). If I harden the transform, then the image will end up with two or even three slices, in the axial direction.</p>
<p>Tested with the latest preview release (revision 30342).</p>

---

## Post #2 by @lassoan (2021-11-01 20:47 UTC)

<p>This is the intended behavior. Thin-plate spline transform is a warping transform, which can change the size of the volume’s bounding box (e.g., one side of the volume may bulge out). To avoid cutting off any part of the volume, when a warping transform is hardened then the new volume extents will be determined so that the entire bounding box of the volume is included. This may be larger or smaller than the volume’s original extent.</p>
<p>If you prefer your volume to have a specific geometry then you can use “Resample Scalar/Vector/DWI volume” module and specify the desired geometry as reference volume.</p>

---

## Post #3 by @giovform (2021-11-04 13:56 UTC)

<p>Even for 2D images only? Because right now, it is transforming a 2D image into a 3D volume. The newly created slices (in the axial direction) don’t contain any meaningful data (just some constant value). I understand that on the image plane the dimensions will probably change.</p>
<p>Original image:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/e/ce6c0e3a2ceb02d91e2fc56ca8929078f563d8da.png" alt="image" data-base62-sha1="ts5RKq202za1tb0B2JXq4CXVORk" width="575" height="41"></p>
<p>Registered image:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/5104fc753a22a34c2002cf379142010cefb361c8.png" alt="image" data-base62-sha1="byJmbOFDDQ8CtOu9s9wMdywHHmw" width="581" height="41"></p>
<p>Newly created slice content:<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/1/517496c9eb49427f48bf54b4115337b20c87c4d6.png" alt="image" data-base62-sha1="bCAsT1lBGBDx0qlj4HbNfiyb6F8" width="476" height="390"></p>

---

## Post #4 by @lassoan (2021-11-05 03:58 UTC)

<p>Yes, regardless of how many slices the volume contains (one or more), if the transform even slightly moves out of plane then the volume bounds will increase and the extents will be increased to accommodate that. If out-of-plane translation component is very little then the other slice may appear blank (due to the linear interpolation).</p>
<p>Since due to numerical precision issues it is almost inevitable to limit out-of-plane transformation component to exactly 0 in every situations (e.g., for oblique image axes), it could make sense to add some tolerance to the computations <a href="https://github.com/Slicer/Slicer/blob/4960b400b3d7135a7b03f28a408358a650fc0a82/Libs/MRML/Core/vtkMRMLVolumeNode.cxx#L1069-L1074">here</a>. For example, if the bounds are off by less than <code>0.001 * spacing</code> then that can be ignored.</p>

---
