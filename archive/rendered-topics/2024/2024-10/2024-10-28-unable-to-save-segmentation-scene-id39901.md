---
topic_id: 39901
title: "Unable To Save Segmentation Scene"
date: 2024-10-28
url: https://discourse.slicer.org/t/39901
---

# Unable to save segmentation/scene

**Topic ID**: 39901
**Date**: 2024-10-28
**URL**: https://discourse.slicer.org/t/unable-to-save-segmentation-scene/39901

---

## Post #1 by @OwenProulx (2024-10-28 20:39 UTC)

<p>Hi all, marine biology student very new to slicer here. Been having this issue pop up when I try to save my scene to a folder on my PC. I’ve tried saving it to other folders to no avail. Would love some help!<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/573ad4a4f1d95e3d9754221f0c524e57f1bb5af5.png" data-download-href="/uploads/short-url/crFAcT3JA9TDqSNPWmQEYgUnv2R.png?dl=1" title="Screenshot 2024-10-27 214520" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/573ad4a4f1d95e3d9754221f0c524e57f1bb5af5_2_690x349.png" alt="Screenshot 2024-10-27 214520" data-base62-sha1="crFAcT3JA9TDqSNPWmQEYgUnv2R" width="690" height="349" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/7/573ad4a4f1d95e3d9754221f0c524e57f1bb5af5_2_690x349.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/573ad4a4f1d95e3d9754221f0c524e57f1bb5af5.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/7/573ad4a4f1d95e3d9754221f0c524e57f1bb5af5.png 2x" data-dominant-color="302D2B"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-10-27 214520</span><span class="informations">943×478 103 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75a2f65402d1eca29fcee1e33a8735b9facfecd9.png" data-download-href="/uploads/short-url/gMF0yxWwaBlK9qWq8swAdcemUFr.png?dl=1" title="Screenshot 2024-10-27 214541" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/5/75a2f65402d1eca29fcee1e33a8735b9facfecd9.png" alt="Screenshot 2024-10-27 214541" data-base62-sha1="gMF0yxWwaBlK9qWq8swAdcemUFr" width="501" height="236"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-10-27 214541</span><span class="informations">501×236 13 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2024-10-29 16:45 UTC)

<p>The only thing that occurs to me that you could try are</p>
<ol>
<li>Save to a folder the path of which does not contain special characters or spaces (like “Sand Lance 2”)</li>
<li>Save the scene as MRB (click on the gift box button on top of the save window)</li>
</ol>
<p>Unfortunately on Windows scene saving is not super robust, and since I don’t see in the screenshot the nodes that are saved with the scene (only the mrml file is checked but there are further nodes out of view), let’s start with some trivial things.</p>

---
