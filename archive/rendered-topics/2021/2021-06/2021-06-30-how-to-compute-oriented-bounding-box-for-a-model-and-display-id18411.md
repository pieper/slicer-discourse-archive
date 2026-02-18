# How to compute oriented bounding box for a model and display it using annotation ROI?

**Topic ID**: 18411
**Date**: 2021-06-30
**URL**: https://discourse.slicer.org/t/how-to-compute-oriented-bounding-box-for-a-model-and-display-it-using-annotation-roi/18411

---

## Post #1 by @jumbojing (2021-06-30 02:04 UTC)

<p>In <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#get-size-position-and-orientation-of-each-segment" rel="noopener nofollow ugc">Get size, position, and orientation of each segment</a>, I learned how to compute oriented bounding box for each segment and displays them using annotation ROI.<br>
I want to know how to compute oriented bounding box for a model and display it using annotation ROI .</p>

---

## Post #2 by @jumbojing (2021-06-30 02:06 UTC)

<p>or how to convert model to segmentation node with python?</p>

---

## Post #3 by @lassoan (2021-06-30 02:27 UTC)

<p>You can <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html#load-a-3d-image-or-model-file-as-segmentation">load a surface mesh file as segmentation</a> or import a model into a segmentation node by calling <a href="http://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#a19cdf27aa9e1068d6b39221600086f35"><code>slicer.modules.segmentations.logic().ImportModelToSegmentationNode(modelNode, segmentationNode)</code></a>.</p>

---

## Post #4 by @jumbojing (2021-06-30 03:02 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="18411">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p><a href="http://apidocs.slicer.org/master/classvtkSlicerSegmentationsModuleLogic.html#a19cdf27aa9e1068d6b39221600086f35" rel="noopener nofollow ugc"> <code>slicer.modules.segmentations.logic().ImportModelToSegmentationNode(modelNode, segmentationNode)</code> </a>.</p>
</blockquote>
</aside>
<p>Thanks,谢谢老师! <img src="https://emoji.discourse-cdn.com/twitter/slightly_smiling_face.png?v=12" title=":slightly_smiling_face:" class="emoji" alt=":slightly_smiling_face:" loading="lazy" width="20" height="20"></p>

---
