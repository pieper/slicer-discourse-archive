# Improve ambient occlusion in volume rendering

**Topic ID**: 33590
**Date**: 2023-12-22
**URL**: https://discourse.slicer.org/t/improve-ambient-occlusion-in-volume-rendering/33590

---

## Post #1 by @LucasGandel (2023-12-22 16:49 UTC)

<p>Opening the discussion for improvements for <strong>transparent rendering</strong>. I find the current results disturbing as AO makes the whole thing appear opaque. Here are potential approaches I’m considering to introduce, any insight would be appreciated.</p>
<ol>
<li>Introduce a SSAO intensity factor to reduce the amount of AO applied on the model</li>
<li>Introduce a flag to use the fragment opacity value as an intensity factor to reduce the amount of AO based on the pixel transparency</li>
</ol>
<p>This is how it would look like. From left to right:</p>
<ol>
<li>Current rendering with SSAO enabled (equivalent to Approach 1. with a factor of 1.0)</li>
<li>Approach 1. with a factor of 0.5</li>
<li>Approach 2. (It could also be combined with Approach 1., but here the factor would be 1.0)</li>
<li>Current rendering with SSAO disabled<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/6/f6cf12f44ee4449f7df04a3694240a5a57c61cce.jpeg" data-download-href="/uploads/short-url/zdn6VOPOZwsxTutJlbACe7zYxKS.jpeg?dl=1" title="comp.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6cf12f44ee4449f7df04a3694240a5a57c61cce_2_690x206.jpeg" alt="comp.PNG" data-base62-sha1="zdn6VOPOZwsxTutJlbACe7zYxKS" width="690" height="206" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6cf12f44ee4449f7df04a3694240a5a57c61cce_2_690x206.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6cf12f44ee4449f7df04a3694240a5a57c61cce_2_1035x309.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/6/f6cf12f44ee4449f7df04a3694240a5a57c61cce_2_1380x412.jpeg 2x" data-dominant-color="C6BFB7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">comp.PNG</span><span class="informations">1920×575 89.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></li>
</ol>

---

## Post #2 by @lassoan (2024-01-02 21:16 UTC)

<p>I see some strange effects with transparent surfaces, but I’m not sure if they are the same that you are describing.</p>
<p>I see two main issues:</p>
<ul>
<li>Darkening: where opacity of a semi-transparent surface reaches the volume opacity threshold the image becomes much darker.</li>
<li>Only color is coming through: the semi-transparent region’s surface seems to determine the surface normal (the surface texture of the structure behind is not visible, as if the semi-transparent surface was opaque), while the structure behind can strongly change the color.</li>
</ul>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/e/5ecc02eec2171f8649858755dac3ffa95ae6f9c3.jpeg" data-download-href="/uploads/short-url/dwBYqWfcQ3F3O6WWevSH5q9gtUL.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ecc02eec2171f8649858755dac3ffa95ae6f9c3_2_690x371.jpeg" alt="image" data-base62-sha1="dwBYqWfcQ3F3O6WWevSH5q9gtUL" width="690" height="371" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ecc02eec2171f8649858755dac3ffa95ae6f9c3_2_690x371.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ecc02eec2171f8649858755dac3ffa95ae6f9c3_2_1035x556.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/5/e/5ecc02eec2171f8649858755dac3ffa95ae6f9c3_2_1380x742.jpeg 2x" data-dominant-color="887F94"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1493×803 100 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Making the opacity value scale the AO may be a good solution. Instead of using a single threshold value, we would use a ramp function. “Volume opacity threshold” could specify the center of the ramp function, and a new “volume opacity window” could specify the width of the ramp:</p>
<ul>
<li>AO intensity factor = 0 if fragment opacity &lt;= threshold - window/2</li>
<li>AO intensity factor = 1 if fragment opacity &gt;= threshold + window/2</li>
<li>AO intensity factor is linearly interpolated between</li>
</ul>
<p>Can you push your experimental changes to github/gitlab so that I can experiment with them?</p>

---

## Post #3 by @LucasGandel (2024-01-03 16:30 UTC)

