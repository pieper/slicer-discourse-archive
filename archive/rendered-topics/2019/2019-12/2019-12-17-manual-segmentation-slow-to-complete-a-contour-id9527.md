---
topic_id: 9527
title: "Manual Segmentation Slow To Complete A Contour"
date: 2019-12-17
url: https://discourse.slicer.org/t/9527
---

# Manual segmentation slow to complete a contour

**Topic ID**: 9527
**Date**: 2019-12-17
**URL**: https://discourse.slicer.org/t/manual-segmentation-slow-to-complete-a-contour/9527

---

## Post #1 by @spaper (2019-12-17 15:50 UTC)

<p><strong>Background:</strong><br>
I am currently working on segmenting the articular cartilage and synovial tissue in MRI DICOM images of human knees. The purpose for these segmentations is to compare them to segmentations completed using 3D ultrasound images. My ultrasound images have a voxel size of (0.058 mm, 0.058 mm, 0.333mm) while my MRI images have a voxel size of (0.625 mm, 0.625 mm, 0.400 mm). When I segment my MRI images, the segmentation quality is very poor because of the significantly larger voxel size of MRI compared to the ultrasound I am trying to compare it to. To solve this, I have re-sampled my MRI images in MATLAB to have the same voxel size as the ultrasound images (without changing the slice thickness to avoid interpolation of slices that weren’t actually acquired). After re-sampling my MRI images, they now contain 2748 by 2748 by 236 pixels. I believe that the large of number of pixels is where my problem arises.</p>
<p><strong>Problem:</strong><br>
I need to do my segmentations manually according to the protocol I have developed. I use the segment editor module with the draw tool. When I go to close the current contour I have created on a single slice of an MRI image, it takes <strong>15 seconds</strong> to fill it in. This is much too slow for my needs. I am segmenting my MRI images using every other slice to save time (instead of segmenting around 200 slices, I’ll segment 100 and interpolate between the slices afterwards). So, for <strong>15 seconds</strong> of wait time per slice, times <strong>100 slices</strong> of segmentations, there is a lot of time used to simply wait for the contours to close. This is all part of a single complete segmentation of one MRI DICOM sereies. I have to complete over 25 DICOM series for this project, but with the rate at which it takes to segment, that might not be possible.</p>
<p>Trying to investigate the issue, I have checked my hardware performance to see what might be causing this. When I close a contour, my CPUs (2 intel Xeon 2.40 GHz) hit 100% and my RAM (24 GB) hits 80%. I have 2 GPUs (Quadro 5000 and Quadro 4000) which don’t seem to be utilized for this. I have tried to do the same thing on a colleague’s machine with a better (single) CPU with 4.00 GHz and 32 GB of RAM and the same issue occurs. This leads me to believe it is not a hardware issue. Is there a solution that would speed up the time it takes for me to complete my manual segmentations? Is it possible to multi-thread the segment editor module? I have 6 cores with 12 threads but I believe slicer is only using 1 for my segmentations.</p>
<p>Any feedback would be greatly appreciated, I have hit a roadblock and need some help. I apologize for a long post, I just wanted to give everyone as much information about this problem as I can. If you need any more information please let me know!</p>

---

## Post #2 by @lassoan (2019-12-17 22:12 UTC)

