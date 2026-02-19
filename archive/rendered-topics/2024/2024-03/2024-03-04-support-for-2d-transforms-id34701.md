---
topic_id: 34701
title: "Support For 2D Transforms"
date: 2024-03-04
url: https://discourse.slicer.org/t/34701
---

# Support for 2D transforms?

**Topic ID**: 34701
**Date**: 2024-03-04
**URL**: https://discourse.slicer.org/t/support-for-2d-transforms/34701

---

## Post #1 by @dzenanz (2024-03-04 17:49 UTC)

<p>sample2D.tfm</p>
<pre data-code-wrap="txt"><code class="lang-txt">#Insight Transform File V1.0
#Transform 0
Transform: AffineTransform_float_2_2
Parameters: 0.99985015 0.017311562 -0.017311562 0.99985015 -0.64851546 -0.7623114
FixedParameters: 0 0
</code></pre>
<p>when opened in Slicer, produces this non-sense:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f660594e90436af3c2f39b28fe86d24f19298721.png" data-download-href="/uploads/short-url/z9xSORHs6TjrvxbtstjdDQf3KjT.png?dl=1" title="Screenshot 2024-03-04 12.46.01" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f660594e90436af3c2f39b28fe86d24f19298721.png" alt="Screenshot 2024-03-04 12.46.01" data-base62-sha1="z9xSORHs6TjrvxbtstjdDQf3KjT" width="690" height="264" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screenshot 2024-03-04 12.46.01</span><span class="informations">1008×387 6.64 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Is this a known issue? Are there any plans to address it?</p>

---

## Post #2 by @pieper (2024-03-04 18:32 UTC)

<p>I suppose that converting these into a 3D affine might be useful in some cases.  Otherwise just refusing to read them seems like an easy option.</p>
<p>Looks like this is being done implicitly in <a href="https://github.com/Slicer/Slicer/blob/5e831bcfad3e501c79b03d32f053d5c2d9effc93/Libs/MRML/Core/vtkMRMLTransformStorageNode.cxx#L303-L511">this code</a> somewhere.</p>
<p><a class="mention" href="/u/dzenanz">@dzenanz</a> what happens in ITK if you try to read this 2D transform with a 3D transform reader?</p>

---

## Post #3 by @dzenanz (2024-03-04 18:37 UTC)

<p>Converting 2D transforms into 3D transforms would be quite useful (transformations in the 3rd dimension all identity/zero). And ideally, not just for affines but for displacement fields too.</p>
<blockquote>
<p>try to read this 2D transform with a 3D transform reader</p>
</blockquote>
<p>I assume it would crash as there are not enough parameters, or maybe because the transform name does not match the expectation.</p>

---

## Post #4 by @dzenanz (2025-11-10 16:20 UTC)

<p>For posterity: I created an <a href="https://github.com/Slicer/Slicer/issues/7633" rel="noopener nofollow ugc">issue with more detail</a>.</p>

---
