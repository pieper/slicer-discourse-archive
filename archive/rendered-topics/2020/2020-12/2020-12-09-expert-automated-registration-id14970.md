---
topic_id: 14970
title: "Expert Automated Registration"
date: 2020-12-09
url: https://discourse.slicer.org/t/14970
---

# Expert automated registration

**Topic ID**: 14970
**Date**: 2020-12-09
**URL**: https://discourse.slicer.org/t/expert-automated-registration/14970

---

## Post #1 by @HodaGH (2020-12-09 20:18 UTC)

<p>Hi everyone,</p>
<p>I’m working on a project about registration of MR and CT images of pelvis. The only module that works for me without providing initial manual transformation is Expert Automated module which registers when the CT is the fixed Volume and MR is the moving. When I put MR as the fixed volume not only I don’t get an alignment but also the field of view changes. I’m attaching the result of both. I need to know what is the reason and how do I know which parameters and in which way should I change them to improve my results? I appreciate any help.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/e/ded91bcb075f88f676911fa68b2d6f00aeb4e75a.jpeg" data-download-href="/uploads/short-url/vNp9nYx4aTRKpOLYaRJeLlsTYOC.jpeg?dl=1" title="Screen Shot 2020-12-09 at 3.09.10 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ded91bcb075f88f676911fa68b2d6f00aeb4e75a_2_533x500.jpeg" alt="Screen Shot 2020-12-09 at 3.09.10 PM" data-base62-sha1="vNp9nYx4aTRKpOLYaRJeLlsTYOC" width="533" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ded91bcb075f88f676911fa68b2d6f00aeb4e75a_2_533x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ded91bcb075f88f676911fa68b2d6f00aeb4e75a_2_799x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/ded91bcb075f88f676911fa68b2d6f00aeb4e75a_2_1066x1000.jpeg 2x" data-dominant-color="7E7E82"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-12-09 at 3.09.10 PM</span><span class="informations">1282×1202 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/1/31056398f5e409ca4e95cde11d96a2b999352498.jpeg" data-download-href="/uploads/short-url/6ZEWpdwqpW2oXbQ9Coe96Z1ysME.jpeg?dl=1" title="Screen Shot 2020-12-09 at 3.13.21 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31056398f5e409ca4e95cde11d96a2b999352498_2_591x500.jpeg" alt="Screen Shot 2020-12-09 at 3.13.21 PM" data-base62-sha1="6ZEWpdwqpW2oXbQ9Coe96Z1ysME" width="591" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31056398f5e409ca4e95cde11d96a2b999352498_2_591x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31056398f5e409ca4e95cde11d96a2b999352498_2_886x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/31056398f5e409ca4e95cde11d96a2b999352498_2_1182x1000.jpeg 2x" data-dominant-color="404043"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-12-09 at 3.13.21 PM</span><span class="informations">1420×1200 338 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2020-12-09 22:20 UTC)

<p>Expert automated registration is a very basic registration method, which require extensive parameter tuning. I would recommend to use SlicerElastix extension instead. Its default registration presets work without the need for any parameter adjustments. See more information <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html">here</a>.</p>

---

## Post #3 by @HodaGH (2020-12-15 16:20 UTC)

<p>Thanks very much for your reply. I have tried Elastix and Brainsfit but no luck. I get this line in my Errorlog: Stop condition from optimizer.RegularStepGradientDescentOptimizerv4: Step too small after 481 iterations. Current step (0.00078125) is less than minimum step (0.001).<br>
Does this mean that the optimization is stuck in an extrema ?</p>
<p>By comparing the volumes in the slicer I see that the coronal and sagittal views need a simple translation but the axial views seem flipped or very far away to me (please find attached the picture). I have tried transforming the right/left axes in the transform matrix of Transform module and also centering the volumes but the registration still does not work.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/4/d43a7d04fba5ae864fde33f6df2d9f5a6ad1f1ae.jpeg" data-download-href="/uploads/short-url/uhsx8treL4AvOgAG2GqMHj04LE2.jpeg?dl=1" title="Screen Shot 2020-12-15 at 10.23.13 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d43a7d04fba5ae864fde33f6df2d9f5a6ad1f1ae_2_582x500.jpeg" alt="Screen Shot 2020-12-15 at 10.23.13 AM" data-base62-sha1="uhsx8treL4AvOgAG2GqMHj04LE2" width="582" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d43a7d04fba5ae864fde33f6df2d9f5a6ad1f1ae_2_582x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d43a7d04fba5ae864fde33f6df2d9f5a6ad1f1ae_2_873x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/d/d43a7d04fba5ae864fde33f6df2d9f5a6ad1f1ae_2_1164x1000.jpeg 2x" data-dominant-color="333131"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-12-15 at 10.23.13 AM</span><span class="informations">1564×1342 429 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Is there any way to do changes on the axial view only? like rebuilding or flipping the slices?</p>
<p>When I do manual transform I have to put the Inferior Superior scroll bar of translation on -206.0000mm to be able to match the geometry. Does this distant seem out of reach for the registration algorithms to work ?</p>