<aside class="quote no-group" data-username="spaper" data-post="1" data-topic="9527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/e99b99/48.png" class="avatar"> spaper:</div>
<blockquote>
<p>My ultrasound images have a voxel size of (0.058 mm, 0.058 mm, 0.333mm)</p>
</blockquote>
</aside>
<p>Unfortunately, this image resolution is not well suited for 3D processing, as your voxels are not cubes but long sticks. Unless you can develop some smart image reconstruction method (that uses prior knowledge to fill in the gaps), you need to downsample these images before you can do any meaningful processing. Something like 0.2-0.3mm isotropic spacing may work. You can perform this resampling using “Crop volume” module.</p>
<aside class="quote no-group" data-username="spaper" data-post="1" data-topic="9527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/e99b99/48.png" class="avatar"> spaper:</div>
<blockquote>
<p>To solve this, I have re-sampled my MRI images in MATLAB to have the same voxel size as the ultrasound images</p>
</blockquote>
</aside>
<p>Due to the reasons described above, you cannot utilize high in-plane resolution of the ultrasound image slices, so instead of resampling everything to the ultrasound in-plane resolution, I would recommend to resample everything to an isotropic grid of 0.2-0.6mm spacing. This will most likely solve your memory and performance issues, too.</p>
<aside class="quote no-group" data-username="spaper" data-post="1" data-topic="9527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/e99b99/48.png" class="avatar"> spaper:</div>
<blockquote>
<p>When I go to close the current contour I have created on a single slice of an MRI image, it takes <strong>15 seconds</strong> to fill it in</p>
</blockquote>
</aside>
<p>This is highly unusual, even if for large images. A few things you can try:</p>
<ul>
<li>We have implemented many segmentation performance improvements, so you may try if latest Slicer Preview Release works any better for you.</li>
<li>Make sure you have 10x more physical RAM than the total size of all data that you load at once.</li>
<li>If you enabled “Show 3D” option then disable “Surface smoothing” to make updates faster.</li>
<li>Double-check that you don’t have any auto-complete effect (Grow from seeds, Fill between slices, Watershed) active in the background.</li>
</ul>
<aside class="quote no-group" data-username="spaper" data-post="1" data-topic="9527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/e99b99/48.png" class="avatar"> spaper:</div>
<blockquote>
<p>When I close a contour, my CPUs (2 intel Xeon 2.40 GHz) hit 100% and my RAM (24 GB) hits 80%. I have 2 GPUs (Quadro 5000 and Quadro 4000) which don’t seem to be utilized for this.</p>
</blockquote>
</aside>
<p>Multiple CPU cores are used in processing algorithms that can be parallelized efficiently, while others will just use one core. GPU is only used for visualization and by few filters and segmentation tools, so having a stronger GPU is not expected to make much difference in general (other than faster rendering of 3D view).</p>

---

## Post #3 by @spaper (2019-12-18 19:46 UTC)

<p>Thanks for the reply!</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="9527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This is highly unusual, even if for large images. A few things you can try:</p>
<ul>
<li>We have implemented many segmentation performance improvements, so you may try if latest Slicer Preview Release works any better for you.</li>
<li>Make sure you have 10x more physical RAM than the total size of all data that you load at once.</li>
<li>If you enabled “Show 3D” option then disable “Surface smoothing” to make updates faster.</li>
<li>Double-check that you don’t have any auto-complete effect (Grow from seeds, Fill between slices, Watershed) active in the background.</li>
</ul>
</blockquote>
</aside>
<p>I downloaded the newest preview release which cut the time down from 15 seconds to 10 seconds. I have tried to segment the images on a separate computer with the amount of RAM matching your suggestion but the issue still arose with no improvements in the time it took. I have ensured that show 3D and surface smoothing were un-selected, and the background autocomplete effects were disabled.</p>
<p>It is strange that with the same voxel sizes, the ultrasound images do not take this long to complete a contour on a single slice. It is only happening with the MRI images. When I reduce the number of slices I load into 3D Slicer from the MRI dicom series to match the number of slices in my ultrasound images, the time it takes reduces to 5 seconds. This is much better, but this is only using part of the dicom series which is not ideal. Also, it takes under 1 second to complete a contour on the ultrasound images with the exact same voxel size and number of slices.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="9527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Unless you can develop some smart image reconstruction method (that uses prior knowledge to fill in the gaps), you need to downsample these images before you can do any meaningful processing.</p>
</blockquote>
</aside>
<p>I am not sure that I follow what you are saying here. What gaps are you referring to? The gaps in slice thickness compared to the in plane resolution? We are completing our segmentations using the plane with high resolution and interpolating between every other slice along the poorer resolution slice thickness. I am currently able to produce segmentations using this method that match expected values from other experiments. I don’t think I completely understand why I need to have isotropic spacing before completing these segmentations.</p>

