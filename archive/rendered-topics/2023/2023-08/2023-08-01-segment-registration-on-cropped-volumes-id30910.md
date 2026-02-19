---
topic_id: 30910
title: "Segment Registration On Cropped Volumes"
date: 2023-08-01
url: https://discourse.slicer.org/t/30910
---

# Segment registration on cropped volumes

**Topic ID**: 30910
**Date**: 2023-08-01
**URL**: https://discourse.slicer.org/t/segment-registration-on-cropped-volumes/30910

---

## Post #1 by @Malika (2023-08-01 15:27 UTC)

<p>Hi, I’m trying to register two volumes by segments with the help of Segment Registration. A fixed volume and the corresponding segmentation mask have more segments compared to a moving volume (19 vs 8). An issue arises when I select the same segment to register on in both volumes: it stretches the cropped (moving) volume and fits it to the whole fixed volume, even though the moving volume corresponds to a lower part of the fixed volume.</p>
<p>Please see the screenshots attached, where the bottom right picture is the fixed volume, bottom left is a registered moving volume, top left is the original moving volume and top right is a registered 3d model. How can I fix this?  Thank you.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/0/500a7bd3325e982e52e38ea369540322ccb24152.jpeg" data-download-href="/uploads/short-url/bq4EQAgXIIEpFNuNyfUSkNOFu0y.jpeg?dl=1" title="Screenshot from 2023-08-01 11-00-58" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/500a7bd3325e982e52e38ea369540322ccb24152_2_690x419.jpeg" alt="Screenshot from 2023-08-01 11-00-58" data-base62-sha1="bq4EQAgXIIEpFNuNyfUSkNOFu0y" width="690" height="419" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/500a7bd3325e982e52e38ea369540322ccb24152_2_690x419.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/500a7bd3325e982e52e38ea369540322ccb24152_2_1035x628.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/0/500a7bd3325e982e52e38ea369540322ccb24152_2_1380x838.jpeg 2x" data-dominant-color="9F9FA4"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot from 2023-08-01 11-00-58</span><span class="informations">3162×1924 747 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
