---
topic_id: 39640
title: "Select Complex Area For Segmentation"
date: 2024-10-10
url: https://discourse.slicer.org/t/39640
---

# Select complex area for segmentation

**Topic ID**: 39640
**Date**: 2024-10-10
**URL**: https://discourse.slicer.org/t/select-complex-area-for-segmentation/39640

---

## Post #1 by @Thomas_Bourdeau (2024-10-10 19:22 UTC)

<p>Hello Everyone,</p>
<p>I hope this message will reach someone who can help me.</p>
<p>I am doing micro CT for space material application. I am looking for a way to only process segmentation in a specific area. The objective is to measure and determine the porosity (which appear in black) inside a printing object. However, during the segmentation process, even the background is calculated as it is in black (as the porosity). Normally one slice is uploaded.</p>
<p>Do you have any solution to only process the segmentation on the specific aera</p>
<p>Thanks a lot to any person who will read and maybe can help me.</p>
<p>Thomas</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/8/88e66398a2d3a895a10ab7fef0eb6c30b8c870d6.jpeg" data-download-href="/uploads/short-url/jx4xCmQGTDa10PI1HfDSzZndE4m.jpeg?dl=1" title="cropped cropped C50_Tamb_4mm_noz_8mm_Rec0001" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88e66398a2d3a895a10ab7fef0eb6c30b8c870d6_2_466x500.jpeg" alt="cropped cropped C50_Tamb_4mm_noz_8mm_Rec0001" data-base62-sha1="jx4xCmQGTDa10PI1HfDSzZndE4m" width="466" height="500" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88e66398a2d3a895a10ab7fef0eb6c30b8c870d6_2_466x500.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88e66398a2d3a895a10ab7fef0eb6c30b8c870d6_2_699x750.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/8/88e66398a2d3a895a10ab7fef0eb6c30b8c870d6_2_932x1000.jpeg 2x" data-dominant-color="292929"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">cropped cropped C50_Tamb_4mm_noz_8mm_Rec0001</span><span class="informations">1002×1074 106 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2024-10-11 13:12 UTC)

<p>You can use the Threshold effect to segment all dark area and then use the Islands effect’s “Remove selected island” tool to remove the large dark background region.</p>

---
