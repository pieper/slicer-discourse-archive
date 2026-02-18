# Possible to reset a segment ID inside the SegmentEditor?

**Topic ID**: 22613
**Date**: 2022-03-21
**URL**: https://discourse.slicer.org/t/possible-to-reset-a-segment-id-inside-the-segmenteditor/22613

---

## Post #1 by @aiden.zhu (2022-03-21 04:12 UTC)

<p>Inside windows,<br>
Version: 4.11.20210226</p>
<p>Hi guys,<br>
I have an issue like this:<br>
while I apply<br>
Method-A: slicer.modules.segmentations.logic().ImportLabelmapToSegmentationNode(self.labelNode, self.segmentationNode), the resulted segmentsID go as numbers as “1, 2, 3, 4, 5…”</p>
<p>Method-B: While inside segment-editor to click “Add” to have a new segment which will have a segmentID as “Segment_1”, “Segment_2”…</p>
<p>So how can I share a consistent way to control those segmentIDs there?<br>
Either numbers (A) or “Segment_x” (B) works for me but I prefer to having the consistent way.</p>

---

## Post #2 by @lassoan (2022-03-21 13:35 UTC)

<p>In recent Slicer Preview Releases we use the color names instead of just 1, 2, 3, … when you import a labelmap volume into a segmentation. Color names are used as segment IDs by default, too (but if needed a suffix is added to make them unique).</p>
<p>Segment IDs are never displayed to the user, so they can be treated as unique strings with random content. They are usually initialized with human-readable strings for more convenient debugging, but if we find that it confuses developers then we might consider switching to some random hash in the future.</p>

---

## Post #3 by @aiden.zhu (2022-03-21 13:39 UTC)

<p><a class="mention" href="/u/lassoan">@lassoan</a><br>
Thanks a lot.</p>

---
