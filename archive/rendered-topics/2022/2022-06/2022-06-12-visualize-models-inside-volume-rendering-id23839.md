# Visualize models inside volume rendering?

**Topic ID**: 23839
**Date**: 2022-06-12
**URL**: https://discourse.slicer.org/t/visualize-models-inside-volume-rendering/23839

---

## Post #1 by @sunwei921119 (2022-06-12 15:33 UTC)

<p>hello，The enclosed visibility enables the point to perspective in volume rendering. Is there a plug-in that can perspective models in volume rendering?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/787fc9b3d8e09feb79858b48bf82c08b03d96570.jpeg" data-download-href="/uploads/short-url/hbZ50thwphUAFqWXaGQLHXs3yi4.jpeg?dl=1" title="mmexport1655047642883" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/787fc9b3d8e09feb79858b48bf82c08b03d96570_2_453x500.jpeg" alt="mmexport1655047642883" data-base62-sha1="hbZ50thwphUAFqWXaGQLHXs3yi4" width="453" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/787fc9b3d8e09feb79858b48bf82c08b03d96570_2_453x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/787fc9b3d8e09feb79858b48bf82c08b03d96570.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/8/787fc9b3d8e09feb79858b48bf82c08b03d96570.jpeg 2x" data-dominant-color="F3F3F3"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mmexport1655047642883</span><span class="informations">508×560 33.5 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a535316e046f606658c2d643b67259bd32c58f32.jpeg" data-download-href="/uploads/short-url/nzuKooNWAGx5NkhBKRgJeIG2W9c.jpeg?dl=1" title="IMG_20220612_232759" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a535316e046f606658c2d643b67259bd32c58f32_2_523x500.jpeg" alt="IMG_20220612_232759" data-base62-sha1="nzuKooNWAGx5NkhBKRgJeIG2W9c" width="523" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a535316e046f606658c2d643b67259bd32c58f32_2_523x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/a/a535316e046f606658c2d643b67259bd32c58f32_2_784x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/5/a535316e046f606658c2d643b67259bd32c58f32.jpeg 2x" data-dominant-color="534D42"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">IMG_20220612_232759</span><span class="informations">836×799 71.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0cfb5f4b4712551e5229a428d4eb83594c3d99e9.jpeg" data-download-href="/uploads/short-url/1QQi7bgRSY849boOLPsZbigwuLf.jpeg?dl=1" title="mmexport1655047645344" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/c/0cfb5f4b4712551e5229a428d4eb83594c3d99e9.jpeg" alt="mmexport1655047645344" data-base62-sha1="1QQi7bgRSY849boOLPsZbigwuLf" width="681" height="500" data-dominant-color="9B93A8"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">mmexport1655047645344</span><span class="informations">804×590 39.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2022-06-13 04:44 UTC)

<p>Occluded visibility is a feature unique to markups. You can adjust volume rendering transfer functions to make the skull semi-transparent:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f2735f582a8db30f1d97c8bcfc42b789456ef1d3.jpeg" data-download-href="/uploads/short-url/yAOJoq4D3H7rO5bDHshBkQYPYA3.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2735f582a8db30f1d97c8bcfc42b789456ef1d3_2_690x418.jpeg" alt="image" data-base62-sha1="yAOJoq4D3H7rO5bDHshBkQYPYA3" width="690" height="418" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2735f582a8db30f1d97c8bcfc42b789456ef1d3_2_690x418.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2735f582a8db30f1d97c8bcfc42b789456ef1d3_2_1035x627.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f2735f582a8db30f1d97c8bcfc42b789456ef1d3_2_1380x836.jpeg 2x" data-dominant-color="79778F"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×1165 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #3 by @rbumm (2022-06-13 12:10 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a> is there a way to set the “total opacity” of the volume rendering somewhere? If I preset the volume rendering to “CT muscle” and superimpose an airway segmentation, the latter always falls “behind” the volume rendering.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/7/f7408b538515be307de12c6a8f0dab2cc52e792f.jpeg" alt="image" data-base62-sha1="zhidG08FV9kWOJZ6eMx1WP5qY8L" width="612" height="343"></p>

---

## Post #4 by @mau_igna_06 (2022-06-13 12:17 UTC)

<p>Yes but you need to use the VolumeRenderingMapper to set a lablelmapMask</p>

---

## Post #5 by @lassoan (2022-06-13 12:41 UTC)

<aside class="quote no-group" data-username="mau_igna_06" data-post="4" data-topic="23839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mau_igna_06/48/9056_2.png" class="avatar"> mau_igna_06:</div>
<blockquote>
<p>you need to use the VolumeRenderingMapper to set a lablelmapMask</p>
</blockquote>
</aside>
<p>You can achieve the same by using “Mask volume” effect in Segment Editor. However, I’m not sure if this is <a class="mention" href="/u/rbumm">@rbumm</a> is looking for.</p>
<aside class="quote no-group" data-username="rbumm" data-post="3" data-topic="23839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>If I preset the volume rendering to “CT muscle” and superimpose an airway segmentation, the latter always falls “behind” the volume rendering</p>
</blockquote>
</aside>
<p>It is not always behind. Volume rendering and segmentation are composited in 3D. Whatever appears closer to the viewer will occlude what is behind it (as in real life).</p>
<aside class="quote no-group" data-username="rbumm" data-post="3" data-topic="23839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>is there a way to set the “total opacity” of the volume rendering somewhere?</p>
</blockquote>
</aside>
<p>You can make volume rendering more transparent by moving all control points of the opacity transfer function lower (lowering the opacity values associated with each control point). If you think this would be frequently useful then we could add a slider for it to make it much easier to change.</p>

---

