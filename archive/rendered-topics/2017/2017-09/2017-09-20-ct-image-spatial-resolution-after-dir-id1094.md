# CT image spatial resolution after DIR

**Topic ID**: 1094
**Date**: 2017-09-20
**URL**: https://discourse.slicer.org/t/ct-image-spatial-resolution-after-dir/1094

---

## Post #1 by @pwang (2017-09-20 21:54 UTC)

<p>Operating system: Win7<br>
Slicer version:4.7.0<br>
The spatial resolution of CT image after deformable image registration is worsened. <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60a04a7f806ea0d3b12c79452c85a837890c6953.jpeg" alt="image" data-base62-sha1="dMNg3QbYdm4W8IcAZCr1R47tWj9" width="173" height="182"> How to solve it? Here is the steps I have taken:</p>
<ol>
<li>Convert the dicom image to .nrrd files. (I have tested, this step won’t worse the resolution)</li>
<li>Crop the images to have the same region of interest. (The Crop makes the image blur) <img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/6/e6ab2a01e387f4125a1ac9dc16cb360a86d18ea4.jpeg" alt="image" data-base62-sha1="wUAxcL9nfRDg7t1dAvmkrhXdbzm" width="329" height="367">
</li>
<li>Use the Plastimatch plugin to perform the deformable registration.</li>
<li>Save as dicom files. The blur is seen as the first image.<br>
My questions is how to avoid reducing the spatial resolution in the step of crop? Are there any other steps could reduce the spatial resolution, how to avoid it? Thank you very much.</li>
</ol>

---

## Post #2 by @lassoan (2017-09-21 00:59 UTC)

<p>You can do non-interpolated cropping. Voxel values will be preserved without any changes.</p>
<p>However, you’ll have blurring when you resample the moving volume with the computed warping transform.</p>
<p>You can minimize blurring if during resampling you use a higher-resolution volume as reference volume (e.g., reduce the voxel size of fixed volume using Crop volume module) and use a higher-order interpolator (sinc or bspline).</p>
<p>If your input volume spacing is highly anisotropic (voxels are not cube shaped) then blurring can only be reduced but not eliminated. What is the spacing of your fixed and moving volume?</p>

---
