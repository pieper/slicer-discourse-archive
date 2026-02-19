---
topic_id: 13833
title: "Converting Labelmapvolume Node With Only One Label To Segmen"
date: 2020-10-02
url: https://discourse.slicer.org/t/13833
---

# Converting labelmapvolume node with only one label to segmentation node does not use colour table

**Topic ID**: 13833
**Date**: 2020-10-02
**URL**: https://discourse.slicer.org/t/converting-labelmapvolume-node-with-only-one-label-to-segmentation-node-does-not-use-colour-table/13833

---

## Post #1 by @Vincent_C (2020-10-02 22:27 UTC)

<p>Hi all,</p>
<p>I have a labelmap volume node with only 1 label and I am using a custom LUT for it. When I convert the labelmap volume node to a segmentation node, the segment inside does not respect the colour table name for that label, but rather, it names it after the node name.</p>
<p>If the labelmap volume node has 2 labels or more, and a custom LUT is loaded, converting to a segmentation node will create segments that respect the colour table name for those labels.</p>
<p>I think this behaviour should be changed! What do you guys think?</p>
<p><img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/f/f/ff3e0bbd2bd9cbb884e62cf84962018f61c964d7.png" alt="Screenshot 2020-10-02 152441" data-base62-sha1="ApYGD7sMZJEwwz8Da5tIb6SM9jV" width="544" height="131"></p>
<p>Vince</p>

---

## Post #2 by @Sunderlandkyl (2020-10-02 23:50 UTC)

<p>Thanks for reporting! I’ll take a look at it.</p>

---

## Post #3 by @sogo (2021-01-11 06:16 UTC)

<p>Hi,<br>
I am facing similar issue when I try to ExportSegmentsToLabelmapNode or ImportLabelmapToSegmentationNode with only one segment programmatically. The labelmap node ignores the provided color table and when  doing “ImportLabelmapToSegmentationNode”  makes a default segmentID with name labelmapvolume (this is after I ImportLabelmapToSegmentationNode). The workaround I do for this issue so far is to</p>
<ol>
<li>Make new segment</li>
<li>Deepcopy new segment by newSegment-&gt;DeepCopy()</li>
<li>Remove old segment, name new segment as per the required segment ID and add to segmentation node</li>
</ol>
<p>This workaround is working so far but would like to know if there is any fix for this issue. Thanks</p>

---

## Post #4 by @lassoan (2021-01-11 06:26 UTC)

<p>I’ve just checked and this works well in latest Slicer Preview Release. If the latest preview release does not work as you expect then please describe the exact steps you perform. What do you mean by “the labelmap node ignores the provided color table”? What did you do, what did you expect to happen, and what happened instead?</p>

---

## Post #5 by @sogo (2021-01-11 12:51 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, the issue is exactly as shown in screenshot by the thread creator. It is like the segment ID does not matches the color table color name when there is only one segment even when I try to set the colortable node to the display node from SetAndObserveColorNodeID. I tried manually setting the name of segment but it only changes the name tag but does not change segment ID. I hope this makes it more clear. I will try with latest preview release and let you know.</p>

---

## Post #6 by @kpopuri (2021-01-13 04:06 UTC)

<p><a class="mention" href="/u/sogo">@sogo</a></p>
<p>Yes, this fix was apparently made here:<br>
<a href="https://github.com/Slicer/Slicer/commit/ca7d0905343728b1a666d573ff6c3235ceb9cb8a#diff-a860209146aa5634ba99b5b9f046c2b91a90f8f0db2c980dbd0f216a2df103d5" class="inline-onebox" rel="noopener nofollow ugc">BUG: Set segment name from color table when the labelmap has one label · Slicer/Slicer@ca7d090 · GitHub</a>.</p>

---

## Post #7 by @sogo (2021-01-13 07:42 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a>  <a class="mention" href="/u/kpopuri">@kpopuri</a>  Thank you, tested it and the issue is fixed.</p>

---

## Post #8 by @Vincent_C (2021-01-13 07:51 UTC)

<p>Thanks <a class="mention" href="/u/sunderlandkyl">@Sunderlandkyl</a> and <a class="mention" href="/u/lassoan">@lassoan</a> !</p>

---
