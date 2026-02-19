---
topic_id: 30564
title: "Displaying A Colorbar Across Viewers For Diffusion Scalar Ma"
date: 2023-07-12
url: https://discourse.slicer.org/t/30564
---

# Displaying a colorbar across viewers for diffusion scalar maps on tractography data

**Topic ID**: 30564
**Date**: 2023-07-12
**URL**: https://discourse.slicer.org/t/displaying-a-colorbar-across-viewers-for-diffusion-scalar-maps-on-tractography-data/30564

---

## Post #1 by @jhlegarreta (2023-07-12 19:19 UTC)

<p>Hi,<br>
is it possible to add a colorbar across the Slicer viewers (just as shown in <a href="https://discourse.slicer.org/t/how-to-find-a-default-colorbar-unit-or-calibrate-in-mm/22501/6">the image in this post</a> for another type of data) when we load some tractography data and load an associated scalar map, e.g. FA? If yes, how can this be done? At the very least in the 3D viewer?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/b/4b60c060c1715fed548bc27e495dc1b132b0f164.png" data-download-href="/uploads/short-url/aKP69XEurPfyVd72NDDcfsvRsXy.png?dl=1" title="slicer_tractography_scalarmap_color_highlight" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b60c060c1715fed548bc27e495dc1b132b0f164_2_690x402.png" alt="slicer_tractography_scalarmap_color_highlight" data-base62-sha1="aKP69XEurPfyVd72NDDcfsvRsXy" width="690" height="402" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b60c060c1715fed548bc27e495dc1b132b0f164_2_690x402.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b60c060c1715fed548bc27e495dc1b132b0f164_2_1035x603.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/4/b/4b60c060c1715fed548bc27e495dc1b132b0f164_2_1380x804.png 2x" data-dominant-color="9C9DB7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">slicer_tractography_scalarmap_color_highlight</span><span class="informations">1856×1082 442 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks</p>

---

## Post #2 by @lassoan (2023-07-12 19:23 UTC)

<p>You can show the color legend in slice or 3D views as described <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/colors.html#show-color-legend">here</a>.</p>

---

## Post #3 by @jhlegarreta (2023-07-13 20:26 UTC)

<p>Thanks Andras, but I mean the scalar values of streamlines, not the values corresponding to any underlying volume or structural image. Maybe I did not get it right, but following the linked instructions, I did not find the described context menus, options. Also, being able to click on a point and knowing the value of the scalar value associated to the streamline vertex would be ideal. Hope the two videos in here illustrate it:</p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37c2bdb1d746cc52a6cc3c7c04199c92151a29de.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37c2bdb1d746cc52a6cc3c7c04199c92151a29de.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37c2bdb1d746cc52a6cc3c7c04199c92151a29de.mp4</a>
    </video>
  </div><p></p>
<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/691a5c4cd26742a0cf62b11b080cfd770f7164ba.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/691a5c4cd26742a0cf62b11b080cfd770f7164ba.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/9/691a5c4cd26742a0cf62b11b080cfd770f7164ba.mp4</a>
    </video>
  </div><p></p>

---

## Post #4 by @lassoan (2023-07-15 15:12 UTC)

<p>I think tracts are models, so you can use it Mable their color legend in Models module. In addition to that, you can display color legend for any color table in Colors module, but then you need to set the scalar range manually.</p>

---

## Post #5 by @jhlegarreta (2023-07-17 23:43 UTC)