---

## Post #4 by @lassoan (2019-12-18 21:14 UTC)

<aside class="quote no-group" data-username="spaper" data-post="3" data-topic="9527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/e99b99/48.png" class="avatar"> spaper:</div>
<blockquote>
<p>The gaps in slice thickness compared to the in plane resolution? We are completing our segmentations using the plane with high resolution and interpolating between every other slice along the poorer resolution slice thickness.</p>
</blockquote>
</aside>
<p>Yes, I mean that you cannot use a simple interpolation to recover details that are missing between slices because interpolation can only reconstruct the original signal if the Nyquist criterion is fulfilled (your sampling is sufficiently dense compared to the spatial frequency of the signal). If you apply anti-aliasing filter to ensure the criterion is not violated, then the filtering removes the high-frequency content, so essentially the high-resolution details in the ultrasound slices cannot contribute to the 3D image reconstruction.</p>
<p>A common, very visible result of Nyquist criterion violation is staircase artifacts on the reconstructed surface. See <a href="https://discourse.slicer.org/t/combining-volumes-what-am-i-missing/2941/2">this</a> and related posts for details.</p>
<p>You may be able to utilize the high in-plane resolution of the ultrasound images by using superresolution techniques, but not by simple image interpolation. If you don’t have time to explore such methods then I would recommend to remove the information content that you cannot use anyway, early in the data processing pipeline (downsample the ultrasound images), to avoid pushing through huge amount of data through the pipeline that actually cannot contribute to the end results.</p>
<aside class="quote no-group" data-username="spaper" data-post="3" data-topic="9527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/e99b99/48.png" class="avatar"> spaper:</div>
<blockquote>
<p>It is strange that with the same voxel sizes, the ultrasound images do not take this long to complete a contour on a single slice. It is only happening with the MRI images.</p>
</blockquote>
</aside>
<p>It is hard to guess what could go wrong. Maybe voxels in you MRI image are floating-point? If you can share a scene that demonstrates the unexpected performance issue or you can reproduce the problem with any of the public sample data sets (maybe resampling them using Crop volume module) then we can investigate this further.</p>

---

## Post #5 by @spaper (2019-12-19 18:13 UTC)

<p>Thank you very much for the clarification. I am currently looking into ways to work around this resolution issue taking some of the things you have told me into account. I appreciate the feedback!</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="9527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>If you can share a scene that demonstrates the unexpected performance issue or you can reproduce the problem with any of the public sample data sets (maybe resampling them using Crop volume module) then we can investigate this further.</p>
</blockquote>
</aside>
<p>I am starting to think that it has to do with the number of pixels in my image. The MRI are 2748 by 2748 by 250. When I crop the MRI image size to match the number of pixels as my ultrasound images, the problem goes away. The issue with doing this is that the field of view of the cropped MRI is not big enough to contain the tissues I am segmenting.</p>
<p>In the meantime, I have changed the degree of re-sampling in my MRI images so they are now 1063 by 1063 (without changing the slice thickness). The time now to close a contour is around 2 seconds.</p>
<p>I was able to recreate the issue by re-sampling the MRHead sample data using the “resample scalar volume” module which allows me to choose a new dimension for the voxels.</p>
<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="9527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Maybe voxels in you MRI image are floating-point?</p>
</blockquote>
</aside>
<p>My ultrasound are unsigned char while the MRI are short.</p>
<p>As an unrelated side note, is there a way to change the default tool selected when opening the latest release of slicer to allow me to adjust window/level without needing to select the window/level tool from the toolbar? This changed when I downloaded the preview release.</p>

---

## Post #6 by @lassoan (2019-12-19 18:57 UTC)

