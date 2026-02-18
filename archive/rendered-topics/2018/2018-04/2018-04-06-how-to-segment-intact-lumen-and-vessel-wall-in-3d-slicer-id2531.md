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
