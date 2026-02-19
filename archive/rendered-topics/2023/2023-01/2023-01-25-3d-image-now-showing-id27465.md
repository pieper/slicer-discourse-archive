---
topic_id: 27465
title: "3D Image Now Showing"
date: 2023-01-25
url: https://discourse.slicer.org/t/27465
---

# 3d image now showing

**Topic ID**: 27465
**Date**: 2023-01-25
**URL**: https://discourse.slicer.org/t/3d-image-now-showing/27465

---

## Post #1 by @Biomed321 (2023-01-25 17:46 UTC)

<p>Operating system: 3dslicer<br>
Slicer version: 5.2.1 and 5.0.3<br>
Expected behavior: to produce a 3d image<br>
Actual behavior: not producing 3d image</p>
<p>So I have CT scans of hearts however I can only see the 2d pictures after growing seeds. When trying to initialise a 3d image should show up on 4th screen (top right) however it remains blank. I am using dcm files.</p>
<p>Do I need different extensions? And where do I find them?</p>
<p>Please help <img src="https://emoji.discourse-cdn.com/twitter/frowning.png?v=12" title=":frowning:" class="emoji" alt=":frowning:" loading="lazy" width="20" height="20"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/0/60128296e48c4f0b34c4348f4f64eba05c175b6d.jpeg" data-download-href="/uploads/short-url/dHTuGoSpDrO0An4D3Hqqt3PMym1.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60128296e48c4f0b34c4348f4f64eba05c175b6d_2_666x500.jpeg" alt="image" data-base62-sha1="dHTuGoSpDrO0An4D3Hqqt3PMym1" width="666" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60128296e48c4f0b34c4348f4f64eba05c175b6d_2_666x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60128296e48c4f0b34c4348f4f64eba05c175b6d_2_999x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/0/60128296e48c4f0b34c4348f4f64eba05c175b6d_2_1332x1000.jpeg 2x" data-dominant-color="817F7A"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">4032×3024 2.48 MB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-01-25 20:06 UTC)

<p>You (or one of the modules that you used) switched to the <code>Four-Up Plot</code> layout, which does not contain a 3D view (just slice views and a plot view).</p>
<p>You can switch to the <code>Four-Up</code> layout using the toolbar to get a view layout that shows 3 slice views and a 3D view.</p>

---

## Post #3 by @Matthew_Pontell (2025-07-29 23:55 UTC)

<p>Hello, I am having trouble generating a 3d image from my DICOM file. When I upload the DICOM file  I get the error “Image slices are not equally spaced” but then the axial and reformats will show in four up layout. I click the volume rendering module, open the eye and select the 3d center button but nothing shows up. I have tried the demo MRI and the 3d image will show. Any assistance would be much appreciated.</p>

---

## Post #4 by @pieper (2025-07-30 16:22 UTC)

<p>Yes, this is probably not obvious: when there are irregular spacings Slicer creates a nonlinear “acquisition transform” which isn’t handled by volume rendering.  For now you need to <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#harden-transform-on-a-node">harden the transform</a> for volume rendering.</p>

---