## Post #6 by @rbumm (2022-06-13 16:07 UTC)

<p>Thank you, that works quite well !<br>
Reducing the O value by 0.3 in each of the control points made the airways shine through much better.</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/b/eb612a832caccfc5e8ea0aa63751bbab40c4bad7.jpeg" alt="image" data-base62-sha1="xAgnJOR1VFK23djU3KU71Bf47Aj" width="624" height="334"></p>
<p>(source: MONAILabel Task06_Lung dataset)</p>
<p>So yes, it would be great if we would have a slider for general opacity!</p>

---

## Post #7 by @rbumm (2022-06-13 16:50 UTC)

<p>Follow up question, sry:</p>
<p>Anatomical orientation is already very good for a  &lt; 5-minute 3D reconstruction.<br>
Ideally, the thoracic wall would be stripped off the mediastinal volume rendering  block by a convex cutting plane - to get the rip stumps out of view</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aec7fe47aa995a19bfa00ec178f8bfbe6daea8e6.jpeg" data-download-href="/uploads/short-url/oWbyW2DGbyal5dw5pBO68Ntz5Km.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/e/aec7fe47aa995a19bfa00ec178f8bfbe6daea8e6.jpeg" alt="image" data-base62-sha1="oWbyW2DGbyal5dw5pBO68Ntz5Km" width="690" height="464" data-dominant-color="7E6B78"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1076×724 81.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Any idea to do this apart from PRISM rendering, which seems to be not yet working in 5.1?</p>

---

## Post #8 by @pieper (2022-06-13 17:06 UTC)

<p>You can define an arbitrary segmentation (i.e. with scissors) and then use the Mask Volume effect in the segment editor to create a new volume without the ribs or any other structures you don’t want, then volume render the masked volume (use -1000 for the background on a CT to mimic air).  <a href="https://github.com/SlicerIGT/SlicerMarkupsToModel#:~:text=README.md-,Overview,created%3A%20closed%20surfaces%20and%20curves.">Markups To Model</a> could also be helpful for making a free-form shape that can be converted to a segmentation for masking.</p>

---

## Post #9 by @lassoan (2022-06-13 19:28 UTC)

<p>“Markups to model” is also available in the Segment Editor as “Surface cut” effect (provided by SegmentEditorExtraEffects extension).</p>
<p><a class="mention" href="/u/rbumm">@rbumm</a> Is there a specific clinical application for displaying some structures from the CT or it is just for making the visualization nicer/more interesting?</p>
<aside class="quote no-group" data-username="rbumm" data-post="7" data-topic="23839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>Any idea to do this apart from PRISM rendering, which seems to be not yet working in 5.1?</p>
</blockquote>
</aside>
<p>It is working but there are bugs. I’ve submitted a <a href="https://github.com/ETS-vis-interactive/SlicerPRISMRendering/pull/16">fix for chroma depth rendering</a> and submitted issue reports (<a href="https://github.com/ETS-vis-interactive/SlicerPRISMRendering/issues/18">18</a>, <a href="https://github.com/ETS-vis-interactive/SlicerPRISMRendering/issues/19">19</a>, <a href="https://github.com/ETS-vis-interactive/SlicerPRISMRendering/issues/20">20</a>).</p>
<p>There are some nice/interesting effects. For example, without any segmentation or preprocessing, Opacity peeling can render a chest CT like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/2/f277604df31862ab68eb4af0aa827e6fd9cba613.jpeg" data-download-href="/uploads/short-url/yAXjeeBurBAffg2O5ogLXn2qjth.jpeg?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f277604df31862ab68eb4af0aa827e6fd9cba613_2_690x308.jpeg" alt="image" data-base62-sha1="yAXjeeBurBAffg2O5ogLXn2qjth" width="690" height="308" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f277604df31862ab68eb4af0aa827e6fd9cba613_2_690x308.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f277604df31862ab68eb4af0aa827e6fd9cba613_2_1035x462.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f277604df31862ab68eb4af0aa827e6fd9cba613_2_1380x616.jpeg 2x" data-dominant-color="606C72"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1920×859 147 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>First you need to enable Volume Rendering in PRISM then choose the <code>CT-Air</code> preset in Volume  Rendering module.</p>

---

## Post #10 by @rbumm (2022-06-14 05:16 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="9" data-topic="23839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a class="mention" href="/u/rbumm">@rbumm</a> Is there a specific clinical application for displaying some structures from the CT or it is just for making the visualization nicer/more interesting?</p>
</blockquote>
</aside>
<p>We would like to go a step further and add lung vessel information to the result of Lung CT Segmenter, which is currently the base program when we plan surgical resections.<br>
I will give Opacity peeling a try.<br>
Does that answer your question?</p>

---

## Post #11 by @sunwei921119 (2022-06-14 15:33 UTC)

<p>I think it’s good to add such a slider, which is conducive to understanding anatomy</p>

---

## Post #12 by @lassoan (2022-06-15 03:13 UTC)

<aside class="quote no-group" data-username="rbumm" data-post="10" data-topic="23839">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/rbumm/48/9404_2.png" class="avatar"> rbumm:</div>
<blockquote>
<p>We would like to go a step further and add lung vessel information to the result of Lung CT Segmenter</p>
</blockquote>
</aside>
<p>Yes, this answers my question about what you would like to visualize. Do you find that by volume rendering you can easily visualize the vessels? Do you use contrast agent to opacify the vessels?</p>

---

## Post #13 by @rbumm (2022-06-15 06:59 UTC)

<p>Yes <a class="mention" href="/u/lassoan">@lassoan</a> , we use iodinated contrast medium if ever possible to better display the vessels. However, in some scanned CT datasets from external institutions or from databases this contrast is not always available.</p>

---
