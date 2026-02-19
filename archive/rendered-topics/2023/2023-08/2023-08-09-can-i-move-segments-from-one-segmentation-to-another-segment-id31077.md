---
topic_id: 31077
title: "Can I Move Segments From One Segmentation To Another Segment"
date: 2023-08-09
url: https://discourse.slicer.org/t/31077
---

# Can I move segments from one segmentation to another segmentation using a Script?

**Topic ID**: 31077
**Date**: 2023-08-09
**URL**: https://discourse.slicer.org/t/can-i-move-segments-from-one-segmentation-to-another-segmentation-using-a-script/31077

---

## Post #1 by @Sergio (2023-08-09 20:54 UTC)

<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/6/5/65c261a2a2b88a235ba3e265ecc16beb0c7e4347.jpeg" alt="Capture" data-base62-sha1="ewcGs3vRoTr1XrSANv6Vv0u59hd" width="478" height="162"></p>
<p>For example, I would like to move the body_trunc and the body_extremities to Organs.</p>
<p>Thanks in advance.</p>

---

## Post #2 by @ebrahim (2023-08-09 23:42 UTC)

<p>I think this would work</p>
<pre><code class="lang-py">source_segmentation = getNode('BodyContour').GetSegmentation()
source_segment_id = source_segmentation.GetSegmentIdBySegmentName('body_trunc') # repeat for each segment we want to move
target_segmentation = getNode('Organs').GetSegmentation()
target_segmentation.CopySegmentFromSegmentation(source_segmentation, source_segment_id, True)
</code></pre>
<p>(the last parameter <code>True</code> is <code>removeFromSource</code> <a href="https://apidocs.slicer.org/master/classvtkSegmentation.html#a001c13d90bea679cb7697e33e56b59e5" rel="noopener nofollow ugc">here</a>)<br>
(I don’t know if there is a data copy going on or if there is a way to avoid it)</p>

---
