# 2D visualization in Slicer (Spectrogram, contour plot)

**Topic ID**: 18727
**Date**: 2021-07-14
**URL**: https://discourse.slicer.org/t/2d-visualization-in-slicer-spectrogram-contour-plot/18727

---

## Post #1 by @keri (2021-07-14 11:02 UTC)

<p>Hi,</p>
<p>I’m searching for information about 2D visualization in Slicer. For example I can see this <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Plots" rel="noopener nofollow ugc">doc page</a> but I can’t understand what library is used for 2D plotting? Is it VTK?</p>
<p>In near future I have to decide what library to use to display some matrices in form of Spectrogram and contour plot <a href="https://qwt.sourceforge.io/spectrogramscreenshots.html" rel="noopener nofollow ugc">like in the pictures here</a></p>
<p>Previously I had some experience of working with <a href="https://qwt.sourceforge.io/index.html" rel="noopener nofollow ugc">QWT</a> library but now when I work with Slicer I think I could replace QWT by some internal Slicer’s visualization library (probably VTK or some other)</p>

---

## Post #2 by @pieper (2021-07-14 14:52 UTC)

<p>Yes, Plotting in Slicer uses VTK (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/FAQ#What_is_the_difference_between_Slicer_Plot_and_Chart_.3F" class="inline-onebox">Documentation/Nightly/Developers/FAQ - Slicer Wiki</a>).</p>
<p>I never used QWT.  In theory it looks like it could be added to Slicer’s Qt build but I’m not sure how much work that would vs making the same features in VTK.</p>
<p>Slicer’s <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/transforms.html#display">transform display functions</a> are a good example of what you can do in Slicer/VTK.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6433f542dbbb78dfe8ba2702120a5bcfbd74823e.jpeg" data-download-href="/uploads/short-url/eir48e9BNLtISD8AUVcQ7BBkXmK.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6433f542dbbb78dfe8ba2702120a5bcfbd74823e_2_690x411.jpeg" alt="image" data-base62-sha1="eir48e9BNLtISD8AUVcQ7BBkXmK" width="690" height="411" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/6/6433f542dbbb78dfe8ba2702120a5bcfbd74823e_2_690x411.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6433f542dbbb78dfe8ba2702120a5bcfbd74823e.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/4/6433f542dbbb78dfe8ba2702120a5bcfbd74823e.jpeg 2x" data-dominant-color="959094"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">856×511 116 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @keri (2021-07-14 15:17 UTC)

<p>Thank you, then I will try VTK for 2D plotting</p>
<p>By the way does Slicer use Matplotlib? Just wondering</p>

---

## Post #4 by @pieper (2021-07-14 18:34 UTC)

<aside class="quote no-group" data-username="keri" data-post="3" data-topic="18727">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/keri/48/11618_2.png" class="avatar"> keri:</div>
<blockquote>
<p>By the way does Slicer use Matplotlib? Just wondering</p>
</blockquote>
</aside>
<p>It’s a bit clunky but you can do it with something like this:<br>
<a href="https://www.slicer.org/wiki/Slicer3:Python#Matplotlib_plotting_functionality" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Slicer3:Python#Matplotlib_plotting_functionality</a></p>
<p>Or you can use SlicerJupyter.</p>

---

## Post #5 by @lassoan (2021-07-14 23:41 UTC)

<p>You can create static plots using any of the Python plotting packages (there are literally hundreds of them). Integrating interactions is a bit more tricky.</p>
<p><a href="https://qwt.sourceforge.io/#screenshotsonmainpage">Visual appearance of QWT plots</a> are about just as rudimentary as VTK (looks like designed by engineers and not artists). So, I’m not sure it would be a significant step up from VTK, and it would require some work to connect it with VTK data structures (that Slicer uses not just for visualization but as data model) and with the Slicer GUI.</p>
<p>We use VTK plots for real-time spectrogram plots of diffuse reflective spectroscopy, see for example here:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="ag7fWY27lus" data-video-title="Navigated optical spectroscopy" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=ag7fWY27lus" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/ag7fWY27lus/maxresdefault.jpg" title="Navigated optical spectroscopy" width="" height="">
  </a>
</div>

<p>It may be better to use VTK plots for interactive visualization and some Python packages for large, complex, static plots.</p>

---
