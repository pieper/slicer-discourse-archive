---
topic_id: 2531
title: "how to segment intact lumen and vessel wall in 3d slicer?"
date: 2018-04-06
url: https://discourse.slicer.org/t/2531
last_bumped: 2026-11-02T14:03:17.134Z
---

# how to segment intact lumen and vessel wall in 3d slicer?

**Topic ID**: 2531
**Date**: 2018-04-06
**URL**: https://discourse.slicer.org/t/how-to-segment-intact-lumen-and-vessel-wall-in-3d-slicer/2531

---

## Post #1 by @Bio_Medical (2018-04-06 21:28 UTC)

<p>I want to create lumen and plaque inside an arterial wall(similar to the structure in attached file).So it will be a hollow wall and lumen inside it(fixed,no spaces between them).How can i do it in slicer?<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b770646bbd6beb378bb1c569e617f5f290219516.jpeg" data-download-href="/uploads/short-url/qaMaW9kmKfqoZHRabobn8dMalBY.jpg?dl=1" title="computational_model_carotid_plaque" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b770646bbd6beb378bb1c569e617f5f290219516_2_303x500.jpg" alt="computational_model_carotid_plaque" data-base62-sha1="qaMaW9kmKfqoZHRabobn8dMalBY" width="303" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/b/b770646bbd6beb378bb1c569e617f5f290219516_2_303x500.jpg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b770646bbd6beb378bb1c569e617f5f290219516.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b770646bbd6beb378bb1c569e617f5f290219516.jpeg 2x" data-dominant-color="4B6E84"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">computational_model_carotid_plaque</span><span class="informations">447×737 60.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2018-04-06 21:31 UTC)

<p>To create vessel wall, use <a href="https://discourse.slicer.org/t/new-segment-editor-effect-for-creating-hollow-objects/2464">“Hollow” effect</a> in recent nightly version of Segment editor. If you import model or labelmap from other software then you need to import it into a Segmentation node. Let us know if you stuck at any point or you don’t get good enough quality segmentation.</p>

---

## Post #3 by @lassoan (2018-04-09 15:57 UTC)

<p>3 posts were split to a new topic: <a href="/t/running-recent-nightly-slicer-on-old-computers/2542">Running recent nightly Slicer on old computers</a></p>

---

## Post #4 by @brhoom (2018-04-07 10:49 UTC)

<p>Uninstall previous Slicer if found then remove Slicer configuration folder manually. Install Slicer. It should works.</p>
<p>To get the best result, resample your volume (using “Resample Scala Volume” module)to iso then resample to a higher resolution e.g. 0.06,0.06,0.06. Then use Hollow with the minimum shell thinness.</p>
<p>P.S:</p>
<ul>
<li>It is also useful if you provide more details e.g. your operating system and the error message.</li>
<li>Edit your post and reply to look more nice. If you don’t put effort to write your question, probably no one will put effort to write an answer.</li>
</ul>

---

## Post #5 by @liam26 (2026-05-27 17:28 UTC)

<p>Hi, I’m looking to make similar segmentations. What procedures and tools did you use? Thanks!</p>

---

## Post #6 by @chir.set (2026-05-27 19:09 UTC)

<p>You may use many modules like in this <a href="https://disk.yandex.com/i/Jemz9bGEhsxW1A" rel="noopener nofollow ugc">video</a>.</p>
<p>The arterial wall is not a CT structure, it’s too thin, even diseased ones. You can however estimate the wall’s location, based on contrast, lesions and known anatomical shape of an artery. It’s an estimation. If you need 100% accuracy, you’re out of luck, even opening the patient won’t help you, alive or dead.</p>
<p>The Shape module of the ExtraMarkups extensions allows you to draw a Tube of varying radius, with which you can draw the wall at best estimate. Then you can do many things.</p>
<p>Admittedly, I do that fast for reasons. If you want to go that way seriously, make a few months allowance to learn all  these tools. The benefit is lasting.</p>
<p>If you look towards AI, my bet is that’s it’s not ready yet for this kind of processing, maybe in 25 years, it will certainly mature; this does not mean it will be a sort of a new deity!</p>

---

## Post #7 by @mhouse (2026-11-02 06:50 UTC)

