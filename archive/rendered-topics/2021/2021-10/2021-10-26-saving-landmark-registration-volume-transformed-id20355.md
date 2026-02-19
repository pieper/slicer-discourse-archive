---
topic_id: 20355
title: "Saving Landmark Registration Volume Transformed"
date: 2021-10-26
url: https://discourse.slicer.org/t/20355
---

# Saving landmark registration volume transformed

**Topic ID**: 20355
**Date**: 2021-10-26
**URL**: https://discourse.slicer.org/t/saving-landmark-registration-volume-transformed/20355

---

## Post #1 by @lolamartinalonso (2021-10-26 08:24 UTC)

<p>Operating system:64 bit<br>
Slicer version: 4.11.20210226<br>
Expected behavior: Open the transformed volume after landmark registration and see changes<br>
Actual behavior:</p>
<p>I am applying some landmark registration to my volume. And at the third raw I am able to see how the volume changes when I apply them. So then I click on save and I save this last volum transformed as a .nrrd file but when I open on Fiji, I can´t see any changes comparing with the original volume.</p>
<p>Do I have to make another process to obtain the volume?<br>
Maybe I have seen, some people than apply a Resample Image (BRAINS), but it´s also taking too much time.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/885c7f85ca9d9f641728ddd3005b7570ee47ac4e.jpeg" data-download-href="/uploads/short-url/jsj6XLrtQT9e2IUQhlNKC3EieBg.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/885c7f85ca9d9f641728ddd3005b7570ee47ac4e_2_690x375.jpeg" alt="image" data-base62-sha1="jsj6XLrtQT9e2IUQhlNKC3EieBg" width="690" height="375" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/885c7f85ca9d9f641728ddd3005b7570ee47ac4e_2_690x375.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/885c7f85ca9d9f641728ddd3005b7570ee47ac4e_2_1035x562.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/885c7f85ca9d9f641728ddd3005b7570ee47ac4e_2_1380x750.jpeg 2x" data-dominant-color="AEAFBE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1045 180 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @muratmaga (2021-10-26 14:33 UTC)

<p>Yes, Fiji ignores the orientation matrix written to the file after hardening.<br>
İf you want to use Fiji, you will have to resample. Or you can tell us what you want to do and we might be able to suggest alternatives in Slicer.</p>

---

## Post #3 by @lolamartinalonso (2021-10-26 14:51 UTC)

<p>Perfect, now I understand. With the resampling it seems good on Fiji.</p>
<p>But I have another question, because to compare the volumes I click on Center Volumes, so it´s easier to compare them. But is it applied only on 3D Slicer? Or when I open the volume that I obtain after registering and resampling on Fiji, this centering is also applied?</p>
<p>Thanks in advance</p>

---

## Post #4 by @muratmaga (2021-10-26 16:05 UTC)

<p>Yes, I believe all metadata about image orientation is ignored in Fiji.</p>

---
