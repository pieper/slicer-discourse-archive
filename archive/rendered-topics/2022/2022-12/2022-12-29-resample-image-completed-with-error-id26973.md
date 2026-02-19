---
topic_id: 26973
title: "Resample Image Completed With Error"
date: 2022-12-29
url: https://discourse.slicer.org/t/26973
---

# Resample Image completed with error

**Topic ID**: 26973
**Date**: 2022-12-29
**URL**: https://discourse.slicer.org/t/resample-image-completed-with-error/26973

---

## Post #1 by @lolamartinalonso (2022-12-29 10:27 UTC)

<p>Hi all,</p>
<p>After applying the landmark registration, I continue with the module of Resample image to finally get the new volume registrated by applying the Transform file obtained through the registration.</p>
<p>But it gives me the following message:</p>
<pre><code class="lang-txt">=====================================================
Input Volume:     C:/Users/mariadolores.martin/AppData/Local/Temp/Slicer/CBHJC_vtkMRMLScalarVolumeNodeB.nrrd
Reference Volume: C:/Users/mariadolores.martin/AppData/Local/Temp/Slicer/CBHJC_vtkMRMLScalarVolumeNodeC.nrrd
Output Volume:    C:/Users/mariadolores.martin/AppData/Local/Temp/Slicer/CBHJC_vtkMRMLScalarVolumeNodeE.nrrd
Pixel Type:       uchar
Interpolation:    Linear
Background Value: 0
Warp By Transform: C:/Users/mariadolores.martin/AppData/Local/Temp/Slicer/CBHJC_vtkMRMLTransformNodeB.h5
=====================================================
******* HERE *******D:\D\P\S-0-build\BRAINSTools\BRAINSResample\BRAINSResample.cxx 628

itk::MemoryAllocationError (000000A2448FDB90)
Location: "unknown" 
File: D:\D\P\S-0-build\ITK\Modules\Core\Common\include\itkImportImageContainer.hxx
Line: 191
Description: Failed to allocate memory for image.

=====================================================
</code></pre>
<p>I can´t understand it because I have performed a lot of registrations like that in the past.</p>
<p>The two volumes have the size of 6,832 MB</p>
<p>I am trying to make the resample operation to get an output of a pixel type uchar.</p>
<p>Thanks in advance</p>
<p>Lola<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7bc9c63d831bb6f3b32addaa8f6fd200a2ba75b6.jpeg" data-download-href="/uploads/short-url/hF51LrK397Tvxnob3BFa724TAWi.jpeg?dl=1" title="Screenshot 2022-12-29 112533" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bc9c63d831bb6f3b32addaa8f6fd200a2ba75b6_2_690x372.jpeg" alt="Screenshot 2022-12-29 112533" data-base62-sha1="hF51LrK397Tvxnob3BFa724TAWi" width="690" height="372" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bc9c63d831bb6f3b32addaa8f6fd200a2ba75b6_2_690x372.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bc9c63d831bb6f3b32addaa8f6fd200a2ba75b6_2_1035x558.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7bc9c63d831bb6f3b32addaa8f6fd200a2ba75b6_2_1380x744.jpeg 2x" data-dominant-color="BCBCBB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2022-12-29 112533</span><span class="informations">1920×1037 141 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-12-29 16:13 UTC)

<p>According to the error message you have run out of memory.</p>
<p>It seems that the images you work with are very large, therefore you need a lot of memory space. Ideally, you would add more physical RAM to your system, or (at the cost of longer computation time) you can just increase the virtual memory size in Windows system settings.</p>
<p>Alternatively, you can use Crop volume module for resampling, as it allows reducing the output image extent and resolution, thereby reducing memory needs.</p>

---
