---
topic_id: 32518
title: "Total Segmentator Extension"
date: 2023-11-01
url: https://discourse.slicer.org/t/32518
---

# Total Segmentator Extension

**Topic ID**: 32518
**Date**: 2023-11-01
**URL**: https://discourse.slicer.org/t/total-segmentator-extension/32518

---

## Post #1 by @akmal871026 (2023-11-01 01:46 UTC)

<p>Dear all,</p>
<p>I looked at the extension manager description for the total segmentator extension can segment 104, but when I run it, it just only segment 72.</p>
<p>How does is it?</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/f/6fc9281c5e7c4de4111bad657aaf1bc66beb3661.jpeg" data-download-href="/uploads/short-url/fWTYtx9wO69YbRcaeR5hVgHZqCZ.jpeg?dl=1" title="Untitled1" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fc9281c5e7c4de4111bad657aaf1bc66beb3661_2_690x362.jpeg" alt="Untitled1" data-base62-sha1="fWTYtx9wO69YbRcaeR5hVgHZqCZ" width="690" height="362" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fc9281c5e7c4de4111bad657aaf1bc66beb3661_2_690x362.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fc9281c5e7c4de4111bad657aaf1bc66beb3661_2_1035x543.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/f/6fc9281c5e7c4de4111bad657aaf1bc66beb3661_2_1380x724.jpeg 2x" data-dominant-color="C7C9C5"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitled1</span><span class="informations">1920×1010 129 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div><br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/3/63056a9a7feefd7077d60d376ab35c6c2e31ab8c.png" data-download-href="/uploads/short-url/e7YScqvSKd3Aoa1Wen1ncJpFLnm.png?dl=1" title="Untitledk" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63056a9a7feefd7077d60d376ab35c6c2e31ab8c_2_690x370.png" alt="Untitledk" data-base62-sha1="e7YScqvSKd3Aoa1Wen1ncJpFLnm" width="690" height="370" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63056a9a7feefd7077d60d376ab35c6c2e31ab8c_2_690x370.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63056a9a7feefd7077d60d376ab35c6c2e31ab8c_2_1035x555.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/6/3/63056a9a7feefd7077d60d376ab35c6c2e31ab8c_2_1380x740.png 2x" data-dominant-color="837E80"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Untitledk</span><span class="informations">1920×1032 342 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @rbumm (2023-11-01 07:52 UTC)

<p>The number of detected classes largely depend on the CT volume and the tasks you involve. With all tasks, TotalSegmenter v2 can segment &gt;133 classes in different body regions.</p>

---

## Post #3 by @lassoan (2023-11-01 13:50 UTC)

<p>If a structure is not detected in the image then it will not be included in the segmentation result. We could add an empty segment for each structure that is not present, but it would just add clutter.</p>

---
