# Fill between slices bug

**Topic ID**: 6338
**Date**: 2019-03-30
**URL**: https://discourse.slicer.org/t/fill-between-slices-bug/6338

---

## Post #1 by @roozbehshams (2019-03-30 18:08 UTC)

<p>Hi,<br>
There seems to be a bug with fill between slices tool in the nightly version 4.11.0-2019-03-26. It was also in the nightly 3 days before that.<br>
The problem is the interpolated labelmap is inverted :<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/f/5feaee6ceea75924c40694a3bc489b02995849fe.jpeg" data-download-href="/uploads/short-url/dGwHgiprLCdXGZaoTz31R6ffzFc.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5feaee6ceea75924c40694a3bc489b02995849fe_2_690x374.jpeg" alt="image" data-base62-sha1="dGwHgiprLCdXGZaoTz31R6ffzFc" width="690" height="374" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5feaee6ceea75924c40694a3bc489b02995849fe_2_690x374.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5feaee6ceea75924c40694a3bc489b02995849fe_2_1035x561.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/f/5feaee6ceea75924c40694a3bc489b02995849fe_2_1380x748.jpeg 2x" data-dominant-color="B4B3B9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">3839×2083 841 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>To replicate this, just try to use the tool with any volume. (I’ve tested this with MRHead)</p>
<p>Roozbeh</p>

---

## Post #2 by @cpinter (2019-04-04 13:24 UTC)

<p>Hi Roozbeh,</p>
<p>Sorry for the late reply. I tried to reproduce it, and indeed, the Fill between slices effect does this reliably.</p>
<p>We’ll fix this asap. Thanks for the report!</p>

---

## Post #3 by @cpinter (2019-04-04 13:28 UTC)

<p>I added a ticket for the bug: <a href="https://issues.slicer.org/view.php?id=4687" rel="nofollow noopener">https://issues.slicer.org/view.php?id=4687</a></p>

---
