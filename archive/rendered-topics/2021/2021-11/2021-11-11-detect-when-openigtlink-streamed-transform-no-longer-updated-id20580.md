# Detect when OpenIGTlink streamed transform no longer updated

**Topic ID**: 20580
**Date**: 2021-11-11
**URL**: https://discourse.slicer.org/t/detect-when-openigtlink-streamed-transform-no-longer-updated/20580

---

## Post #1 by @atracsys-sbt (2021-11-11 14:53 UTC)

<p>Hi,<br>
I stream tracking data to Slicer via OpenIGTlink, but I would like to be able to detect (i.e. emit an event) when tracking is no longer updated (e.g. the tracked object goes out of range).<br>
I have looked at what methods are available for vtkMRMLLinearTransformNode, but found nothing conclusive.<br>
Thanks<br>
S.</p>

---

## Post #2 by @Sunderlandkyl (2021-11-11 15:07 UTC)

<p>You might want to look at the Watchdog module in SlicerIGT. It can monitor any number of nodes, and will trigger a ModifiedEvent on the Watchdog node if their status changes. The status of individual nodes can be checked with vtkMRMLWatchdogNode::GetWatchedNodeUpToDate().</p>
<p>If you’re using Plus, and SendValidTransformsOnly is “FALSE”, then you can check the TransformStatus attribute on the TransformNode which is sent over OpenIGTLink as metadata.</p>

---

## Post #3 by @atracsys-sbt (2021-11-12 09:12 UTC)

<aside class="quote no-group" data-username="Sunderlandkyl" data-post="2" data-topic="20580">
<div class="title">
<div class="quote-controls"></div>
<img alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex002/user_avatar/discourse.slicer.org/sunderlandkyl/48/79987_2.png" class="avatar"> Sunderlandkyl:</div>
<blockquote>
<p>TransformStatus</p>
</blockquote>
</aside>
<p>Since I am indeed using Plus, I opted for the second solution and it works like a charm, thanks !</p>

---
