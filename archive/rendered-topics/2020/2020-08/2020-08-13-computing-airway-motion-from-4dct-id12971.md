# Computing airway motion from 4DCT

**Topic ID**: 12971
**Date**: 2020-08-13
**URL**: https://discourse.slicer.org/t/computing-airway-motion-from-4dct/12971

---

## Post #1 by @mc_barbour (2020-08-13 05:41 UTC)

<p>Hi, I’m attempting to compute the motion of a pediatric airway from 4DCT images. Eventually, I’d like to use the displacement fields to control the motion/location of the segmented airway surface in a moving mesh CFD simulation. I’ve been attempting to perform a b-spline registration with the  Sequence Registration module, but with limited success: the displacement vectors are not capturing the airway motion. I believe the issue is that the motion i’m trying to capture is very small wrt the entire image - 95% of my image remains in place and only the airway walls are moving. I’ve been playing with the registration parameters but haven’t found a combination that works yet. My questions are:</p>
<ol>
<li>Is this Sequence Registration Module the right approach for what I want to do?</li>
<li>What parameters should I be adjusting to make sure the registration captures motion in a small area? So far I’ve made the GridSpacing equal to a single voxel and attempted to use every point in the optimization/cost function instead of a random selection (This is obviously brute force and unfortunately exceeded the memory of my laptop).</li>
<li>Is it possible to provide a mask before performing the registration, or crop the full image? I know you can use a mask with Elastix but it doesn’t look like it’s an option inside Slicer.</li>
</ol>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/5/053ed2530450b6ae57352593fd719f8cc27d426d.png" data-download-href="/uploads/short-url/KoYSFL1dUkRL0T1K5OwYMmwDuJ.png?dl=1" title="Screen Shot 2020-08-12 at 3.56.53 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/053ed2530450b6ae57352593fd719f8cc27d426d_2_690x171.png" alt="Screen Shot 2020-08-12 at 3.56.53 PM" data-base62-sha1="KoYSFL1dUkRL0T1K5OwYMmwDuJ" width="690" height="171" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/053ed2530450b6ae57352593fd719f8cc27d426d_2_690x171.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/053ed2530450b6ae57352593fd719f8cc27d426d_2_1035x256.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/5/053ed2530450b6ae57352593fd719f8cc27d426d_2_1380x342.png 2x" data-dominant-color="848483"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-08-12 at 3.56.53 PM</span><span class="informations">2310×574 349 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Operating system:Mac OS Catalina<br>
Slicer version: 4.10.2</p>

---

## Post #2 by @lassoan (2020-08-13 12:58 UTC)

<aside class="quote no-group" data-username="mc_barbour" data-post="1" data-topic="12971">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d9b06d/48.png" class="avatar"> mc_barbour:</div>
<blockquote>
<p>Is this Sequence Registration Module the right approach for what I want to do?</p>
</blockquote>
</aside>
<p>Yes, SequenceRegistration extension should be able to nicely do this, providing a 3D displacement field changing in time.</p>
<aside class="quote no-group" data-username="mc_barbour" data-post="1" data-topic="12971">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d9b06d/48.png" class="avatar"> mc_barbour:</div>
<blockquote>
<p>What parameters should I be adjusting to make sure the registration captures motion in a small area? So far I’ve made the GridSpacing equal to a single voxel and attempted to use every point in the optimization/cost function instead of a random selection (This is obviously brute force and unfortunately exceeded the memory of my laptop).</p>
</blockquote>
</aside>
<p>The default generic registration preset should work. Setting grid spacing to a single voxel would make the registration very unstable and tremendously slow, so don’t do it.</p>
<aside class="quote no-group" data-username="mc_barbour" data-post="1" data-topic="12971">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d9b06d/48.png" class="avatar"> mc_barbour:</div>
<blockquote>
<p>Is it possible to provide a mask before performing the registration, or crop the full image? I know you can use a mask with Elastix but it doesn’t look like it’s an option inside Slicer.</p>
</blockquote>
</aside>
<p>As with all intensity-based image registration tasks, you need to crop the volume to the minimum necessary region, with a small margin. The computed displacement field then can be applied to the entire image.</p>
<p>After cropping, masking is very rarely necessary. It is only useful if you want to exclude a small but very prominent object from the registration, such as a fiducial marker, implant, or surgical tool. Trying to exclude larger regions using masking (instead of cropping) leads to slowdowns and problems in random image sampling. Masking option is available in SlicerElastix module, so you can experiment with it there (between two selected frames). Masking is not yet exposed on Sequence Registration module GUI, as it is so rarely needed, but if you confirm that you need it (registration does not work without it, and works well if you use it) then we can add it.</p>

