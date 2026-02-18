# How can I get the coordinates of markups?

**Topic ID**: 22167
**Date**: 2022-02-24
**URL**: https://discourse.slicer.org/t/how-can-i-get-the-coordinates-of-markups/22167

---

## Post #1 by @kjg (2022-02-24 20:20 UTC)

<p>Hi,<br>
I’m new to 3dSlicer and am trying to understand how to work with the markup function.<br>
My goal is to get the coordinates of three points that I marked up using the “angle” function, so that I can work with them to define a plane when I work with the scan in nifti format in python.<br>
I saw that I can save the markups as .json, and that the file contains positions for each of the points. However I don’t understand how these coordinates translate to the coordinates in the nifti. Is there a way to see the transformation that I need to do? Or an altogether different way of approaching this?</p>
<p>Thanks!<br>
Kari</p>

---

## Post #2 by @lassoan (2022-02-25 07:14 UTC)

<p>The point coordinates in the .json file is in LPS coordinate system, i.e. the DICOM coordinate system.</p>
<p>See the nifti file format specification about how the nifti scanner coordinate system is related to the DICOM coordinate system. For example, you can find a summary here: <a href="https://www.fieldtriptoolbox.org/faq/coordsys/#details-of-the-scanner-ras-coordinate-system" class="inline-onebox">How are the different head and MRI coordinate systems defined? - FieldTrip toolbox</a></p>
<p>Note that in Slicer you can specify a plane markup using 3 control points, which may be more suitable for representing a plane (as it is visualized as a plane in slice and 3D views, you can more easily shift and rotate it, you can specify boundaries, etc.).</p>

---

## Post #3 by @Vathsan (2023-04-05 23:37 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, I was wondering what’s the easiest option to get the x, y ,z coordinates of markup points. For the following landmark point, would it be possible to get the number of other two slices? I do not fully understand the slicer’s coordinates, since there are positive and negative values.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/9/e923d859e7b237a7ee53182cc77223df59085259.jpeg" data-download-href="/uploads/short-url/xgs30baTq05HnkrBOYPLaexHgO5.jpeg?dl=1" title="slicer" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e923d859e7b237a7ee53182cc77223df59085259_2_690x407.jpeg" alt="slicer" data-base62-sha1="xgs30baTq05HnkrBOYPLaexHgO5" width="690" height="407" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e923d859e7b237a7ee53182cc77223df59085259_2_690x407.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e923d859e7b237a7ee53182cc77223df59085259_2_1035x610.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/9/e923d859e7b237a7ee53182cc77223df59085259_2_1380x814.jpeg 2x" data-dominant-color="757675"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer</span><span class="informations">1920×1134 171 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Something similar to what we get for x, y, z position here,</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/c/ac47693db19c7f399774ad2a2fc23ed7df2c099c.png" data-download-href="/uploads/short-url/oA37AQnVqs2Y5BV6g2dRkWAwjs8.png?dl=1" title="itk" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac47693db19c7f399774ad2a2fc23ed7df2c099c_2_690x489.png" alt="itk" data-base62-sha1="oA37AQnVqs2Y5BV6g2dRkWAwjs8" width="690" height="489" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac47693db19c7f399774ad2a2fc23ed7df2c099c_2_690x489.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac47693db19c7f399774ad2a2fc23ed7df2c099c_2_1035x733.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/c/ac47693db19c7f399774ad2a2fc23ed7df2c099c_2_1380x978.png 2x" data-dominant-color="4E4E4E"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">itk</span><span class="informations">1977×1402 289 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Thanks,<br>
Vathsan</p>

---
