---
topic_id: 46973
title: "Invisible wall limiting segmentation"
date: 2026-05-08
url: https://discourse.slicer.org/t/46973
last_bumped: 2026-05-10T23:52:49.506Z
---

# Invisible wall limiting segmentation

**Topic ID**: 46973
**Date**: 2026-05-08
**URL**: https://discourse.slicer.org/t/invisible-wall-limiting-segmentation/46973

---

## Post #1 by @FabricioFO (2026-05-08 18:05 UTC)

<pre><code class="lang-auto">Example
</code></pre>
<p><span lang="en">Hello, everyone. </span></p>
<p><span lang="en">I’m facing the same problem as in the video: I try to segment a specific region and it doesn’t work, it seems like there’s an invisible wall preventing me from segmenting that region even with the threshold enabled and capturing the region’s density. When I go to Source Volume and select the same volume I’m using, this invisible barrier disappears, but everything becomes very heavy, making it difficult to work. Has this happened to you before? Were you able to fix it?</span> There is an example in the link!</p>

---

## Post #2 by @muratmaga (2026-05-08 20:00 UTC)

<p>You might have forgotten to attach video or the screenshot that explains your problem.</p>
<p>From your description this sounds like geometry mismatch between the source volume and the segmentation object. Right click on your volume, choose Segment this, and then retry, and see if it fixes.</p>

---

## Post #3 by @lassoan (2026-05-10 23:52 UTC)

<p>See some more details in the <a href="https://slicer.readthedocs.io/en/latest/user_guide/modules/segmenteditor.html#cannot-paint-outside-some-boundaries">Segmentation FAQ</a>.</p>

---