<aside class="quote no-group" data-username="spaper" data-post="5" data-topic="9527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/e99b99/48.png" class="avatar"> spaper:</div>
<blockquote>
<p>The MRI are 2748 by 2748 by 250.</p>
</blockquote>
</aside>
<p>This is extreme. This is probably about 100x larger than the original image. By resampling your MRI to this resolution, you increased memory need and computation time by about 100x (so your computer cannot easily handle it anymore), without gaining any extra information (the resampled image still has the same information content as the original).</p>
<p>Working with the original MRI resolution for joint MRI/ultrasound processing should be fine, or maybe oversample a bit and make spacing isotropic (cube voxel size).</p>
<aside class="quote no-group" data-username="spaper" data-post="5" data-topic="9527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/e99b99/48.png" class="avatar"> spaper:</div>
<blockquote>
<p>The issue with doing this is that the field of view of the cropped MRI is not big enough to contain the tissues I am segmenting.</p>
</blockquote>
</aside>
<p>When you use Crop volume module to resample the MRI to be isotropic and optionally oversample it, you can also set the field of view. You can make the field of view to cover the entire region that you are interested in.</p>
<aside class="quote no-group" data-username="spaper" data-post="5" data-topic="9527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/e99b99/48.png" class="avatar"> spaper:</div>
<blockquote>
<p>is there a way to change the default tool selected when opening the latest release of slicer to allow me to adjust window/level without needing to select the window/level tool from the toolbar</p>
</blockquote>
</aside>
<p>Yes. Everything is configurable in Slicer, we just cannot put everything in the application settings GUI. You can set the default mouse mode mode to window/level by putting <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Make_mouse_left-click_and_drag_on_the_image_adjust_window.2Flevel">this line</a> in your <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ/Python_Scripting#How_to_systematically_execute_custom_python_code_at_startup_.3F">.slicerrc.py file</a>.</p>

---

## Post #7 by @spaper (2019-12-20 16:59 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="9527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>without gaining any extra information (the resampled image still has the same information content as the original).</p>
<p>Working with the original MRI resolution for joint MRI/ultrasound processing should be fine, or maybe oversample a bit and make spacing isotropic (cube voxel size).</p>
<p><img src="https://avatars.discourse.org/v4/letter/s/e99b99/40.png" alt="" width="20" height="20" role="presentation"> spaper:</p>
</blockquote>
</aside>
<p>I am not trying to gain more information through re-sampling, I am only trying to reduce the voxel size so that my segmentation contours are smooth. The issue with working at the original MRI resolution is the segmentation quality. I will try to attach images to explain this visually, but because of the scale of the cartilage relative to the voxel size, the segmentation becomes quite jagged and not smooth. The first two images are of the original MRI while the second two are of the resampled one.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc24dbce26476e698909c2aa4af095a1b225d5e4.jpeg" data-download-href="/uploads/short-url/zYzi5z0jX9kapZW3u6e8nugXj1O.jpeg?dl=1" title="Traced Contour.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc24dbce26476e698909c2aa4af095a1b225d5e4_2_690x476.jpeg" alt="Traced Contour.PNG" data-base62-sha1="zYzi5z0jX9kapZW3u6e8nugXj1O" width="690" height="476" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc24dbce26476e698909c2aa4af095a1b225d5e4_2_690x476.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/fc24dbce26476e698909c2aa4af095a1b225d5e4_2_1035x714.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/c/fc24dbce26476e698909c2aa4af095a1b225d5e4.jpeg 2x" data-dominant-color="424242"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Traced Contour.PNG</span><span class="informations">1363×941 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b6ad5b5a436a5da72c08b48bf69de2756e89630.jpeg" data-download-href="/uploads/short-url/6c5qgQPpPtdnlAWvXZTBw2qvYm4.jpeg?dl=1" title="Completed Contour.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b6ad5b5a436a5da72c08b48bf69de2756e89630_2_690x480.jpeg" alt="Completed Contour.PNG" data-base62-sha1="6c5qgQPpPtdnlAWvXZTBw2qvYm4" width="690" height="480" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b6ad5b5a436a5da72c08b48bf69de2756e89630_2_690x480.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2b6ad5b5a436a5da72c08b48bf69de2756e89630_2_1035x720.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/b/2b6ad5b5a436a5da72c08b48bf69de2756e89630.jpeg 2x" data-dominant-color="424241"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Completed Contour.PNG</span><span class="informations">1368×953 153 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/749c562c5ba048cf972237843d698908b655a8a0.jpeg" data-download-href="/uploads/short-url/gDAkQruhSh5M2SiN1zGlxPf5pp6.jpeg?dl=1" title="Traced Contour resampled.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/749c562c5ba048cf972237843d698908b655a8a0_2_683x499.jpeg" alt="Traced Contour resampled.PNG" data-base62-sha1="gDAkQruhSh5M2SiN1zGlxPf5pp6" width="683" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/749c562c5ba048cf972237843d698908b655a8a0_2_683x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/749c562c5ba048cf972237843d698908b655a8a0_2_1024x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/4/749c562c5ba048cf972237843d698908b655a8a0.jpeg 2x" data-dominant-color="333333"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Traced Contour resampled.PNG</span><span class="informations">1339×979 158 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c6123affaf5dc734ff938f2afeb3b1c4c20fb97.jpeg" data-download-href="/uploads/short-url/hKjkffKl2PufLRg81ANb7JlvRbx.jpeg?dl=1" title="Completed Contour resampled.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c6123affaf5dc734ff938f2afeb3b1c4c20fb97_2_677x499.jpeg" alt="Completed Contour resampled.PNG" data-base62-sha1="hKjkffKl2PufLRg81ANb7JlvRbx" width="677" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c6123affaf5dc734ff938f2afeb3b1c4c20fb97_2_677x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/7c6123affaf5dc734ff938f2afeb3b1c4c20fb97_2_1015x748.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/c/7c6123affaf5dc734ff938f2afeb3b1c4c20fb97.jpeg 2x" data-dominant-color="343433"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Completed Contour resampled.PNG</span><span class="informations">1327×979 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I have tried to apply smoothing algorithms or other smoothing methods but those seem to always change the volume of my segmentation in unpredictable ways. Is there a way to improve the smoothness of these segmentations that doesn’t involve me re-sampling the MRI images to unreasonable sizes?</p>
<p>When using the “Fill between slices” tool, is the interpolation along 1 dimension? Or is it in 3 dimensions? Would it only be interpolating between the slices or also within the slices to fill in the gaps? If the interpolation occurs in three dimensions, is there a way to change the interpolation to be restricted to a given dimension?</p>

