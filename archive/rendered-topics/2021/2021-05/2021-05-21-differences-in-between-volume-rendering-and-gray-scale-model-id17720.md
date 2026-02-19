---
topic_id: 17720
title: "Differences In Between Volume Rendering And Gray Scale Model"
date: 2021-05-21
url: https://discourse.slicer.org/t/17720
---

# Differences in between volume rendering and gray scale model in Registration

**Topic ID**: 17720
**Date**: 2021-05-21
**URL**: https://discourse.slicer.org/t/differences-in-between-volume-rendering-and-gray-scale-model-in-registration/17720

---

## Post #1 by @nayanw775 (2021-05-21 07:22 UTC)

<p>Operating system: Windows 10<br>
Slicer version:4.11<br>
Hello Slicer community,</p>
<p>I am unable to create accurate grey scale model so that its quality matches up to the standards of Volume rendering at the point of registration, somehow there is always a difference of 2-5mm in volume rendering and model after registration. I also tried to use the use shift value of the Volume rendering model to put it as a threshold(I don’t know if that are equal) assuming that they serve the same purpose, but that fails to create the accurate model. I tried by the segmentation method also by that is also not the one that we can use for the registration.<br>
Can you tell what changes should I make to accurately create the model.? I am using T1MPRAGE images.</p>

---

## Post #2 by @lassoan (2021-05-21 12:53 UTC)

<p>A surface mesh (closed surface representation of segmentation) will never be able to match what a dense 3D point cloud (volume rendering) can display.</p>
<p>If you want exact match between volume rendering and segmentation (or model) display then you need to dumb down the volume rendering to isosurface rendering by having a single step function as scalar opacity function. The step must go from 0 to 1 at the same X value that you use for thresholding in “Segment Editor” or “Grayscale model maker” module.</p>

---

## Post #3 by @nayanw775 (2021-05-22 07:46 UTC)

<p>Thank you <a class="mention" href="/u/lassoan">@lassoan</a> for your reply. I will try it and get back to you soon with the results</p>
<p>Regards<br>
Nayan</p>

---

## Post #4 by @nayanw775 (2021-12-17 06:24 UTC)

<p>Hello <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Is there a way to perform ICP registration without making a model, current method that is available for the ICP, is the fiducial model registration(in SlicerIGT), for the model making is the mandatory step,  but we want to perform the ICP on surface/volume rendering.<br>
What would be the correct way to proceed for it.</p>

---

## Post #5 by @lassoan (2021-12-17 21:39 UTC)

<p>ICP registration requires a mesh and a point cloud (or another mesh). Volume rendering does not provide a mesh (a solid surface): the depth where a point is placed when you click on volume-rendered image depends on the viewing angle. Therefore, you cannot use ICP to register a volume with a model.</p>
<p>You need to create a surface from the image (for example, using Segment Editor module) if you want to register an image with a volume using ICP method. However, there are other model-to-image registration methods that don’t require segmentation of the volume. You can ask on the <a href="https://discourse.itk.org/">ITK forum</a> for details.</p>

---

## Post #6 by @nayanw775 (2021-12-18 08:43 UTC)

<p>I do not know whether ITK would be the good platform to ask this question, but I will try to be more specific with my query.<br>
What current navigations systems are using for the registration procedures is the surface/volume rendering(IMO), for the ICP registration, but with the current IGT module we have to create a model, so the question that has stuck on my mind is the how they are doing the surface registration on the volume rendering(its not hollow as model usually is), I know I can create model from the segment editor module that seems to be a very hefty and lengthy process and we have to do it every time for each patients, here I am looking for the one solution for all. One method that I can think of is, use a Foreground masking options, create a mask or the output image that is also creating models, but this method is not creating good surface meshes. What else do you suggest as a work around for the  or is there way that we can create models that is not hollow.</p>

---

## Post #7 by @lassoan (2021-12-19 14:34 UTC)

<p>In Slicer/SlicerIGT you get a full toolbox of modules allows you to experiment with a wide range of patient registration tools (landmark registration, point to surface registration, surface scan based registration, tracked ultrasound-guided registration, 3D printed guide based registration, fiducial marker set based registration, etc.).</p>
<p>These modules expose many options, which of course makes things look complex and you need to do a lot of clicking: manually switch between modules, select inputs/outputs, etc. However, you only use this this GUI when you are designing and testing your workflow in the lab in your first phantom experiments. Usually once you know exactly what you want to do and how, you write up a small Python scripted module to automate all the steps that do not require user inputs. You can tune this script by performing further phantom/animal/cadaver experiments and when everything works as expected then you proceed to patients.</p>
<p>By using the general-purpose GUI of multiple modules it probably takes about 15 clicks to do a point-to-surface patient registration. With your scripted module it will probably take just 2 clicks (set the threshold for surface generation then click OK when the surface looks good) and then you can collect landmark points for point-to-point registration without any further mouse clicks (e.g., by detecting stationary stylus tip or pivot gesture). If you want you can collect further points for point-to-surface (ICP) registration by tracing the surface using the stylus, using a physical button on the stylus or some automated outlier rejection.</p>
<p>If you describe what you want to register (knee, hip, brain, liver, breast, etc.), imaging modality, and procedure (hip/knee replacement, neurosurgery, RF ablation, lumpectomy, etc.) you are interested in then we can give more specific advice.</p>

---

## Post #8 by @nayanw775 (2021-12-20 08:15 UTC)

