---
topic_id: 7119
title: "Cant Display Two Different Segmentations In Two Slice Views"
date: 2019-06-11
url: https://discourse.slicer.org/t/7119
---

# Can't display two different segmentations in two slice views

**Topic ID**: 7119
**Date**: 2019-06-11
**URL**: https://discourse.slicer.org/t/cant-display-two-different-segmentations-in-two-slice-views/7119

---

## Post #1 by @muratmaga (2019-06-11 03:32 UTC)

<p>I have two volumes (volume1, volume2) and their respective segmentations (segmentation_1, segmentation_2).</p>
<p>I couldn’t figure out how to have red slice view display the volume_1 and segmentation_1, while yellow slice view displays volume_2 and segmentation_2. Turning on/off segmentation selection seems to affect all views, even though they are not linked.</p>

---

## Post #2 by @lassoan (2019-06-11 13:47 UTC)

<p>Per-view visibility can be adjusted in Segmentations module Display / Advanced / Views.</p>

---

## Post #3 by @pieper (2019-06-11 13:51 UTC)

<p>For example:<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/669eccdbebdec8352665ca3739ec34758221b177.png" data-download-href="/uploads/short-url/eDOVEzPV2DlRvZvUzXsTnLLEj0r.png?dl=1" title="image"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/669eccdbebdec8352665ca3739ec34758221b177.png" alt="image" data-base62-sha1="eDOVEzPV2DlRvZvUzXsTnLLEj0r" width="690" height="391" data-dominant-color="A7A7AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1443×818 226 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #4 by @muratmaga (2019-06-11 14:44 UTC)

<p>Yes, it makes sense. Works great. Thanks.</p>

---