---

## Post #3 by @mc_barbour (2020-08-14 23:36 UTC)

<p>Thanks for the responses. After cropping the volume, the displacement fields and mapped images look much more reasonable.</p>
<p>I’d now like to compute/interpolate the displacement values to specific control points on a surface mesh (to start, having the displacement at every surface mesh node should work). After reading around in the support section, it seems this is pretty straightforward (<a href="https://discourse.slicer.org/t/registration-deformation-export/5197/20" class="inline-onebox">Registration Deformation Export</a>). I’m assuming that I can import the full sequence of displacement fields, and compute an array of displacements at each mesh point and then export in vtk? I’d also like to do this in the python environment. Can you point me in the right direction of the functions or documentation for this?</p>
<p>Also, just confirming that each displacement vector is computed wrt to the first/reference image and not the previous image?</p>

---

## Post #4 by @lassoan (2020-08-15 03:41 UTC)

<aside class="quote no-group" data-username="mc_barbour" data-post="3" data-topic="12971">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d9b06d/48.png" class="avatar"> mc_barbour:</div>
<blockquote>
<p>I’d now like to compute/interpolate the displacement values to specific control points on a surface mesh (to start, having the displacement at every surface mesh node should work). After reading around in the support section, it seems this is pretty straightforward</p>
</blockquote>
</aside>
<p>Yes, it is straightforward. You can apply the computed transforms to any node - model (surface mesh), markups (point list, curve), image, etc.</p>
<aside class="quote no-group" data-username="mc_barbour" data-post="3" data-topic="12971">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d9b06d/48.png" class="avatar"> mc_barbour:</div>
<blockquote>
<p>I’d also like to do this in the python environment.</p>
</blockquote>
</aside>
<p>All features of Slicer are available in Python. You just need to run the scripts in the Python environment provided by Slicer.</p>
<aside class="quote no-group" data-username="mc_barbour" data-post="3" data-topic="12971">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d9b06d/48.png" class="avatar"> mc_barbour:</div>
<blockquote>
<p>Also, just confirming that each displacement vector is computed wrt to the first/reference image and not the previous image?</p>
</blockquote>
</aside>
<p>Yes, sequence registration module computes transformations to/from a chosen reference image.</p>
<aside class="quote no-group" data-username="mc_barbour" data-post="3" data-topic="12971">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/d9b06d/48.png" class="avatar"> mc_barbour:</div>
<blockquote>
<p>Can you point me in the right direction of the functions or documentation for this?</p>
</blockquote>
</aside>
<p>Everything should be fairly straightforward. For an introduction to using Slicer features from Python, you can check out <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">Slicer programming tutorials</a>.</p>

---

## Post #5 by @mc_barbour (2020-08-27 22:31 UTC)

<p>I’m running into issues extracting the displacement vector at the individual mesh locations, and I think it has to do with the fact that I’m trying to extract data from a sequence transform.</p>
<p>I’ve converted the Transform to a vector volume using the convert function in the Transform module. I use the original, unregistered MulitVolume sequence as the reference volume in the convert function. I’ve saved the displacement volume as .nrrd and re-loaded as a volumeSequence. I then use the Probe Volume with Model module to extract the displacement vector at each mesh point, but this only gives me a single scalar value at each point, not the vector. When I visualize the 3D slices, they are black and white and I can step through 3 displacement images which i assume are the three vector components. (If i was looking at a sequence of displacement vectors from the full sequence registration, there’d be many more time-steps). When i load the displacement image as a single volume, the slices display as multi-color images with 3 vector components at each point, but the volume does not show-up as an option to extract from in the Probe Volume with Model module. Thoughts?</p>
<p>I’d like to extract the displacement values from each timestep of the sequence transform. It seems that that convert and probe tools are only set-up for a single volume. I can loop through this process if that’s the case (once I can extract the vector displacement values at each point).</p>

---

## Post #6 by @lassoan (2020-09-02 16:58 UTC)

<p>Yes, you need to write a short Python script that iterates through the sequence. See for example how the <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/CropVolumeSequence/CropVolumeSequence.py">Crop volume sequence module</a>.</p>

---
