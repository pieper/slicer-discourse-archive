---
topic_id: 36852
title: "Only One Mr Slice Is Visible In The Image Viewer"
date: 2024-06-17
url: https://discourse.slicer.org/t/36852
---

# Only one MR slice is visible in the image viewer

**Topic ID**: 36852
**Date**: 2024-06-17
**URL**: https://discourse.slicer.org/t/only-one-mr-slice-is-visible-in-the-image-viewer/36852

---

## Post #1 by @3D_y_Salud (2024-06-17 21:08 UTC)

<p>Hi, I have been working in a 3D slicer based on tomographies and this is my first experience with a resonance. When trying to open the study, there is only one slice, the strange thing is that the series has 640 slices. Does anyone know why it doesn’t reconstruct the cuts correctly? There is no problem viewing the study from the DVD. Thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/935e275d40de6c68b9616c62eabd7113d6ca0500.jpeg" data-download-href="/uploads/short-url/l1FUwsFWBKaxQNqTR1ft4bedyAE.jpeg?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/935e275d40de6c68b9616c62eabd7113d6ca0500_2_690x422.jpeg" alt="1" data-base62-sha1="l1FUwsFWBKaxQNqTR1ft4bedyAE" width="690" height="422" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/935e275d40de6c68b9616c62eabd7113d6ca0500_2_690x422.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/3/935e275d40de6c68b9616c62eabd7113d6ca0500_2_1035x633.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/3/935e275d40de6c68b9616c62eabd7113d6ca0500.jpeg 2x" data-dominant-color="373743"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">1355×830 92.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06e6a3c310a2f49c95d83933d417801f5d9fb513.png" data-download-href="/uploads/short-url/Z30v6f11j1genw988kzIHgOGR5.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/6/06e6a3c310a2f49c95d83933d417801f5d9fb513.png" alt="2" data-base62-sha1="Z30v6f11j1genw988kzIHgOGR5" width="690" height="138" data-dominant-color="30373D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1328×267 15.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-06-17 21:20 UTC)

<p>The “3D” suggests that it is a 3D acquisition but the “dinamico” may indicate that it is a time sequence. Most likely it is actually both, i.e., a 3D + t = 4D image, because 640 slices is quite a lot. Storage of 4D images are standardized across vendors, so 3D Slicer probably does not recognize the fourth dimension in this acquisition and just loads it as a 2D + t image.</p>
<p>The fix is quite simple: you need to add the grouping DICOM tag to the <a href="https://github.com/fedorov/MultiVolumeImporter/blob/c8a37eb5e4f35b78ccc9287b298457a064c9d001/MultiVolumeImporterPlugin.py#L38-L59">list in Slicer’s MultiVolumeImporter module</a>. The DICOM tag that you need is the one that has the same value for all frames acquired at the same time point; while it has different value in all other time points. I can help figuring out which field is that if you can share an anonymized sample data set.</p>

---

## Post #3 by @3D_y_Salud (2024-06-18 17:06 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="36852">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>dinamico” may indicate that it is a time sequence. Most likely it is actually both, i.e., a 3D + t = 4D image, because 640 slices is quite a lot. Storage of 4D images are standardized across vendors, so 3D Slicer probably does not recognize the fourth dimension in this acquisition and just loads it as a 2D + t ima</p>
</blockquote>
</aside>
<p>Thank you very much for answering. I was trying to visualize it as you told me and I looked for information about the “multi volume importer” module. I came across this video: <a href="https://www.youtube.com/watch?v=zqZIx77Z4VI" rel="noopener nofollow ugc">https://www.youtube.com/watch?v=zqZIx77Z4VI</a><br>
That helped me visualize the animation, capture a moment of the animation and be able to segment it.</p>
<p>I share with you some captures from the dicom studio</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a719a2bb9ea62a3b888296ceed7285ee05f215a.png" data-download-href="/uploads/short-url/aCyIUQYHdYbxn8FMeFuPTLVXbcK.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/a/4a719a2bb9ea62a3b888296ceed7285ee05f215a.png" alt="imagen" data-base62-sha1="aCyIUQYHdYbxn8FMeFuPTLVXbcK" width="690" height="97" data-dominant-color="2A2A2A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">1270×180 8.87 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f7a60ffd322d9ff5e81d548118e9f7a5761eea9.png" data-download-href="/uploads/short-url/bl5UMazoqmLmhlt78HOzHyOM1RL.png?dl=1" title="imagen" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f7a60ffd322d9ff5e81d548118e9f7a5761eea9.png" alt="imagen" data-base62-sha1="bl5UMazoqmLmhlt78HOzHyOM1RL" width="690" height="100" data-dominant-color="2D3E4C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">imagen</span><span class="informations">1274×186 8.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This is the final result I got when capturing a frame from the studio.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b6fcdedcaeb405b5ee5e89d86bc3cf2ce268d2e.jpeg" data-download-href="/uploads/short-url/fkqD0zspUiBhQO68IgEWFFpq6xU.jpeg?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b6fcdedcaeb405b5ee5e89d86bc3cf2ce268d2e_2_689x427.jpeg" alt="3" data-base62-sha1="fkqD0zspUiBhQO68IgEWFFpq6xU" width="689" height="427" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b6fcdedcaeb405b5ee5e89d86bc3cf2ce268d2e_2_689x427.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/b/6b6fcdedcaeb405b5ee5e89d86bc3cf2ce268d2e_2_1033x640.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/b/6b6fcdedcaeb405b5ee5e89d86bc3cf2ce268d2e.jpeg 2x" data-dominant-color="4A494F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1299×804 142 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>It’s the result I was looking for! I see that it has few cuts but I understand that it is a peculiarity of the study carried out. If you think I could do this process in a better way, I would like you to let me know. thank you so much!</p>

---
