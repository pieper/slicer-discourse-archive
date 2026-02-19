---
topic_id: 35413
title: "Creat Smooth Model"
date: 2024-04-10
url: https://discourse.slicer.org/t/35413
---

# Creat smooth model

**Topic ID**: 35413
**Date**: 2024-04-10
**URL**: https://discourse.slicer.org/t/creat-smooth-model/35413

---

## Post #1 by @Slogish (2024-04-10 16:53 UTC)

<p>Hello!Friends!<br>
I am trying to measure the max curvature of the part of aorta.Why the max curvature in  the Tree centerline curve and the Network curve is so different?Which is accurate?<br>
Is there a way to make the centerline smoother?Because i think the curve is not very smooth,there are some hard turns on the curve,so that the curvature is not accurate.The curvature i measured was much larger than that in the paper.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/922f919b369a6024ba6acae4a41479687b203da0.png" data-download-href="/uploads/short-url/kRdCPyr4NoIxBtPbut4ldz2u4VO.png?dl=1" title="1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/922f919b369a6024ba6acae4a41479687b203da0_2_652x500.png" alt="1" data-base62-sha1="kRdCPyr4NoIxBtPbut4ldz2u4VO" width="652" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/2/922f919b369a6024ba6acae4a41479687b203da0_2_652x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/922f919b369a6024ba6acae4a41479687b203da0.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/2/922f919b369a6024ba6acae4a41479687b203da0.png 2x" data-dominant-color="9D9FD1"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1</span><span class="informations">771×591 18.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/7/a7b3973b398a206387d5423e1b53c4f117420b03.png" data-download-href="/uploads/short-url/nVyvyt3ekEnixa2MPDpio6XrVNF.png?dl=1" title="2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7b3973b398a206387d5423e1b53c4f117420b03_2_690x388.png" alt="2" data-base62-sha1="nVyvyt3ekEnixa2MPDpio6XrVNF" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7b3973b398a206387d5423e1b53c4f117420b03_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7b3973b398a206387d5423e1b53c4f117420b03_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/7/a7b3973b398a206387d5423e1b53c4f117420b03_2_1380x776.png 2x" data-dominant-color="BCBFE0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2</span><span class="informations">1920×1080 155 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66be60c4099ea5dc0e254b6598e22b105387df43.png" data-download-href="/uploads/short-url/eEUAgycNI49PkjBC2qxVZRha4uf.png?dl=1" title="3" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66be60c4099ea5dc0e254b6598e22b105387df43_2_690x388.png" alt="3" data-base62-sha1="eEUAgycNI49PkjBC2qxVZRha4uf" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66be60c4099ea5dc0e254b6598e22b105387df43_2_690x388.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66be60c4099ea5dc0e254b6598e22b105387df43_2_1035x582.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66be60c4099ea5dc0e254b6598e22b105387df43_2_1380x776.png 2x" data-dominant-color="BCBFE0"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">3</span><span class="informations">1920×1080 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
Pic 1 is a 3D image reconstructed with a manually Region of Interest<br>
Pic 2 is the Network curve and it’s max curvature<br>
Pic 3 is the Tree centerline curve and it’s max curvature<br>
THANKS!!!</p>

---
