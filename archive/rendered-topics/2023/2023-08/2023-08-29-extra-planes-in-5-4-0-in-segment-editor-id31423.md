---
topic_id: 31423
title: "Extra Planes In 5 4 0 In Segment Editor"
date: 2023-08-29
url: https://discourse.slicer.org/t/31423
---

# Extra planes in 5.4.0 in Segment Editor

**Topic ID**: 31423
**Date**: 2023-08-29
**URL**: https://discourse.slicer.org/t/extra-planes-in-5-4-0-in-segment-editor/31423

---

## Post #1 by @tsehrhardt (2023-08-29 12:55 UTC)

<p>I just upgraded to 5.4.0 and this is the second scene where extra planes are showing up in my scene. I couldn’t replicate it yesterday, but today I opened a scene that I haven’t worked on in a few months, enabled 3D view in SegmentEditor and the extra planes are there in 3D and in sagittal and coronal views. They don’t show up in the axial view. I didn’t do any editing to this scene, just opened it and clicked “Show 3D” in Segment Editor.</p>
<p>Any ideas what would cause this?<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/e/8e5d9faaae5d69f015293c5c5d6ac1b3caea273f.jpeg" data-download-href="/uploads/short-url/kjqo5YDoTf2PxIcHVDHyARN1jTV.jpeg?dl=1" title="2023-08-29_8-51-13" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e5d9faaae5d69f015293c5c5d6ac1b3caea273f_2_690x377.jpeg" alt="2023-08-29_8-51-13" data-base62-sha1="kjqo5YDoTf2PxIcHVDHyARN1jTV" width="690" height="377" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e5d9faaae5d69f015293c5c5d6ac1b3caea273f_2_690x377.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e5d9faaae5d69f015293c5c5d6ac1b3caea273f_2_1035x565.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/8/e/8e5d9faaae5d69f015293c5c5d6ac1b3caea273f_2_1380x754.jpeg 2x" data-dominant-color="9393AB"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">2023-08-29_8-51-13</span><span class="informations">1920×1050 105 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @pieper (2023-08-29 12:57 UTC)

<p>Thanks for reporting.  Can you replicate this with SampleData and share an mrb that illustrates the difference?</p>

---

## Post #3 by @tsehrhardt (2023-08-29 13:21 UTC)

<p>Ok I’m trying to make it happen again–it’s not showing up on the sample sets so I’m opening other old files to see if it’s there. I can just send you this file if you want. It’s from TCIA.</p>

---

## Post #4 by @pieper (2023-08-29 15:36 UTC)

<p>Yes, any public dataset that demonstrates the issue is fine.</p>

---

## Post #5 by @pieper (2023-08-31 18:59 UTC)

<p>Thanks for reporting this and sharing the example, I was able to replicate it, but I’m not sure what causes it.  Probably there’s some different rounding behavior between the VTK versions in use.  Maybe <a class="mention" href="/u/lassoan">@lassoan</a> has an idea where to look.  It could help to have the original scene that didn’t have the issue in the earlier Slicer version so we can track what’s happening to it when you open in the new version.</p>
<p>As a workaround though, I was able to use the Segmentation Geometry button in the Segment Editor to select the CT as the source and the issue went away.</p>

---

## Post #6 by @tsehrhardt (2023-09-02 19:41 UTC)

<p>Thanks for taking a look! I’ll report if it happens again. I tried the Segmentation Geometry button and it worked to clear the planes.</p>

---

## Post #7 by @lassoan (2023-09-05 16:18 UTC)

<aside class="quote no-group" data-username="pieper" data-post="5" data-topic="31423">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>Thanks for reporting this and sharing the example, I was able to replicate it</p>
</blockquote>
</aside>
<p>How have you replicated it?</p>

---

## Post #8 by @pieper (2023-09-05 16:44 UTC)

<p>I got the file via a direct message.  <a class="mention" href="/u/tsehrhardt">@tsehrhardt</a> can you send it to <a class="mention" href="/u/lassoan">@lassoan</a> as well?</p>

---

## Post #9 by @tsehrhardt (2023-09-05 16:53 UTC)

<p>Sure, sending it now.</p>

---
