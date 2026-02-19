---
topic_id: 23617
title: "Slice Thickness For Multi Frame Ultrasound"
date: 2022-05-27
url: https://discourse.slicer.org/t/23617
---

# Slice Thickness for multi-frame ultrasound

**Topic ID**: 23617
**Date**: 2022-05-27
**URL**: https://discourse.slicer.org/t/slice-thickness-for-multi-frame-ultrasound/23617

---

## Post #1 by @svesal (2022-05-27 22:49 UTC)

<p>Hi,</p>
<p>I am just new to 3D slicer and I wanted to ask one question. I have a set of raw ultrasound data (cineloop) and I have the pixel spacing information (0.03x0.03) and not slice thickness for volumetric reconstruction. It seems the voxels are not isotropic, so when I reconstruct the volume the sagittal view is prefect (with pixel spacing of (0.03x0.03.0x0.03)) but the axial and coronal plane looks not correct (compressed, thin).</p>
<p>I wanted to ask, how I can compute the slice thickness (z-axis) if I have only pixel-spacing info for x and y axes?</p>
<p>Thank you,<br>
Best,</p>

---

## Post #2 by @lassoan (2022-05-27 23:29 UTC)

<p>Was the image series acquired by sliding the transducer on the patient’s body?</p>
<p>Was a position tracker used to record accurate pose of the transducer for each image slice?</p>

---

## Post #3 by @svesal (2022-05-28 00:18 UTC)

<p>Hi Lasso,</p>
<p>The ultrasound images acquired using side-fire probe! these are micro-ultrasound images similar to transrectal ultrasound after inserting the probe into rectum to capture prostate gland images.</p>
<p>The pose information is not there, since we had only processed RF data.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e3301ec52cfb084c06bee9f73bd651340267d69.jpeg" data-download-href="/uploads/short-url/khX5cutnwiQVQZABfjLgSFkpRjz.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8e3301ec52cfb084c06bee9f73bd651340267d69_2_690x465.jpeg" alt="image" data-base62-sha1="khX5cutnwiQVQZABfjLgSFkpRjz" width="690" height="465" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8e3301ec52cfb084c06bee9f73bd651340267d69_2_690x465.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8e3301ec52cfb084c06bee9f73bd651340267d69_2_1035x697.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/8e3301ec52cfb084c06bee9f73bd651340267d69_2_1380x930.jpeg 2x" data-dominant-color="363642"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1886×1271 114 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #4 by @lassoan (2022-05-28 00:30 UTC)

<p>Which imaging system is this? A commercial device or a custom-built research tool?</p>
<p>Was the probe rotated or translated during acquisition? Was it moved by a motor or just freehand?</p>
<p>Is the <code>image position patient</code> and <code>image orientation patient</code> tags are set correctly for each frame?</p>

---
