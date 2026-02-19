---
topic_id: 19636
title: "Resizing Slice View Doesnt Preserve Field Of View"
date: 2021-09-13
url: https://discourse.slicer.org/t/19636
---

# Resizing slice view doesn't preserve field of view

**Topic ID**: 19636
**Date**: 2021-09-13
**URL**: https://discourse.slicer.org/t/resizing-slice-view-doesnt-preserve-field-of-view/19636

---

## Post #1 by @keri (2021-09-13 01:44 UTC)

<p>Hi,</p>
<p>Let’s suppose I intensionally changed field of view in slice node:</p>
<pre data-code-wrap="python"><code class="lang-python">sliceNode = layoutManager = slicer.app.layoutManager().sliceWidget('Red').sliceView().mrmlSliceNode()
sliceNode.SetFieldOfView(100, 300, 1)
</code></pre>
<p>and then I change slice view either by gragging QSplitter or by clicking on maximize button (on the picture) and apparently restores field of view to default.</p>
<p>Is this a drawback and the behaviour will be fixed in the future or it is done intensionally and to preserve my custom aspect ratio I need to hardcode my module?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/5/c/5c81f1a9373d1d6f868d3c5dec0eddac495e417b.png" alt="image" data-base62-sha1="dcmkwkIanf8zrd654CyI3FCepqX" width="351" height="162"></p>

---

## Post #2 by @pieper (2021-09-13 14:45 UTC)

<p>The field of view needs to match the shape of the window, which can change when the layout changes.  We can’t have the aspect ratio of the image change (it would distort the anatomy).  So if you change the field of view in your custom code you will need to reset it when the layout changes.</p>

---
