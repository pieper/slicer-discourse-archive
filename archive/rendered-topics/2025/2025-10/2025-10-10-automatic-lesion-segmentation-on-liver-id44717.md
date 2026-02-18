# Automatic Lesion Segmentation on Liver

**Topic ID**: 44717
**Date**: 2025-10-10
**URL**: https://discourse.slicer.org/t/automatic-lesion-segmentation-on-liver/44717

---

## Post #1 by @akmal871026 (2025-10-10 07:20 UTC)

<p>Dear Expert,</p>
<p>Is there any extension that can segment lesions/tumors on the Liver? CTA image or any CT images.</p>

---

## Post #2 by @lassoan (2025-10-16 12:38 UTC)

<p>Liver tumor segmentation is a very commonly studied problem, so there are many pre-trained AI segmentation models for it. Check out TotalSegmentator and MONAIAuto3DSeg first, as they are already easily available via their own Slicer extensions. If those don’t work well then you can find pre-trained nnU-net based segmentation models that you can run using NNUnet extension.</p>

---

## Post #3 by @akmal871026 (2025-10-19 09:57 UTC)

<p>Dear <a class="mention" href="/u/lassoan">@lassoan</a> ,</p>
<p>I was go through what you mentioned. But there is no tumor liver on.</p>

---

## Post #4 by @Matteboo (2025-10-22 09:04 UTC)

<p>From memory you’re supposed to do the “liver vessel” in Total segmentator task to get the liver lesion.<br>
In my experience, this only works on very visible lesion and struggle to catch the small ones.<br>
If you manage to find a way to automatically segment the liver lesion I’m interested</p>

---
