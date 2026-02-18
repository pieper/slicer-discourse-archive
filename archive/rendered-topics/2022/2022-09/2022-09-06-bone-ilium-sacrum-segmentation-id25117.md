# Bone (ilium, sacrum) segmentation

**Topic ID**: 25117
**Date**: 2022-09-06
**URL**: https://discourse.slicer.org/t/bone-ilium-sacrum-segmentation/25117

---

## Post #1 by @yyokoyama (2022-09-06 08:34 UTC)

<p>version: latest (5.0.3), win11<br>
dataset: dicom file (enhanced dicom)<br>
I’m new to slicer, and am working bone segmentations (ilium, sacrum).<br>
I’m watching the video (<a href="https://www.youtube.com/watch?v=t4KTmcqzKnE&amp;t=328s" class="inline-onebox" rel="noopener nofollow ugc">Organ segmentation 1: Bones - YouTube</a>) on how to do it, although the slicer version (4.10.2) is old in this video. The “surface cut” bottom doesn’t exist in the latest version, but exited in the old version. Is there a function equivalent to surface cut?</p>
<p>Best regards</p>

---

## Post #2 by @lassoan (2022-09-07 03:05 UTC)

<p>“Surface cut” effect is provided by SegmentEditorExtraEffects extension. You can install it in Slicer in the Extensions Manager.</p>
<p>Since the iliac and sacrum are well separated, you can probably segment them using “Grow from seeds” effect as shown in this tutorial:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="0at15gjk-Ns" data-video-title="Creating femur model from CT volume using 3D Slicer" data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=0at15gjk-Ns" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/0at15gjk-Ns/maxresdefault.jpg" title="Creating femur model from CT volume using 3D Slicer" width="" height="">
  </a>
</div>


---
