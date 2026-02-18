# Displacement vector from a deformable reg; WARNING inverse innaccuate

**Topic ID**: 5569
**Date**: 2019-01-29
**URL**: https://discourse.slicer.org/t/displacement-vector-from-a-deformable-reg-warning-inverse-innaccuate/5569

---

## Post #1 by @Lowey (2019-01-29 21:05 UTC)

<p>Slicer 4.8.1<br>
Windows 10</p>
<p>Hi there,</p>
<p>I am doing research regarding deforming dose distributions and have questions about the warning you can receive regarding inverse displacement vectors.</p>
<p>The warning is -  Warning: inverse is inaccurate! (see attached image)!<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/0/909f93efc33feb3a9dc02908c4b14f89d6e6860d.png" data-download-href="/uploads/short-url/kDoEhIlBsvfG8bojYUFAsNwARD7.png?dl=1" title="Alpha_29_inverse_inaccurate" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/909f93efc33feb3a9dc02908c4b14f89d6e6860d_2_690x315.png" alt="Alpha_29_inverse_inaccurate" data-base62-sha1="kDoEhIlBsvfG8bojYUFAsNwARD7" width="690" height="315" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/909f93efc33feb3a9dc02908c4b14f89d6e6860d_2_690x315.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/909f93efc33feb3a9dc02908c4b14f89d6e6860d_2_1035x472.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/9/0/909f93efc33feb3a9dc02908c4b14f89d6e6860d_2_1380x630.png 2x" data-dominant-color="B0A796"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Alpha_29_inverse_inaccurate</span><span class="informations">1880×859 369 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I am curious (i.e., the mathematics behind) how slicer determines that the inverse is inaccurate? Or, is this warning encoded in the DICOM metadata somewhere?</p>
<p>Many thanks<br>
Nick</p>

---

## Post #2 by @lassoan (2019-01-30 00:48 UTC)

<p>The warning is displayed when the forward and inverse transform at the mouse pointer position is not consistent: applying forward then the inverse transform result in non-zero translation.</p>

---

## Post #3 by @Lowey (2019-01-30 01:34 UTC)

<p>Great - makes sense now of course! Thank you!</p>

---

## Post #4 by @Lowey (2019-01-30 03:54 UTC)

<p>Sorry one more question, is there a method with Slicer to export deformable spatial registrations to DICOM? I can’t seem to export these files, even if they are grouped in a patient (see attached)</p>
<p>Many thanks!</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66b700c91e18b7d8ee58a1b2607ed9f662f7ccd5.png" data-download-href="/uploads/short-url/eEEMCFjWyPSOM6PSk1fvIXhDL4F.png?dl=1" title="exportDR" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66b700c91e18b7d8ee58a1b2607ed9f662f7ccd5_2_690x408.png" alt="exportDR" data-base62-sha1="eEEMCFjWyPSOM6PSk1fvIXhDL4F" width="690" height="408" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66b700c91e18b7d8ee58a1b2607ed9f662f7ccd5_2_690x408.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/6/66b700c91e18b7d8ee58a1b2607ed9f662f7ccd5_2_1035x612.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66b700c91e18b7d8ee58a1b2607ed9f662f7ccd5.png 2x" data-dominant-color="D2D2D2"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">exportDR</span><span class="informations">1339×793 75.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #5 by @lassoan (2019-01-31 00:23 UTC)

<p>You need to install SlicerRT extension to be able to save the displacement field as a DICOM spatial registration object.</p>

---
