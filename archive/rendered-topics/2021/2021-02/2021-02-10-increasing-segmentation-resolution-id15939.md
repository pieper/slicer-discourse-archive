---
topic_id: 15939
title: "Increasing Segmentation Resolution"
date: 2021-02-10
url: https://discourse.slicer.org/t/15939
---

# Increasing segmentation resolution

**Topic ID**: 15939
**Date**: 2021-02-10
**URL**: https://discourse.slicer.org/t/increasing-segmentation-resolution/15939

---

## Post #1 by @Aep93 (2021-02-10 22:10 UTC)

<p>Hello all,<br>
How can I increase the resolution of a current segmentation?<br>
The master volume has its own quality and we cannot increase it but I want a segmentation with higher quality. I tried to crop the master volume with the spacing scale of 0.5 and with both linear and B-spline interpolators. However, it seems not to be working. Is this the correct way of doing what I am looking for or there other ways too?<br>
Thanks in advance.</p>

---

## Post #2 by @lassoan (2021-02-11 04:33 UTC)

<aside class="quote no-group" data-username="Aep93" data-post="1" data-topic="15939">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/aep93/48/5990_2.png" class="avatar"> Aep93:</div>
<blockquote>
<p>I tried to crop the master volume with the spacing scale of 0.5 and with both linear and B-spline interpolators. However, it seems not to be working. Is this the correct way of doing what I am looking for or there other ways too?</p>
</blockquote>
</aside>
<p>Using Crop volume module to crop and resample is a good way to create higher-resolution segmentation than the original image.</p>
<p>If you change the segmentation geometry then the same happens anyway inside the segment editor (the master volume gets automatically resampled to match geometry of the segmentation).</p>

---

## Post #3 by @muratmaga (2021-02-11 05:07 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="2" data-topic="15939">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>the master volume gets automatically resampled to match geometry of the segmentation</p>
</blockquote>
</aside>
<p>I don’t want to hijack the thread, but that’s not what I am observing in my tests. Oversampling seems to only change the segmentations geometry, doesn’t seem to change the geometry of the master volume at all (confirmed by checking property of the master in the volumes module after the segment geometry operation). Am I missing something? Or is this meant to be on-the-fly, non-persistent kind of thing?</p>

---

## Post #4 by @lassoan (2021-02-11 05:32 UTC)

<aside class="quote no-group" data-username="muratmaga" data-post="3" data-topic="15939">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/muratmaga/48/3622_2.png" class="avatar"> muratmaga:</div>
<blockquote>
<p>Oversampling seems to only change the segmentations geometry, doesn’t seem to change the geometry of the master volume at all (confirmed by checking property of the master in the volumes module after the segment geometry operation). Am I missing something? Or is this meant to be on-the-fly, non-persistent kind of thing?</p>
</blockquote>
</aside>
<p>When a segment editor effect asks the segment editor for the “master volume” it gets a volume that conforms to the internal labelmap’s geometry. This volume is generated internally, automatically, by converting the master volume to single-component scalar volume and resample to the internal labelmap geometry (applying all relative transforms, including non-linear warping). This resampled volume does not appear in the MRML scene, only available to the segment editor effects. You can access that image data by calling:</p>
<pre data-code-wrap="python"><code class="lang-python">segmentEditor = slicer.modules.segmenteditor.widgetRepresentation().self().editor
segmentEditor.effectByName('Threshold').masterVolumeImageData()
</code></pre>

---
