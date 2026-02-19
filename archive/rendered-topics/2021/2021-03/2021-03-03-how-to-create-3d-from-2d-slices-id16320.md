---
topic_id: 16320
title: "How To Create 3D From 2D Slices"
date: 2021-03-03
url: https://discourse.slicer.org/t/16320
---

# How to create 3D from 2D slices?

**Topic ID**: 16320
**Date**: 2021-03-03
**URL**: https://discourse.slicer.org/t/how-to-create-3d-from-2d-slices/16320

---

## Post #1 by @Akeem_Azeez (2021-03-03 05:06 UTC)

<p>Operating system: MacOS<br>
Slicer version:4.11.20210226<br>
Expected behavior:<br>
Actual behavior:<br>
I want to reconstruct 10 2D images to 3D. I have tried MatLab but I am having difficulties interpolating the gaps in between the adjacent slices. A colleague told me to try Slicer but I don’t know how to navigate the app. Here is the link to the slices:<a href="https://www.dropbox.com/sh/1trxs9fy0btcbsa/AABJ_t-6-JLDXqtAPWU0jBQea?dl=0" class="inline-onebox" rel="noopener nofollow ugc">Dropbox - OCT_42_pix - Simplify your life</a><br>
I want to recreate a solid 3D. Thanks</p>

---

## Post #2 by @jcfr (2021-03-03 05:11 UTC)

<p>To help us understand the context, here are few additional questions:</p>
<ul>
<li>How were these images acquired ? <s>Are these “Optical Coherence Tomography” images ? </s>
</li>
<li><s>What should be the spacing in mm between slices ?</s></li>
<li>Is the plan to use 3d printing ? Do you expect to generate a surface model ?</li>
</ul>
<p>Edit: It looks like these images where generated using Matlab or similar ? It seems like you could use a different plotting function to generate a 3D representation.</p>
<p>For reference, here is one of the image you shared:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5bead243f1fa60135df423536a41b772d53c884.jpeg" data-download-href="/uploads/short-url/z3Xv9jhJGFUf4erYdGNDBHG3rG4.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f5bead243f1fa60135df423536a41b772d53c884_2_666x500.jpeg" alt="image" data-base62-sha1="z3Xv9jhJGFUf4erYdGNDBHG3rG4" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f5bead243f1fa60135df423536a41b772d53c884_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f5bead243f1fa60135df423536a41b772d53c884_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/5/f5bead243f1fa60135df423536a41b772d53c884.jpeg 2x" data-dominant-color="5050BB"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1120×840 112 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @Akeem_Azeez (2021-03-03 13:09 UTC)

<p>Hi,<br>
The images are acquired from OCT; after image processing, I have 10 (450x600 array) that was plotted on MatLab using the Imagesc function. Each slice represents a cross-section of a sample. My goal is to put the 10 slices together to reconstruct the surface of my sample.<br>
I want to interpolate one slice into another so as to create a surface model of the sample. I tried Matlab and what I got is in the attachment. Thank you, I appreciate your response.</p>
<p>Akeem</p>

---

## Post #4 by @lassoan (2021-03-03 14:58 UTC)

<p>You can load a stack of images as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html#load-a-series-of-png-jpeg-or-tiff-images-as-volume">here</a>, then remove the Matlab plot axes by using Crop volume.</p>
<p>You can then go to Data module and drag-and-drop the image to a 3D view to see it with volume rendering:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/7/47e7cbdf3b0549b773b088cb894642f02bb463d7.png" data-download-href="/uploads/short-url/ag6wlYfh9sUy0MT1EFeIkSEpQp1.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47e7cbdf3b0549b773b088cb894642f02bb463d7_2_690x419.png" alt="image" data-base62-sha1="ag6wlYfh9sUy0MT1EFeIkSEpQp1" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47e7cbdf3b0549b773b088cb894642f02bb463d7_2_690x419.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47e7cbdf3b0549b773b088cb894642f02bb463d7_2_1035x628.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/47e7cbdf3b0549b773b088cb894642f02bb463d7_2_1380x838.png 2x" data-dominant-color="838180"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">2255×1371 654 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>I would recommend to save the image array as nrrd (for example, using <a href="https://github.com/PerkLab/SlicerMatlabBridge/blob/master/MatlabCommander/commandserver/nrrdwrite.m">nrrdwrite.m</a>) instead of saving resampled, color-mapped screenshots.</p>

---

## Post #5 by @Akeem_Azeez (2021-03-03 18:08 UTC)

<p>Hi,<br>
I have followed the steps you recommended but how do I use the volume rendering to view the image. Kindly see the attached file for what I got after the drag and drop in the data module. Thanks</p>
<p>Akeem</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/920d578fa3425acfce64acc9b57cda7c7e62caa1.jpeg" data-download-href="/uploads/short-url/kQ2iliR7n8QUfYjeUEJY5fQA6xb.jpeg?dl=1" title="Screen Shot 2021-03-03 at 12.04.09 PM.jpg" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/920d578fa3425acfce64acc9b57cda7c7e62caa1_2_690x409.jpeg" alt="Screen Shot 2021-03-03 at 12.04.09 PM.jpg" data-base62-sha1="kQ2iliR7n8QUfYjeUEJY5fQA6xb" width="690" height="409" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/920d578fa3425acfce64acc9b57cda7c7e62caa1_2_690x409.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/920d578fa3425acfce64acc9b57cda7c7e62caa1_2_1035x613.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/9/920d578fa3425acfce64acc9b57cda7c7e62caa1_2_1380x818.jpeg 2x" data-dominant-color="7F8097"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-03-03 at 12.04.09 PM.jpg</span><span class="informations">2878×1708 517 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #6 by @Akeem_Azeez (2021-03-03 18:48 UTC)

<p>Yes, the images were reconstructed using Matlab. I tried using Matlab to generate a 3D representation but I am not able to view the interested surface. The images represent the cross-sections of a surface, I want to put them together to reconstruct the surface. This is what I got when I tried it on matlab. Surface plot is not working as well. Thanks for the response. <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4ff056091f063bf99aac9b99a21e52203fedd364.jpeg" data-download-href="/uploads/short-url/bpaDxPW1ToV7Oal6pgqJqo03i4Y.jpeg?dl=1" title="Screen Shot 2021-03-03 at 12.46.56 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ff056091f063bf99aac9b99a21e52203fedd364_2_355x500.jpeg" alt="Screen Shot 2021-03-03 at 12.46.56 PM" data-base62-sha1="bpaDxPW1ToV7Oal6pgqJqo03i4Y" width="355" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ff056091f063bf99aac9b99a21e52203fedd364_2_355x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ff056091f063bf99aac9b99a21e52203fedd364_2_532x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4ff056091f063bf99aac9b99a21e52203fedd364_2_710x1000.jpeg 2x" data-dominant-color="B8B8DD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-03-03 at 12.46.56 PM</span><span class="informations">1048×1474 199 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #7 by @lassoan (2021-03-03 19:11 UTC)

<p>You need to follow <em>all the steps</em> described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumes.html#load-a-series-of-png-jpeg-or-tiff-images-as-volume">here</a>, specifically:</p>
<ul>
<li>since you unnecessarily applied a color mapping to the image for plotting it in Matlab, you need to undo that using “Vector to scalar volume” module</li>
<li>since a bmp stack cannot store the image spacing, you need to specify the spacing between slices (third spacing value)</li>
</ul>
<p>These steps would not be necessary and all the information in the original images would have been better preserved if you loaded the original image into Slicer (e.g., from DICOM, NRRD, etc.) instead of trying to recover them from Matlab plots.</p>

---
