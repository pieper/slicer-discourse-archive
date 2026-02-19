---
topic_id: 24624
title: "Touchscreen Compatibility Questions"
date: 2022-08-03
url: https://discourse.slicer.org/t/24624
---

# Touchscreen compatibility questions

**Topic ID**: 24624
**Date**: 2022-08-03
**URL**: https://discourse.slicer.org/t/touchscreen-compatibility-questions/24624

---

## Post #1 by @sannpeterson (2022-08-03 17:39 UTC)

<p>I’m using the Surface Studio to perform segmentations and was wondering if there’s a way to set hand gestures to selection only (no editing) and the pen would be set to the current editing tool. This way going back and forth between panning and drawing would be more seamless.</p>

---

## Post #2 by @lassoan (2022-08-03 21:40 UTC)

<p>This indeed would be great, but I’m not sure if it is possible to disable/ignore the mouse events synthesized from touch events. I could not find an operating system or driver level configuration for this. There is a Qt application option that might work. Try to run Slicer using:</p>
<pre><code>Slicer.exe -platform windows:nomousefromtouch
</code></pre>

---
