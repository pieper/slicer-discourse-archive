# Is there a way to fix this model quickly

**Topic ID**: 27774
**Date**: 2023-02-12
**URL**: https://discourse.slicer.org/t/is-there-a-way-to-fix-this-model-quickly/27774

---

## Post #1 by @slicer365 (2023-02-12 06:16 UTC)

<p>I want to fill this area quickly ,then turn this model into a solid model,</p>
<p>I know the tool WrapSolidify can work,but it works very slowly</p>
<p>I need a fast way</p>
<p>thankyou very much</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/a/5ac9f44d0d16ee7a47ad877bca4164c36519a094.jpeg" data-download-href="/uploads/short-url/cX9ELaY0gBykwILlrg01tsFWkpS.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5ac9f44d0d16ee7a47ad877bca4164c36519a094_2_344x250.jpeg" alt="image" data-base62-sha1="cX9ELaY0gBykwILlrg01tsFWkpS" width="344" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5ac9f44d0d16ee7a47ad877bca4164c36519a094_2_344x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5ac9f44d0d16ee7a47ad877bca4164c36519a094_2_516x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/a/5ac9f44d0d16ee7a47ad877bca4164c36519a094_2_688x500.jpeg 2x" data-dominant-color="5F6363"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1246×903 211 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2023-02-12 22:31 UTC)

<p>Shrink-wrapping is the best tool in Slicer (and probably in general one of the best methods) for filling internal holes. You can make it much faster by cropping the image to the relevant region and/or by tuning its parameters (decrease oversampling, decrease teration).</p>
<p>You could also very significantly improve the speed and robustness (therefore reduce the number of required iterations and so further improving the speed) by remeshing using ACVD uniform remeshing instead of rasterizing+mesh extraction. Let me know if you want to work on this (it is just a bit of Python scripting) and I can help you getting started.</p>

---

## Post #3 by @slicer365 (2023-02-13 11:54 UTC)

<p>Thank you very much，Mr. Lasso</p>
<p>I am interested in the second way , hope you can give me more information about it .</p>

---
