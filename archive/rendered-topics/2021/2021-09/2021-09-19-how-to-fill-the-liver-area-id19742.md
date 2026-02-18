# How to fill the liver area?

**Topic ID**: 19742
**Date**: 2021-09-19
**URL**: https://discourse.slicer.org/t/how-to-fill-the-liver-area/19742

---

## Post #1 by @akmal871026 (2021-09-19 08:39 UTC)

<p>Hi all,</p>
<p>Does anyone know how to fill the area of the liver in a red circle? I used Nvidia Auto segmentation Clara</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/7/7/77f6612d31f5f17cc33f9798082b0ea52d4a52b4.jpeg" data-download-href="/uploads/short-url/h7eGsuU3OAJnXet2pyn30NrbqYc.jpeg?dl=1" title="liver" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77f6612d31f5f17cc33f9798082b0ea52d4a52b4_2_690x468.jpeg" alt="liver" data-base62-sha1="h7eGsuU3OAJnXet2pyn30NrbqYc" width="690" height="468" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77f6612d31f5f17cc33f9798082b0ea52d4a52b4_2_690x468.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77f6612d31f5f17cc33f9798082b0ea52d4a52b4_2_1035x702.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/7/77f6612d31f5f17cc33f9798082b0ea52d4a52b4_2_1380x936.jpeg 2x" data-dominant-color="BFC0C2"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">liver</span><span class="informations">2640×1792 317 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @rbumm (2021-09-19 15:13 UTC)

<p>You should be able to use “Local Threshold” of the “Segment editor”. Select the blue segment, then “Local Threshold”, adjust the thresholds so that the missing area is blinking, and left-Click into the missing area. This should add the missing area to the blue segment.</p>
<p>“Local Threshold” is included in “SegmentEditorExtraEffects” extension.</p>

---

## Post #3 by @akmal871026 (2021-09-20 04:20 UTC)

<p>But looklike not function for local threshold. Can you give video or some else</p>

---

## Post #4 by @rbumm (2021-09-20 10:08 UTC)

<p>You need to install the SegmentEditorExtraEffects extension, then you get this:</p>
<div class="youtube-onebox lazy-video-container" data-video-id="cevlMLyhfK8" data-video-title='Segment Editor: New "Local threshold" effect' data-provider-name="youtube">
  <a href="https://www.youtube.com/watch?v=cevlMLyhfK8" target="_blank" rel="noopener">
    <img class="youtube-thumbnail" src="https://img.youtube.com/vi/cevlMLyhfK8/maxresdefault.jpg" title='Segment Editor: New "Local threshold" effect' width="" height="">
  </a>
</div>


---
