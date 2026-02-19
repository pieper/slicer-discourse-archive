---
topic_id: 45301
title: "Segmenting Of Mouse Ct 3D Dataset Using A Mouse Phantom"
date: 2025-12-01
url: https://discourse.slicer.org/t/45301
---

# segmenting of mouse CT 3D dataset using a mouse phantom. 

**Topic ID**: 45301
**Date**: 2025-12-01
**URL**: https://discourse.slicer.org/t/segmenting-of-mouse-ct-3d-dataset-using-a-mouse-phantom/45301

---

## Post #1 by @Ayman_Alshehabi (2025-12-01 21:32 UTC)

<p>Hey you guys,</p>
<p>im trying to segment 3D CT mouse data using the phantom developed by <a href="https://neuroimage.usc.edu/neuro/Digimouse_Download" class="inline-onebox" rel="noopener nofollow ugc">Digimouse_Download - Biomedical Imaging Group"</a> . I am having the difficulty to overlap the segmented phantom that i created with the mouse CT dataset in order to do a radiation dosimetry examination exmination. im new to 3D slicer and i require some guidance on how to do this. I would really appreciate some help. Thank you very much!!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06c89744c8edf33e04ae746d4f8ba3d2dd9785b8.png" data-download-href="/uploads/short-url/Y0CZdHjI26SXZZ4N8KTP7w13m0.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06c89744c8edf33e04ae746d4f8ba3d2dd9785b8_2_690x332.png" alt="image" data-base62-sha1="Y0CZdHjI26SXZZ4N8KTP7w13m0" width="690" height="332" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06c89744c8edf33e04ae746d4f8ba3d2dd9785b8_2_690x332.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06c89744c8edf33e04ae746d4f8ba3d2dd9785b8_2_1035x498.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/6/06c89744c8edf33e04ae746d4f8ba3d2dd9785b8_2_1380x664.png 2x" data-dominant-color="323438"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1877×904 55.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/8/c86868fa51308835b7b55f753c4cfc5c4ad8865c.jpeg" data-download-href="/uploads/short-url/sATbSDiscCFmb1UwRltWzH5EGu0.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c86868fa51308835b7b55f753c4cfc5c4ad8865c_2_690x314.jpeg" alt="image" data-base62-sha1="sATbSDiscCFmb1UwRltWzH5EGu0" width="690" height="314" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c86868fa51308835b7b55f753c4cfc5c4ad8865c_2_690x314.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c86868fa51308835b7b55f753c4cfc5c4ad8865c_2_1035x471.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/8/c86868fa51308835b7b55f753c4cfc5c4ad8865c_2_1380x628.jpeg 2x" data-dominant-color="3A3A3E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×875 280 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @cpinter (2025-12-02 09:56 UTC)

<p>It seems that you loaded the segmentation in one Slicer instance and then loaded the CT in another. How do they look if you load them together?</p>

---
