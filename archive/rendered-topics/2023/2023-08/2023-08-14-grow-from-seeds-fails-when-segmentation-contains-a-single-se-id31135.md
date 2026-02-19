---
topic_id: 31135
title: "Grow From Seeds Fails When Segmentation Contains A Single Se"
date: 2023-08-14
url: https://discourse.slicer.org/t/31135
---

# Grow from seeds fails when segmentation contains a single segment

**Topic ID**: 31135
**Date**: 2023-08-14
**URL**: https://discourse.slicer.org/t/grow-from-seeds-fails-when-segmentation-contains-a-single-segment/31135

---

## Post #1 by @qinyi_Zhang (2023-08-14 13:31 UTC)

<p>When I first marked certain areas with paint, I tried to use seed growth for automatic splitting, but when I clicked on initialize, the software didn’t respond, and the APPLY place was grayed out. I would like to ask for advice on which step I have a problem with.</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/a/0/a00f062aba13168568bcd7e4b6a153e3363cf8ea.jpeg" data-download-href="/uploads/short-url/mPWAdNzAybWdjRJrzeozGlRixWW.jpeg?dl=1" title="1692013336834" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a00f062aba13168568bcd7e4b6a153e3363cf8ea_2_690x373.jpeg" alt="1692013336834" data-base62-sha1="mPWAdNzAybWdjRJrzeozGlRixWW" width="690" height="373" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a00f062aba13168568bcd7e4b6a153e3363cf8ea_2_690x373.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a00f062aba13168568bcd7e4b6a153e3363cf8ea_2_1035x559.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/a/0/a00f062aba13168568bcd7e4b6a153e3363cf8ea_2_1380x746.jpeg 2x" data-dominant-color="94949C"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">1692013336834</span><span class="informations">1920×1040 137 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Sunderlandkyl (2023-08-14 15:02 UTC)

<p>You’ll need to create a second segment, and paint outside of the structure that you are segmenting.</p>

---
