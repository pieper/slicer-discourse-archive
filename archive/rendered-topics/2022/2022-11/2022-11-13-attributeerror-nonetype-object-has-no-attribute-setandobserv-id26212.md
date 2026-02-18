# AttributeError: 'NoneType' object has no attribute 'SetAndObserveTransformNodeID'

**Topic ID**: 26212
**Date**: 2022-11-13
**URL**: https://discourse.slicer.org/t/attributeerror-nonetype-object-has-no-attribute-setandobservetransformnodeid/26212

---

## Post #1 by @hourglassnam (2022-11-13 07:10 UTC)

<p>Dear community,<br>
First of all, thank you always for helping!<br>
I had been trying to modify the <a href="https://github.com/jmhuie/Slicer-SegmentGeometry/blob/ecefdc3b4e0e7bbb80de4409c7baab4097d69cfe/SegmentGeometry/SegmentGeometry.py#L387" rel="noopener nofollow ugc">onPrincipalAxes()</a> of the SegmentGeometry module to fit my use.</p>
<pre><code class="lang-auto">def troubleGetName(selectedSeg):
	sourceNode = slicer.mrmlScene.GetNodeByID("vtkMRMLSegmentationNode1")
	sourceSeg = sourceNode.GetSegmentation()
	volumeNode = slicer.mrmlScene.GetNodeByID('vtkMRMLScalarVolumeNode1')
	volumeName = volumeNode.GetName()
	segmentId = sourceSeg.GetSegmentIdBySegmentName(selectedSeg)
	segmentationNode = sourceSeg.GetSegment(selectedSeg)
	displayNode = sourceNode.GetDisplayNode()
	displayNode.SetAllSegmentsVisibility(True)
	segmentationNode.SetAndObserveTransformNodeID(None)

#my segment name  is "Grain"
troubleGetName("Grain")
</code></pre>
<p>And I soon came across a situation where below error happens.</p>
<blockquote>
<p>Traceback (most recent call last):<br>
File “”, line 1, in <br>
File “”, line 10, in troubleGetName<br>
AttributeError: ‘NoneType’ object has no attribute ‘SetAndObserveTransformNodeID’</p>
</blockquote>
<p>I looked up the SetAndObserveTransformNodeID on the <a href="https://apidocs.slicer.org/master/classvtkMRMLTransformableNode.html" rel="noopener nofollow ugc">vtkMRMLTransformableNode Class Reference</a>  and saw that SetAndObserveTransformNodeID is supposed to be after a vtkMRMLTransformableNode.</p>
<blockquote>
<p>bool vtkMRMLTransformableNode::SetAndObserveTransformNodeID	(	const char * 	transformNodeID	)</p>
</blockquote>
<p><div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/a/fad32cbaf4deebb5c22bab78fd73f1694b32ac6b.jpeg" data-download-href="/uploads/short-url/zMTO3zd8q4zK6RqLq9GtNJA0yv1.jpeg?dl=1" title="image" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fad32cbaf4deebb5c22bab78fd73f1694b32ac6b_2_690x431.jpeg" alt="image" data-base62-sha1="zMTO3zd8q4zK6RqLq9GtNJA0yv1" width="690" height="431" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fad32cbaf4deebb5c22bab78fd73f1694b32ac6b_2_690x431.jpeg, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fad32cbaf4deebb5c22bab78fd73f1694b32ac6b_2_1035x646.jpeg 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/f/a/fad32cbaf4deebb5c22bab78fd73f1694b32ac6b_2_1380x862.jpeg 2x" data-dominant-color="F6F6F6"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">image</span><span class="informations">1813×1134 118 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>
<p>The captured image and other people’s cases seems to be telling me that segment node can be used as the vtkMRMLTransformableNode. So I cannot figure out what went wrong.<br>
Can anyone please tell me what I am doing wrong?</p>
<p>By the way, I just have to mention how much I love this module!<br>
Easy to use and so convenient!!</p>
<p>Thank you in advance!!</p>
<p>*** I posted wrong error message at first, so I fixed it!! Sorry about that!!</p>

---

## Post #2 by @lassoan (2022-11-13 14:59 UTC)

<p>Only “segmentation” is a node. A “segment” is not a node, therefore you cannot move it independently from other segments.</p>
<p>To transform a single segment, you need to create a new segmentation node, move the segment there, apply and harden a transform on the segmentation node, then move the segment back to the original segmentation node (and the temporary segmentation node can be removed). These may sound like a lot of steps, but all of them are very lightweight (except maybe hardening the transform, which may be somewhat computationally intensive for a non-linear warping transform).</p>

---