<p>Thank you so much for your wonderful insight as always. I love the idea of using a ramp function for scaling AO, I will try to play around with it and will update.<br>
In the meantime, here is a WIP change where I hardcoded the scaling of AO for both approaches I presented in my previous post: <a href="https://gitlab.kitware.com/LucasGandelKitware/vtk/-/commit/e0781fd62b197c110cccacad5c12f1566cf24d26" class="inline-onebox" rel="noopener nofollow ugc">WIP: Improve SSAO for translucent volumes (e0781fd6) · Commits · Lucas Gandel / VTK · GitLab</a></p>
<p>I confirm we are on the same page about “Darkening”, and scaling AO with a good approach should fix this.<br>
Regarding “Only color is coming through”, I confirm this is a limitation of the approach, the semi-transparent surface writes to the depth buffer as soon as the opacity threshold is reached, anything behind is “occluded” in the depth texture. However, this side-effect is probably even more visible because AO is too strong, I need to play a bit with it to be sure, as I don’t reproduce such strong artefacts for now.</p>

---

## Post #4 by @LucasGandel (2024-01-16 14:30 UTC)

<p>I have updated the WIP branch referenced in the previous post to provide a fixed version of the second approach: ssao contribution premultiplied by the sample opacity.<br>
One can now call <code>vtkSSAOPass::VolumeOpacityPremultipliedOn()</code> to scale down the SSAO intensity with the opacity value of the sample that writes to the depth buffer.<br>
From left to right: VolumeOpacityPremultipliedOff, VolumeOpacityPremultipliedOn, SSAO disabled<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/486a415fb23f2d1c4f81f5f9b6e398d38ad0e824.jpeg" data-download-href="/uploads/short-url/akC1NgpRy0ihO7nmDoFjVVEqQkI.jpeg?dl=1" title="comp.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/486a415fb23f2d1c4f81f5f9b6e398d38ad0e824_2_690x264.jpeg" alt="comp.PNG" data-base62-sha1="akC1NgpRy0ihO7nmDoFjVVEqQkI" width="690" height="264" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/486a415fb23f2d1c4f81f5f9b6e398d38ad0e824_2_690x264.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/486a415fb23f2d1c4f81f5f9b6e398d38ad0e824_2_1035x396.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/8/486a415fb23f2d1c4f81f5f9b6e398d38ad0e824_2_1380x528.jpeg 2x" data-dominant-color="887D70"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">comp.PNG</span><span class="informations">1920×737 99.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This approach is almost equivalent to multiplying the SSAO intensity by the VolumeOpacityThreshold value and results in almost no SSAO being applied if the volume opacity is very low. I think this is a good improvement towards enabling SSAO by default for volumes.</p>
<p>Besides that, I am still investigating how to improve further the approach, to try to work around the limitation that only color is coming through. Using a window with a linear ramp for the opacity threshold, or even multiple contour values as the existing isosurface blending mode, does not help because we can only write one voxel depth value in the depth texture…</p>

---

## Post #5 by @lassoan (2024-01-17 23:45 UTC)

<p>Thanks for the update, it looks promising!</p>
<p>Can you post some pictures about the effect of <code>IntensityScale</code> value?</p>
<p>I’m wondering if we adding scaling&amp;offset instead of just scaling would allow to achieve nicer rendering, i.e., instead of the current</p>
<pre><code>gl_FragData[0] = vec4(vec3(1.0 - occlusion * "&lt;&lt; this-&gt;IntensityScale &lt;&lt;"), 1.0);
</code></pre>
<p>could we get better results by using this (probably we also need to clamp the result to 0…1 range):</p>
<pre><code>gl_FragData[0] = vec4(vec3(1.0 - (occlusion - " &lt;&lt; this-&gt;IntensityOffset &lt;&lt; ") * "&lt;&lt; this-&gt;IntensityScale &lt;&lt;"), 1.0);
</code></pre>

---

## Post #6 by @lassoan (2024-01-18 22:51 UTC)

