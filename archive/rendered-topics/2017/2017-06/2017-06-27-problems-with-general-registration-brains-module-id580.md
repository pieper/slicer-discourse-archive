# Problems with General Registration (BRAINS) module

**Topic ID**: 580
**Date**: 2017-06-27
**URL**: https://discourse.slicer.org/t/problems-with-general-registration-brains-module/580

---

## Post #1 by @LGG (2017-06-27 16:01 UTC)

<p>Hi everyone,</p>
<p>I am having trouble with the alignment of different image-sets of one person. I have a DWI, a T1 anatomical MRI and TMS-Data which I all want to align.<br>
Now I can’t even chose the DWI as a fixed or moving image and I don’t understand why. I can only chose the T1-MRI and the TMS-Data. When aligning TMS with T1 they are obviously not aligned at all (which they were - theoretically - before alignment since the TMS-Data takes the T1-images as registration basis). Now I want to align those two images to use the TMS-points as a labelmap and combine them with a specific brain region-labelmap taken out of the T1-MRI. Because without that, I think it does not understand them as labelmaps for Tractography Seeding (because it won’t do a tracking).</p>
<p>I am thankful for any help!</p>

---

## Post #2 by @yannick_s (2017-06-29 12:40 UTC)

<p>Hi Lioba,</p>
<p>I think the DWI volume cannot be directly registered to e.g. a T1 in Slicer, you have to use the baseline (B0) image for this.</p>
<p>To create the baseline image from your DWI volume, you need the SlicerDMRI extension. If you don’t have SlicerDMRI  installed, you can do so through the Extensions Manager.</p>
<p>You can get the baseline volume using the “Diffusion Brain Masking” module (Diffusion → Process → Diffusion Brain Masking):<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b88621b61e3b27db8ab24e607cbc1c4a8f41adac.png" alt="image" data-base62-sha1="qknehygpVzEsGuWhhJfh4gT2s1u" width="577" height="313"></p>
<p>Now you should be able to register the baseline volume to e.g. your anatomical T1 and use the transform for your original DWI volume.</p>

---

## Post #3 by @LGG (2017-06-30 11:26 UTC)

<p>Hi Yannick!</p>
<p>Thank you for your reply! I did the Brain Masking already, and the registration with it worked. Thanks! Do you maybe know why? <img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=5" title=":slight_smile:" class="emoji" alt=":slight_smile:"></p>
<p>Lioba</p>

---

## Post #4 by @yannick_s (2017-06-30 12:22 UTC)

<p>Hi Lioba,</p>
<p>Great <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=12" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:" loading="lazy" width="20" height="20"><br>
The anatomical T1 is an image volume with a single scalar per voxel (the “gray value”). For DWI, you need the information for each gradient direction and baseline, and this is stored as a vector per voxel. Like a volume for each gradient direction/baseline stacked together.</p>
<p>The registration algorithm tries to align two images by some objective function and therefore would have to compare a single scalar to a vector for a given voxel for a DWI ↔ scalar volume registration. Since there are many different types of vector image volumes (e.g. color images (3 components if it’s RGB), DTI (9 components), DWI, …), there is no general rule how a registration method should compare a vector to a single scalar.</p>
<p>If you extract the baseline volume (just one scalar per voxel), you can perform the registration as if you would when you have e.g. a T1 and T2 image. Since the baseline volume is an image taking into account tissue signals and contrasts without diffusion gradients, the “regular” registration methods work.</p>
<p>You can check how many scalars per voxel you have for a given image volume in the “Volumes” module at the “Number of Scalars” entry (43 scalars in this example):</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/1X/529a5020dc7a88acac6589bf9aa1add6fb104f8d.png" width="186" height="28"></p>

---

## Post #5 by @LGG (2017-07-03 07:05 UTC)

<p>Aaah, wow thanks Yannick, now I understand!</p>

---
