---
topic_id: 5124
title: "Adding Operations To Segment Editors Scissors Tool"
date: 2018-12-18
url: https://discourse.slicer.org/t/5124
---

# Adding operations to Segment Editor's Scissors tool

**Topic ID**: 5124
**Date**: 2018-12-18
**URL**: https://discourse.slicer.org/t/adding-operations-to-segment-editors-scissors-tool/5124

---

## Post #1 by @hherhold (2018-12-18 14:19 UTC)

<p>Greetings Slicers,</p>
<p>I was thinking about combining some operations with the Scissors tool. It would be really useful in some of my scans to be able to do island removal in a certain area, for example - draw a symmetric slice cut that defines a small volume that then has island removal performed in it, preferably in a single operation.</p>
<p>I’m pretty sure this can be done “manually” in python, but I was wondering how doable/acceptable it would be to add another operation to the Scissors module. I’m happy to investigate this and implement it, I’m not asking for someone else to do it! I’m mostly wondering if it would be generally useful to anybody but me.</p>
<p>Thanks!!!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2018-12-18 15:39 UTC)

<p>It would be enough to update Islands effect to use masking. You would then:</p>
<ul>
<li>create a new segment: <em>YourMaskSegment</em>
</li>
<li>fill it using Scissors effect, using Mode: Fill inside, enable overlap with existing segments (Masking / Overwrite other segments: None)</li>
<li>use the new segment as mask (Masking / Editable area: Inside Segment <em>YourMaskSegment</em>)</li>
<li>use Islands effect to remove small islands (only masked region would be affected)</li>
</ul>
<p>Making Island effect use masking settings would be nice for other use cases as well, so it would be great if you could work on it. The change may be as simple as using <em>modifySelectedSegmentByLabelmap</em> instead of <em>SetBinaryLabelmapToSegment</em> (see <em>SegmentEditorLogicalEffect</em> as an example).</p>

---

## Post #3 by @hherhold (2018-12-19 16:09 UTC)

<p>I will take a look. Thanks for the pointers on getting started!</p>

---
