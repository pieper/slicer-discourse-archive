# Segmentation resolution

**Topic ID**: 1394
**Date**: 2017-11-07
**URL**: https://discourse.slicer.org/t/segmentation-resolution/1394

---

## Post #1 by @AndFor (2017-11-07 15:16 UTC)

<p>Hello<br>
Can I select the pixel resolution of my segmentation?</p>
<p>is it the same as native image resolution?</p>
<p>thanks</p>

---

## Post #2 by @lassoan (2017-11-07 15:32 UTC)

<p>Binary labelmap representation has the same resolution as the master volume that you select first.</p>

---

## Post #3 by @AndFor (2017-11-07 15:52 UTC)

<p>the 3d result is good, but the segmentation path appear with large pixel</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3cadc408656f44baf404461ae86847ef9721adbd.png" data-download-href="/uploads/short-url/8EMWfXzkynAEepFmJB0uDtfKW0R.png?dl=1" title="segment" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3cadc408656f44baf404461ae86847ef9721adbd_2_690x265.png" alt="segment" data-base62-sha1="8EMWfXzkynAEepFmJB0uDtfKW0R" width="690" height="265" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/3/c/3cadc408656f44baf404461ae86847ef9721adbd_2_690x265.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3cadc408656f44baf404461ae86847ef9721adbd.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/c/3cadc408656f44baf404461ae86847ef9721adbd.png 2x" data-dominant-color="694853"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segment</span><span class="informations">741×285 135 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @lassoan (2017-11-07 16:19 UTC)

<p>Before you start segmenting your volume, use “Crop volume” module to crop it to the minimum necessary size, enable isotropic voxel size (check <code>Isotropic spacing</code>), and reduce voxel size (e.g., set <code>Spacing scale</code> to 0.5). Use this cropped and resampled volume as master volume for segmentation.</p>

---

## Post #5 by @AndFor (2017-11-07 16:29 UTC)

<p><img src="https://emoji.discourse-cdn.com/twitter/slight_smile.png?v=12" title=":slight_smile:" class="emoji only-emoji" alt=":slight_smile:" loading="lazy" width="20" height="20"><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea6d446a7b0a04281b3725edfdd052c3eeeff259.png" data-download-href="/uploads/short-url/xrPPAxSeoJ9VisZXMIkuTgj7YYF.png?dl=1" title="Capture" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea6d446a7b0a04281b3725edfdd052c3eeeff259_2_690x266.png" alt="Capture" data-base62-sha1="xrPPAxSeoJ9VisZXMIkuTgj7YYF" width="690" height="266" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/e/a/ea6d446a7b0a04281b3725edfdd052c3eeeff259_2_690x266.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea6d446a7b0a04281b3725edfdd052c3eeeff259.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/e/a/ea6d446a7b0a04281b3725edfdd052c3eeeff259.png 2x" data-dominant-color="595A34"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture</span><span class="informations">726×280 123 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #6 by @lassoan (2017-11-07 18:59 UTC)

<p>I see a cropping ROI but it seems that you haven’t actually cropped the volume. Was that intentional? If you use a smaller ROI then you can have much finer resolution volume (so you can segment small, thin structures very nicely) without having a large volume. Also note that you can smooth the segment (using Smoothing effect) and/or you can apply smoothing during labelmap-&gt;3D surface conversion (using <code>Show 3D</code> button’s <code>Set surface smoothing</code> option).</p>

---

## Post #7 by @AndFor (2017-11-08 09:58 UTC)

<p>Yes it is true</p>
<p>re-done</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d2a6f4e9ac4cdc14a687dbc1adde96ecf1b38fd.png" data-download-href="/uploads/short-url/4a0Li4ZgtMFVyQu4t4N329Hd4QJ.png?dl=1" title="Capture1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d2a6f4e9ac4cdc14a687dbc1adde96ecf1b38fd_2_690x262.png" alt="Capture1" data-base62-sha1="4a0Li4ZgtMFVyQu4t4N329Hd4QJ" width="690" height="262" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/1/d/1d2a6f4e9ac4cdc14a687dbc1adde96ecf1b38fd_2_690x262.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d2a6f4e9ac4cdc14a687dbc1adde96ecf1b38fd.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/d/1d2a6f4e9ac4cdc14a687dbc1adde96ecf1b38fd.png 2x" data-dominant-color="1F231F"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Capture1</span><span class="informations">720×274 57.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #8 by @AndFor (2017-11-08 12:57 UTC)

