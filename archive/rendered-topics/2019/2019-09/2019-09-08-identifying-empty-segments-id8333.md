# Identifying empty segments?

**Topic ID**: 8333
**Date**: 2019-09-08
**URL**: https://discourse.slicer.org/t/identifying-empty-segments/8333

---

## Post #1 by @Amine (2019-09-08 00:51 UTC)

<p>Hi, i’ve been using this code to grab a segment, but i found no way to check if it’s empty or not.</p>
<pre><code>segmentation_node = getNode("Segmentation")
seg = segmentation_node.GetSegmentation()
seg0 = seg.GetNthSegment(0)
</code></pre>
<p>i tried using <code>polydata = seg0.GetRepresentation("Closed surface")</code> then <code>polydata.GetNumberOfCells()</code> but it only works if there is a closed surface representation of the segment, i’m looking for some approach that is independent of the existence of a closed surface if available, thanks for any inputs.</p>

---

## Post #2 by @cpinter (2019-09-08 13:55 UTC)

<p>First of all, you can make your life a bit easier by using the utility functions to get representations:<br>
<a href="https://apidocs.slicer.org/master/classvtkMRMLSegmentationNode.html#a71ebfa4439ec3ebdf57994888f572623" class="onebox" target="_blank" rel="nofollow noopener">https://apidocs.slicer.org/master/classvtkMRMLSegmentationNode.html#a71ebfa4439ec3ebdf57994888f572623</a></p>
<p>As for your question, you can check if the image data is empty by using the IsEmpty function<br>
<a href="https://apidocs.slicer.org/master/classvtkOrientedImageData.html#a8ba73e835202dc5e05539a9e4441d70f" class="onebox" target="_blank" rel="nofollow noopener">https://apidocs.slicer.org/master/classvtkOrientedImageData.html#a8ba73e835202dc5e05539a9e4441d70f</a></p>
<p>If it can occur in your use case that you have an image data with a valid extent but you’re wondering if there are only background voxels, you can use the vkImageAccumulate class<br>
<a href="https://vtk.org/doc/nightly/html/classvtkImageAccumulate.html" class="onebox" target="_blank" rel="nofollow noopener">https://vtk.org/doc/nightly/html/classvtkImageAccumulate.html</a></p>

---

## Post #3 by @lassoan (2019-09-08 17:17 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="8333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>If it can occur in your use case that you have an image data with a valid extent but you’re wondering if there are only background voxels, you can use the vkImageAccumulate class<br>
<a href="https://vtk.org/doc/nightly/html/classvtkImageAccumulate.html">https://vtk.org/doc/nightly/html/classvtkImageAccumulate.html </a></p>
</blockquote>
</aside>
<p>You can also use <code>slicer.util.arrayFromSegment(segmentation_node, segment_id).max() &gt; 0</code> to see if the segment has any non-zero voxels.</p>

---

## Post #4 by @Amine (2019-09-08 18:54 UTC)

<aside class="quote no-group" data-username="lassoan" data-post="3" data-topic="8333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/lassoan/48/13_2.png" class="avatar"> lassoan:</div>
<blockquote>
<p>You can also use <code>slicer.util.arrayFromSegment(segmentation_node, segment_id).max() &gt; 0</code> to see if the segment has any non-zero voxels.</p>
</blockquote>
</aside>
<p>Thanks, that worked fine, only needed to make sure the binary label map extent was not empty(New and unedited segment), as arrayfromsegment returned an attribute error in that case</p>

---

## Post #5 by @Amine (2019-09-08 19:00 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="2" data-topic="8333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>If it can occur in your use case that you have an image data with a valid extent but you’re wondering if there are only background voxels, you can use the vkImageAccumulate class</p>
</blockquote>
</aside>
<p>Thanks, indeed i need to check for the existence of foreground voxels, i could not get vtkImageAccumulate to work properly(result is always 0) im i doing it wrong?</p>
<blockquote>
<p>segmentation = getNode(“Segmentation”)<br>
seg = segmentation.GetSegmentation()<br>
seg0 = seg.GetNthSegment(0)<br>
segID = seg.GetSegmentIdBySegment(seg0)<br>
stat = vtk.vtkImageAccumulate()<br>
stat.SetInputData(segmentation.GetBinaryLabelmapRepresentation(segID))<br>
print int(stat.GetVoxelCount())</p>
</blockquote>

---

## Post #6 by @cpinter (2019-09-08 19:18 UTC)

<p>I don’t quite understand. You marked <a class="mention" href="/u/lassoan">@lassoan</a>’s suggestion as solution still you try to use my suggestion for the exact same issue? I guess what solved your initial problem was the IsEmpty function, correct?</p>
<p>Anyway, you can use <a class="mention" href="/u/lassoan">@lassoan</a>’s simpler way to do the voxel counting.<br>
As for your actual question, you need to call Update to have vtkImageAccumulate actually do the processing. also, if you just call GetVoxelCount like this, it will return the number of all voxels. Use SetIgnoreZero(True) to only get the number of foreground voxels.</p>

---

## Post #7 by @Amine (2019-09-08 19:37 UTC)

<aside class="quote no-group" data-username="cpinter" data-post="6" data-topic="8333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>You marked <a class="mention" href="/u/lassoan">@lassoan</a>’s suggestion as solution still you try to use my suggestion for the exact same issue?</p>
</blockquote>
</aside>
<p>my issue is indeed solved, i tried vkImageAccumulate before but could not get it work, it’s interesting to have the voxel count rather than a boolean for future uses.</p>
<aside class="quote no-group" data-username="cpinter" data-post="6" data-topic="8333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>I guess what solved your initial problem was the IsEmpty function, correct?</p>
</blockquote>
</aside>
<p>I actually did use both isEmpty to eliminate new segments (returned an error with arrayfromsegment) and then <code>slicer.util.arrayFromSegment(segmentation_node, segment_id).max()</code> to check for foregroud voxels existence,  the final code is this:</p>
<pre><code>if label.IsEmpty():
    full = False
elif not(label.IsEmpty()):
    if slicer.util.arrayFromSegment(segmentation, segmentID).max() &gt; 0:
        full = True
    else:
        full = False
</code></pre>
<aside class="quote no-group" data-username="cpinter" data-post="6" data-topic="8333">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/cpinter/48/7995_2.png" class="avatar"> cpinter:</div>
<blockquote>
<p>you need to call Update to have vtkImageAccumulate actually do the processing. also, if you just call GetVoxelCount like this, it will return the number of all voxels. Use SetIgnoreZero(True) to only get the number of foreground voxels.</p>
</blockquote>
</aside>
<p>Thanks, that made it work.</p>

---

## Post #8 by @lassoan (2019-09-09 17:38 UTC)

<p>You can use either VTK or numpy functions - for this very simple check they are about equally simple and efficient. If you use numpy then you can make things simpler and more pythonic like this:</p>
<pre><code class="lang-python">try:
  full = slicer.util.arrayFromSegment(segmentation, segmentID).max() &gt; 0
except AttributeError:
  # there is no labelmap in the segment
  full = False
</code></pre>

---