---

## Post #4 by @lassoan (2020-12-15 16:25 UTC)

<aside class="quote no-group" data-username="HodaGH" data-post="3" data-topic="14970">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/858c86/48.png" class="avatar"> HodaGH:</div>
<blockquote>
<p>Errorlog: Stop condition from optimizer.RegularStepGradientDescentOptimizerv4: Step too small after 481 iterations. Current step (0.00078125) is less than minimum step (0.001).<br>
Does this mean that the optimization is stuck in an extrema ?</p>
</blockquote>
</aside>
<p>It is good, it means that the solution converged. It might not have been the global optimum, though.</p>
<p>Brainsfit requires parameter tuning, so I would recommend to start with Elastix.</p>
<aside class="quote no-group" data-username="HodaGH" data-post="3" data-topic="14970">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/858c86/48.png" class="avatar"> HodaGH:</div>
<blockquote>
<p>By comparing the volumes in the slicer I see that the coronal and sagittal views need a simple translation but the axial views seem flipped or very far away to me</p>
</blockquote>
</aside>
<p>For all automatic intensity-based image registration you need to prealign the images, to have not more than a 5-10 mm and 5-10 degrees error. You can use landmark registration for this. Make sure to harden the transform on the images before you start the automatic registration.</p>

---

## Post #5 by @HodaGH (2020-12-18 09:35 UTC)

<p>Your comments are amazing Andras, thank you for your time.</p>
<p>I wonder if it’s possible to change the sequence of slices so that when the registration puts the images together the axial view would also match up? for example if the axial view now shows me 159th slide when I fit the image to the window, I would like it to show me the 39th slide first on top.</p>
<p>Also trying other methods to be able to compare for my thesis, I have a model of the pelvis in the CT image which I would like to register on the MRI image. In the FAQ page of registration mentions that “You can run surface and image registrations separately and then combine the transforms”. I’m not sure if I understand correctly! does this mean  first to make a model out of the MRI image (which I found not easy) and do the surface registration with the CT model. Second do the registration between CT and MRI images and finally combine the transform of these two steps ?</p>

---

## Post #6 by @lassoan (2020-12-19 06:44 UTC)

<p>Slicer does not rely on order of slices, it only matters where the slices are mapped in the physical space (using IJKToRAS transform). If you want to make sure that two volumes have the same geometry (same IJK voxel is located at the same physical RAS position) then you can use “Resample scalar/vector/DWI volume” module and use one volume as reference to resample the other volume.</p>
<p>Bone segmentation on MRI is hard, so probably you don’t want to do surface registration.</p>

---

## Post #7 by @HodaGH (2021-01-13 23:45 UTC)

<p>Greetings,</p>
<p>I applied gradient anisotropic diffusion to both CT and MRI of one of the patients and I got the perfect automatic registration via Elastix for when MRI was the fixed image and CT moving. I inverted the transform and applied manually to CT and got the perfect registration however when I do this with Elastix on fixed CT I don’t get the right transform.  What could be the reason for this and is there a way to tune it?</p>
<p>As gradient anisotropic diffusion was successful for automatic registration I would like to use fuzzy edge detection on CT and MRIs to be able to help other registrations that Elastix doesn’t work. For that I need to do the edge detection on the individual slices in Matlab but looking at the MatlabBridge tutorial it uses voxels in the matlab file for further codings. I’m confused on how to get to pixels(on individual slices) for edge detection and again back to voxel for slicer to view the images. I appreciate if you can guide me on this. Thank you.</p>

---

## Post #8 by @lassoan (2021-01-14 02:30 UTC)

