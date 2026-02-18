# Slicer will change the shape of the model?

**Topic ID**: 16962
**Date**: 2021-04-06
**URL**: https://discourse.slicer.org/t/slicer-will-change-the-shape-of-the-model/16962

---

## Post #1 by @slicer365 (2021-04-06 11:14 UTC)

<p>Dear friends!<br>
win<br>
slicer v4.11 0226<br>
I imported a blood vessel model into the software, and then imported it into the segmentation editor,do nothing, show 3D directly,the model as you see.It is not clear. The red is the primary one,the yellow is the new one.Without smoothing.<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/829f361cb34ceac55b96339868f3ba12798685ad.jpeg" data-download-href="/uploads/short-url/iDxb9KO4dyoY5DgPgaCShYDbrCR.jpeg?dl=1" title="捕获" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/829f361cb34ceac55b96339868f3ba12798685ad_2_690x344.jpeg" alt="捕获" data-base62-sha1="iDxb9KO4dyoY5DgPgaCShYDbrCR" width="690" height="344" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/829f361cb34ceac55b96339868f3ba12798685ad_2_690x344.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/8/829f361cb34ceac55b96339868f3ba12798685ad_2_1035x516.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/2/829f361cb34ceac55b96339868f3ba12798685ad.jpeg 2x" data-dominant-color="9F9EA3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">捕获</span><span class="informations">1338×668 130 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @pieper (2021-04-06 12:59 UTC)

<p>That’s not unexpected because converting from a surface model to a voxel volume is lossy operation.  You can increase the sampling resolution but it will never completely go away.  Some operations can be done on the surface model mesh directly but not all.</p>

---
