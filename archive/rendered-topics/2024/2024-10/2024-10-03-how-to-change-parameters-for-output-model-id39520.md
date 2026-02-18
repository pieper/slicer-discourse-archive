# How to change parameters for output model?

**Topic ID**: 39520
**Date**: 2024-10-03
**URL**: https://discourse.slicer.org/t/how-to-change-parameters-for-output-model/39520

---

## Post #1 by @JonNithal (2024-10-03 13:51 UTC)

<p>Hello,</p>
<p>I am an orthopedic specialist in the United States, specializing in knee replacements. Our organization has been using Mimics for years, but we decided to switch to an alternative due to the increasing cost of the software. I came across your free 3D Slicer software, and it has helped me visualize some of my cases. However, I am facing a slight difficulty when visualizing a model.When I click on the “Export Visible Segment to Model” option under the Data section in Slicer, I expected to see options to apply adjustments to the model before converting it. From a surgeon’s perspective, having some control over the final model based on parameters would be beneficial.</p>
<p>Mimics parameters:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/376ca3dadca58f350cc685ade02553d196551265.png" data-download-href="/uploads/short-url/7Uj1jcXiYKldzeK0BDUS8q6Dd5j.png?dl=1" title="IMG_20241003_152448" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/376ca3dadca58f350cc685ade02553d196551265_2_690x407.png" alt="IMG_20241003_152448" data-base62-sha1="7Uj1jcXiYKldzeK0BDUS8q6Dd5j" width="690" height="407" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/7/376ca3dadca58f350cc685ade02553d196551265_2_690x407.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/376ca3dadca58f350cc685ade02553d196551265.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/376ca3dadca58f350cc685ade02553d196551265.png 2x" data-dominant-color="F9F9F9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20241003_152448</span><span class="informations">800×472 195 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>As I am new to Slicer, is it possible to adjust parameters such as the number of large shells (shell reduction), triangle reduction (tolerance, iterations, edge angle, etc.), matrix reduction (XY or Z reduction), etc., when exporting a visible segment to a model?</p>
<p>Thank you for any help.</p>

---

## Post #2 by @lassoan (2024-10-03 14:00 UTC)

<p>This is a typical example of MIMICS combining several simple, independent operations into a single very complex operation. In Slicer, exporting to mesh is independent from mesh reduction and smoothing, because several mesh reduction and smoothing operations are available in Slicer, and the user is free to choose between them.</p>
<p>You can smooth the segmentation before export in Segment Editor, using <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#smoothing">Smoothing effect</a>. You can adjust Smoothing factor during mesh generation using the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#main-options"><code>Show 3D</code> button</a>. You can smooth and decimate the exported model using <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/surfacetoolbox.html">Surface Toolbox</a> module.</p>

---

## Post #3 by @JonNithal (2024-10-04 05:29 UTC)

<p>Thank you for your reply.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="39520">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>This is a typical example of MIMICS combining several simple, independent operations into a single very complex operation. In Slicer, exporting to mesh is independent from mesh reduction and smoothing, because several mesh reduction and smoothing operations are available in Slicer, and the user is free to choose between them.</p>
</blockquote>
</aside>
<p>I see, that makes sense now.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="39520">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can smooth the segmentation before export in Segment Editor, using <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#smoothing" rel="noopener nofollow ugc">Smoothing effect</a>. You can adjust Smoothing factor during mesh generation using the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#main-options" rel="noopener nofollow ugc"><code>Show 3D</code> button</a>. You can smooth and decimate the exported model using <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/surfacetoolbox.html" rel="noopener nofollow ugc">Surface Toolbox</a> module.</p>
</blockquote>
</aside>
<p>What about matrix reduction and interpolation? I noticed Slicer performs gray value interpolation, if I am correct.</p>
<p>I have installed the Surface Toolbox but didn’t see an option for matrix reduction or interpolation.</p>

---

## Post #4 by @JonNithal (2024-10-07 04:05 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> , Can you please answer on this matter?</p>

---

## Post #5 by @muratmaga (2024-10-07 04:17 UTC)

<aside class="quote no-group" data-username="JonNithal" data-post="3" data-topic="39520">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/j/6de8d8/48.png" class="avatar"> JonNithal:</div>
<blockquote>
<p>I have installed the Surface Toolbox but didn’t see an option for matrix reduction or interpolation.</p>
</blockquote>
</aside>
<p>We are not experts in MIMICS, you have to explain to use what matrix reduction does (it simply seems like independent reduction of each axis, I don’t know what “matrix” refers to in this context), so that we can guide you.</p>

---

## Post #6 by @JonNithal (2024-10-07 08:53 UTC)

<p>I use matrix reduction to reduce the resolution in either the X, Y, or Z dimension. The values define how much reduction we want to apply to decrease the computational load while maintaining acceptable model quality.</p>

---

## Post #7 by @muratmaga (2024-10-07 16:24 UTC)

<p>Again I am not a mimics person, but from my experience that type of anisotropic resampling cannot be applied to the surface models. My guess is, similar to <a class="mention" href="/u/lassoan">@lassoan</a> previously said, Mimics is downsampling the voxel data first, and then making the model, which are explicitly separate operations in Slicer.</p>
<p>You can export your model, and then use the decimate option to reduce the number of faces. This is far more simple. You can dial down the decimation to determine the model quality (no decimation to 99% decimation).</p>
<p>However, if you want to do exactly do what mimics is doing, you can do that as well. It will be separate steps. You can export your segmentation as a labelmap, then use the <code>ResampleScalarVolume</code> to downsample each axis independently, and then from that you use the <code>ModelMaker</code> module to create the model from the downsampled labelmap.</p>

---
