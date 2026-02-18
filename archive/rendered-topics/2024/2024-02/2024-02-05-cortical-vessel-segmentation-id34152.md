# Cortical vessel segmentation

**Topic ID**: 34152
**Date**: 2024-02-05
**URL**: https://discourse.slicer.org/t/cortical-vessel-segmentation/34152

---

## Post #1 by @anja_pantovic (2024-02-05 13:09 UTC)

<p>Hello,<br>
I am trying to segment cortical vessels fro gadolinium enhanced t1 MRI images. I tried using local thresholding as well as vessleness filtering, however, scalp and even white matter interfere with the segmentation.</p>
<p>I don’t know how to get a clean segmentation of vessels and I think the vessels are visible enough in the images, as given below.<br>
Do you have any suggestions on what could help?</p>
<p>Thanks!<br>
Anja</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1cc78f4c1f16e9f6eac74c0e3c735e8f4f56dd94.jpeg" data-download-href="/uploads/short-url/46AVhLrrO5WLaJkSBr5lWZomX64.jpeg?dl=1" title="Screenshot 2024-02-05 at 14.08.38" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cc78f4c1f16e9f6eac74c0e3c735e8f4f56dd94_2_605x500.jpeg" alt="Screenshot 2024-02-05 at 14.08.38" data-base62-sha1="46AVhLrrO5WLaJkSBr5lWZomX64" width="605" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cc78f4c1f16e9f6eac74c0e3c735e8f4f56dd94_2_605x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cc78f4c1f16e9f6eac74c0e3c735e8f4f56dd94_2_907x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1cc78f4c1f16e9f6eac74c0e3c735e8f4f56dd94_2_1210x1000.jpeg 2x" data-dominant-color="3A3A3A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-02-05 at 14.08.38</span><span class="informations">1308×1080 62.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2024-02-05 13:46 UTC)

<p>That’s a hard problem and I don’t think there’s anything automated.   Eventually there will be a deep learning solution I’m sure.  If you don’t find anything you could try training something using MONAI Label or nnU-Net.</p>

---

## Post #3 by @kopachini (2024-02-07 05:01 UTC)

<p>The best approach is manual segmentation, or if you want to speed up, do a treshold and then manual corrections (used with treshold settings also) but it won’t work for small structures.</p>

---

## Post #4 by @dokay1 (2024-02-07 17:37 UTC)

<p>If you have good quality T1-pre images (without motion) using the same protocol, doing subtraction of T1post - T1pre can give you the vasculature map and then you can clean that up as needed.</p>

---
