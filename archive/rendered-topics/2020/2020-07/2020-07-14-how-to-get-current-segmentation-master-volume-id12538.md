# How to get current segmentation master volume?

**Topic ID**: 12538
**Date**: 2020-07-14
**URL**: https://discourse.slicer.org/t/how-to-get-current-segmentation-master-volume/12538

---

## Post #1 by @vertebra (2020-07-14 17:40 UTC)

<p>Hello! Thank you for all the help <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> <a class="mention" href="/u/lassoan">@lassoan</a> - we got our module to work.</p>
<p>Our very last question is when we assign our masterVolumeNode right now:</p>
<p>masterVolumeNode = SampleData.SampleDataLogic().downloadCTACardio()</p>
<p>We assign it to a newly downloaded CTACardio. Is there a way to just assign it to the current master volume? Let’s say I upload my own files, what is the Python syntax to assign it to those files automatically?</p>
<p>Thanks!</p>

---

## Post #2 by @Sunderlandkyl (2020-07-14 20:39 UTC)

<p>Have you tried vtkMRMLSegmentEditorNode::GetMasterVolumeNode()?<br>
<a href="https://apidocs.slicer.org/master/classvtkMRMLSegmentEditorNode.html#ae7dbe89f755f115624dc1c701e9dcf80" class="onebox" target="_blank" rel="nofollow noopener">https://apidocs.slicer.org/master/classvtkMRMLSegmentEditorNode.html#ae7dbe89f755f115624dc1c701e9dcf80</a></p>

---

## Post #3 by @vertebra (2020-07-15 13:12 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="2" data-topic="12538">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>GetMasterVolumeNode</p>
</blockquote>
</aside>
<p>Thank you! It works in our module.</p>

---
