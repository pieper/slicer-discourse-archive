# "Overwrite all" setting in paint or scissors (fill inside) creates large gaps between segments that should be connected

**Topic ID**: 17665
**Date**: 2021-05-17
**URL**: https://discourse.slicer.org/t/overwrite-all-setting-in-paint-or-scissors-fill-inside-creates-large-gaps-between-segments-that-should-be-connected/17665

---

## Post #1 by @sannpeterson (2021-05-17 21:18 UTC)

<p>Ive tried several ways to try to get around this issue. For instance, I’ve tried allowing overlap (under Modify other segments) then going back to erase the portion of the segment that is overlapping using subtract. When I look at the slice views, it shows that everything is filled in correctly. But in 3D view, there’s always a gap where there shouldn’t be. What am i doing wrong?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/6/66f82c4a939461993bec18c423fa0e318e8d8cf0.png" alt="before" data-base62-sha1="eGUpqRrnJxYHH6XOlEFhhbtSbGo" width="549" height="396"></p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/1/4/146739651228c9de08f74c83581043aacbad284c.png" alt="after" data-base62-sha1="2UuHMLopiS4zMMCXjQQxNx7IObG" width="496" height="374"></p>

---

## Post #2 by @lassoan (2021-05-18 01:07 UTC)

<p>This looks all good. What you see is the result of smoothing. By default we show non-smoothed labelmap in slice views and smoothed closed surface representation 3D views. You can disable smoothing or choose to show the closed surface representation in slice views. However, if the difference between the smoothed and non-smoothed representations is significant for you then it means that the resolution of the segmentation’s binary labelmap representation is too low. You can follow <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#segmentation-is-not-accurate-enough">these instructions</a> to improve the resolution.</p>

---

## Post #3 by @sannpeterson (2021-05-18 14:59 UTC)

<p>Thank you so much for the explanation!</p>

---
