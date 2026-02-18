# Muscle segmentation - Can you duplicate a segment?

**Topic ID**: 8090
**Date**: 2019-08-19
**URL**: https://discourse.slicer.org/t/muscle-segmentation-can-you-duplicate-a-segment/8090

---

## Post #1 by @tsjamo (2019-08-19 14:52 UTC)

<p>Hello,</p>
<p>I have created a segment and wish to duplicate so I can edit one copy, whilst keeping the original copy intact. Please can someone tell me if this is possible.</p>
<p>More detail - I have segmented whole thigh muscle CSA but then wish to duplicate the segment so I can remove everything but the quadriceps to get a quadriceps CSA, and then do the same but keep the hamstrings to get a hamstrings CSA, etc.</p>
<p>Thank you,<br>
Tom</p>

---

## Post #2 by @lassoan (2019-08-19 15:24 UTC)

<p>You can duplicate a segment by creating a new one and copy content from another segment using Logical operators effect. Make sure you change masking settings to enable overlap, to prevent overlapping segments overwrite each other.</p>
<p>Note that if you want to separate a segment into multiple segments then it is usually better to not clone the original segment but instead change masking settings to allow editing only in that segment. You can then create a new empty segment and use paint, draw, scissors, etc effects to assign parts of the original segment to this new segment.</p>
<p>You may find that it is even more efficient to segment individual muscles from the beginning, instead of segmenting a group of muscles and then split them. Since muscles tend to be elongated structures, you can segment them very quickly by doing a full segmentation on one of every 5-10 slices and interpolate between them using “Fill between slices” effect.</p>

---
