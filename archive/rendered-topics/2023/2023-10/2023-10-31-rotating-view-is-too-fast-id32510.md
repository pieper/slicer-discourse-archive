---
topic_id: 32510
title: "Rotating View Is Too Fast"
date: 2023-10-31
url: https://discourse.slicer.org/t/32510
---

# Rotating view is too fast

**Topic ID**: 32510
**Date**: 2023-10-31
**URL**: https://discourse.slicer.org/t/rotating-view-is-too-fast/32510

---

## Post #1 by @mohammed_alshakhas (2023-10-31 17:17 UTC)

<p>the rotating view is too fast, no idea why I didn’t select anything different this time</p>
<p></p><div class="video-placeholder-container" data-video-src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/2/3/23d11f74c19e508a339e44a35da3c017dac8a35e.mp4">
  </div><p></p>

---

## Post #2 by @lassoan (2023-10-31 19:32 UTC)

<p>It looks like you (or some module that you used) reconfigured your view animation settings. You can revert to defaults like this:</p>
<pre><code class="lang-python">viewWidget = slicer.app.layoutManager().threeDWidget(0).viewWidget()
viewWidget.animationIntervalMs = 5
viewWidget.spinIncrement = 2
</code></pre>
<p>These view properties are not stored persistently, so you another option to reset them is to save the scene, restart Slicer, and load the scene.</p>

---
