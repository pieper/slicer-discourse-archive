#  UKF tractography vs MRtrix CSD in my data 

**Topic ID**: 33165
**Date**: 2023-12-01
**URL**: https://discourse.slicer.org/t/ukf-tractography-vs-mrtrix-csd-in-my-data/33165

---

## Post #1 by @gaunny (2023-12-01 16:50 UTC)

<p>Hi!<br>
I meet problem when I use UKF tractography in my data. I used the default parameters in Slicer 3D, but the traced out fibres are very discontinuous and even in the wrong direction. For example, the corticospinal tract, pictured below, is broken.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/e/6ee01aa0e8d4d6debd30bbd96f9d2934ea2dd482.jpeg" data-download-href="/uploads/short-url/fOQF4ePcOfTNEDm1TGC9qQO3BL4.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ee01aa0e8d4d6debd30bbd96f9d2934ea2dd482_2_641x500.jpeg" alt="image" data-base62-sha1="fOQF4ePcOfTNEDm1TGC9qQO3BL4" width="641" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ee01aa0e8d4d6debd30bbd96f9d2934ea2dd482_2_641x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ee01aa0e8d4d6debd30bbd96f9d2934ea2dd482_2_961x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/e/6ee01aa0e8d4d6debd30bbd96f9d2934ea2dd482_2_1282x1000.jpeg 2x" data-dominant-color="689CBB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1840×1434 418 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I checked my data, it has 3 b-values, 0,1000 and 2000, and each b-value contains 9, 50, 50 directions. A slice of b0 is shown below:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/a/ba969dd5d4cb4bc11005a5a71490606407071eaa.jpeg" data-download-href="/uploads/short-url/qCDvfdZLAobOWoShqSVdpYEkNMC.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba969dd5d4cb4bc11005a5a71490606407071eaa_2_669x500.jpeg" alt="image" data-base62-sha1="qCDvfdZLAobOWoShqSVdpYEkNMC" width="669" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba969dd5d4cb4bc11005a5a71490606407071eaa_2_669x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba969dd5d4cb4bc11005a5a71490606407071eaa_2_1003x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/a/ba969dd5d4cb4bc11005a5a71490606407071eaa_2_1338x1000.jpeg 2x" data-dominant-color="282828"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1710×1278 64 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
I checked different slices in the same direction, and images in different directions of the same slice, and all were fine.<br>
When I use CSD in MRtrix, it works well, like this:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/b/abdc6cfd7fa7b25b8f161f9a396ce85a1e0fd9ff.jpeg" data-download-href="/uploads/short-url/owlUg8nC1rehY6UwkZtmmbRhELl.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abdc6cfd7fa7b25b8f161f9a396ce85a1e0fd9ff_2_470x500.jpeg" alt="image" data-base62-sha1="owlUg8nC1rehY6UwkZtmmbRhELl" width="470" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abdc6cfd7fa7b25b8f161f9a396ce85a1e0fd9ff_2_470x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abdc6cfd7fa7b25b8f161f9a396ce85a1e0fd9ff_2_705x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/b/abdc6cfd7fa7b25b8f161f9a396ce85a1e0fd9ff_2_940x1000.jpeg 2x" data-dominant-color="443F4D"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1116×1186 221 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>So I’m wondering why the UKF method can’t achieve proper tracking on this data?<br>
Looking forward to your reply.<br>
Best regards.</p>

---

## Post #2 by @pieper (2023-12-01 18:40 UTC)

<p>Probably something in the gradient directions or measurement frame is incorrect.</p>

---

## Post #3 by @gaunny (2023-12-05 00:55 UTC)

<p>Thank you. I found that SlicerDMRI can’t handle GE scan headers well?My data has 0,1000,2000 b-values, but I found that using DicomToFSL in DWIConvert, I only get 0 and 2000 b-values.</p>

---

## Post #4 by @pieper (2023-12-05 19:10 UTC)

<p>Diffusion scans are notoriously tricky.  We suggest <a href="https://github.com/rordenlab/dcm2niix">dcm2niix</a> since it is actively maintained and DWIConvert is very old at this point.</p>

---

## Post #5 by @gaunny (2023-12-06 09:18 UTC)

<p>Thank you and it works well now.</p>

---