<p>Thank Lasso for the detailed reply,</p>
<p>We are doing it for Neurosurgeries, and we have automated all the things, the thing we could not achieve is the good accuracy of surface registration with the model, whatever the threshold we set, it always has a large error, we have tried it multiple times, in our lab on phantom and also in the OT, error in the sense that, we can see the tip, going inside the dura, whose exact location has to be on the surface, we can not achieve good accuracy than, we have to skip surface registration due to the model issues and have to satisfy ourselves with the fiducial registration, which can be achieved on rendering itself.</p>
<p>Thanks<br>
Nayan</p>

---

## Post #9 by @mau_igna_06 (2021-12-20 16:39 UTC)

<p>Did you check if <a href="https://discourse.slicer.org/t/partial-surface-registration-tutorial/21118">Partial Surface Registration </a> is useful for you?</p>

---

## Post #10 by @lassoan (2021-12-21 05:50 UTC)

<p>There could be many reasons for registration inaccuracy. If you can attach a couple of images showing your surfaces and landmarks, and the resulting mismatched surface then it may give some clues.</p>
<p>Partial surface registration (register only those part pf the surface meshes that are near the region of interest) that <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a> recommended above could alleviate some of the problems (e.g., MRI distortion).</p>

---

## Post #11 by @nayanw775 (2021-12-22 04:38 UTC)

<p>Dear <a class="mention" href="/u/mau_igna_06">@mau_igna_06</a><br>
I went through the tutorial of your tools, I don’t think it is useful for me.</p>
<p>Thank you for the support.</p>

---

## Post #12 by @nayanw775 (2021-12-22 05:02 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a></p>
<p>Here I am attaching the images.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3f059066bc63dba2e7dd5a0f730aaa44d2419723.jpeg" data-download-href="/uploads/short-url/8Zw068TwtoCJ8xhROBHNxp53XXl.jpeg?dl=1" title="image2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f059066bc63dba2e7dd5a0f730aaa44d2419723_2_375x500.jpeg" alt="image2" data-base62-sha1="8Zw068TwtoCJ8xhROBHNxp53XXl" width="375" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f059066bc63dba2e7dd5a0f730aaa44d2419723_2_375x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f059066bc63dba2e7dd5a0f730aaa44d2419723_2_562x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/3f059066bc63dba2e7dd5a0f730aaa44d2419723_2_750x1000.jpeg 2x" data-dominant-color="6C6B71"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image2</span><span class="informations">960×1280 124 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4db8a828dc22321bc184fc0f131ad1239a87ba6c.jpeg" data-download-href="/uploads/short-url/b5yoe2ZMsBGOkvqVFN6eIA6K7AE.jpeg?dl=1" title="Image1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4db8a828dc22321bc184fc0f131ad1239a87ba6c_2_666x500.jpeg" alt="Image1" data-base62-sha1="b5yoe2ZMsBGOkvqVFN6eIA6K7AE" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4db8a828dc22321bc184fc0f131ad1239a87ba6c_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4db8a828dc22321bc184fc0f131ad1239a87ba6c_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/d/4db8a828dc22321bc184fc0f131ad1239a87ba6c.jpeg 2x" data-dominant-color="66696C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Image1</span><span class="informations">1280×960 133 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #13 by @lassoan (2021-12-22 13:45 UTC)

<p>With CT image of a phantom and optical tracking the total system error should be below 1mm.</p>
<p>For this, you need to get everything right. Just a few examples of what you need to pay attention to:</p>
<ul>
<li>use rigid tools: preferably use metal markers; if you use plastic markers then make sure they are not deformed during use (even 1mm displacement of a marker would ruin your entire system accuracy); 3D-printed plastic is OK but resin is not reliable (it slowly deforms)</li>
<li>use rigid marker mounting: use screws or hot glue to fix the tracking marker to the phantom and the stylus (tape, blu tack, etc. are not rigid enough)</li>
<li>marker design: make the marker larger for higher accuracy, have at least one marker out of plane (there are many other design guidelines for marker design, look them up in publications or your tracker’s documentation), make sure the marker balls are not damaged</li>
<li>stylus design: use sharp tip, place the marker as close as possible to the tip</li>
<li>stylus sharp tip, pivot on hard but non-slip material</li>
<li>position the camera so that markers are at optimal direction and distance from the tracking camera</li>
<li>pivot calibration: use rigid but non-slip surface, pivot in as much angle range as possible but make sure the marker can be tracked accurately in that range; the error should be less than 0.2 mm</li>
<li>landmark registration (between fiducial points marked on the image and on the physical phantom): collect 6-10 landmarks, distributed around all sides of the phantom; the RMS error should be less than 0.2mm.</li>
</ul>
<p>With Fiducials-model registration (ICP registration between the CT-derived surface and many points that you acquire with the stylus) you can further increase accuracy of the registration in the region where you acquire the many points, but only if the region contains high-curvature areas. If you only collected points  on the top or back of the head (a spherical shape) would completely throw off your registration.</p>

---

## Post #14 by @nayanw775 (2021-12-27 10:03 UTC)

<p>Until the fiducial registration with the rendering we are good, we do not get such large errors with that, but as soon as we switch to the surface registration part, which requires the model to collect the points, we get this kind of accuracy, so from our perception, problem lies in the model making rather than the registrations, we tried making the model using the shift function of the volume rendering, still we could not get good accuracy, rest all, we have managed to do as you have mentioned.<br>
Here is the one solution that I was thinking, can we convert dicom images directly into labelmap and then convert that labelmap directly into model, may be then we have to set the different parameters, to get the accurate surfaces, that we can manage, that would not be an issue.</p>

---

## Post #15 by @lassoan (2021-12-27 12:40 UTC)

<p>Please post a screenshot that shows the collected points on the surface and the registration module’s GUI after the registration is complete. It is even better if you can share the scene (save the scene as .mrb file, upload to OneDrive/dropbox/Google drive and post the link here).</p>

---
