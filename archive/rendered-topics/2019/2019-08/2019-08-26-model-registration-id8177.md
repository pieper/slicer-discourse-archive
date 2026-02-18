# Model registration

**Topic ID**: 8177
**Date**: 2019-08-26
**URL**: https://discourse.slicer.org/t/model-registration/8177

---

## Post #1 by @Jainey (2019-08-26 15:20 UTC)

<p>Hi<br>
Thank you for all the previous inputs; this seems to be working.</p>
<p>One more question- When I register two models the mean distance appear in decimals , say 0.65 but when I check the translations on the transforms module for the linear transforms they are in the range of 34 mm, 44 mm eat on xy and z. How could this happen. Could someone please let me know. In reality the distance between the centre of the models would only change 1-2 mm.</p>
<p>Thanks a lot</p>

---

## Post #2 by @lassoan (2019-08-27 13:56 UTC)

<p>Which module do you use to register the models?</p>
<p>Fiducial registration wizard reports residual error. You can find registration translation/rotation values in Transforms module.</p>
<aside class="quote no-group" data-username="Jainey" data-post="1" data-topic="8177">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a88e57/48.png" class="avatar"> Jainey:</div>
<blockquote>
<p>In reality the distance between the centre of the models would only change 1-2 mm.</p>
</blockquote>
</aside>
<p>Can you post screenshots - before/after registration, GUI of the module you use for registration, and resulting transform shown in Transforms module?</p>

---

## Post #3 by @Jainey (2019-08-27 16:54 UTC)

<p>Thanks Prof <a class="mention" href="/u/lassoan">@lassoan</a><br>
I use mode to model registration with ICP  algorithm</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/7/d78262e1e17acfa11708bb58ad5b4e7651dcd166.jpeg" data-download-href="/uploads/short-url/uKu0sw1CKYEnSPPR3ZgeVabLFTU.jpeg?dl=1" title="28" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d78262e1e17acfa11708bb58ad5b4e7651dcd166_2_690x418.jpeg" alt="28" data-base62-sha1="uKu0sw1CKYEnSPPR3ZgeVabLFTU" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d78262e1e17acfa11708bb58ad5b4e7651dcd166_2_690x418.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d78262e1e17acfa11708bb58ad5b4e7651dcd166_2_1035x627.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/7/d78262e1e17acfa11708bb58ad5b4e7651dcd166_2_1380x836.jpeg 2x" data-dominant-color="95959A"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">28</span><span class="informations">3360×2036 926 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/2/427546a1f194edf90e5a31ef0293c816b2fe8c90.jpeg" data-download-href="/uploads/short-url/9tUM57iTn9Rme6UrqIq5eXlORKU.jpeg?dl=1" title="26" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/427546a1f194edf90e5a31ef0293c816b2fe8c90_2_541x500.jpeg" alt="26" data-base62-sha1="9tUM57iTn9Rme6UrqIq5eXlORKU" width="541" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/427546a1f194edf90e5a31ef0293c816b2fe8c90_2_541x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/427546a1f194edf90e5a31ef0293c816b2fe8c90_2_811x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/2/427546a1f194edf90e5a31ef0293c816b2fe8c90_2_1082x1000.jpeg 2x" data-dominant-color="F2F3F3"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">26</span><span class="informations">1722×1590 252 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div> Snip 2019-08-28 02.26.26.png</p>

---

## Post #4 by @lassoan (2019-08-27 17:16 UTC)

<p>Thanks for the additional information, it was useful.</p>
<aside class="quote no-group" data-username="Jainey" data-post="1" data-topic="8177">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/a88e57/48.png" class="avatar"> Jainey:</div>
<blockquote>
<p>In reality the distance between the centre of the models would only change 1-2 mm.</p>
</blockquote>
</aside>
<p>As you say, the distance between the <em>center</em> of the models is 1-2mm. However, the translation component that you see in Transforms module is the translation at the origin (RAS=(0,0,0) position). To get translation at the center of the model, get the center of the model and transform that point coordinate using the transform.</p>

---

## Post #5 by @Jainey (2019-08-28 00:47 UTC)

<p>Thanks Prof <a class="mention" href="/u/lassoan">@lassoan</a><br>
How could I do that please. Or any particular point in the model. Thank you very much</p>

---

## Post #6 by @lassoan (2019-08-28 14:51 UTC)

<p>You can retrieve the VTK transform from the transform node and then use its <code>TransformPoint</code> method to transform a point coordinate. Search for <code>TransformPoint</code> in <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository" rel="nofollow noopener">script repository</a> for examples.</p>

---

## Post #8 by @johny723 (2025-04-17 14:05 UTC)

<p>Hi, I need help. I am trying to register a segmented sacrum from CT onto a sacrum from MRI. It is the same patient. When I use “model registration” I do not see the output model. What is wrong?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bfbfcecbef540bd24fe4431338a06bb1655f9e4.png" data-download-href="/uploads/short-url/mfTT9YI2SEKDPtRivqNJV5gXSIs.png?dl=1" title="Snímka obrazovky 2025-04-17 160302" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/9/b/9bfbfcecbef540bd24fe4431338a06bb1655f9e4.png" alt="Snímka obrazovky 2025-04-17 160302" data-base62-sha1="mfTT9YI2SEKDPtRivqNJV5gXSIs" width="581" height="348"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Snímka obrazovky 2025-04-17 160302</span><span class="informations">581×348 6.62 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>I tried 5,6.1, 5.8.1 and even 5.9, but it does not work. I also do not see the transforms, just this rather small table</p>

---
