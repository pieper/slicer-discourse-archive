# Align two models

**Topic ID**: 30129
**Date**: 2023-06-19
**URL**: https://discourse.slicer.org/t/align-two-models/30129

---

## Post #1 by @rcapozza (2023-06-19 21:10 UTC)

<p>I have a volume composed of several peripheral quantitative computed tomography (pQCT) slices. Since the scans were taken with repositioning, the proximal half of the tibia ended up misaligned with respect to the distal half. Therefore, I first segmented the tibia and then copied the proximal and distal halves into separate segments. Next, I realigned the halves using a transformation with the IGT module. Then, I created two models, one for each half, and used the merge module to join the models into one, so I could export the whole, aligned tibia for further analysis. But as you can see in the last image, the resulting model returned to the original misalignment. Where is my mistake? Thank you for any insights you can provide.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a63099785273e99147b7cadfc1a98ae1446698f.jpeg" data-download-href="/uploads/short-url/fb8Nw4aQ0RSsfKWeVeJb5BYPFrp.jpeg?dl=1" title="misalignedTibia" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a63099785273e99147b7cadfc1a98ae1446698f_2_689x487.jpeg" alt="misalignedTibia" data-base62-sha1="fb8Nw4aQ0RSsfKWeVeJb5BYPFrp" width="689" height="487" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a63099785273e99147b7cadfc1a98ae1446698f_2_689x487.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/a/6a63099785273e99147b7cadfc1a98ae1446698f_2_1033x730.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/a/6a63099785273e99147b7cadfc1a98ae1446698f.jpeg 2x" data-dominant-color="73728C"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">misalignedTibia</span><span class="informations">1292×913 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/854df346ed840ba370ba47f77638f58a62466d69.jpeg" data-download-href="/uploads/short-url/j1gvHvJK13nYcbHFTbnS1oVZ0mJ.jpeg?dl=1" title="alignedTibia" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/854df346ed840ba370ba47f77638f58a62466d69_2_689x487.jpeg" alt="alignedTibia" data-base62-sha1="j1gvHvJK13nYcbHFTbnS1oVZ0mJ" width="689" height="487" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/854df346ed840ba370ba47f77638f58a62466d69_2_689x487.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/5/854df346ed840ba370ba47f77638f58a62466d69_2_1033x730.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/5/854df346ed840ba370ba47f77638f58a62466d69.jpeg 2x" data-dominant-color="6C6F90"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">alignedTibia</span><span class="informations">1292×913 143 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12fefcaeea85ba0c40522ad31432f81c47369b02.jpeg" data-download-href="/uploads/short-url/2I2TU63fOZYr8egvgJQLCNp8p1M.jpeg?dl=1" title="models" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12fefcaeea85ba0c40522ad31432f81c47369b02_2_689x487.jpeg" alt="models" data-base62-sha1="2I2TU63fOZYr8egvgJQLCNp8p1M" width="689" height="487" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12fefcaeea85ba0c40522ad31432f81c47369b02_2_689x487.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/2/12fefcaeea85ba0c40522ad31432f81c47369b02_2_1033x730.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/2/12fefcaeea85ba0c40522ad31432f81c47369b02.jpeg 2x" data-dominant-color="6D6F90"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">models</span><span class="informations">1292×913 139 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f96a29926f66a7e55ec984b0c79d476a6a0a9e81.jpeg" data-download-href="/uploads/short-url/zAqlcHI79kLfedIY4gnJGsqMb73.jpeg?dl=1" title="merged_models" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f96a29926f66a7e55ec984b0c79d476a6a0a9e81_2_689x487.jpeg" alt="merged_models" data-base62-sha1="zAqlcHI79kLfedIY4gnJGsqMb73" width="689" height="487" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f96a29926f66a7e55ec984b0c79d476a6a0a9e81_2_689x487.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/9/f96a29926f66a7e55ec984b0c79d476a6a0a9e81_2_1033x730.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/9/f96a29926f66a7e55ec984b0c79d476a6a0a9e81.jpeg 2x" data-dominant-color="727288"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">merged_models</span><span class="informations">1292×913 144 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @SANTIAGO_PENDON_MING (2023-06-20 12:54 UTC)

<p>You probably have to Harden transform the previous models in order to “remember” the transform you made  when you merge both models.</p>

---

## Post #3 by @rcapozza (2023-06-20 18:02 UTC)

<p>Thank you very much. By applying the Harden Transform, the resulting model respects the individual transformations. The only thing left is to achieve a smoother transition. Any ideas?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7f35d22fbc402919aee1ec13c7cdc5136f63121.png" data-download-href="/uploads/short-url/x5VHpJsOQImZmb02grN1754fK8h.png?dl=1" title="tibia_final" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7f35d22fbc402919aee1ec13c7cdc5136f63121_2_689x487.png" alt="tibia_final" data-base62-sha1="x5VHpJsOQImZmb02grN1754fK8h" width="689" height="487" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7f35d22fbc402919aee1ec13c7cdc5136f63121_2_689x487.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/7/e7f35d22fbc402919aee1ec13c7cdc5136f63121_2_1033x730.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/7/e7f35d22fbc402919aee1ec13c7cdc5136f63121.png 2x" data-dominant-color="6A6A81"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">tibia_final</span><span class="informations">1292×913 66.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---
