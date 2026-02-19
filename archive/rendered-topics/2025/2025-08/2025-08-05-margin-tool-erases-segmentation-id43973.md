---
topic_id: 43973
title: "Margin Tool Erases Segmentation"
date: 2025-08-05
url: https://discourse.slicer.org/t/43973
---

# Margin Tool Erases Segmentation

**Topic ID**: 43973
**Date**: 2025-08-05
**URL**: https://discourse.slicer.org/t/margin-tool-erases-segmentation/43973

---

## Post #1 by @jr2637 (2025-08-05 15:40 UTC)

<p>Hi, I am trying to grow my segment using the margin tool, but when I attempt to do so, the segment erases. How can I fix this?</p>
<p>Thank you!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/c/1c3bf75f11e87755695ade635aad2814d8c2113d.jpeg" data-download-href="/uploads/short-url/41LQtqFrlpSojb1WafW3bZHYiiF.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c3bf75f11e87755695ade635aad2814d8c2113d_2_690x388.jpeg" alt="image" data-base62-sha1="41LQtqFrlpSojb1WafW3bZHYiiF" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c3bf75f11e87755695ade635aad2814d8c2113d_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c3bf75f11e87755695ade635aad2814d8c2113d_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/c/1c3bf75f11e87755695ade635aad2814d8c2113d_2_1380x776.jpeg 2x" data-dominant-color="4F4F4D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 151 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/9/c91f2d693b996cf424240016cf8e26ce8df152c3.jpeg" data-download-href="/uploads/short-url/sHcLFht61mzC6ON8ODeBGRsRtbJ.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c91f2d693b996cf424240016cf8e26ce8df152c3_2_690x388.jpeg" alt="image" data-base62-sha1="sHcLFht61mzC6ON8ODeBGRsRtbJ" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c91f2d693b996cf424240016cf8e26ce8df152c3_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c91f2d693b996cf424240016cf8e26ce8df152c3_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/9/c91f2d693b996cf424240016cf8e26ce8df152c3_2_1380x776.jpeg 2x" data-dominant-color="4E4E4C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2025-08-05 15:57 UTC)

<p>Is this just a single slice?  You might need to replicate it to form a 3D volume is you want to use 3D operations.</p>

---

## Post #3 by @jr2637 (2025-08-06 15:15 UTC)

<p>Thanks for the reply! No, it is a 3d reconstruction with many slices.</p>
<p>-Jaime</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/07db49928173334d821594b3c678270cb83a8b31.jpeg" data-download-href="/uploads/short-url/17va7Y19mx5xTO5fHnTXRXJsNO1.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07db49928173334d821594b3c678270cb83a8b31_2_690x388.jpeg" alt="image" data-base62-sha1="17va7Y19mx5xTO5fHnTXRXJsNO1" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07db49928173334d821594b3c678270cb83a8b31_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07db49928173334d821594b3c678270cb83a8b31_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/07db49928173334d821594b3c678270cb83a8b31_2_1380x776.jpeg 2x" data-dominant-color="626371"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1080 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @pieper (2025-08-06 15:42 UTC)

<p>Check the logs for any messages and compare your data to sample data that works (i.e. check the information section of the Volumes module).</p>

---

## Post #5 by @jr2637 (2025-08-07 15:36 UTC)

<p>Thank you, I checked the logs and needed to clear space in my hard drive.</p>
<p>-Jaime</p>

---
