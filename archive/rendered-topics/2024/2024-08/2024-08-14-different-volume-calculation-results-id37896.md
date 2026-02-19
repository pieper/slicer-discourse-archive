---
topic_id: 37896
title: "Different Volume Calculation Results"
date: 2024-08-14
url: https://discourse.slicer.org/t/37896
---

# Different Volume Calculation Results

**Topic ID**: 37896
**Date**: 2024-08-14
**URL**: https://discourse.slicer.org/t/different-volume-calculation-results/37896

---

## Post #1 by @dzzhang (2024-08-14 22:46 UTC)

<p>I have a binary mask, I loaded it in 3D slicer as a segmentation file, and in Data module, I used “export visible segments to model”. Then in Models module, I can see the model volume is 55349.06 mm^3 (none smooth).<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7bde0346c20532c6dc214004a396b623def3964e.jpeg" data-download-href="/uploads/short-url/hFMo7Fyjho1QEnkxxHPYCAgCZ2e.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bde0346c20532c6dc214004a396b623def3964e_2_690x200.jpeg" alt="image" data-base62-sha1="hFMo7Fyjho1QEnkxxHPYCAgCZ2e" width="690" height="200" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bde0346c20532c6dc214004a396b623def3964e_2_690x200.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bde0346c20532c6dc214004a396b623def3964e_2_1035x300.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7bde0346c20532c6dc214004a396b623def3964e.jpeg 2x" data-dominant-color="A0ACB8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1348×392 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Then, I used my own vtk codes to calculate its volume:</p>
<pre><code class="lang-auto">mask = vtk.vtkNIFTIImageReader()
mask.SetFileName('origCT_nodule_0.nii.gz')
mask.Update()
nodule = vtk.vtkDiscreteMarchingCubes()
nodule.SetInputData(mask.GetOutput())
nodule.Update()

massProperties = vtk.vtkMassProperties()
massProperties.SetInputData(nodule.GetOutput())
massProperties.Update()
volume = massProperties.GetVolume()
print(volume)
</code></pre>
<p>However, the volume is 47789.92 mm^3. I visualized it to check what happened:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/5/551daf7049b1e25383d35573ca2ff25bde8f107e.png" data-download-href="/uploads/short-url/c8YbuVAzCE3PZCikBDuhCJGAy4u.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/551daf7049b1e25383d35573ca2ff25bde8f107e_2_345x213.png" alt="image" data-base62-sha1="c8YbuVAzCE3PZCikBDuhCJGAy4u" width="345" height="213" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/551daf7049b1e25383d35573ca2ff25bde8f107e_2_345x213.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/551daf7049b1e25383d35573ca2ff25bde8f107e_2_517x319.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/5/551daf7049b1e25383d35573ca2ff25bde8f107e_2_690x426.png 2x" data-dominant-color="975050"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1135×701 65.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Oh, it seems this is an unclosed surface representation. I know 3D Slicer will close it first and then calculate its volume (as in the first screenshot). Then, I used vtkFillHolesFilter() to close the surface first:</p>
<pre><code class="lang-auto">fill_holes_filter = vtk.vtkFillHolesFilter()
fill_holes_filter.SetInputData(nodule.GetOutput())
fill_holes_filter.SetHoleSize(100.0)
fill_holes_filter.Update()
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/8560eacd372a3029bd93ef93df9d614f633791ab.png" data-download-href="/uploads/short-url/j1V99L14EPDc29sSwROG1KYURqb.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/8560eacd372a3029bd93ef93df9d614f633791ab_2_345x213.png" alt="image" data-base62-sha1="j1V99L14EPDc29sSwROG1KYURqb" width="345" height="213" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/8560eacd372a3029bd93ef93df9d614f633791ab_2_345x213.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/8560eacd372a3029bd93ef93df9d614f633791ab_2_517x319.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/8560eacd372a3029bd93ef93df9d614f633791ab_2_690x426.png 2x" data-dominant-color="9B9B9B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1135×701 50.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This time, the volume is 40265.35 mm^3. What happened???</p><aside class="onebox googledrive" data-onebox-src="https://drive.google.com/file/d/1U_n0JB-oBHwwA_0QbKkXfjeiQDnLhhVH/view?usp=sharing">
  <header class="source">

      <a href="https://drive.google.com/file/d/1U_n0JB-oBHwwA_0QbKkXfjeiQDnLhhVH/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">drive.google.com</a>
  </header>

  <article class="onebox-body">
      <a href="https://drive.google.com/file/d/1U_n0JB-oBHwwA_0QbKkXfjeiQDnLhhVH/view?usp=sharing" target="_blank" rel="noopener nofollow ugc"><span class="googledocs-onebox-logo g-drive-logo"></span></a>



<h3><a href="https://drive.google.com/file/d/1U_n0JB-oBHwwA_0QbKkXfjeiQDnLhhVH/view?usp=sharing" target="_blank" rel="noopener nofollow ugc">origCT_nodule_0.nii.gz</a></h3>

<p>Google Drive file.</p>

  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>


---

## Post #2 by @chir.set (2024-08-15 08:17 UTC)

<aside class="quote no-group" data-username="dzzhang" data-post="1" data-topic="37896">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/dzzhang/48/66871_2.png" class="avatar"> dzzhang:</div>
<blockquote>
<p><code>vtk.vtkMassProperties()</code></p>
</blockquote>
</aside>
<p>This class needs also a triangulated surface, try applying vtkTriangleFilter().</p>

---

## Post #3 by @lassoan (2024-08-15 09:43 UTC)

<p>Estimating volume from a mesh is much more complicated and many things can influence the result. Slicer uses more robust and accurate surface reconstruction method than discrete marching cubes. If you use a simpler method then you will get a different, most likely less accurate results.</p>
<p>If you have a labelmap image then you can compute the volume very easily and robustly, using <code>Segment Statistics</code> module. There is only one single computation method (multiply the volume of one voxel by the number of voxels in the segment), so there are no options, no questions, no doubts.</p>

---

## Post #4 by @dzzhang (2024-08-15 17:11 UTC)

<p>I tried the following codes but there’s no luck</p>
<blockquote>
<p>t = vtk.vtkTriangleFilter()<br>
t.SetInputData(nodule.GetOutput())<br>
t.PassVertsOn()<br>
t.PassLinesOn()<br>
t.Update()</p>
</blockquote>

---

## Post #5 by @dzzhang (2024-08-15 17:24 UTC)

<p>Solved it by using the following codes, thanks for the idea:</p>
<pre><code>image_data = mask_image2.GetOutput()
spacing = image_data.GetSpacing()

# Extract the voxel data and convert to a NumPy array
dims = image_data.GetDimensions()
scalars = image_data.GetPointData().GetScalars()
from vtkmodules.util import numpy_support
mask_image_array = numpy_support.vtk_to_numpy(scalars)
mask_image_array = mask_image_array.reshape(dims, order='F')  # Reshape to 3D array with Fortran order

# Convert the segmentation mask to a binary array (1 for segmented regions, 0 otherwise)
binary_array = np.where(mask_image_array &gt; 0, 1, 0)

# Count the number of non-zero voxels
voxel_count = binary_array.sum()

# Calculate the volume in physical units (e.g., mm^3)
voxel_volume = spacing[0] * spacing[1] * spacing[2]
total_volume = voxel_count * voxel_volume

print(total_volume)
</code></pre>

---