<blockquote>
<p>in Models module</p>
</blockquote>
<p>OK, thanks Andras. That (<code>Models</code>; <code>ColorLegend</code>) seems to work for the 3D.</p>
<p>However, it only works for lines and not tubes. Thus at times, if we are unaware that lines are being displayed, we will be showing a colorbar that does not correspond to what we think we are looking at. And at times, we prefer to get more insight using the tube visualization.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/f/cfc4388b3208b4a2ee62d6ca3ea78b172444faf5.png" data-download-href="/uploads/short-url/tDZeJAAvvX9ItTIibTiLAvIzuhn.png?dl=1" title="Slicer_color_by_fa1_models_line_vs_tube_line_cmap" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfc4388b3208b4a2ee62d6ca3ea78b172444faf5_2_517x294.png" alt="Slicer_color_by_fa1_models_line_vs_tube_line_cmap" data-base62-sha1="tDZeJAAvvX9ItTIibTiLAvIzuhn" width="517" height="294" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfc4388b3208b4a2ee62d6ca3ea78b172444faf5_2_517x294.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfc4388b3208b4a2ee62d6ca3ea78b172444faf5_2_775x441.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/f/cfc4388b3208b4a2ee62d6ca3ea78b172444faf5_2_1034x588.png 2x" data-dominant-color="A2A7BE"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_color_by_fa1_models_line_vs_tube_line_cmap</span><span class="informations">1856×1055 474 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Seeing the wrong correspondence of colorbar values and data along tubes:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a5ca0ea41712cd2bb7dcfa0cc565552b761e9fa3.jpeg" data-download-href="/uploads/short-url/nEDGFhMECqqp1oq47Tyq9vHomoH.jpeg?dl=1" title="Slicer_color_by_fa1_tubes_colorbar_corr_lines" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5ca0ea41712cd2bb7dcfa0cc565552b761e9fa3_2_517x294.jpeg" alt="Slicer_color_by_fa1_tubes_colorbar_corr_lines" data-base62-sha1="nEDGFhMECqqp1oq47Tyq9vHomoH" width="517" height="294" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5ca0ea41712cd2bb7dcfa0cc565552b761e9fa3_2_517x294.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5ca0ea41712cd2bb7dcfa0cc565552b761e9fa3_2_775x441.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/5/a5ca0ea41712cd2bb7dcfa0cc565552b761e9fa3_2_1034x588.jpeg 2x" data-dominant-color="9BA2B5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_color_by_fa1_tubes_colorbar_corr_lines</span><span class="informations">1856×1055 443 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Seeing the true correspondence of colorbar values and data along lines:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fa0779de93c4b3cb3db504f215f8e8c0ffbe1c74.png" data-download-href="/uploads/short-url/zFRnRRJ0XOYnvhTPWoVtQtYUT2Y.png?dl=1" title="Slicer_color_by_fa1_lines_colorbar_corr_lines" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa0779de93c4b3cb3db504f215f8e8c0ffbe1c74_2_517x294.png" alt="Slicer_color_by_fa1_lines_colorbar_corr_lines" data-base62-sha1="zFRnRRJ0XOYnvhTPWoVtQtYUT2Y" width="517" height="294" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa0779de93c4b3cb3db504f215f8e8c0ffbe1c74_2_517x294.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa0779de93c4b3cb3db504f215f8e8c0ffbe1c74_2_775x441.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fa0779de93c4b3cb3db504f215f8e8c0ffbe1c74_2_1034x588.png 2x" data-dominant-color="A2AABD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_color_by_fa1_lines_colorbar_corr_lines</span><span class="informations">1856×1055 205 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>And it does not work for the 2D: the context menu shows no option to show the colorbar.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/7/b74607caca52c26019022fb3457c5af3da507595.png" data-download-href="/uploads/short-url/q9jpPsJt4D1hx9tMnK7ECg30Pl3.png?dl=1" title="Slicer_color_by_fa1_models_2d_context" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b74607caca52c26019022fb3457c5af3da507595_2_517x294.png" alt="Slicer_color_by_fa1_models_2d_context" data-base62-sha1="q9jpPsJt4D1hx9tMnK7ECg30Pl3" width="517" height="294" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b74607caca52c26019022fb3457c5af3da507595_2_517x294.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b74607caca52c26019022fb3457c5af3da507595_2_775x441.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/7/b74607caca52c26019022fb3457c5af3da507595_2_1034x588.png 2x" data-dominant-color="9C9FA9"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Slicer_color_by_fa1_models_2d_context</span><span class="informations">1853×1053 408 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<blockquote>
<p>Colors module,</p>
</blockquote>
<p>Where is this module ? I cannot find it.</p>
<aside class="quote no-group" data-username="jhlegarreta" data-post="3" data-topic="30564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>Also, being able to click on a point and knowing the value of the scalar value associated to the streamline vertex would be ideal. Hope the two videos in here illustrate it:</p>
</blockquote>
</aside>
<p>What about this ?</p>