---

## Post #8 by @lassoan (2019-12-20 18:10 UTC)

<aside class="quote no-group" data-username="spaper" data-post="7" data-topic="9527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/e99b99/48.png" class="avatar"> spaper:</div>
<blockquote>
<p>I am not trying to gain more information through re-sampling, I am only trying to reduce the voxel size so that my segmentation contours are smooth.</p>
</blockquote>
</aside>
<p>OK, not it’s more clear what you want to do.</p>
<p>Segmenting thin structures is always tricky for a number of reasons. A rule of thumb is that spacing of the binary labelmap should be at least 3-5x smaller than the thickness of finest structure you want to segment. If you have a thin membrane represented by only 1-2 voxels then it may break up, leak, etc. during various segmentation operations.</p>
<p>If this requirement leads to very small spacing and therefore very large volume then you either need to reduce the extent of the volume (crop the volume or at least the segmentation to the smallest possible region of interest) or upgrade your hardware.</p>
<p>Don’t worry about the jagged look of the segment in slice views. They meant to show the actual resolution of the binary labelmap representation. When you generate surface, the contours get automatically smoothed, without any significant change in shape or volume. You can choose to show the smoothed representation in slice views (Segmentations module / Display / Advanced / Representation in 2D views / Closed surface) but that triggers mesh smoothing after each editing operation, which slow things down.</p>
<p>I would recommend to spend some time with figuring out what is a good image resolution and extent for you, which can sufficiently represent fine details and your computer can handle it. When deciding what is sufficient, focus on your requirements based on the driving clinical problem: do not try to create a perfect segmentation - <strong>there is no such thing as perfect segmentation</strong> - your segmentation will never be good enough for every possible applications.</p>
<aside class="quote no-group" data-username="spaper" data-post="7" data-topic="9527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/e99b99/48.png" class="avatar"> spaper:</div>
<blockquote>
<p>When using the “Fill between slices” tool, is the interpolation along 1 dimension? Or is it in 3 dimensions?</p>
</blockquote>
</aside>
<p>The algorithm automatically detects the dimension to interpolate along. It does not interpolate within a slice.</p>