<p><a class="mention" href="/u/lucasgandel">@LucasGandel</a> I’ve experimented with your code a bit and I think that IntensityScale property is not used optimally. If we use scaling &lt; 1 values then the shadows are just become too weak - almost no shadowing occurs. However, using scaling &gt; 1 values seem useful, as they can increase darkening. But we would not want to darken values that are below the VolumeOpacityThreshold, because that would just make the entire image dark. To solve this, I would propose to scale around the VolumeOpacityThresholdValue.</p>
<p>Currently in your branch (everything gets darker as scaling increases):</p>
<pre><code>"  gl_FragData[0] = vec4(vec3(1.0 - occlusion * " &lt;&lt; this-&gt;"  gl_FragData[0] = vec4(vec3(1.0 - (occlusion - " &lt;&lt; this-&gt;VolumeOpacityThreshold &lt;&lt; ") * " &lt;&lt; this-&gt;IntensityScale &lt;&lt; "), 1.0); \n"; &lt;&lt; "), 1.0); \n";
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/9/d9db4c2b09e7684eb5693b6156021c95c0eadea1.jpeg" data-download-href="/uploads/short-url/v5fs8IQLqEKCLQSIm1ZVxqIiPlf.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9db4c2b09e7684eb5693b6156021c95c0eadea1_2_690x180.jpeg" alt="image" data-base62-sha1="v5fs8IQLqEKCLQSIm1ZVxqIiPlf" width="690" height="180" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9db4c2b09e7684eb5693b6156021c95c0eadea1_2_690x180.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9db4c2b09e7684eb5693b6156021c95c0eadea1_2_1035x270.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/9/d9db4c2b09e7684eb5693b6156021c95c0eadea1_2_1380x360.jpeg 2x" data-dominant-color="7D6B71"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×502 146 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Proposed (only occluded regions get darker with increased scaling):</p>
<pre><code>"  gl_FragData[0] = vec4(vec3(1.0 - clamp((occlusion - " &lt;&lt; this-&gt;VolumeOpacityThreshold &lt;&lt;" ) * "&lt;&lt; this-&gt;IntensityScale &lt;&lt;", 0.0, 1.0)), 1.0); \n";
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/648e836476e485b60356ee71ac606f4f81867b0f.jpeg" data-download-href="/uploads/short-url/elz4YACrrTGzHS3oiM1ZK4e2pun.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/648e836476e485b60356ee71ac606f4f81867b0f_2_690x183.jpeg" alt="image" data-base62-sha1="elz4YACrrTGzHS3oiM1ZK4e2pun" width="690" height="183" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/648e836476e485b60356ee71ac606f4f81867b0f_2_690x183.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/648e836476e485b60356ee71ac606f4f81867b0f_2_1035x274.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/4/648e836476e485b60356ee71ac606f4f81867b0f_2_1380x366.jpeg 2x" data-dominant-color="8D7677"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×511 160 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The set function of IntensityScale also needs to be changed to allow &gt;1 values (range of 0.0 to about 5.0 should suffice).</p>
<p>I have not looked at the OpacityPremultiplied option yet.</p>

---

## Post #7 by @LucasGandel (2024-01-19 13:48 UTC)

<p>This is brilliant <a class="mention" href="/u/lassoan">@lassoan</a>, thank you so much for working on this, this looks like great improvements. I will try to experiment with your code today and see how it behaves with premultiplied alpha.</p>

---

## Post #8 by @lassoan (2024-01-19 16:27 UTC)

<p>I have tried the OpacityPremultiplied option but I could not really find any useful applications of it, as the improved IntensityScale option already provides much more stable control over how transparent regions are renderered.</p>
<p>I experimented with tuning how scale is computed, but then I realized that I don’t understand how scale value is used to . Could you explain how the <code>scale</code> is used to control “ssao contribution”?</p>
<pre><code>l_ssaoFragNormal = normalize(g_dataNormal) * scale;
</code></pre>
<p>What is <code>l_ssaoFragNormal</code> used for? How the magnitude of the normal controls SSAO contribution?</p>

---

## Post #9 by @LucasGandel (2024-01-19 16:47 UTC)

<p>After a quick try, I can already say that what you proposed is a great improvement.<br>
I agree it makes sense to have a scale &gt; 1.0<br>
I also think using an offset value is a great improvements. Coupled with the scale &gt; 1, it offers some kind of control over the “slope” of the shadow intensity.<br>
However, I think using a separate variable as in your 1st proposition (IntensityOffset) makes more sense than using the VolumeOpacityThreshold value. The side-effect of using VolumeOpacityThreshold is that it shifts the position of the shadow layer. Having both variables should offer more control.<br>
Finally, the premultiplied alpha option is not very useful as the scale can manage reducing the ambient occlusion effect on transparent volumes.</p>
<p>Just saw your feedback. Basically the magnitude of the normal is used to “encode” the raycast sample opacity value. The idea was to multiply the occlusion value with the alpha value of the sample (which is actually different from using the fragment (screenspace) alpha value as I initially implemented). Because the sample alpha value is only accessible during the raycasting of the volume and not in the SSAO texture where the occlusion is computed, I decided to encode it in the normal magnitude. It’s just a way to avoid adding additional textures to pass float values to the SSAO pass.</p>

