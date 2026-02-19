---
topic_id: 14807
title: "Slicer 4 10 2 Vs Slicer 4 11 2 Volumes Rendering"
date: 2020-11-29
url: https://discourse.slicer.org/t/14807
---

# Slicer 4.10.2 vs Slicer 4.11.2 volumes rendering

**Topic ID**: 14807
**Date**: 2020-11-29
**URL**: https://discourse.slicer.org/t/slicer-4-10-2-vs-slicer-4-11-2-volumes-rendering/14807

---

## Post #1 by @a10227 (2020-11-29 17:54 UTC)

<p>Good day,</p>
<p>I had Slicer 4.10.2 version on my PC. After a while, I noticed that for some images the uploading time is too slow, so I installed the latest stable version 4.11.2. In the latest version, I have no problem with the uploading time, but I noticed a difference in how these two versions display the volume in the volume rendering module (screenshot attached, on the left - 4.10.2, on the right - 4.11.2). Slicer 4.10.2 seems to provide more accurate volume rendering (less noise, smoother texture). I noticed that for these two versions, the scalar opacity and scalar color mapping are different for the same image, so the reason seems to be in the fact how the default values are set for the opacity and color.</p>
<p>Could you please tell me why the renderings are different and what I should do to get the same visualization in the latest stable release as in 4.10.2? I know I can adjust the visualization manually, but it would be nice to get a nice visualization like in 4.10.2 without any effort.<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4866290d98f614be11e87ac97dacf515912cd7c2.jpeg" data-download-href="/uploads/short-url/aktfPV1odLwVXjg2NCS7xSWFFZ0.jpeg?dl=1" title="volumes.PNG" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4866290d98f614be11e87ac97dacf515912cd7c2_2_690x287.jpeg" alt="volumes.PNG" data-base62-sha1="aktfPV1odLwVXjg2NCS7xSWFFZ0" width="690" height="287" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/4866290d98f614be11e87ac97dacf515912cd7c2_2_690x287.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4866290d98f614be11e87ac97dacf515912cd7c2.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/8/4866290d98f614be11e87ac97dacf515912cd7c2.jpeg 2x" data-dominant-color="47475B"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">volumes.PNG</span><span class="informations">960×400 40.7 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>
<p>Note. This screenshot is only to show the difference - unfortunately, for confidential reasons I cannot post images where this difference is more noticeable.</p>

---

## Post #2 by @lassoan (2020-11-29 20:53 UTC)

<p>Both these renderings seem to just use the default grayscale mapping, based on the current window/level value. The default window/level detection method was slightly improved in Slicer-4.11, which may explain the difference in the default volume rendering preset. You can edit this setting in Volume rendering module: move the Shift slider and optionally also adjust Scalar Opacity Mapping function in Advanced/Volume properties section (see <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/volumerendering.html#display-a-ct-or-mri-volume">documentation</a>).</p>
<p>However, I would strongly recommend to choose a volume rendering preset (Volume rendering module / Display / Preset) and use Shift slider to adjust it to your image.</p>

---

## Post #3 by @a10227 (2020-11-29 22:41 UTC)

<p>Thank you for the reply. I was trying to choose a preset but none of them work - the image disappears or turns into the black cube, my guess is that this is due to the fact that all of my images are normalized to the 0…1 range. Shift without any preset doesn’t work also (i think this is for the same reason).<br>
Are there any ways to fix it? Maybe I can somehow  adjust the scale or return the W/L detection method to the old one?</p>

---
