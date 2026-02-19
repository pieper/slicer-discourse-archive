---
topic_id: 8297
title: "How Through Python To Reach Or Open Segmentation Geometry Wi"
date: 2019-09-04
url: https://discourse.slicer.org/t/8297
---

# How, through python, to reach or open Segmentation-Geometry-Widget dialog or set up parameters before opening a dialog?

**Topic ID**: 8297
**Date**: 2019-09-04
**URL**: https://discourse.slicer.org/t/how-through-python-to-reach-or-open-segmentation-geometry-widget-dialog-or-set-up-parameters-before-opening-a-dialog/8297

---

## Post #1 by @aiden.zhu (2019-09-04 18:10 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>
<p>Hi all,<br>
how to open Segmentation-Geometry-Widget dialog inside the segment-editor? how to setup parameters? through python.</p>
<p>I try this:<br>
geometryWidget = slicer.qMRMLSegmentationGeometryWidget()<br>
segmentationNode = getNode(‘Segmentation’)<br>
geometryWidget.setSegmentationNode(segmentEditorNode)<br>
geometryWidget.show()</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37880c0a7eb5154a76c67d233f5e3ae7f94c5c49.png" data-download-href="/uploads/short-url/7VfJTIYMyLHdjXmYIHtav9kLkr7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/7/37880c0a7eb5154a76c67d233f5e3ae7f94c5c49.png" alt="image" data-base62-sha1="7VfJTIYMyLHdjXmYIHtav9kLkr7" width="690" height="487" data-dominant-color="FAFAFA"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">715×505 10.9 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>This one seems not associated with my current segment-editor.</p>
<p>From the segment-editor to open the dialog, which looks like this:</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bc8432135f20687f7c4eb97e517302d9d6b02b9.png" data-download-href="/uploads/short-url/8wReipryZnQSNujM2ZUoU1NVFJ7.png?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/3/b/3bc8432135f20687f7c4eb97e517302d9d6b02b9.png" alt="image" data-base62-sha1="8wReipryZnQSNujM2ZUoU1NVFJ7" width="690" height="413" data-dominant-color="F7F7F7"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">854×512 16.1 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>Thanks a lot</p>

---

## Post #2 by @lassoan (2019-10-02 01:24 UTC)

<p>Sorry for the slow response. I guess you’ve figured out that the problem was the typo in your code (you passed the segment editor node to the widget instead of the segmentation node). This works well for me:</p>
<pre><code class="lang-python">geometryWidget = slicer.qMRMLSegmentationGeometryWidget()
segmentationNode = getNode('Segmentation')
geometryWidget.setSegmentationNode(segmentationNode)
geometryWidget.show()
</code></pre>

---
