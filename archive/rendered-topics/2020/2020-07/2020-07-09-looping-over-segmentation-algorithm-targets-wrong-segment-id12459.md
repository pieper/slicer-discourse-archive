---
topic_id: 12459
title: "Looping Over Segmentation Algorithm Targets Wrong Segment"
date: 2020-07-09
url: https://discourse.slicer.org/t/12459
---

# Looping Over Segmentation Algorithm Targets Wrong Segment

**Topic ID**: 12459
**Date**: 2020-07-09
**URL**: https://discourse.slicer.org/t/looping-over-segmentation-algorithm-targets-wrong-segment/12459

---

## Post #1 by @vertebra (2020-07-09 13:38 UTC)

<p>We have got our segmentation algorithm working! Now we are looping over it to allow doctors to segment multiple vertebrae. Whenever we run our code in a for loop, the seed around the second point, F-2(purple in the diagram on the yellow slice), works. However, when we run the effect function, the algorithm works perfectly fine but adds the segmented piece to the first segmentation. Does anyone have any ideas why?</p>
<p>We think the issue is in these lines of code when looping:</p>
<p>segmentationNode.AddSegmentFromClosedSurfaceRepresentation(lumbarSeed.GetOutput(), “Lumbar-” + str(x+1), [random(), random(), random()])<br>
segmentEditorWidget = slicer.qMRMLSegmentEditorWidget()<br>
segmentEditorWidget.setMRMLScene(slicer.mrmlScene)<br>
segmentEditorNode = slicer.vtkMRMLSegmentEditorNode()<br>
slicer.mrmlScene.AddNode(segmentEditorNode)<br>
segmentEditorWidget.setMRMLSegmentEditorNode(segmentEditorNode)<br>
segmentEditorWidget.setSegmentationNode(segmentationNode)<br>
segmentEditorWidget.setMasterVolumeNode(masterVolumeNode)</p>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/4/3/43bfe0104b2e9cf3ba854585c9b3267e3383b204.jpeg" data-download-href="/uploads/short-url/9Fl52GD7P96MI3wPBYFzvUfBgYQ.jpeg?dl=1" title="Screen Shot 2020-07-09 at 9.35.02 AM" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/43bfe0104b2e9cf3ba854585c9b3267e3383b204_2_690x431.jpeg" alt="Screen Shot 2020-07-09 at 9.35.02 AM" data-base62-sha1="9Fl52GD7P96MI3wPBYFzvUfBgYQ" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/43bfe0104b2e9cf3ba854585c9b3267e3383b204_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/43bfe0104b2e9cf3ba854585c9b3267e3383b204_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/2X/4/43bfe0104b2e9cf3ba854585c9b3267e3383b204_2_1380x862.jpeg 2x" data-dominant-color="474750"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">Screen Shot 2020-07-09 at 9.35.02 AM</span><span class="informations">1440×900 231 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @lassoan (2020-07-09 13:48 UTC)

<aside class="quote no-group" data-username="vertebra" data-post="1" data-topic="12459">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vertebra/48/7475_2.png" class="avatar"> vertebra:</div>
<blockquote>
<p>However, when we run the effect function, the algorithm works perfectly fine but adds the segmented piece to the first segmentation.</p>
</blockquote>
</aside>
<p>This is exactly how the effect is supposed to work: incrementally add more parts to the current segment with each click.</p>
<p>If you want to create a separate segment for each click then create and select a new segment before each click.</p>

---

## Post #4 by @vertebrae (2020-07-09 15:20 UTC)

<aside class="quote no-group quote-post-not-found" data-username="vertebra" data-post="3" data-topic="12459">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/vertebra/48/7475_2.png" class="avatar"> vertebra:</div>
<blockquote>
<p>We thought the new segmentationNode would automatically do that.</p>
</blockquote>
</aside>
<p>We also looked in the class reference linked below but we did not find anything.</p>
<p><a href="https://apidocs.slicer.org/master/classqMRMLSegmentEditorWidget.html#a07f1984ccaea1b8e49245d4b79be4382" class="onebox" target="_blank" rel="noopener nofollow ugc">https://apidocs.slicer.org/master/classqMRMLSegmentEditorWidget.html#a07f1984ccaea1b8e49245d4b79be4382</a></p>

---