<aside class="quote no-group" data-username="HodaGH" data-post="7" data-topic="14970">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/858c86/48.png" class="avatar"> HodaGH:</div>
<blockquote>
<p>Elastix on fixed CT I don’t get the right transform. What could be the reason for this and is there a way to tune it?</p>
</blockquote>
</aside>
<p>There could be many reasons. Asymmetric extent (one image is larger than the other), number of samples, voxel size, etc.</p>
<aside class="quote no-group" data-username="HodaGH" data-post="7" data-topic="14970">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/858c86/48.png" class="avatar"> HodaGH:</div>
<blockquote>
<p>when I do this with Elastix on fixed CT I don’t get the right transform</p>
</blockquote>
</aside>
<p>In general, you need both the forward and inverse transform, so it does not matter what direction you compute. If image resampling time is an issue (resampling an image takes longer time if the inverse transform needs to be computed) then you can precompute and store the inverse transform in a grid transform.</p>
<aside class="quote no-group" data-username="HodaGH" data-post="7" data-topic="14970">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/858c86/48.png" class="avatar"> HodaGH:</div>
<blockquote>
<p>As gradient anisotropic diffusion was successful for automatic registration I would like to use fuzzy edge detection on CT and MRIs to be able to help other registrations that Elastix doesn’t work</p>
</blockquote>
</aside>
<p>I would not recommend applying any additional preprocessing, unless it is absolutely unavoidable. It makes the registration time longer, introduces several new variables and overall increases complexity of the algorithm and so the uncertainty of the end result.</p>

---

## Post #9 by @HodaGH (2021-02-09 07:19 UTC)

<p>Hi Andras,</p>
<p>I cropped CT and MRI’s to exclude extra darkness in the MRIs and also the table from CT images. At the same time made voxels isotropic and increased spacing scale (in CropVolume module) in both modalities so that image dimensions and voxel sizes get close together. Doing these changes, finally rigid registration with Elastix was successful. I experimented with many isotropic voxel sizes between CT and MRI to find this optimum registration. But I have pelvis CT and MRI’s of other patients(with original same voxel sizes and dimensions only better contrasts) that just register with no manipulation needed so I want to optimize registration parameters for images that need manipulation to get registered but I don’t know how to interpret the above trick in terms of registration parameters! Would you give me a hint on this?</p>
<p>To try other ways, I masked the pelvis area to give as ROI to Elastix but it wasn’t successful as cropping the images. Shouldn’t masking and cropping give the same result?</p>

---

## Post #10 by @lassoan (2021-02-10 03:42 UTC)

<p>Registration should not very sensitive to voxel size, because sampling is done in physical space and the sample is interpolated similarly how you interpolate when you resample the images before registration.</p>
<p>Cropping the images to approximately to the same region helps the registration for many reasons (helps automatic initial alignment, optimal center of rotation position, ensures image samples are taken from relevant regions). It is also very important to crop or mask any regions that are incorrect in any of the images (e.g., if an image has a black border than that border must be removed or masked).</p>
<p>Masking can help with suppressing irrelevant regions in the image, but does not have all the other benefits of cropping, so it is not a replacement of cropping. Masking is rather can be used in addition to cropping as a further refinement. For example, for cases when you cannot remove all irrelevant parts with a rectangular cropping region (e.g., you have removed a tumor from the center of the image or  some interventional tools are visible in one of the image then you can mask out those small regions inside the volume).</p>

---

## Post #11 by @HodaGH (2021-02-25 15:51 UTC)

<p>Hello,</p>
<p>The cropping and masking that works for my other image registrations don’t work on one of the CT/MRI pairs. I used Volume Rendering to see them relative to each other , they seem close together but I don’t really understand what’s wrong with them. I attach them here and appreciate if you could take a quick look.<br>
<a href="https://drive.google.com/drive/folders/1fTQKcpUgxNUJPwylsMNYcOr1rHotNbie?usp=sharing" class="onebox" target="_blank" rel="noopener nofollow ugc">https://drive.google.com/drive/folders/1fTQKcpUgxNUJPwylsMNYcOr1rHotNbie?usp=sharing</a></p>
<p>The scan order in CT is Axial and in MRI is Coronal.  Can this difference make a problem?</p>
<p>Every time I perform the registration with slightly different cropping or voxel sizes I get a different transformation matrix but the result looks the same to my eyes. How can I explain this?</p>

---

## Post #12 by @lassoan (2021-02-25 18:06 UTC)

<p>Rigid registration of these data sets work well, using SlicerElastix:</p>
<ul>
<li>Prealign the volumes (for example, you can use 3 landmark points and SlicerIGT extension’s Fiducial Registration wizard module)</li>
<li>Define a ROI that contains the common region between the CT and MRI</li>
<li>Crop the CT and the MRI using this common ROI using Crop volume module (you will have a cropped MRI and cropped CT)</li>
<li>Apply bias field correction to the cropped MRI (slightly improves the end result)</li>
<li>Register the cropped CT with the cropped bias-corrected MRI using SlicerElastix, using “generic rigid (all)” preset</li>
</ul>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bac504f9291c605fd3e4e9a3af4622df9c18d52.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bac504f9291c605fd3e4e9a3af4622df9c18d52.mp4">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/b/1bac504f9291c605fd3e4e9a3af4622df9c18d52.mp4</a>
    </source></video>
  </div><p></p>
