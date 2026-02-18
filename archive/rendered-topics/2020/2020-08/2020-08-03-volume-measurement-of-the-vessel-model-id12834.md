# Volume measurement of the vessel model

**Topic ID**: 12834
**Date**: 2020-08-03
**URL**: https://discourse.slicer.org/t/volume-measurement-of-the-vessel-model/12834

---

## Post #1 by @Andreas (2020-08-03 15:34 UTC)

<p>Hello,</p>
<p>I have printed a vessel model (3D) and would like to use the main branch (approx. 5.6mm) with a syringe /cannula (approx.3.5mm) to introduce a liquid to determine the volume of the vessel.</p>
<p>My problem is the transition from the main branch to the syringe/cannula. Is there an idea for this?</p>
<p>One could also provide a cover with a precisely fitting opening for the cannula when designing the model.</p>
<p>It is important that no liquid escapes, otherwise the result would be falsified.</p>
<p>see attached sketch</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36cad78970ad53745bc045555e28a9df9eae80e7.jpeg" data-download-href="/uploads/short-url/7OImXgWbK2Z0JsYkV6a567Rrad1.jpeg?dl=1" title="Sketch _Vessel - Syringe" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36cad78970ad53745bc045555e28a9df9eae80e7_2_351x500.jpeg" alt="Sketch _Vessel - Syringe" data-base62-sha1="7OImXgWbK2Z0JsYkV6a567Rrad1" width="351" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36cad78970ad53745bc045555e28a9df9eae80e7_2_351x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/3/36cad78970ad53745bc045555e28a9df9eae80e7_2_526x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/6/36cad78970ad53745bc045555e28a9df9eae80e7.jpeg 2x" data-dominant-color="FDFDFD"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Sketch _Vessel - Syringe</span><span class="informations">540×768 15.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>best regards</p>

---

## Post #2 by @lassoan (2020-08-03 15:58 UTC)

<p>There is no need to print the model, you can measure segment volumes in model (using “Segment Statistics” module) much more accurately than in a physical model.</p>
<p>You can draw tubes in the segmentation using “Draw tube” effect (provided by SegmentEditorExtraEffects extension).</p>

---