<p>It mainly depends on the parameters of the CT scan. Normally a CTA is done for this purpose and the native resolution in 2021 was already possible with 0,7mm, which is around 3 times of the regular thickness of the aortic wall. The slice thickness should be nearly the same so that you have nearly isometric voxels, without any resampling. To reduce motion artifacts the scan should be ECG triggered. This was done in 2021 without a so called deep learning post processing.</p>
<p>In the pictures the lumen at the descending aorta was segmented with <code>Local threshold</code>. This was made beginning of 2023 from the CTA 2021 with a GE scanner.</p>
<p>The blue segmentation was done with the venous sequence and the red one with the arterial sequence. The issue here is with the influence of the spine against the aortic wall.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7ac1e78b2c5374f4f8342f4fa1794ca0b89be85.jpeg" data-download-href="/uploads/short-url/sunMm5eG4UfS7JrUKwIV7BDwgOp.jpeg?dl=1" title="BWS-Aorta-Jct21m8" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7ac1e78b2c5374f4f8342f4fa1794ca0b89be85_2_639x500.jpeg" alt="BWS-Aorta-Jct21m8" data-base62-sha1="sunMm5eG4UfS7JrUKwIV7BDwgOp" width="639" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7ac1e78b2c5374f4f8342f4fa1794ca0b89be85_2_639x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/7/c7ac1e78b2c5374f4f8342f4fa1794ca0b89be85_2_958x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/7/c7ac1e78b2c5374f4f8342f4fa1794ca0b89be85.jpeg 2x" data-dominant-color="333F41"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">BWS-Aorta-Jct21m8</span><span class="informations">1178×921 341 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d1910156914f7ad699698baba761167617f5910.jpeg" data-download-href="/uploads/short-url/8IuOZU71ErnG27e49sAuoLsQouI.jpeg?dl=1" title="Aorta-BWS-Jct21-2c" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d1910156914f7ad699698baba761167617f5910_2_576x500.jpeg" alt="Aorta-BWS-Jct21-2c" data-base62-sha1="8IuOZU71ErnG27e49sAuoLsQouI" width="576" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d1910156914f7ad699698baba761167617f5910_2_576x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/d/3d1910156914f7ad699698baba761167617f5910_2_864x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/d/3d1910156914f7ad699698baba761167617f5910.jpeg 2x" data-dominant-color="381C18"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Aorta-BWS-Jct21-2c</span><span class="informations">1017×882 161 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @mhouse (2026-11-02 14:03 UTC)

<p>The last CCTA was even finer with 0,35 x 0,35 x 0,62mm. Normally I combine the segmentation with the volume rendering, so that it looks more natural.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/3/33e8a70b8db3c7a08431440dba4c60d082b99cc9.jpeg" data-download-href="/uploads/short-url/7pcO11xM3PnmK8uOF85USMjh7ex.jpeg?dl=1" title="Aorta-Spine-t11-10-ct26j-c8" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33e8a70b8db3c7a08431440dba4c60d082b99cc9_2_690x455.jpeg" alt="Aorta-Spine-t11-10-ct26j-c8" data-base62-sha1="7pcO11xM3PnmK8uOF85USMjh7ex" width="690" height="455" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33e8a70b8db3c7a08431440dba4c60d082b99cc9_2_690x455.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33e8a70b8db3c7a08431440dba4c60d082b99cc9_2_1035x682.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/3/33e8a70b8db3c7a08431440dba4c60d082b99cc9_2_1380x910.jpeg 2x" data-dominant-color="503D3E"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Aorta-Spine-t11-10-ct26j-c8</span><span class="informations">1920×1268 484 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/8/b895db15090b61745049861e0a2733025f17fcf9.jpeg" data-download-href="/uploads/short-url/qkUUZ3YuMcGoJaFEDD5hGpLXGqd.jpeg?dl=1" title="Aorta-Spine-ct26j-k2" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b895db15090b61745049861e0a2733025f17fcf9_2_690x455.jpeg" alt="Aorta-Spine-ct26j-k2" data-base62-sha1="qkUUZ3YuMcGoJaFEDD5hGpLXGqd" width="690" height="455" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b895db15090b61745049861e0a2733025f17fcf9_2_690x455.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b895db15090b61745049861e0a2733025f17fcf9_2_1035x682.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/8/b895db15090b61745049861e0a2733025f17fcf9_2_1380x910.jpeg 2x" data-dominant-color="453223"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Aorta-Spine-ct26j-k2</span><span class="informations">1920×1268 821 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
