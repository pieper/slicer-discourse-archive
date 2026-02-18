# tractography single color tract not multi-color tract

**Topic ID**: 29952
**Date**: 2023-06-09
**URL**: https://discourse.slicer.org/t/tractography-single-color-tract-not-multi-color-tract/29952

---

## Post #1 by @GunnarE (2023-06-09 20:15 UTC)

<p>Hi Slicer community,</p>
<p>We have been following multiple tutorials from Dr. Sonia Pujol on diffusion tractography including <a href="https://www.slicer.org/w/img_auth.php/f/f1/NeurosurgicalPlanning_SoniaPujol.pdf" rel="noopener nofollow ugc">“Exploring Peritumoral White Matter Fibers for Neurosurgical Planning”</a>, “Diffusion MRI Analsyis”, and “UKF Tractography Tutorial”. We are having issues with the visualization of the tracts.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11b0cc23f3874e841b378a2cc6c113267cf61e06.jpeg" data-download-href="/uploads/short-url/2wuU1WknAPJpciBvGTefPV6gyTI.jpeg?dl=1" title="Screenshot 2023-06-09 at 1.53.54 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11b0cc23f3874e841b378a2cc6c113267cf61e06_2_520x500.jpeg" alt="Screenshot 2023-06-09 at 1.53.54 PM" data-base62-sha1="2wuU1WknAPJpciBvGTefPV6gyTI" width="520" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11b0cc23f3874e841b378a2cc6c113267cf61e06_2_520x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11b0cc23f3874e841b378a2cc6c113267cf61e06_2_780x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11b0cc23f3874e841b378a2cc6c113267cf61e06_2_1040x1000.jpeg 2x" data-dominant-color="6C7B61"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-06-09 at 1.53.54 PM</span><span class="informations">1588×1526 125 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
This is the expected results from the “Exploring Peritumoral White Matter Fibers for Neurosurgical Planning” tutorial with different colors per single tract.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/a/7a1c42633cfdb0b6429797309eafd02447187817.jpeg" data-download-href="/uploads/short-url/hqeNoBqBIkn0YWJXLzRE2ik3rdt.jpeg?dl=1" title="Screenshot 2023-06-09 at 1.50.51 PM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a1c42633cfdb0b6429797309eafd02447187817_2_631x500.jpeg" alt="Screenshot 2023-06-09 at 1.50.51 PM" data-base62-sha1="hqeNoBqBIkn0YWJXLzRE2ik3rdt" width="631" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a1c42633cfdb0b6429797309eafd02447187817_2_631x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a1c42633cfdb0b6429797309eafd02447187817_2_946x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/7/a/7a1c42633cfdb0b6429797309eafd02447187817_2_1262x1000.jpeg 2x" data-dominant-color="6FAB8D"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2023-06-09 at 1.50.51 PM</span><span class="informations">1920×1519 218 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
Our results, as seen in this screenshot, have one solid color per tract, instead of changing per direction as expected. For example, the end tips of the tracts near the green solid tumor should be yellow, but in our screenshot it is only green. We have been using the Slicer 4.10.2 on osx.</p>
<p>We are also having issues making the tracts thicker.<br>
Any advice would be great, thank you!</p>

---

## Post #2 by @lassoan (2023-06-16 14:43 UTC)

<p>Could you try if the current Slicer version (Slicer-5.2.2) works better?</p>

---

## Post #3 by @GunnarE (2023-07-24 22:43 UTC)

<p>HI <a class="mention" href="/u/lassoan">@lassoan</a>,</p>
<p>I am working in the <a class="mention" href="/u/nicholas.jacobson">@Nicholas.jacobson</a> lab, we have done this successfully on 4.10.2 and 5.2.2. We are not getting the direct results from the tutorial of the directional coloring. Any thoughts to what might have changed? Could it be user error?</p>
<p>Thanks,<br>
Gunnar</p>

---
