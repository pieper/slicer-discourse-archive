---
topic_id: 46699
title: "Multiple Organs Segmentation In A Mri Sequence"
date: 2026-04-09
url: https://discourse.slicer.org/t/46699
---

# Multiple organs segmentation in a MRI sequence?

**Topic ID**: 46699
**Date**: 2026-04-09
**URL**: https://discourse.slicer.org/t/multiple-organs-segmentation-in-a-mri-sequence/46699

---

## Post #1 by @koperkill (2026-04-09 13:36 UTC)

<p>Hello,</p>
<p>For a DCE-MRI study, I would like to extract the signal intensity, through time, for a dozen organs and regions of the upper body.</p>
<p>I have successfully built a time sequence using my 40 volumes in time, drawn a segmentation mask for a single ROI, and experimented with the automatic segmentation with the excellent tutorial provided by <a class="mention" href="/u/lassoan">@lassoan</a> at <a href="https://discourse.slicer.org/t/automatic-segmentation-of-sequences-in-time/20756" class="inline-onebox">Automatic segmentation of sequences in time</a> , successfully propagating the registration through time.</p>
<p>This works with some success for bigger structures, but finer ones likes arteries and veins occasionally suffer from very bad registration; registration translates my veins into other organs for a few volumes, yet works fine for most of them…</p>
<p>I’m inclined to think that drawing more regions would add physiologically sound constraints on the registration, thus avoiding a transformation that misplaces, for example, the liver outside of the body, but this is purely speculative.</p>
<p>Finally, here is my questions:</p>
<ul>
<li>How would one solve this specific problem?
<ul>
<li>Should each organ be separately segmented or all should be done simultaneously as I suspect?</li>
<li>If registration of ROI works on most volumes, is it possible to manually adjust the few that do not align well?</li>
<li>Is there a hidden functionality that I’m not aware of for this specific problem?</li>
</ul>
</li>
</ul>
<p>Looking forward to reading your ideas! Thank you for your help</p>

---
