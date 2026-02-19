---
topic_id: 46117
title: "Odd Behavior After Adding A Moving Mask In The Ants Extensio"
date: 2026-02-10
url: https://discourse.slicer.org/t/46117
---

# Odd behavior after adding a moving mask in the ANTs extension

**Topic ID**: 46117
**Date**: 2026-02-10
**URL**: https://discourse.slicer.org/t/odd-behavior-after-adding-a-moving-mask-in-the-ants-extension/46117

---

## Post #1 by @sulli419 (2026-02-10 20:05 UTC)

<p>I’ve been using the ANTs extension for registering two single-label volumes to eachother with good results.  In an attempt to improve registration robustness, I started incorporating fixed and moving masks (FM, MM), but this is yielding some unexpected results.  To simplify the issue I’m just focusing on a single stage affine transform. The affine transform with the fixed mask alone looks very reasonable; but if I add a moving mask to this same affine configuration (along with the fixed) the registration is much poorer.  For now, the moving mask is essentially just a bounding box with zeros at the edges.</p>
<p>When working properly, the largest components of the final affine transform are a Z translation (shift) and a Z scaling (expansion).  Something about showing the MM (in addition to FM) loses this info.  As a test, I ran a “good” FM only registration but also included a 2nd dummy affine stage (following the correct/complete one), where there are zero convergence steps, but now both the FM and MM are shown.  This somehow changes the 3-3 matrix value (Z scaling factor) from 1.2 (ideal) to ~1.  If this dummy step only has the FM, the “affine erasure” doesn’t happen.</p>
<p>Trouble shooting I created a MM that is “all 1s”, expecting that it should work the same as a having no moving mask but this wasn’t the case, the all 1s MM worsened the quality.</p>
<p>Any chance this is a bug? Might the image origin of the moving mask be getting read improperly?  Perhaps I’m just ignorant of how masks interact by design in ANTs.</p>
<p>If it’s any help I’m including an image<br>
Red: Fixed volume (my tissue); Yellow: Moving volume (atlas); Green: fixed mask; Purple: moving mask</p>
<p>**Note, this doesn’t show the dimensions of the zero values.  For example, how large the virtual space of the fixed volume is.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1093bf97e79e1fa29dfd43eacd1441c8fa6fab0.jpeg" data-download-href="/uploads/short-url/tPdzGRT0m1TRxw6K90ytkXjKDWE.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1093bf97e79e1fa29dfd43eacd1441c8fa6fab0_2_215x499.jpeg" alt="image" data-base62-sha1="tPdzGRT0m1TRxw6K90ytkXjKDWE" width="215" height="499" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/1/d1093bf97e79e1fa29dfd43eacd1441c8fa6fab0_2_215x499.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1093bf97e79e1fa29dfd43eacd1441c8fa6fab0.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/1/d1093bf97e79e1fa29dfd43eacd1441c8fa6fab0.jpeg 2x" data-dominant-color="9387A6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">320×744 34.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
