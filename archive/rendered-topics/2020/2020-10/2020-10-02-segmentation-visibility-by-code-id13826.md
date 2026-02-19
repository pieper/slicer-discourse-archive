---
topic_id: 13826
title: "Segmentation Visibility By Code"
date: 2020-10-02
url: https://discourse.slicer.org/t/13826
---

# Segmentation visibility by code

**Topic ID**: 13826
**Date**: 2020-10-02
**URL**: https://discourse.slicer.org/t/segmentation-visibility-by-code/13826

---

## Post #1 by @aldoSanchez (2020-10-02 19:58 UTC)

<p>Hi, guys.<br>
today I am trying to access the visibility of objects created in 3d models by code.<br>
What I’m trying to do is what’s in the image just show Left-Cerebral-Cortex and remove the visibility of all the others.<br>
thanks<br>
<div class="lightbox-wrapper"><a class="lightbox" href="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00ffeeb87382ba795e2b09d8702fc7f38e38b692.png" data-download-href="/uploads/short-url/8QkDv3MzwvrIUgCAc3dxv6ryaS.png?dl=1" title="segmentation" rel="noopener nofollow ugc"><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00ffeeb87382ba795e2b09d8702fc7f38e38b692_2_690x352.png" alt="segmentation" data-base62-sha1="8QkDv3MzwvrIUgCAc3dxv6ryaS" width="690" height="352" srcset="https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00ffeeb87382ba795e2b09d8702fc7f38e38b692_2_690x352.png, https://us1.discourse-cdn.com/flex002/uploads/slicer/optimized/3X/0/0/00ffeeb87382ba795e2b09d8702fc7f38e38b692_2_1035x528.png 1.5x, https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/0/0/00ffeeb87382ba795e2b09d8702fc7f38e38b692.png 2x" data-dominant-color="979398"><div class="meta"><svg class="fa d-icon d-icon-far-image svg-icon" aria-hidden="true"><use href="#far-image"></use></svg><span class="filename">segmentation</span><span class="informations">1366×698 168 KB</span><svg class="fa d-icon d-icon-discourse-expand svg-icon" aria-hidden="true"><use href="#discourse-expand"></use></svg></div></a></div></p>

---

## Post #2 by @Sunderlandkyl (2020-10-02 20:04 UTC)

<p>Try something like this:</p>
<pre><code class="lang-auto">displayNode.SetAllSegmentsVisibility(False)
displayNode.SetSegmentVisibility(leftCerebralCortexSegmentID, True)
</code></pre>
<p><a href="https://apidocs.slicer.org/master/classvtkMRMLSegmentationDisplayNode.html#ac6f83b3e93af6d030690b7cc955abcdd" rel="noopener nofollow ugc">SetAllSegmentsVisibility</a> (bool visible)<br>
<a href="https://apidocs.slicer.org/master/classvtkMRMLSegmentationDisplayNode.html#aee65fdd850b42e1b1d1f7117bc082b92" rel="noopener nofollow ugc">SetSegmentVisibility</a> (std::string segmentID, bool visible)</p>
<p>If you still want all of the the 2D representations to be visible, you can use these functions:<br>
<a href="https://apidocs.slicer.org/master/classvtkMRMLSegmentationDisplayNode.html#a9ad8635b19e7168dc1a693cf9872bbbe" rel="noopener nofollow ugc">SetAllSegmentsVisibility3D</a> (bool visible, bool changeVisibleSegmentsOnly=false)<br>
<a href="https://apidocs.slicer.org/master/classvtkMRMLSegmentationDisplayNode.html#a14e8c2cd351be7cea8793283845c6526" rel="noopener nofollow ugc">SetSegmentVisibility3D</a> (std::string segmentID, bool visible)</p>

---

## Post #3 by @aldoSanchez (2020-10-03 22:58 UTC)

<p>hi<br>
this works to hide all segmentation:</p>
<pre><code class="lang-auto">disp=slicer.util.getNode('Segmentation')
disp.SetDisplayVisibility(False)
</code></pre>
<p>but I can’t make it show only Left-Cerebral-Cortex .<br>
try this:</p>
<pre><code class="lang-auto">slicer.vtkMRMLSegmentationDisplayNode('Segmentation').SetAllSegmentsVisibility(False)
</code></pre>
<p>but I have the following error:</p>
<pre><code class="lang-auto">ValueError: could not extract hexadecimal address from argument string
</code></pre>

---

## Post #4 by @Sunderlandkyl (2020-10-05 14:55 UTC)

<pre><code class="lang-auto">segmentationNode = slicer.util.getNode('Segmentation')
displayNode = segmentationNode.GetDisplayNode()
displayNode.SetAllSegmentsVisibility(False) # Hide all segments
displayNode.SetSegmentVisibility(leftCerebralCortexSegmentID, True) # Show specific segment
</code></pre>

---

## Post #5 by @aldoSanchez (2020-10-05 15:03 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="4" data-topic="13826">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p><code>leftCerebralCortexSegmentID</code></p>
</blockquote>
</aside>
<p>How can I see the ID of<br>
leftCerebralCortexSegmentID<br>
the label name is Left-Cerebral-Cortex</p>

---

## Post #6 by @Sunderlandkyl (2020-10-05 15:05 UTC)

<p>You can use this:</p>
<pre><code class="lang-auto">segmentation = segmentationNode.GetSegmentation()
leftCerebralCortexSegmentID = segmentation.GetSegmentIdBySegmentName("Left-Cerebral-Cortex")
</code></pre>
<p><a href="https://apidocs.slicer.org/master/classvtkSegmentation.html#adda91e085fa229cd6d88abc1aa268b12" rel="noopener nofollow ugc">GetSegmentIdBySegmentName</a> (std::string name)</p>

---

## Post #7 by @aldoSanchez (2020-10-05 15:15 UTC)

<p>thank you so much it works perfect i leave the code here:</p>
<pre><code class="lang-python">segmentationNode=getNode('Segmentation')
segmentation = segmentationNode.GetSegmentation()
leftCerebralCortexSegmentID = segmentation.GetSegmentIdBySegmentName("Left-Cerebral-Cortex")
displayNode = segmentationNode.GetDisplayNode()
displayNode.SetAllSegmentsVisibility(False) # Hide all segments
displayNode.SetSegmentVisibility(leftCerebralCortexSegmentID, True) # Show specific segment
</code></pre>

---
