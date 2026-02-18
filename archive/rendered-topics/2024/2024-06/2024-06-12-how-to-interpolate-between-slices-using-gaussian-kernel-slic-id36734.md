# How to Interpolate Between Slices Using Gaussian Kernel - SlicerITKUltrasound Module

**Topic ID**: 36734
**Date**: 2024-06-12
**URL**: https://discourse.slicer.org/t/how-to-interpolate-between-slices-using-gaussian-kernel-sliceritkultrasound-module/36734

---

## Post #1 by @valerie (2024-06-12 18:45 UTC)

<p>Hi,</p>
<p>I am trying to interpolate between the slices of my 3D volume. The desired interpolation method must be Gaussian Kernel weighted average. Upon my research online, there are lots of sources on Gaussian Kernel filtering and smoothing, but that is not what I am trying to achieve. The aim of my project is to reconstruct the kidney by stacking 2D ultrasound images and interpolating between slices to create a denser volume. During my research, I found this module in 3D slicer that relates to ultrasound imaging and has my desired interpolation methods (ITKGaussian, VTKGaussianKernel).</p><aside class="onebox allowlistedgeneric" data-onebox-src="https://www.kitware.com/3d-slicer-resamples-ultrasound-images/">
  <header class="source">
      <img src="https://www.kitware.com/main/wp-content/themes/kitwarean/assets/img/favicon/android-icon-192x192.png" class="site-icon" width="192" height="192">

      <a href="https://www.kitware.com/3d-slicer-resamples-ultrasound-images/" target="_blank" rel="noopener nofollow ugc">kitware.com</a>
  </header>

  <article class="onebox-body">
    <div class="aspect-image" style="--aspect-ratio:426/396;"><img src="https://www.kitware.com/main/wp-content/uploads/2017/01/slicer_dev_fig4.png" class="thumbnail" width="426" height="396"></div>

<h3><a href="https://www.kitware.com/3d-slicer-resamples-ultrasound-images/" target="_blank" rel="noopener nofollow ugc">3D Slicer Resamples Ultrasound Images</a></h3>

  <p>As a medical imaging modality, one of greatest strengths of ultrasound is its ability to inspect the body’s condition in real time. For decades, radiologists, physicians, and ultrasonographers have leveraged traditional two-dimensional (2D)...</p>


  </article>

  <div class="onebox-metadata">
    
    
  </div>

  <div style="clear: both"></div>
</aside>

<p>However, when I try to resample the 3D volume I created using ImageStacks, there is no image/volume displayed. I tried playing around with the settings and did get something, but not the full image I was hoping for. Does anyone know how to troubleshoot the settings in this module to get the desired volume?</p>
<p>Step 1: Stack 57 .jpg ultrasound images into 3D volume using ImageStacks.<br>
Step 2: Visualized volume using VolumeRendering.<br>
Step 3: Applied resampling methods using ScanConvertCurvilinearArray.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/3/b367ea68ab2c8a4d20d918223e15cccb88096b43.png" data-download-href="/uploads/short-url/pB66xtREeftAQzC96JN2qPcuLU7.png?dl=1" title="Default settings" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b367ea68ab2c8a4d20d918223e15cccb88096b43_2_690x377.png" alt="Default settings" data-base62-sha1="pB66xtREeftAQzC96JN2qPcuLU7" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b367ea68ab2c8a4d20d918223e15cccb88096b43_2_690x377.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b367ea68ab2c8a4d20d918223e15cccb88096b43_2_1035x565.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/3/b367ea68ab2c8a4d20d918223e15cccb88096b43_2_1380x754.png 2x" data-dominant-color="52535B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Default settings</span><span class="informations">2560×1400 235 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/e/fe5bbda1e7ba8eabcd87d47cf9580775c4bc1309.jpeg" data-download-href="/uploads/short-url/Ai9PwVSav46qfH8CTqDFYQijvkJ.jpeg?dl=1" title="Arbitrary settings" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe5bbda1e7ba8eabcd87d47cf9580775c4bc1309_2_690x377.jpeg" alt="Arbitrary settings" data-base62-sha1="Ai9PwVSav46qfH8CTqDFYQijvkJ" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe5bbda1e7ba8eabcd87d47cf9580775c4bc1309_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe5bbda1e7ba8eabcd87d47cf9580775c4bc1309_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/e/fe5bbda1e7ba8eabcd87d47cf9580775c4bc1309_2_1380x754.jpeg 2x" data-dominant-color="65666E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Arbitrary settings</span><span class="informations">2560×1400 332 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-06-16 18:54 UTC)

<p>If you use freehand ultrasound with tracking then you can use <code>Volume Reconstruction</code> module in <code>SlicerIGT</code> extension. You can use the “sticks” method for interpolation between slices.</p>
<p>If you have images acquired by a 4D ultrasound probe then you can use SlicerITKUltrasound extension for reconstructing 3D volumes. B-mode conversion is for creating B-mode voxel values from RF data, so you probably do not need this module. Scan conversion is for converting scanlines or slices into a 2D image fan or 3D volume. There are many variations for scan conversion (if your inputs are scanlines or slices, if your transducer slides, rotates, etc.), so I would recommend to check with ITK developers if the current modules support your data.</p>

---
