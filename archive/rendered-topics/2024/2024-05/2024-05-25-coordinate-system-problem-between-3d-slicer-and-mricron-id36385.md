# Coordinate system problem between 3d slicer and Mricron

**Topic ID**: 36385
**Date**: 2024-05-25
**URL**: https://discourse.slicer.org/t/coordinate-system-problem-between-3d-slicer-and-mricron/36385

---

## Post #1 by @lotus (2024-05-25 10:15 UTC)

<p>Dear expert,</p>
<p>I have a problem with the slicer coordinate system. When the T2WI images of the same subject are opened in slicer and mricron, the AP position and PA position will be opposite. In this case, how do I operate in slicer so that the display is the same as in mricron. Thanks a lot!</p>
<p>The hyperlinked addresses below are screenshots of T2WI images opened by both software:<br>
<a href="https://app.yinxiang.com/fx/3d4ccc1d-301c-4811-99f0-620cb229eefe" class="onebox" target="_blank" rel="noopener nofollow ugc">https://app.yinxiang.com/fx/3d4ccc1d-301c-4811-99f0-620cb229eefe</a></p>

---

## Post #2 by @pieper (2024-05-25 16:04 UTC)

<p>You’ll need to doublecheck the pipeline that led to these images.  The one loaded in Slicer looks to be upside down, as you noted.  You don’t specify what file format you used, but whichever it is the geometry information describing the patient orientation is incorrect and you should be very careful using it for any purpose.  It’s very important that every piece of software you use maintains the orientations coorrectly.</p>

---