---

## Post #10 by @LucasGandel (2024-01-22 16:05 UTC)

<p>Using the gradient (normal magnitude) instead of the opacity value should also be considered at some point. (i.e. replacing <code>"if (!g_skip &amp;&amp; g_fragColor.a &gt;"</code> with <code>"if (!g_skip &amp;&amp; length(g_dataNormal) &gt; "</code>). I am currently experimenting with it to improve rendering of highly transparent volumes. It seems to provide more controls for highlighting different structures when changing the VolumeOpacityThreshold. Here is an example with different VolumeOpacityThreshold values but without scaling down the shadows.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6260d4946c186c74eae73db6bce8737ef6e19a3.jpeg" data-download-href="/uploads/short-url/uyrHG4L9UI9r7bH8tsoansiSW0b.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6260d4946c186c74eae73db6bce8737ef6e19a3_2_235x250.jpeg" alt="image" data-base62-sha1="uyrHG4L9UI9r7bH8tsoansiSW0b" width="235" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6260d4946c186c74eae73db6bce8737ef6e19a3_2_235x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6260d4946c186c74eae73db6bce8737ef6e19a3_2_352x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6260d4946c186c74eae73db6bce8737ef6e19a3_2_470x500.jpeg 2x" data-dominant-color="726961"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1433×1523 95.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/a/8a0e327d65f69787f61fed6f053ccc8dd9a943a7.jpeg" data-download-href="/uploads/short-url/jHij7fDk2K74bNRsPyr2scKqVhl.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a0e327d65f69787f61fed6f053ccc8dd9a943a7_2_244x250.jpeg" alt="image" data-base62-sha1="jHij7fDk2K74bNRsPyr2scKqVhl" width="244" height="250" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a0e327d65f69787f61fed6f053ccc8dd9a943a7_2_244x250.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a0e327d65f69787f61fed6f053ccc8dd9a943a7_2_366x375.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/a/8a0e327d65f69787f61fed6f053ccc8dd9a943a7_2_488x500.jpeg 2x" data-dominant-color="797168"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1590×1627 92.2 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>My ultimate goal is to find an approach that produces acceptable results by default, without having to tune parameters of the transfer function.</p>

---

## Post #11 by @lassoan (2024-01-22 16:39 UTC)

<p>Does <code>g_fragColor.a</code> already contain the gradient opacity mapping result? If yes, then it should not be necessary to use the raw gradient magnitude value, but the desired effect should be possible to achieve by tuning the gradient opacity function.</p>
<aside class="quote no-group" data-username="LucasGandel" data-post="10" data-topic="33590">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lucasgandel/48/18202_2.png" class="avatar"> LucasGandel:</div>
<blockquote>
<p>My ultimate goal is to find an approach that produces acceptable results by default, without having to tune parameters of the transfer function.</p>
</blockquote>
</aside>
<p>This would be really nice, but it is not impossible to have a single set of rendering parameters (volume rendering transfer functions and SSAO parameters) that work well for a wide range of images. We always work with parameter sets optimized for a certain clinical task for a certain image type. Still, we need to expose at least an intensity offset value in the scalar opacity transfer function, because image intensity values are standardized mostly for just CT (but even then there is some variety due contrast dilution, bone density, etc.). A feasible goal is to have a parameter set for showing skin surface on CT, another parameter set for showing bones in CT, and another for soft tissues on CT.</p>
<p>I would try to prioritize for finding independent SSAO parameters, i.e., each parameter affecting only a single aspect of the rendering result (no crosstalk between them) and affecting only the darkened regions. For example, if the user adjusts “ssao intensity” parameter then it should not be necessary to adjust the “ssao volume opacity threshold”, or to adjust lighting to preserve the overall brightness of the rendered image. This would allow the user to start from a parameter set and then tune just 1-2 parameters in a couple of seconds to achieve the desired visualization. I think most of the SSAO parameters are already mostly independent, we just need to make sure any new one that we introduce are like that, too.</p>

---
