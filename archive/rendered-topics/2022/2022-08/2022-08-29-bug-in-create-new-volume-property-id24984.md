---
topic_id: 24984
title: "Bug In Create New Volume Property"
date: 2022-08-29
url: https://discourse.slicer.org/t/24984
---

# Bug in Create New Volume Property

**Topic ID**: 24984
**Date**: 2022-08-29
**URL**: https://discourse.slicer.org/t/bug-in-create-new-volume-property/24984

---

## Post #1 by @muratmaga (2022-08-29 19:52 UTC)

<p>I have 16 bit dataset where intensity ranges from 0-65535. When I use volume rendering the very first time on this dataset, I can create a scalar opacity mapping that makes sense for this dataset</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc8d83437733003f4887f0311fc60c4743f93f3c.png" data-download-href="/uploads/short-url/tbyANW9FoENY7y4KGvctXQ4gP80.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc8d83437733003f4887f0311fc60c4743f93f3c_2_690x392.png" alt="image" data-base62-sha1="tbyANW9FoENY7y4KGvctXQ4gP80" width="690" height="392" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/c/c/cc8d83437733003f4887f0311fc60c4743f93f3c_2_690x392.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc8d83437733003f4887f0311fc60c4743f93f3c.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/c/c/cc8d83437733003f4887f0311fc60c4743f93f3c.png 2x" data-dominant-color="E6E7E8"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">712×405 39.6 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>When I go to volume rendering the second time and ask to create a new volume rendering property, this is what I get. I cannot create a transfer function points that exceeds 1024.0, which results in a solid white box for this dataset. (To clarify, I cannot create points pass 1024, nor I can type in a value that exceeds 1024).</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc72cf42de47ffbb279227b0ba6831871c892ef9.png" data-download-href="/uploads/short-url/qT5K3JOnzC6mH1YfZVHde25XTg5.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc72cf42de47ffbb279227b0ba6831871c892ef9_2_690x380.png" alt="image" data-base62-sha1="qT5K3JOnzC6mH1YfZVHde25XTg5" width="690" height="380" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/b/c/bc72cf42de47ffbb279227b0ba6831871c892ef9_2_690x380.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc72cf42de47ffbb279227b0ba6831871c892ef9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/c/bc72cf42de47ffbb279227b0ba6831871c892ef9.png 2x" data-dominant-color="BBBCBD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">701×387 29 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Sliding the shift all the way to the right, I can only go up to 1968, which is insufficient for this data. Zoom sliders are not useful either.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6b1d5e716064785ef010ffb1d3b9c983d63eda9.png" data-download-href="/uploads/short-url/uDhbKP6I9y1RVqqCYWB9GgDW5sJ.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6b1d5e716064785ef010ffb1d3b9c983d63eda9_2_604x500.png" alt="image" data-base62-sha1="uDhbKP6I9y1RVqqCYWB9GgDW5sJ" width="604" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/d/6/d6b1d5e716064785ef010ffb1d3b9c983d63eda9_2_604x500.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6b1d5e716064785ef010ffb1d3b9c983d63eda9.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/d/6/d6b1d5e716064785ef010ffb1d3b9c983d63eda9.png 2x" data-dominant-color="CBCCCD"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">721×596 55.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This bug was going on for a while, but now that we are using 16 bit data more and more it is getting quite hard to deal with. The only solution I found is to reset the scene and reload the data, which is tedious for the size of datasets we work with.</p>

---

## Post #2 by @lassoan (2022-08-31 11:55 UTC)

<p>You can set any range: after you moved the control point out of the chart region then move the range slider below the plot to show the entire range.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee99f92fdf6b8647fefc93baa002e6be8797b9d4.png" data-download-href="/uploads/short-url/y2LwvTww8Eqw2g8fItLFhLtgB8w.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/e/ee99f92fdf6b8647fefc93baa002e6be8797b9d4.png" alt="image" data-base62-sha1="y2LwvTww8Eqw2g8fItLFhLtgB8w" width="690" height="205" data-dominant-color="898989"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1040×309 10.4 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>After that you can drag the control point to the right again.</p>
<p>I agree that this is not very convenient when you need to significantly increase the transfer function range.</p>
<p>A default volume property node with transfer functions covering the full intensity range of the volume is created automatically. What is the reason for creating a new volume property node?</p>
<p>You can add a volume rendering preset with transfer functions covering a wide range (0 to 32000 or 65000) and selecting that the user could avoid the complicated dragging of transfer function control points. However, I’m not sure why your CTs have this wide intensity range. If they were properly calibrated then their range would be about -1000 to 3000. Do you know why these CTs are not calibrated? What the intensity values correspond to? Could we calibrate (or at least somewhat normalize) their intensity on import or add a module for intensity calibration?</p>

---

## Post #3 by @muratmaga (2022-08-31 20:49 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="24984">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>A default volume property node with transfer functions covering the full intensity range of the volume is created automatically. What is the reason for creating a new volume property node?</p>
</blockquote>
</aside>
<p>Mostly to test what the differences are or experimenting with coloring scheme. This usually takes more than one take. I ideally would like to clone an existing one continue operating on the cloned one, but currently that doesn’t seem to be the possible.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="24984">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can add a volume rendering preset with transfer functions covering a wide range (0 to 32000 or 65000)</p>
</blockquote>
</aside>
<p>THat’s the current solution we are looking into, at least for our needs. However, there is no guarantee that the one TF will work as well for the next scan. But still should give a more reasonable starting point then the solid block.</p>
<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="24984">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>Do you know why these CTs are not calibrated?</p>
</blockquote>
</aside>
<p>These are all microCT, which rarely (if any) are calibrated. Normally the reconstruction software outputs as these 8 bit PNG images, but to preserve most of the dynamic range (as these are diffusable iodine contrast enhanced soft tissue scans) we chose to keep them as 16 bit tiff sequences.</p>
<p>I know the volume rendering is one of the more challenging parts of the slicer to modify. So for my need, all I need is the “Create New Volume Property” function to perform as exactly the first time rendering (create a simple ramp that covers all the intensity range). Alternative work around would be the ability to clone volume property nodes in the Data module.</p>

---

## Post #4 by @lassoan (2022-09-01 04:36 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="24984">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>diffusable iodine contrast enhanced soft tissue scans</p>
</blockquote>
</aside>
<p>If these images have a typical content then having one or few good presets for them would be great.</p>
<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="24984">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>So for my need, all I need is the “Create New Volume Property” function to perform as exactly the first time rendering (create a simple ramp that covers all the intensity range).</p>
</blockquote>
</aside>
<p>You can achieve this by a single click on the <code>Synchronize with Volumes module</code> button. I’ve now <a href="https://github.com/Slicer/Slicer/commit/0ff0e7bce595368ab8f1e5a1d8788ad67be6d005">added activating of this feature automatically</a> when you add a new volume property node using the node selector.</p>

---

## Post #5 by @muratmaga (2022-09-01 15:11 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="4" data-topic="24984">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can achieve this by a single click on the <code>Synchronize with Volumes module</code> button</p>
</blockquote>
</aside>
<p>This worked great, thank you!</p>

---