<p>Deformable registration is challenging, maybe because of the large difference in rectal and bladder filling, but maybe further reducing the region of interest and tuning registration parameters could help.</p>

---

## Post #13 by @HodaGH (2021-04-25 16:25 UTC)

<p>Hi Andras,</p>
<p>Would you tell me how did you capture all the three views in this video? The screen capture module only allows individual slice views at a time. and in the layout toolbar I found side by side option which only has red and yellow slice views and not three.</p>
<p>Thanks so much.</p>

---

## Post #14 by @lassoan (2021-04-25 17:35 UTC)

<p>You can enable “Capture all views” option to capture all views.</p>

---

## Post #15 by @HodaGH (2021-04-25 19:27 UTC)

<p>Yes I tried that but the 3D view will also be included. I don’t want the 3D view in the video.</p>

---

## Post #16 by @lassoan (2021-04-25 21:24 UTC)

<p>There are several layouts where you can move the splitter between the 3D view and the slice views. Choose one of those and move the slider towards the 3D view until it disappears. You can also define a layout that contains only slice views.</p>

---

## Post #17 by @HodaGH (2021-06-04 20:09 UTC)

<p>Hi Andras,</p>
<p>Hope you’re doing well. I finally could find the automatic registration with Elastix using NMI and it doesn’t need cropping of images.<br>
Now I want to compare this result with other ways of registration i.e. fiducial + default elastix MI. I got expert identified landmarks for my images. when I use the rigid transform the RMS value is 5.7 for when the CT fiducials are in “From fiducials” menu but when I do the other way around RMS value will be 53. What could be wrong?<br>
Also going from rigid to similarity and warping the RMS value decreases. Should I choose warping because RMS value is smaller? and is this a good idea to compare this result with my automatic rigid registration to see if I needed a non-rigid registration after all?</p>

---

## Post #18 by @lassoan (2021-06-04 20:29 UTC)

<aside class="quote no-group" data-username="HodaGH" data-post="17" data-topic="14970">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/858c86/48.png" class="avatar"> HodaGH:</div>
<blockquote>
<p>I got expert identified landmarks for my images. when I use the rigid transform the RMS value is 5.7 for when the CT fiducials are in “From fiducials” menu but when I do the other way around RMS value will be 53. What could be wrong?</p>
</blockquote>
</aside>
<p>It is hard to guess what’s happening. The best would be if you could save the scene as mrb, upload it somewhere, and post the link here. Or at least attach a few screenshots</p>
<aside class="quote no-group" data-username="HodaGH" data-post="17" data-topic="14970">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/h/858c86/48.png" class="avatar"> HodaGH:</div>
<blockquote>
<p>Also going from rigid to similarity and warping the RMS value decreases. Should I choose warping because RMS value is smaller? and is this a good idea to compare this result with my automatic rigid registration to see if I needed a non-rigid registration after all?</p>
</blockquote>
</aside>
<p>If you register targets in soft tissues then warping registration is generally more appropriate and expected to result in smaller residual error reported by the fiducial registration module.</p>
<p>Target registration error can be computed by applying the computed transform to the ground truth fiducials of the moving image and compute RMS error with the ground truth fiducials of the fixed image.</p>

---

## Post #19 by @HodaGH (2021-06-29 23:27 UTC)

<p>Thank you. I learned from the registration case library how to assess the landmarks in relation to each other and it seems if there is symmetry between landmarks on the right and left the RMS value can’t be calculated very accurately so I deleted some of the landmarks. I did a Mutual Information registration with elastix after the fiducial registration so I need to add the transform parameters from the fiducial registration to the elastix parameters to be able to compare it with transform parameters from other techniques . I don’t know how to change the resulting transform from fiducial registration to the elastix format. would you tell me how to do it?</p>

---

## Post #20 by @lassoan (2021-07-09 04:40 UTC)

<p>Elastix typically computes a grid transform (it can output a custom linear and bspline transform, but we cannot import those reliably into Slicer), while you typically use fiducial registration to compute a linear transform or thin-plate spline transform. You don’t change the format of these transforms, but you can concatenate them (by applying and then hardening one transform on te other) and store them in a single transform node.</p>

---
