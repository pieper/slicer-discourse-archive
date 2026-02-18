# Remove atifacts background after registration

**Topic ID**: 12551
**Date**: 2020-07-15
**URL**: https://discourse.slicer.org/t/remove-atifacts-background-after-registration/12551

---

## Post #1 by @1116 (2020-07-15 10:17 UTC)

<p>After rigid registration using Elastix, I got CT data with artifacts at background</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11182dfd7f87e7ba54980beff0563e22d90760c5.png" data-download-href="/uploads/short-url/2rdV8QLiXMTrn5Lk42MBfvrSx7L.png?dl=1" title="캡처" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11182dfd7f87e7ba54980beff0563e22d90760c5_2_663x500.png" alt="캡처" data-base62-sha1="2rdV8QLiXMTrn5Lk42MBfvrSx7L" width="663" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11182dfd7f87e7ba54980beff0563e22d90760c5_2_663x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/1/11182dfd7f87e7ba54980beff0563e22d90760c5_2_994x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/1/11182dfd7f87e7ba54980beff0563e22d90760c5.png 2x" data-dominant-color="B3B3C3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">캡처</span><span class="informations">1001×754 175 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
is there any way to remove background remaining only head volume?</p>

---

## Post #2 by @cpinter (2020-07-15 10:45 UTC)

<p>If you selected an output transform node, then instead of using the output volume, apply the transform on the moving volume.</p>

---

## Post #3 by @1116 (2020-07-15 12:28 UTC)

<p>Thank you for the reply!</p>
<p>It removes the background, but the demension and spacing do not fit with MR data.<br>
What should be done  after applying the transform node?</p>

---

## Post #4 by @cpinter (2020-07-15 12:45 UTC)

<p>You probably didn’t actually apply the transform on the moving volume.</p>
<p>It can be done from the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/data.html">Data module</a> (right-click the transform column ans select the transform) or the <a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/Transforms">Transforms module</a> (select transform, and move the volume under it)</p>

---
