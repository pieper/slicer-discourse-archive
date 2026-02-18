# DynamicModeler hole-size-threshold for surface-capping?

**Topic ID**: 22272
**Date**: 2022-03-02
**URL**: https://discourse.slicer.org/t/dynamicmodeler-hole-size-threshold-for-surface-capping/22272

---

## Post #1 by @Fluvio_Lobo (2022-03-02 21:05 UTC)

<p>Hello,</p>
<p>Is there a way to control the “surface capping” option or feature of the DynamicModeler’s PlaneCut function?</p>
<p>I am using the PlaceCut function to transform dental impressions into dental splints, but I am struggling to  avoid dental impressions from being capped by the “surface cap” feature.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69acba49db5a3446ffc843e758e041b1244d2332.jpeg" data-download-href="/uploads/short-url/f4QcvAgTEp0r35y2Zm4oxVjJeRY.jpeg?dl=1" title="seen_here" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/69acba49db5a3446ffc843e758e041b1244d2332_2_690x460.jpeg" alt="seen_here" data-base62-sha1="f4QcvAgTEp0r35y2Zm4oxVjJeRY" width="690" height="460" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/69acba49db5a3446ffc843e758e041b1244d2332_2_690x460.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/69acba49db5a3446ffc843e758e041b1244d2332_2_1035x690.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/69acba49db5a3446ffc843e758e041b1244d2332.jpeg 2x" data-dominant-color="A88FA8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">seen_here</span><span class="informations">1316×878 74 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Circled in blue, are examples of dental impressions that are not “capped”. In re you can see the “surface cap” in action.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/b/5babb7838aeabb9c35dcad1f0c67a64cc231c09f.jpeg" data-download-href="/uploads/short-url/d4XlN2u29rBTvFDBe1KStbTVsjd.jpeg?dl=1" title="result" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5babb7838aeabb9c35dcad1f0c67a64cc231c09f_2_308x250.jpeg" alt="result" data-base62-sha1="d4XlN2u29rBTvFDBe1KStbTVsjd" width="308" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5babb7838aeabb9c35dcad1f0c67a64cc231c09f_2_308x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5babb7838aeabb9c35dcad1f0c67a64cc231c09f_2_462x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/5/5babb7838aeabb9c35dcad1f0c67a64cc231c09f_2_616x500.jpeg 2x" data-dominant-color="8A99AE"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">result</span><span class="informations">877×711 38.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div> <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/3/e396e040b40533642afcff3bacf4cc7a0e69a5ec.jpeg" data-download-href="/uploads/short-url/wtlDrbmSCTiLyhdF3nNqAbx5UqU.jpeg?dl=1" title="result_alpha" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e396e040b40533642afcff3bacf4cc7a0e69a5ec_2_309x250.jpeg" alt="result_alpha" data-base62-sha1="wtlDrbmSCTiLyhdF3nNqAbx5UqU" width="309" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e396e040b40533642afcff3bacf4cc7a0e69a5ec_2_309x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e396e040b40533642afcff3bacf4cc7a0e69a5ec_2_463x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/e/e396e040b40533642afcff3bacf4cc7a0e69a5ec_2_618x500.jpeg 2x" data-dominant-color="9199C1"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">result_alpha</span><span class="informations">853×690 28 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Here you can see a side by side of the resulting splint and a transparent projection. The holes are still there, the cap is the issue.</p>
<p>If this cannot be changed, are there other strategies to make this surface cut? Is there something that can be done in the segment editor?</p>

---

## Post #2 by @Fluvio_Lobo (2022-03-03 19:50 UTC)

<p>I ended-up doing the plane cuts on the surface model before converting the part into a segment and performing the Boolean subtraction of the prints. This is likely the most appropriate order for the operation.</p>

---
