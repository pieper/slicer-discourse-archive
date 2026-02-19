---
topic_id: 12851
title: "Register Mri And Histology"
date: 2020-08-04
url: https://discourse.slicer.org/t/12851
---

# Register MRI and histology

**Topic ID**: 12851
**Date**: 2020-08-04
**URL**: https://discourse.slicer.org/t/register-mri-and-histology/12851

---

## Post #1 by @KatS (2020-08-04 13:56 UTC)

<p>Dear Slicer community,</p>
<p>I would like to register MRI to histology data to compare tumor volumes retrieved from MRI-segmentation with groundtruth.<br>
I have an isotropic T2w 3D (Image dimensions 100 200 120, Image spacing 0.1 0.1 0.1) and an image stack from lightsheet microscopy in nrrd format (image dimensions 2160 2560 472, Image spacing 1 1 1).<br>
As the dimensions are very different, automatic registration does not work (as expected).  I tried to resample the images with various modules, but am unable to find a way to bring the two datasets to similar dimensions and spacing.</p>
<ul>
<li>I installed the IASEM extension and am able to reduce the image dimensions of the histology image to match those of the T2w, but with that image spacing increases.</li>
<li>Using ResampleScalarVolume, I can bring the image spacing of the T2w to match that of the bin shrinked histology, but obviously the result is of not much use. It does not work the other way round either (i.e. bring the image spacing of the histology to match that of the T2w), as the resampling fails with an error (“can’t allocate enough memory”).</li>
</ul>
<p>Is there a way to downsample the histology images so that I can register my T2w to it?</p>

---

## Post #2 by @lassoan (2020-08-04 14:57 UTC)

<p>The main issue is that the image spacing of the microscopy image looks incorrect (2160 pixels x 1mm/pixel = 2.16 meters). You can type the correct spacing value in Volumes module’s Volume information section. After this, you can resample the image to approximately match the MRI image resolution (about 0.1mm, or maybe a bit smaller spacing, such as 0.05 or or 0.03, but as small as 0.01).</p>
<p>After this, registration could work, but MRI/histology registration is usually a hard problem. I would recommend to start registration with manually defined landmarks (for example, using Fiducial registration wizard module of SlicerIGT extension). It is always guaranteed to work, but it requires time and expertise, and it is limited in how many landmarks you can find and how accurately you can specify their position. So, you may want to use it as an initialization step and then refine it using automated methods.</p>
<p>We may give more specific advice if you post a few screenshots of your data set.</p>

---

## Post #3 by @KatS (2020-08-07 08:25 UTC)

<p>Thank you for the reply.<br>
The image spacing information of the microscopy image are indeed wrong. It should be 3.25 x 3.25 x 5 µm and I changed it in the Volumes module manually. I then resampled the image using ResampleScalar Volumes module to match the MRI image resolution as you suggested. This worked nicely.<br>
As the image dimensions of T2w and the microscopy image were then of course different, I followed the instructions in the User FAQ and used ResampleScalarVolumeDWIVolume module to resample the microscopy image again to match the T2w dimensions. This also worked nicely.<br>
Before I start with a fiducial based registration, I have a remaining question:<br>
If I put T2w in the Background and the resampled microscopy image in the foreground and put the fader to 0.5, the microscopy image is much smaller than the T2w. I think I’m missing something, but shouldn’t they appear roughly the same as dimensions and spacing now match?</p>
<p>Moreover, I’m not sure if the repeated resampling is a good idea. Is there a better way of doing it?</p>
<p>In case it helps to understand the issue, these are the volume information of my images:<br>
T2w:<br>
image dimensions: 100 x 200 x 120<br>
image spacing: 0.1 x 0.1 x 0.1 mm</p>
<p>microscopy:<br>
image dimensions: 2160 x 2560 x 472<br>
image spacing: 0.00325 x 0.00325 x 0.005 mm</p>
<p>microscopy after 1st resampling in ResampleScalarVolumes module:<br>
image dimensions: 70 x 83 x 24<br>
image spacing: 0.1 x 0.1 x 0.1 mm</p>
<p>microscopy after 2nd resampling in ResampleScalarVolumeDWIVolume module&gt;<br>
image dimensions: 100 x 200 x 120<br>
image spacing: 0.1 x 0.1 x 0.1 mm</p>

---

## Post #4 by @lassoan (2020-08-08 01:48 UTC)

<p>What is in your image? Prostate, breast,…? It may be normal that the extent of the histology image is much smaller than the MRI, because the resected tissue may be just a small piece of tissue relative to the whole imaged body part. Can you post a screenshot so that we can see what do you find suspicious?</p>
<p>Repeated resampling should be avoided (for example by just concatenating transforms and resample with the final composite transform), but first I would just focus on getting a full registration done and then optimize the workflow.</p>

---

## Post #5 by @KatS (2020-08-08 14:16 UTC)

<p>Sorry, I forgot to mention that I’m working on mouse brain images. It’s a 3D T2w covering the whole brain on the MRI side. For histology, brains were first cleared and then scanned with a lightsheet microscope to acquire Z-stacks with 5 µm step size and coverage of up to 2000 µm (not the whole brain, but a large part of it). LSM images were initially exported as .tif and converted to .nrrd in FIJI. The brain shrinks about 40% during the clearing procedure, but the general anatomy remains intact.<br>
The volume information of T2w and resampled microscopy image displayed in the Volumes module are exactly the same now. Therefore, I thought they should have the same size when displayed together in the viewer.<br>
Perhaps I misunderstand the logic behind the resampling procedure. Do the microscopy data need to be resampled in a way to account for the 40% shrinkage during clearing?<br>
If so, what would be the best way of doing it?<br>
Or isn’t this size differences a problem at all and would disappear with fiducial based-registration?</p>
<p>Attached is a screenshot showing T2w in the background and the double-resampled microscopy image in the foreground.<br>
(The cropped border on the left (i.e. right in radiological view) of the histology image occured during LSM-scanning and is present on the original image as well. It’s not a result of resampling.)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/068488604bff40cc100b03edf587d0bb80ee157c.jpeg" data-download-href="/uploads/short-url/VEOwkZZZuXdW474kGQCJi2jy1K.jpeg?dl=1" title="Overlay" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/068488604bff40cc100b03edf587d0bb80ee157c_2_690x417.jpeg" alt="Overlay" data-base62-sha1="VEOwkZZZuXdW474kGQCJi2jy1K" width="690" height="417" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/068488604bff40cc100b03edf587d0bb80ee157c_2_690x417.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/068488604bff40cc100b03edf587d0bb80ee157c_2_1035x625.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/0/068488604bff40cc100b03edf587d0bb80ee157c_2_1380x834.jpeg 2x" data-dominant-color="383838"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Overlay</span><span class="informations">2299×1392 183 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @timeanddoctor (2020-08-09 14:55 UTC)

<p>Why not input this tif files using slicer directly through “data”, and then you can modify the parameters in “volume” after “VectorToScalar”</p>

---

## Post #7 by @lassoan (2020-08-09 16:41 UTC)

<p>If the tissue shrinks that much then you need to use similarity or affine transform, which computes scale factor from the input points. Since there could be also significant non-linear warping, you may get better results by choosing warping transform.</p>
<p>The main challenge is how to find corresponding points between the images. There are a lot of papers about MRI/histology image registration, describing various techniques for getting point correspondences (using surgical dye, embedded fiducial markers, etc).</p>

---

## Post #8 by @KatS (2020-08-11 13:36 UTC)

<p>Thank you for your advice!</p>
<p>I now used the Fiducial Registration Wizard of the IGT Extension and obtained a good result with the warping transform option!</p>

---
