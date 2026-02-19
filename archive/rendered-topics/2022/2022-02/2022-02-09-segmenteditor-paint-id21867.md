---
topic_id: 21867
title: "Segmenteditor Paint"
date: 2022-02-09
url: https://discourse.slicer.org/t/21867
---

# segmentEditor paint

**Topic ID**: 21867
**Date**: 2022-02-09
**URL**: https://discourse.slicer.org/t/segmenteditor-paint/21867

---

## Post #1 by @wang (2022-02-09 10:20 UTC)

<p>When I use segmentEditor paint I find LeftButtonPressEvent is not triggered.<br>
How do I get LeftButtonPressEvent  when I use segmentEditor paint.<br>
Think you!</p>

---

## Post #2 by @lassoan (2022-02-09 23:02 UTC)

<p>Probably the segment editor consumes the event. If you want to intercept the event before the segment editor gets it, you can add an observer with a higher priority.</p>

---
