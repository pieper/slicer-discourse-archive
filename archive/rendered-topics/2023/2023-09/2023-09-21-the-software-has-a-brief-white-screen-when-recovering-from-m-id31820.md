---
topic_id: 31820
title: "The Software Has A Brief White Screen When Recovering From M"
date: 2023-09-21
url: https://discourse.slicer.org/t/31820
---

# The software has a brief white screen when recovering from minimization

**Topic ID**: 31820
**Date**: 2023-09-21
**URL**: https://discourse.slicer.org/t/the-software-has-a-brief-white-screen-when-recovering-from-minimization/31820

---

## Post #1 by @slicer365 (2023-09-21 03:19 UTC)

<p></p><div class="video-container">
    <video width="100%" height="100%" preload="metadata" controls="">
      <source src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56ad47dc7fa1ee1df1d77f88158a2fdaeaa4ec6f.mp4">
      <a href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56ad47dc7fa1ee1df1d77f88158a2fdaeaa4ec6f.mp4" rel="noopener nofollow ugc">https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/6/56ad47dc7fa1ee1df1d77f88158a2fdaeaa4ec6f.mp4</a>
    </video>
  </div><p></p>
<p>When I open the histogram display, the program will show a white screen when it recovers from the minimized state.<br>
When I turned off the real-time update of the histogram in the source code, it didn’t work.<br>
May I ask how this problem can be solved?</p>

---

## Post #2 by @lassoan (2023-09-21 15:07 UTC)

<p>Thanks for reporting. I could reproduce this behavior on my computer, too.</p>
<p>When you restore the window from minimized state then the histogram is recomputed (in <code>qSlicerScalarVolumeDisplayWidget::showEvent(...)</code>). This may take a little time and maybe it also invalidates some screen buffers, which makes the operating system show a blank window during the window restore animation.</p>
<p>The histogram is recomputed when the widget gets shown because the histogram updates are blocked when when the histogram widget is not visible (otherwise there would be a lot of unnecessary computations when images are continuously streamed into Slicer at a high framerate). So, this histogram recomputation cannot be simply removed, but the logic could be more sophisticated: we could compare the last update time of the histogram and and the last update time of the input image data and if we find that the histogram is more recent than the image then the update could be skipped.</p>
<p>This is a very small cosmetic issue, and a fix is not likely to be needed for any of the funded projects, so I’m not sure if any Slicer developers would work on this right away. However, you can <a href="https://issues.slicer.org">submit a feature request</a> to keep track of it and wait for it to be fixed; or if it’s more urgent then you can provide development resources (e.g., implement it yourself and send a pull request, or fund some developers to work on it).</p>

---

## Post #3 by @slicer365 (2023-09-21 15:41 UTC)

<p>Thank you for your advice, Mr Lasso.</p>
<p>Present, we temporarily commented on the code " this-&gt;updateHIstogram()"</p>
<p>It works well!</p>

---

## Post #4 by @lassoan (2023-09-21 20:31 UTC)

<p>By removing the update, the histogram may show the previously selected volume’s histogram. I would recommend to implement the logic that checks if you need to update the histogram and only skip the update if it is safe to do so.</p>

---
