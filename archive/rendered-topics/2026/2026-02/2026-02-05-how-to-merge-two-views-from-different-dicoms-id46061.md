# How to merge two views from different DICOMs?

**Topic ID**: 46061
**Date**: 2026-02-05
**URL**: https://discourse.slicer.org/t/how-to-merge-two-views-from-different-dicoms/46061

---

## Post #1 by @mrrezaie (2026-02-05 10:24 UTC)

<p>Hello,</p>
<p>I have two DICOMs (EOS bi-plane x-ray); they are orthogonal and synchronized. The program failed to load them as series, I imported each one separately as a volume. Now, I want to merge them, but only one view of each (the AP view of DICOM1 and RL view of DICOM2).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d50bac8d7c4659b044e761349d49975a7cd2872.png" data-download-href="/uploads/short-url/hSAE47MGgZnzDAdIduKnMLgDTSq.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d50bac8d7c4659b044e761349d49975a7cd2872_2_542x500.png" alt="image" data-base62-sha1="hSAE47MGgZnzDAdIduKnMLgDTSq" width="542" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/d/7d50bac8d7c4659b044e761349d49975a7cd2872_2_542x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d50bac8d7c4659b044e761349d49975a7cd2872.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/d/7d50bac8d7c4659b044e761349d49975a7cd2872.png 2x" data-dominant-color="343337"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">642×592 81.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aedf18232a2aaeb0e0db45f8af0e31383c162aee.png" data-download-href="/uploads/short-url/oWZ3xJtlxiziA5k7bxzhjD2lTGe.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aedf18232a2aaeb0e0db45f8af0e31383c162aee_2_535x500.png" alt="image" data-base62-sha1="oWZ3xJtlxiziA5k7bxzhjD2lTGe" width="535" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/e/aedf18232a2aaeb0e0db45f8af0e31383c162aee_2_535x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aedf18232a2aaeb0e0db45f8af0e31383c162aee.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aedf18232a2aaeb0e0db45f8af0e31383c162aee.png 2x" data-dominant-color="363539"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">640×598 87.3 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I was wondering if there is any solution here; thank you in advance.</p>

---

## Post #2 by @cpinter (2026-02-05 10:45 UTC)

<p>These seem to be projection X-rays so there will be no series, but a pair of single images.</p>
<p>After a search I found that “using the sterEOS workstation, clinicians can generate patient-specific 3D reconstructions of the spine, pelvis, and lower limbs from the two 2D images.”. As far as I know, Slicer does not have tools to do such reconstruction from a pair of projections, if this is what you are asking.</p>

---

## Post #3 by @mrrezaie (2026-02-05 10:58 UTC)

<p>Thanks <a class="mention" href="/u/cpinter">@cpinter</a> for your response. The company’s software is mainly for clinical measurements, and the 3D model is merely for visualization (the company no longer provides research features unfortunately).</p>
<p>However, I’m trying to align the bones (femur and patella) to be in the same position and orientation as the images. Something like:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d353262ffbf3b2226b856e5ec903dc4087aba720.jpeg" data-download-href="/uploads/short-url/u9sTkV4WUjWekAIfAEmJMVgUUrm.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/3/d353262ffbf3b2226b856e5ec903dc4087aba720.jpeg" alt="image" data-base62-sha1="u9sTkV4WUjWekAIfAEmJMVgUUrm" width="448" height="389"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">448×389 28.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
