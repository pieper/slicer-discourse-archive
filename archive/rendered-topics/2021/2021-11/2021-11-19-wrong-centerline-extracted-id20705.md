# Wrong centerline extracted

**Topic ID**: 20705
**Date**: 2021-11-19
**URL**: https://discourse.slicer.org/t/wrong-centerline-extracted/20705

---

## Post #1 by @Francesca_Pittoni (2021-11-19 17:23 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/f/2ff4fdd9c65908706376942c104d25c3d210c91b.jpeg" data-download-href="/uploads/short-url/6QfkEPsuioDF4L6d2otuJK5hM8z.jpeg?dl=1" title="centerl" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ff4fdd9c65908706376942c104d25c3d210c91b_2_690x388.jpeg" alt="centerl" data-base62-sha1="6QfkEPsuioDF4L6d2otuJK5hM8z" width="690" height="388" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ff4fdd9c65908706376942c104d25c3d210c91b_2_690x388.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ff4fdd9c65908706376942c104d25c3d210c91b_2_1035x582.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/2/2ff4fdd9c65908706376942c104d25c3d210c91b_2_1380x776.jpeg 2x" data-dominant-color="B2B6D3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">centerl</span><span class="informations">1920×1080 257 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Hi,<br>
I’m trying to extract the centerline of this piece of aorta, but this is my result.<br>
I followed all the steps of the tutorial on youtube (<a href="https://youtu.be/caEuwJ7pCWs" class="inline-onebox" rel="noopener nofollow ugc">Vessel segmentation and centerline extraction using 3D Slicer and VMTK - YouTube</a>)…</p>

---

## Post #2 by @chir.set (2021-11-19 19:44 UTC)

<p>I usually find ‘Fill holes’ of ‘Smoothing’ effect useful in these cases. You should try different kernel sizes, as per hole sizes and segment size. Inspect your model throughout.</p>

---