---

## Post #9 by @spaper (2019-12-20 18:55 UTC)

<p>Thank you very much! <img src="https://emoji.discourse-cdn.com/twitter/smiley.png?v=12" title=":smiley:" class="emoji" alt=":smiley:" loading="lazy" width="20" height="20">  I will spend time thinking about a good middle ground for image resolution that will give me a “good enough” segmentation for my purposes that my particular machine can handle. I apologize for any miscommunication about this problem.</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="9527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>When you generate surface, the contours get automatically smoothed, without any significant change in shape or volume.</p>
</blockquote>
</aside>
<p>What kind of smoothing happens in this step? My main concern is how this smoothing affects the calculation of the volume of my segmentation after I have completed my contour. You mentioned that this should not change the shape or volume significantly, and I assume that’s the case only if the rule of thumb you mentioned is satisfied. If making a segmentation on 1-2 voxels, would the volume of the segmentation no longer represent the volume of a manually traced contour? For example, just doing a quick test by roughly segmenting 2-3 voxels, the completed contour doesn’t match the manually drawn contour exactly (even after I’ve changed the slice view to represent closed surface as you mentioned). It might be that this is simply not a valid scenario for drawing conclusions with segmentaions without changing anything about the image.</p>
<aside class="quote no-group" data-username="lassoan" data-post="8" data-topic="9527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>The algorithm automatically detects the dimension to interpolate along. It does not interpolate within a slice.</p>
</blockquote>
</aside>
<p>Just to clarify, so if I am creating slices on only one plane (for example segmenting using the sagittal slice) then the algorithm will only interpolate in that one dimension (the axis perpendicular to my slices)?</p>
<p>Thanks again for all the help with my issue!</p>

---

## Post #10 by @lassoan (2019-12-20 19:31 UTC)

<aside class="quote no-group" data-username="spaper" data-post="9" data-topic="9527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/e99b99/48.png" class="avatar"> spaper:</div>
<blockquote>
<p>If making a segmentation on 1-2 voxels, would the volume of the segmentation no longer represent the volume of a manually traced contour?</p>
</blockquote>
</aside>
<p>If the segmentation is too thin then the segment may not be considered as continuous (depending on the processing operation, two voxels that only touch at the corners may or may not considered to be neighbors), during smoothing or other processing operations, even a single-voxel thinning of the segment may lead to completely removing parts of the segment, etc.</p>
<aside class="quote no-group" data-username="spaper" data-post="9" data-topic="9527">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/s/e99b99/48.png" class="avatar"> spaper:</div>
<blockquote>
<p>roughly segmenting 2-3 voxels, the completed contour doesn’t match the manually drawn contour exactly (even after I’ve changed the slice view to represent closed surface as you mentioned).</p>
</blockquote>
</aside>
<p>Depending on your voxel size, you may want to adjust the default smoothing settings (drop-down menu of “Show 3D” button in Segment editor):</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a558a87d4f1af00ecb74e0eb704a7b3ceda111d.png" data-download-href="/uploads/short-url/aBABrcmAPBLVA5s4YbzfcfLRI6h.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a558a87d4f1af00ecb74e0eb704a7b3ceda111d_2_645x500.png" alt="image" data-base62-sha1="aBABrcmAPBLVA5s4YbzfcfLRI6h" width="645" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/a/4a558a87d4f1af00ecb74e0eb704a7b3ceda111d_2_645x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a558a87d4f1af00ecb74e0eb704a7b3ceda111d.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a558a87d4f1af00ecb74e0eb704a7b3ceda111d.png 2x" data-dominant-color="DEE1E2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">859×665 32.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
