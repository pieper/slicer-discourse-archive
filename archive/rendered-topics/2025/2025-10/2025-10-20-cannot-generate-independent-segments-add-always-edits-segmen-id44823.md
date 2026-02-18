# Cannot generate independent segments — Add always edits Segment_1

**Topic ID**: 44823
**Date**: 2025-10-20
**URL**: https://discourse.slicer.org/t/cannot-generate-independent-segments-add-always-edits-segment-1/44823

---

## Post #1 by @Saliha_Akcay (2025-10-20 16:16 UTC)

<p>Hello, I am working on lesion segmentation and need to extract a clean 2-mm peri-lesional bone shell for texture/fractal analysis.</p>
<p>The problem is: when I click “Add” to create a new segment (e.g. Segment_2), Slicer still keeps modifying Segment_1 only. Even if I manually select Segment_2 and apply “Margin” (2 mm) or “Logical Operators → SUBTRACT”, Slicer always changes Segment_1 — and Segment_2 does not update at all.</p>
<p>What I have tried:<br>
• Set Application Settings → Segmentations → “Default overwrite mode” = Allow overlap<br>
• Manually selected the segment (Segment_2) before applying Margin<br>
• Confirmed I am in the Segment Editor, not Segmentations<br>
• Tried both 2D slice views and 3D view<br>
• Restarted Slicer</p>
<p>Still, every operation affects only Segment_1.</p>
<p><strong>My goal:</strong><br>
I want to duplicate the original lesion as Segment_2, expand it by exactly +2 mm (Margin effect), then subtract the original lesion (Segment_1) to isolate only the hollow peri-lesional shell.</p>
<p>What could still be forcing Slicer to always keep Segment_1 active, even after adding and selecting a new segment?<br>
Is there any UI or masking setting I might still be missing?</p>
<p>If needed, I can provide a quick screen recording. Thank you in advance.</p>

---

## Post #2 by @lassoan (2025-10-20 16:18 UTC)

<p>Please provide more information. A few screen captures may be enough, but a screen recording video would be even better. You can also join the <a href="https://discourse.slicer.org/c/community/hangout/20">weekly meeting</a> on one of the Tuesdays to share your screen, - we should be able to tell in a few minutes what is going on.</p>

---
