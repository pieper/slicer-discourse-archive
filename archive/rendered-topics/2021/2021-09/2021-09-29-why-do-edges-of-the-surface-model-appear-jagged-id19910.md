---
topic_id: 19910
title: "Why Do Edges Of The Surface Model Appear Jagged"
date: 2021-09-29
url: https://discourse.slicer.org/t/19910
---

# Why do edges of the surface model appear jagged?

**Topic ID**: 19910
**Date**: 2021-09-29
**URL**: https://discourse.slicer.org/t/why-do-edges-of-the-surface-model-appear-jagged/19910

---

## Post #1 by @slicer365 (2021-09-29 11:55 UTC)

<p>This is a needle model I created using Slicer, but when I rotate the model, I can see a lot of jaggies at certain angles. how to avoid this？</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/0/b096ee31a5b466bce7e46b742aab7ab083dd1acd.png" alt="捕获" data-base62-sha1="pcboUsU8d3TuzosvrE7SZicNilT" width="220" height="455"></p>

---

## Post #2 by @lassoan (2021-09-29 13:05 UTC)

<p>This is due to the resolution of your monitor and the fact that one pixel is always assigned to one object (the model or the background) and the appearance of the edge of the model is very different.</p>
<p>Possible solutions:</p>
<ol>
<li>Use higher-resolution screen</li>
</ol>
<p>On a higher-resolution screen, size of a voxel is much smaller, so individual voxels are much less visible.</p>
<ol start="2">
<li>
<p>Reduce the contrast between the object boundary and background. If you use shading, edges of models are dark, so a dark background will make jagged model edges disappear. Alternatively, you can edit model lighting settings to make make the edges of the model appear brighter.</p>
</li>
<li>
<p>Use anti-aliasing - make one pixel rendered from multiple 3D positions. Multi-sampling causes problems with hardware-accelerated point picking and occlusion detection and screen-space methods, such as FXAA can cause rendering artifacts (may suppress some lines and corners).</p>
</li>
</ol>
<p>If rendering artifacts do not cause problem in your application then you can enable FXAA anti-aliasing like this:</p>
<pre data-code-wrap="python"><code class="lang-python">view = slicer.app.layoutManager().threeDWidget(0).threeDView()
# for slice view: view = slicer.app.layoutManager().sliceWidget('Red').sliceView()
renderWindow = view.renderWindow()
renderers = renderWindow.GetRenderers()
for renderer in renderers:
    renderer.UseFXAAOn()

slicer.util.forceRenderAllViews()
</code></pre>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c36d022a5cef142461ba888ec32a125ac962a54c.png" data-download-href="/uploads/short-url/rSOEGKLPU1GmZVeIYKUMnZjdkcI.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c36d022a5cef142461ba888ec32a125ac962a54c_2_690x322.png" alt="image" data-base62-sha1="rSOEGKLPU1GmZVeIYKUMnZjdkcI" width="690" height="322" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c36d022a5cef142461ba888ec32a125ac962a54c_2_690x322.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/3/c36d022a5cef142461ba888ec32a125ac962a54c_2_1035x483.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/3/c36d022a5cef142461ba888ec32a125ac962a54c.png 2x" data-dominant-color="B3B4BD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1037×484 34.8 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---