<p>an off  topic  question: if I want to use this selection, BUT INVERTED, to create a mask in all volume (then to mask all that is outside of this selection)… can i dublicate the selection?  and invert it?</p>

---

## Post #9 by @lassoan (2017-11-08 14:34 UTC)

<p>You can use <code>Logical operators</code> effect to copy and invert segments.</p>

---

## Post #10 by @AndFor (2017-11-08 17:23 UTC)

<p>yes thanks, worked perfectly</p>
<p>for some structures is easiest to select the structure, then invert and mask all outside</p>

---

## Post #11 by @James_Goldfarb (2022-11-21 19:32 UTC)

<p>I am working with a scene with several volumes with different slice thicknesses. I’m trying to understand the resulting number of pixels in the segmentation/segments saved as nrrd.</p>
<p>Above it is stated that “Binary labelmap representation has the same resolution as the master volume that you select first.”  Is that in the Segmentation Module?</p>
<p>Assuming it is the Segmentation Module,  shouldn’t the scene hierarchy determine the initial selection?  It seems random to me, sometimes set by scene hierarchy and sometimes set by last selection.</p>
<p>I would like to have everything in one scene and have the segmentation number of pixels match my volume. Any tips with multiple volumes?</p>
<p>One problem that I encountered is that the minimum pixel value (by segment statistics) is often lower than my threshold value.  I assume due to interpolation.  How is thresholding performed when volume number of pixels &lt; segment number of pixels?</p>
<p>Thanks in advance.</p>

---

## Post #12 by @lassoan (2022-11-25 06:32 UTC)

<aside class="quote no-group" data-username="James_Goldfarb" data-post="11" data-topic="1394">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/james_goldfarb/48/15318_2.png" class="avatar"> James_Goldfarb:</div>
<blockquote>
<p>Above it is stated that “Binary labelmap representation has the same resolution as the master volume that you select first.” Is that in the Segmentation Module?</p>
</blockquote>
</aside>
<p>In Segment Editor module.</p>
<aside class="quote no-group" data-username="James_Goldfarb" data-post="11" data-topic="1394">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/james_goldfarb/48/15318_2.png" class="avatar"> James_Goldfarb:</div>
<blockquote>
<p>Assuming it is the Segmentation Module, shouldn’t the scene hierarchy determine the initial selection? It seems random to me, sometimes set by scene hierarchy and sometimes set by last selection.</p>
</blockquote>
</aside>
<p>It is the source volume that is chosen first in “Segment Editor” module. There is no scene hierarchy there. The choice is arbitrary, but it is not random, but this is what most users would expect. You can change the geometry anytime by clicking on the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">“Specify geometry” button</a>.</p>
<aside class="quote no-group" data-username="James_Goldfarb" data-post="11" data-topic="1394">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/james_goldfarb/48/15318_2.png" class="avatar"> James_Goldfarb:</div>
<blockquote>
<p>I would like to have everything in one scene and have the segmentation number of pixels match my volume. Any tips with multiple volumes?</p>
</blockquote>
</aside>
<p>You can move around segments with any geometry between segmentations. They will be automatically resampled as late as possible (when the segmentation is modified or saved to disk). You can force resampling or changing resolution using “Specify geometry”.</p>
<aside class="quote no-group" data-username="James_Goldfarb" data-post="11" data-topic="1394">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/james_goldfarb/48/15318_2.png" class="avatar"> James_Goldfarb:</div>
<blockquote>
<p>One problem that I encountered is that the minimum pixel value (by segment statistics) is often lower than my threshold value. I assume due to interpolation. How is thresholding performed when volume number of pixels &lt; segment number of pixels?</p>
</blockquote>
</aside>
<p>The source volume is always resampled to the current segmentation’s geometry.</p>

---
