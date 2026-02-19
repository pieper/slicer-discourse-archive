---
topic_id: 5974
title: "Segment Visibility Code Not Functioning For Me"
date: 2019-02-28
url: https://discourse.slicer.org/t/5974
---

# Segment Visibility Code Not Functioning for me

**Topic ID**: 5974
**Date**: 2019-02-28
**URL**: https://discourse.slicer.org/t/segment-visibility-code-not-functioning-for-me/5974

---

## Post #1 by @coolsocks (2019-02-28 22:03 UTC)

<p>Hi,<br>
I have an issue where indeed I can set the entire segmentation to not be visible via vtkMRMLSegmentationNode by doing:<br>
display = segmentation.GetDisplayNode()<br>
display.SetVisibility(0)</p>
<p>However, whenever I attempt to set a particular segment to not be visible by doing:<br>
display.SetSegmentVisibility(segment_id,0)<br>
The segment is still visible to me. When I attempt accessing the node through Python I indeed see that the Visibility for the segment has been set to false, however why is the segment still appearing on my views?<br>
Am I missing some code here?<br>
Thanks!</p>

---

## Post #2 by @cpinter (2019-02-28 22:27 UTC)

<p>Thanks for the detailed explanation!</p>
<p>What Slicer version do you use?<br>
I tried a recent nightly, and the same code works for me. Is it possible that you try to use the name of the segment and not its ID? If you rename a segment then its ID will still be the original ‘Segment_1’ for example, and GetSegmentVisibility will return a simple False on invalid ID as well (but an error appears in the log saying “GetSegmentVisibility: No display properties found for segment with ID artery”).<br>
What if you do this instead?</p>
<p><code>display.SetSegmentVisibility(segmentation.GetSegmentation().GetSegmentIdBySegmentName(segment_id), False)</code></p>

---

## Post #3 by @coolsocks (2019-03-01 14:35 UTC)

<aside class="quote no-group" data-username="coolsocks" data-post="1" data-topic="5974">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/coolsocks/48/3299_2.png" class="avatar"> coolsocks:</div>
<blockquote>
<p>can set the entire segmentation to not be visible via vtkMRMLSegmentationNode by doing:<br>
display = segmentation.GetDisplayNode()<br>
display.SetVisibility(0)</p>
<p>However, whenever I attempt to set a particular segment to not be visible by doing:<br>
display.SetSegmentVisibility(segment_id,0)<br>
The segment is still visible to me. When I attempt accessing the node through Python I indeed see that the Visibility for the segment has been set to false, however why is the segment still appearing on my views?</p>
</blockquote>
</aside>
<p>Thanks that did the trick! I must’ve mixed up the two.</p>

---
