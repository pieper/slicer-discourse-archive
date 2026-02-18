# Brain Artery Segmentation - The Small Arterteries are cut off/incomplete

**Topic ID**: 31093
**Date**: 2023-08-10
**URL**: https://discourse.slicer.org/t/brain-artery-segmentation-the-small-arterteries-are-cut-off-incomplete/31093

---

## Post #1 by @Vineet_Saravanan (2023-08-10 22:12 UTC)

<p>Hello, so I am trying to segment CTA scans and get just the arteries. Right now I follow the steps in this post: <a href="https://discourse.slicer.org/t/extracting-stl-from-dicom-images-to-generate-brain-arteries-geometry/25215/6" class="inline-onebox">Extracting STL from DICOM images to generate Brain Arteries geometry - #6 by tsinesh</a><br>
(Import, N4ITK MRI Bias correction, LaplacianSharpeningImageFilter, vesselness filter, Local threshold and then view 3d)<br>
It seems to work well for the larger arteries and those seem to be complete, but the smaller ones are incomplete like the image below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4ec454b9b6d01efb116d8334a561625daed5ccd1.png" data-download-href="/uploads/short-url/beNSy58kBdZcDKAHPvalh6LOl4B.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4ec454b9b6d01efb116d8334a561625daed5ccd1_2_690x457.png" alt="image" data-base62-sha1="beNSy58kBdZcDKAHPvalh6LOl4B" width="690" height="457" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/e/4ec454b9b6d01efb116d8334a561625daed5ccd1_2_690x457.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4ec454b9b6d01efb116d8334a561625daed5ccd1.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/e/4ec454b9b6d01efb116d8334a561625daed5ccd1.png 2x" data-dominant-color="9CA2C8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">942×624 93.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is there a better way to go about this or another plugin that I could use to get more fine grained detail? Right now I have tried lowering the threshold but this just leads to other matter being added to the 3d model. I also tried a minimum diameter of .1 instead of .5 and that didn’t seem to work either. (But it seems like both are just one pixel anyways)<br>
Here are the pictures of the 3D and red:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bec83becb499864ca2052b2a1b97f63d65a71152.png" data-download-href="/uploads/short-url/rdJIzxPkHmCVys6fcfCflMpmZIm.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bec83becb499864ca2052b2a1b97f63d65a71152_2_619x500.png" alt="image" data-base62-sha1="rdJIzxPkHmCVys6fcfCflMpmZIm" width="619" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bec83becb499864ca2052b2a1b97f63d65a71152_2_619x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/e/bec83becb499864ca2052b2a1b97f63d65a71152_2_928x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/e/bec83becb499864ca2052b2a1b97f63d65a71152.png 2x" data-dominant-color="9197C4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">976×788 138 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b39acf5c7a456a4c73b1e76657b1dcb835c8ae0.jpeg" data-download-href="/uploads/short-url/hA6iuKCdrBqTe0aeHfxCoXXlT1u.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b39acf5c7a456a4c73b1e76657b1dcb835c8ae0_2_455x500.jpeg" alt="image" data-base62-sha1="hA6iuKCdrBqTe0aeHfxCoXXlT1u" width="455" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b39acf5c7a456a4c73b1e76657b1dcb835c8ae0_2_455x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/b/7b39acf5c7a456a4c73b1e76657b1dcb835c8ae0_2_682x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/b/7b39acf5c7a456a4c73b1e76657b1dcb835c8ae0.jpeg 2x" data-dominant-color="242322"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">818×898 69.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2023-08-10 22:16 UTC)

<p>To represent smaller vessels, you may need to reduce the voxel size and make sure the voxels are isotropic. In general, the voxel size (=image spacing) must be at least 3-5x smaller than the diameter of the smallest vessel that you want to extract. Probably the easiest is to use Crop volume module  to crop and resample the input volume before segmentation.</p>

---

## Post #3 by @tsinesh (2023-08-11 05:50 UTC)

<p>Dear Vineet Saravanan,</p>
<p>your first image seems to show a very smoothed cerebral arteries. Could it be, that under “Show 3d” (small arrow) in Segment editor the smoothing factor is activated?</p>
<p>May I ask what the goal of your project is?</p>
<p>tamu</p>

---

## Post #4 by @Vineet_Saravanan (2023-08-11 16:13 UTC)

<p>Should I do this after I use the Vesselness filter?</p>

---

## Post #5 by @Vineet_Saravanan (2023-08-11 16:24 UTC)

<p>I tried this and I believe it made the smaller arteries appear. I am trying to extract the arteries to look for brain aneurysms so the arteries have to very exact. Is there any way to remove the extra material from these arteries. Bellow are the 3d models of a smoothing factor of 0 and then of .20</p>
<p>0:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b7b3789b3480e7b8ab3a461dcbdce19fc68ff0d.jpeg" data-download-href="/uploads/short-url/mbrZWbdX50KV5IXxpL3XcHUELox.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b7b3789b3480e7b8ab3a461dcbdce19fc68ff0d_2_526x500.jpeg" alt="image" data-base62-sha1="mbrZWbdX50KV5IXxpL3XcHUELox" width="526" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b7b3789b3480e7b8ab3a461dcbdce19fc68ff0d_2_526x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/b/9b7b3789b3480e7b8ab3a461dcbdce19fc68ff0d_2_789x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9b7b3789b3480e7b8ab3a461dcbdce19fc68ff0d.jpeg 2x" data-dominant-color="9197BE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">944×896 194 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>.2:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ead8d7d7407a2d37f7da208d1387fb09d263ec26.jpeg" data-download-href="/uploads/short-url/xvyjmEtTYi1ez2JGZtrzAmlhfTg.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ead8d7d7407a2d37f7da208d1387fb09d263ec26_2_684x500.jpeg" alt="image" data-base62-sha1="xvyjmEtTYi1ez2JGZtrzAmlhfTg" width="684" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ead8d7d7407a2d37f7da208d1387fb09d263ec26_2_684x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ead8d7d7407a2d37f7da208d1387fb09d263ec26_2_1026x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ead8d7d7407a2d37f7da208d1387fb09d263ec26.jpeg 2x" data-dominant-color="9096C0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1120×818 181 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2023-08-11 20:57 UTC)

<p>You can use Smoothing effect to reduce the noise.</p>
<p>However, the segmentation looks quite good as is. “Extract Centerline” module in VMTK would probably work well on it and it seems that even a 5mm aneurysm should be discernible.</p>
<p>If the goal is to detect aneurysms then I would recommend to try to do it without segmentation, just based on the images, using deep learning.</p>

---

## Post #7 by @tsinesh (2023-08-11 20:57 UTC)

<p>It look much better. You can try in the Segment Editor the Island tool to remove some not connected, small part. You can clean it manually with the Scissor tool or play with the Smoothing tool.</p>

---

## Post #8 by @Vineet_Saravanan (2023-08-14 15:47 UTC)

<p>Is it possible to do this task with the NvidiaAIAssistedAnnotation plugin?</p>

---

## Post #9 by @Reasat_E_Noor (2024-04-03 12:35 UTC)

<p>I segmented blood vessel from MRI brain image and created an stl model of a bifurcated artery. I uploaded the 3d stl model in Ansys fluent for analysing the blood flow but while meshing the program shows error. How to solve the issue?</p>

---
