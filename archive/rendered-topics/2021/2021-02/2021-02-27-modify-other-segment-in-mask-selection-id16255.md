# Modify other segment in mask selection

**Topic ID**: 16255
**Date**: 2021-02-27
**URL**: https://discourse.slicer.org/t/modify-other-segment-in-mask-selection/16255

---

## Post #1 by @mohammed_alshakhas (2021-02-27 07:36 UTC)

<p>im srtuggling with the new feature of " modify other segments in mask selection "<br>
is there a way to disable it???</p>
<p>in my workflow, i don’t want to modify other segments.  i choose outside all segments but still get issues often and solved by changing this part of options</p>
<p>i find myself going back and forth between options in mask and sometimes i feel im lost and not sure what’s going wrong</p>
<p>thanks <div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/1/f1ce6bb74e166c4f12d89ca3e4f4d18d0de686c7.jpeg" data-download-href="/uploads/short-url/yv7k8DTAH0barJydY5rUlaOItiT.jpeg?dl=1" title="Screen Shot 2021-02-27 at 10.26.52" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f1ce6bb74e166c4f12d89ca3e4f4d18d0de686c7_2_690x431.jpeg" alt="Screen Shot 2021-02-27 at 10.26.52" data-base62-sha1="yv7k8DTAH0barJydY5rUlaOItiT" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f1ce6bb74e166c4f12d89ca3e4f4d18d0de686c7_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f1ce6bb74e166c4f12d89ca3e4f4d18d0de686c7_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/f/f1ce6bb74e166c4f12d89ca3e4f4d18d0de686c7_2_1380x862.jpeg 2x" data-dominant-color="333339"><div class="meta">
<svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2021-02-27 at 10.26.52</span><span class="informations">2880×1800 508 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg>
</div></a></div></p>

---

## Post #2 by @lassoan (2021-02-27 13:11 UTC)

<p>You can choose “Allow overlap” if you don’t want editing one segment overwrite another.</p>
<p>To completely isolate a set of segments, you can create a new segmentation node and move segments there. You can layer move all segments back to one segmentation. You can easily move segments between segmentations by drag-and-drop in Data module.</p>

---

## Post #3 by @mohammed_alshakhas (2021-02-27 13:37 UTC)

<p>what i really wish for is that the segment i made act like a mask or boundery for the new segment ill creat .</p>
<p>most of my work contain really close segments with quite similar threshold , so i make one to differential to set the boundary for others .</p>
<p>i use to make edit outside other segments but it either prevent me from making  the new one</p>

---

## Post #4 by @lassoan (2021-02-27 14:17 UTC)

<p>To make sure you can only paint inside a selected segment (let’s call this “mask” segment), choose the “mask” segment in “Editable area”.</p>
<p>You probably don’t want this “mask” segment to be modified by editing. To achieve this, hide the “mask” segment and choose “Modify other segments” → “Overwrite visible”. This will only allow overwriting visible segments, and since the “mask” segment is not visible, it will not be overwritten.</p>

---

## Post #5 by @mohammed_alshakhas (2021-02-27 14:22 UTC)

<p>the issues is that i need to see the other segment while drawing the new one . like im defining very close muscle or lesion that started in bone and goes out in some location .</p>
<p>i like ( need) to see the previous segment while not modify it at all</p>

---

## Post #6 by @pieper (2021-02-27 14:38 UTC)

<aside class="quote no-group" data-username="mohammed_alshakhas" data-post="5" data-topic="16255">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/mohammed_alshakhas/48/10025_2.png" class="avatar"> mohammed_alshakhas:</div>
<blockquote>
<p>i like ( need) to see the previous segment while not modify it at all</p>
</blockquote>
</aside>
<p>You could export it to a Model and show slicer intersections.  It’ll be a bit smoothed but it won’t interfere with your segments.</p>

---

## Post #7 by @lassoan (2021-02-27 15:51 UTC)

<p>You can also copy or move the segment into another segmentation.</p>

---