---

## Post #6 by @lassoan (2023-07-19 15:51 UTC)

<aside class="quote no-group" data-username="jhlegarreta" data-post="5" data-topic="30564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>OK, thanks Andras. That (<code>Models</code>; <code>ColorLegend</code>) seems to work for the 3D.</p>
</blockquote>
</aside>
<p>It should work for all the views where the model is displayed. If it does not seem to work in the latest Slicer Stable Release then try in the latest Slicer Preview Release, too.</p>
<aside class="quote no-group" data-username="jhlegarreta" data-post="5" data-topic="30564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>Thus at times, if we are unaware that lines are being displayed</p>
</blockquote>
</aside>
<p>You can display any number of data nodes and color legends, so it is possible that you can see unrelated data and color legend in the same view. By default, the node name is displayed in the color legend’s title, which should help in avoiding accidental mixups.</p>
<aside class="quote no-group" data-username="jhlegarreta" data-post="5" data-topic="30564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<p>However, it only works for lines and not tubes.</p>
</blockquote>
</aside>
<p>It seems that tubes does not use the default color mapping, probably because it has some additonal modes. It should be possible to update the code to play nice with the color bar (at least store the color table and color display range in the display node base class). Please create an issue for this in the SlicerDMRI extension’s issue tracker.</p>

---

## Post #7 by @jhlegarreta (2023-07-24 16:38 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="30564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It should work for all the views where the model is displayed. If it does not seem to work in the latest Slicer Stable Release then try in the latest Slicer Preview Release, too.</p>
</blockquote>
</aside>
<p>I cannot afford trying another release, unfortunately, Andras.</p>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="30564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can display any number of data nodes and color legends, so it is possible that you can see unrelated data and color legend in the same view. By default, the node name is displayed in the color legend’s title, which should help in avoiding accidental mixups.</p>
</blockquote>
</aside>
<p>I repeatedly tested the feature to check the behavior, and it was not showing the colorbar corresponding to the <code>Tube</code> display mode.</p>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="30564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>It seems that tubes does not use the default color mapping, probably because it has some additonal modes. It should be possible to update the code to play nice with the color bar (at least store the color table and color display range in the display node base class). Please create an issue for this in the SlicerDMRI extension’s issue tracker.</p>
</blockquote>
</aside>
<p>Here: <a href="https://github.com/Slicer/Slicer/issues/7123" class="inline-onebox" rel="noopener nofollow ugc">Colorbar does not work for streamline tube display mode · Issue #7123 · Slicer/Slicer · GitHub</a></p>

---

## Post #8 by @lassoan (2023-07-24 17:42 UTC)

<aside class="quote no-group quote-modified" data-username="jhlegarreta" data-post="7" data-topic="30564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/jhlegarreta/48/66542_2.png" class="avatar"> jhlegarreta:</div>
<blockquote>
<aside class="quote no-group" data-username="lassoan" data-post="6" data-topic="30564">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can display any number of data nodes and color legends, so it is possible that you can see unrelated data and color legend in the same view. By default, the node name is displayed in the color legend’s title, which should help in avoiding accidental mixups.</p>
</blockquote>
</aside>
<p>I repeatedly tested the feature to check the behavior, and it was not showing the colorbar corresponding to the <code>Tube</code> display mode.</p>
</blockquote>
</aside>
<p>I meant that it in general. Tube display in SlicerDMRI extension is a special case - it had been implemented before color legend feature was added to Slicer core and unfortunately they are not compatible. Until the issue that you created (thank you!) is fixed, you can display a color legend by creating a dummy model node and selecting lookup table and setting the correct scalar range manually.</p>

---
