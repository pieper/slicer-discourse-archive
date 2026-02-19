---
topic_id: 38288
title: "Resample Scalar Vector Dwi Volume Produces Weird Results"
date: 2024-09-09
url: https://discourse.slicer.org/t/38288
---

# Resample Scalar/Vector/DWI Volume produces weird results

**Topic ID**: 38288
**Date**: 2024-09-09
**URL**: https://discourse.slicer.org/t/resample-scalar-vector-dwi-volume-produces-weird-results/38288

---

## Post #1 by @koeglfryderyk (2024-09-09 09:14 UTC)

<p>I want to resample an image to spacing (1,1,1), origin (0,0,0), and direction 1,0,0,0,1,0,0,0,1.</p>
<p>I tried using the “Resample Scalar/Vector/DWI Volume” module.</p>
<p>I loaded a volume, set it as the input volume, and created a new output volume for the output.<br>
The only parameters I changed were Spacig, Size, Origin, and Direction Matrix in “Manual Output Parameters.”</p>
<p>The resampled image, however, doesn’t resemble the input image at all, as you can see in the screenshot (the resampled image is this small white segmentation-like object)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/2/d2f01be670ba85498492e04d5c1d86f04cba044e.jpeg" data-download-href="/uploads/short-url/u62Hov2jdQZul8SsHzM6WhBQVhY.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2f01be670ba85498492e04d5c1d86f04cba044e_2_542x500.jpeg" alt="image" data-base62-sha1="u62Hov2jdQZul8SsHzM6WhBQVhY" width="542" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2f01be670ba85498492e04d5c1d86f04cba044e_2_542x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2f01be670ba85498492e04d5c1d86f04cba044e_2_813x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/2/d2f01be670ba85498492e04d5c1d86f04cba044e_2_1084x1000.jpeg 2x" data-dominant-color="42424D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1756×1617 219 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Am I doing something wrong?</p>
<p>Here is the <a href="https://www.dropbox.com/scl/fi/bmhz8fd3q809o3789q7hl/image_to_resample.nii.gz?rlkey=0hq3lqxcww976d4qamlzloq7v&amp;st=de5yn9fz&amp;dl=0" rel="noopener nofollow ugc">link</a> to the volume that I’m uisng.</p>
<p>Stable Release 3D Slicer 5.6.2, Ubutu 22.04.4 LTS</p>

---

## Post #2 by @koeglfryderyk (2024-09-09 12:43 UTC)

<p>I also tried doing it in the Python console, as described <a href="https://discourse.slicer.org/t/resample-scalar-volumes-scripting-in-python/19736">here</a> but I also get strange results.</p>
<p>When I set those 4 parameters:</p>
<pre><code class="lang-auto">params["inputVolume"] = slicer.util.getFirstNodeByName("moving")
params["outputVolume"] = slicer.util.getFirstNodeByName("moving_2")
params["interpolationType"] = "linear"
params["outputImageSpacing"] = (1,1,1)
</code></pre>
<p>the resampling works.</p>
<p>When I add this parameter</p>
<pre><code class="lang-auto">params["outputImageOrigin"] = (0,0,0)
</code></pre>
<p>the resampling finishes, but the origin remains unchanged and those two messages appear around 25 times each:</p>
<pre><code class="lang-auto">[VTK] Input port 0 of algorithm vtkImageMapToWindowLevelColors (0x80bc240) has 0 connections but is not optional.
[VTK] Input port 0 of algorithm vtkImageThreshold (0x80a9230) has 0 connections but is not optional.
</code></pre>
<p><br>
When I remove the origin parameter and set the direction:</p>
<pre><code class="lang-auto">params["directionMatrix"] = (1,0,0,0,1,0,0,0,1)
</code></pre>
<p>the resampling finishes, the direction matrix is set correctly, but the entire image is now filled with 0s and the same VTK message appear</p>

---

## Post #3 by @pieper (2024-09-09 14:35 UTC)

<p>I’m not sure what is intended when you try to specify those parameters independently, but you could read the source code to see how they are used.</p>
<p>Typically you provide a reference volume to define the grid in which you want the input volume resampled.  That is, you can create a volume that has the origin, spacing, directions, and dimensions to cover the geometric extent you want to sample.  You can look at the CropVolume code to see how this is done.</p>

---

## Post #4 by @koeglfryderyk (2024-09-10 07:36 UTC)

<p>I have a fixed and moving volume, both with non-isotropic spacing and a non-identity direction matrix.</p>
<p>I’m using Slicer to perform a rigid registration of the moving to the fixed.</p>
<p>Then, I want to export both with isotropic spacing and identity direction matrix.</p>
<p>So once I have the fixed with those requirements, I can resample the moving onto the fixed like you described - but I can’t figure out how to process the fixed.</p>

---

## Post #5 by @pieper (2024-09-10 18:07 UTC)

<p>You can create an empty volume with isotropic spacing and identity directions with the origin and dimensions needed to enclose your fixed volume.  Then you can resample both fixed and moving using your empty volume as the reference geometry.</p>

---

## Post #6 by @lassoan (2024-09-10 18:35 UTC)

<p>You can also use the Crop volume module to create a new volume with isotropic spacing, with axis-aligned orientation.</p>

---
