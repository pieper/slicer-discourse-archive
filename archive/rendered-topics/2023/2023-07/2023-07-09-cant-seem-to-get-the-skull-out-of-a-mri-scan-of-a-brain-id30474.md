# Can't seem to get the skull out of a MRI scan of a brain

**Topic ID**: 30474
**Date**: 2023-07-09
**URL**: https://discourse.slicer.org/t/cant-seem-to-get-the-skull-out-of-a-mri-scan-of-a-brain/30474

---

## Post #1 by @Sander_Martens (2023-07-09 17:45 UTC)

<p>Hi, as a project I want to get a STL file from a skull, but when using my MRI scan I can’t seem to only get the skull. It’s either the whole head (with skin) or only the brain.</p>
<p>Could anyone help me with this issue?</p>

---

## Post #2 by @cpinter (2023-07-10 11:28 UTC)

<p>Are you asking about image segmentation? Can you describe <em>in detail</em> what you tried already?</p>

---

## Post #3 by @Sander_Martens (2023-07-10 17:59 UTC)

<p>I tried using the Segment Editor and set a Threshold and tried different presets in the Volume Rendering module, but I have not been able to only show the skull. Each time I try it ends up looking something like this.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/2/52b449572b8bc3add4d608de15c1ab1259e4a0c4.jpeg" data-download-href="/uploads/short-url/bNDpHGZ0X7s5bwXPzYpDtpwstY8.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52b449572b8bc3add4d608de15c1ab1259e4a0c4_2_690x184.jpeg" alt="image" data-base62-sha1="bNDpHGZ0X7s5bwXPzYpDtpwstY8" width="690" height="184" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52b449572b8bc3add4d608de15c1ab1259e4a0c4_2_690x184.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52b449572b8bc3add4d608de15c1ab1259e4a0c4_2_1035x276.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/2/52b449572b8bc3add4d608de15c1ab1259e4a0c4_2_1380x368.jpeg 2x" data-dominant-color="413D43"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×512 65.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @rkikinis (2023-07-10 18:06 UTC)

<p>On MRI, you can see the bone as a black structure. Unfortunately, that is true for air and ligaments/tendons. Accordingly, you need to perform a significant amount of preparation on the data to get a partial skull rendering.</p>

---

## Post #5 by @Sander_Martens (2023-07-10 18:19 UTC)

<p>I see.</p>
<p>How would I go about achieving this? (I am fairly new to the program)</p>

---

## Post #6 by @pieper (2023-07-10 18:23 UTC)

<p>It’s not really about the program, it’s about the nature of CT vs MR scanning.  Bones like the skull are hard to image in MR compared to CT.</p>

---

## Post #7 by @Sander_Martens (2023-07-10 18:27 UTC)

<p>In that case it would be very hard (if not impossible) to be able to export the skull with this data?</p>
<p>aka not possible?</p>

---

## Post #8 by @pieper (2023-07-10 18:28 UTC)

<p>Right - with just the data you have it would be very hard to segment the skull.</p>

---

## Post #9 by @Sander_Martens (2023-07-10 18:29 UTC)

<p>I understand. Thank all of you for you help!</p>

---
