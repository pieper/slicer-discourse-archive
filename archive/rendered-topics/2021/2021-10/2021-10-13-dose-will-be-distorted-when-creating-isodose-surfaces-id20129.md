# Dose will be distorted when creating isodose surfaces

**Topic ID**: 20129
**Date**: 2021-10-13
**URL**: https://discourse.slicer.org/t/dose-will-be-distorted-when-creating-isodose-surfaces/20129

---

## Post #1 by @Cody_Xie (2021-10-13 08:49 UTC)

<p>Dear All,</p>
<p>I am using SlicerRT plug-in, and I would like to <strong>create isodose surfaces</strong>. However, just after clicking “<strong>Create isodose surfaces</strong>”, I found that  <strong>the dose was distorted</strong> automatically.</p>
<p>The two screenshots below are self-explanatory. The first screenshot is before clicking “Create isodose surfaces”, and the second one is after clicking. The three views are from the same slices. You can see that <strong>the dose is enlarged</strong>.</p>
<p>Before:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/7/0729308964a41c8bf3e5c04969c2eb4da5c4e527.png" data-download-href="/uploads/short-url/11lACfH0PZUfpnwrNl6xXhYZUKH.png?dl=1" title="Isodose_before" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/0729308964a41c8bf3e5c04969c2eb4da5c4e527_2_661x500.png" alt="Isodose_before" data-base62-sha1="11lACfH0PZUfpnwrNl6xXhYZUKH" width="661" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/0729308964a41c8bf3e5c04969c2eb4da5c4e527_2_661x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/0729308964a41c8bf3e5c04969c2eb4da5c4e527_2_991x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/7/0729308964a41c8bf3e5c04969c2eb4da5c4e527_2_1322x1000.png 2x" data-dominant-color="36A93A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Isodose_before</span><span class="informations">1486×1124 63.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/f/3fd2c9ad91c1f083e2c5e57ed6e32f6112e3b6c3.png" data-download-href="/uploads/short-url/96BGRQqIYZFE0aUGbz8AJPfiVeX.png?dl=1" title="Isodose_after" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fd2c9ad91c1f083e2c5e57ed6e32f6112e3b6c3_2_661x500.png" alt="Isodose_after" data-base62-sha1="96BGRQqIYZFE0aUGbz8AJPfiVeX" width="661" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fd2c9ad91c1f083e2c5e57ed6e32f6112e3b6c3_2_661x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fd2c9ad91c1f083e2c5e57ed6e32f6112e3b6c3_2_991x750.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/f/3fd2c9ad91c1f083e2c5e57ed6e32f6112e3b6c3_2_1322x1000.png 2x" data-dominant-color="4AA83A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Isodose_after</span><span class="informations">1486×1124 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Could you give me some support that how to avoid the distortion? Thank you so much!</p>

---

## Post #2 by @cpinter (2021-10-14 12:45 UTC)

<p>It could simply be that the window/level settings have changed. Can you go to the Volumes module before and after Isodose generation and check the W/L values?</p>

---

## Post #3 by @Mik (2021-10-14 13:05 UTC)

<p>It looks like that the issue. Dose color table changes palette according to the isodose levels, and  window level for a display dose is set to auto.</p>

---

## Post #4 by @Cody_Xie (2021-10-15 19:40 UTC)

<p>Thanks Csaba! That’s exactly the reason why the dose was magnified. The W/L values were 25/18 before, and 28/14 after.</p>

---
