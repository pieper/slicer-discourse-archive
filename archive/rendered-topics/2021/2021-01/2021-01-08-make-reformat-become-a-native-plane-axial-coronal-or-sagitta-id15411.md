---
topic_id: 15411
title: "Make Reformat Become A Native Plane Axial Coronal Or Sagitta"
date: 2021-01-08
url: https://discourse.slicer.org/t/15411
---

# Make reformat become a native plane (axial, coronal or sagittal)

**Topic ID**: 15411
**Date**: 2021-01-08
**URL**: https://discourse.slicer.org/t/make-reformat-become-a-native-plane-axial-coronal-or-sagittal/15411

---

## Post #1 by @Masteling (2021-01-08 20:04 UTC)

<p>I have a collection of Ultrasound files in .l3d format that I converted to .mhd and .raw.</p>
<p>When converting the .l3d files I have automated the changes in image spacing (because of scaling) and have applied transforms so that the axial, coronal, sagittal views align with the MRI conventions.<br>
When I load the ultrasound while I see the axial in the red, it is called “Reformat”.<br>
Is there a way to make the “Reformat” in the red to become “Axial” and so on?</p>
<p>This is the code I use for the transform:</p>
<p>sliceNodeR = slicer.app.layoutManager().sliceWidget(‘Red’).mrmlSliceNode()<br>
sliceToRasR = sliceNodeR.GetSliceToRAS()<br>
transformR=vtk.vtkTransform()<br>
transformR.RotateX(90)<br>
transformR.RotateY(90)<br>
transformR.RotateZ(180)<br>
sliceToRasR.DeepCopy(transformR.GetMatrix())<br>
sliceNodeR.UpdateMatrices()</p>
<p>This is relevant because my goal is to image fusion between the ultrasound and MRI.</p>
<p>Currently, when I load both the MRI and ultrasound of the same subject the transforms that I apply to the ultrasound disappear.</p>
<p>Thank you for your help.</p>

---

## Post #2 by @lassoan (2021-01-08 20:39 UTC)

<p>“Reformat” just means that image plane is not aligned with any of the patient axes. You can safely ignore it and enable display of an orientation marker in the slice view to make sure you know what it refers to.</p>
<p>Your ultrasound and MRI images do not appear at the same place because they are too far from each other. You can show them in the same place by centering both(using Center Volume button in Volumes Volumes module / Volume Information section) or quickly align them by an approximate landmark registration using <a href="https://slicer.readthedocs.io/en/latest/user_guide/registration.html#semi-automatic-registration">Fiducial Registration Wizard</a>.</p>

---

## Post #3 by @lassoan (2021-01-08 21:01 UTC)

<p>What organs do you want to register?</p>
<p>Prostate US/MRI registration (and for any other registration where you can segment the structure of interest and it deforms smoothly) you can use <a href="https://github.com/SlicerRt/SegmentRegistration">Segment Registration extension</a>. There are many other registration tools, depending on what anatomical parts you want to fuse and what your requirements are.</p>

---

## Post #4 by @Masteling (2021-01-08 22:25 UTC)

<p>Great! Thank you for the quick response.</p>
<p>Our region of interest is the female pelvic floor.<br>
I am using the Prostate MRI-US Contour Propagation using the urethra as the volume of interest.</p>
<p>I removed the transforms from the US and in this case, the red shows the axial MRI and the sagittal US. The anatomical axial of the US is actually the sagittal view.</p>
<p>I made the segmentations in both using the axial image (axial for MRI, sagittal for the US).<br>
The segmentation works in the sense it aligns the 2 axial views. However, it does not do what I would like.</p>
<p>I think due to my initial different alignments in the US, I end up with the axial MRI aligned with the sagittal US.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b85e7a714646cff1637a7dd82ca0e4de9aaab9ed.jpeg" data-download-href="/uploads/short-url/qj0gWP6A9gDs0MttQyt4Fk4W3E1.jpeg?dl=1" title="slicer_registration_issue" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b85e7a714646cff1637a7dd82ca0e4de9aaab9ed_2_508x500.jpeg" alt="slicer_registration_issue" data-base62-sha1="qj0gWP6A9gDs0MttQyt4Fk4W3E1" width="508" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b85e7a714646cff1637a7dd82ca0e4de9aaab9ed_2_508x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b85e7a714646cff1637a7dd82ca0e4de9aaab9ed_2_762x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b85e7a714646cff1637a7dd82ca0e4de9aaab9ed_2_1016x1000.jpeg 2x" data-dominant-color="7F808F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_registration_issue</span><span class="informations">1104×1086 121 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I tried applying my initial transforms to the US but that did not help (basically it rotates my image 90 degrees)</p>
<p>Do you have any suggestions for this issue?</p>

---

## Post #5 by @lassoan (2021-01-09 04:23 UTC)

<p>For approximate reorienting of a volume, I would recommend to use data module to apply a transform then use interactive editing in 3D view. It allows you to quickly rotate and move the transform anywhere in 3D. You can also use Fiducial registration wizard for quick pre-alignment before registration. For more details, see Transforms module documentation: <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#apply-transform-to-a-node">apply transform</a>,  <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#modify-transform">modify transform</a>. After you have positioned the image where you wanted, <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#harden-transform-on-a-node">harden the transform on the image</a>.</p>

---

## Post #6 by @Masteling (2021-01-11 15:28 UTC)

<p>Thanks for the suggestions. It worked for me by doing the following:</p>
<ol>
<li>Open the MRI and US file in the same scene</li>
<li>Remove the “Reformat” planes from the US</li>
<li>Create a new linear transform to the US volume</li>
<li>Harden the transform</li>
</ol>
<p>Now I don’t have any “reformat” planes, which allows me to use the Prostate MRI-US Contour Propagation.</p>

---
