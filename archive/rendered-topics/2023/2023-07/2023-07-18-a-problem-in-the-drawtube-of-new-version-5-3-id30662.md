---
topic_id: 30662
title: "A Problem In The Drawtube Of New Version 5 3"
date: 2023-07-18
url: https://discourse.slicer.org/t/30662
---

# A problem in the DrawTube of new version 5.3

**Topic ID**: 30662
**Date**: 2023-07-18
**URL**: https://discourse.slicer.org/t/a-problem-in-the-drawtube-of-new-version-5-3/30662

---

## Post #1 by @slicer365 (2023-07-18 16:35 UTC)

<p>There is no curve in the 2D view.<br>
</p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f180b99fdbd45ddb29b7d7808251fa942cfe504a.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f180b99fdbd45ddb29b7d7808251fa942cfe504a.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f180b99fdbd45ddb29b7d7808251fa942cfe504a.mp4</a>
    </video>
  </div><p></p>

---

## Post #2 by @Sunderlandkyl (2023-07-18 17:13 UTC)

<p>This is related to the issue in <a href="https://github.com/Slicer/Slicer/issues/7101" class="inline-onebox" rel="noopener nofollow ugc">Model Slice intersections are broken · Issue #7101 · Slicer/Slicer · GitHub</a>.</p>
<p>There was an update in VTK that caused a regression for pipelines using vtkPlaneCutter. Looks like the current approach will be to fix the regression in VTK.</p>

---
