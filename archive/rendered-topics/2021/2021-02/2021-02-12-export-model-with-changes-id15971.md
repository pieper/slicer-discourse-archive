# Export model with changes

**Topic ID**: 15971
**Date**: 2021-02-12
**URL**: https://discourse.slicer.org/t/export-model-with-changes/15971

---

## Post #1 by @Giulia1 (2021-02-12 17:13 UTC)

<p>Hi! I have a problem regarding the export of the final file.<br>
When I import a model as a segmentation, if I edit it on segment editor by adding more segmentations or delete wrong parts, if I export it I get a file with only the changes that have been made (so only the added parts). How do I do if I want to export the final result (so the initial model with the changes) ?</p>
<p>thanks!</p>

---

## Post #2 by @lassoan (2021-02-12 17:23 UTC)

<p>If you export a segmentation to a mesh file then the file contains the final segmentation results (not just some relative changes). Maybe you could attach a few screenshots to better demonstrate what you are experiencing.</p>

---

## Post #3 by @Giulia1 (2021-02-12 17:37 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="15971">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>export a segmentation to a mesh file</p>
</blockquote>
</aside>
<p>Thanks for the reply, unfortunately I don’t have a screenshot, but I can explain it better. I need to reconstruct a knee and I have different volumes. For example I create the segmentation of the femur with the axial part, then I export it (segmentation–&gt;export to file). Then I want to modify it with the coronal part, so I import the previously created file (as segmentation) and in segment editor I modify it, in this case if I export it, the file I get is only about the added part and not the final result.</p>
<p>thanks</p>

---

## Post #4 by @Giulia1 (2021-02-12 18:14 UTC)

<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/f/4f4d5586b0f508c13a52c18eb9ff7eb453d2dfb0.jpeg" data-download-href="/uploads/short-url/bjxph7WnXCpjFwaDROTvROOLbTa.jpeg?dl=1" title="Schermata 2021-02-12 alle 19.12.34" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f4d5586b0f508c13a52c18eb9ff7eb453d2dfb0_2_285x500.jpeg" alt="Schermata 2021-02-12 alle 19.12.34" data-base62-sha1="bjxph7WnXCpjFwaDROTvROOLbTa" width="285" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f4d5586b0f508c13a52c18eb9ff7eb453d2dfb0_2_285x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f4d5586b0f508c13a52c18eb9ff7eb453d2dfb0_2_427x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4f4d5586b0f508c13a52c18eb9ff7eb453d2dfb0_2_570x1000.jpeg 2x" data-dominant-color="929FAA"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Schermata 2021-02-12 alle 19.12.34</span><span class="informations">804×1408 128 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>this is the screenshot considering only the cartilage. In the first image I took the cartilage model and added pieces. In the second is the file I exported and got just the added cartilage parts.</p>

---

## Post #5 by @lassoan (2021-02-12 18:48 UTC)

<p>It seems that you have chosen to paint outside the original segment. You can use masking settings to allow overlap when editing segments; or use Logical operators effect to combine segments.</p>

---
