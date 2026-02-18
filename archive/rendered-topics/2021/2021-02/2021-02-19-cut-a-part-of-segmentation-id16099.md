# Cut a part of segmentation

**Topic ID**: 16099
**Date**: 2021-02-19
**URL**: https://discourse.slicer.org/t/cut-a-part-of-segmentation/16099

---

## Post #1 by @Aep93 (2021-02-19 19:54 UTC)

<p>Hello all,<br>
How can I cut a part of my segmentation that is inside a specific ROI?</p>

---

## Post #2 by @lassoan (2021-02-19 20:07 UTC)

<p>There is no ROI filling effect in Segment Editor yet. We wanted to wait for completion of the new Markups ROI, which has completed this week, so now it would be possible to add it. If you are interested in learning Python scripting in Slicer then it would be great if you could add it (we can help you getting started).</p>
<p>Otherwise, there are similar tools. For example, you can use:</p>
<ul>
<li>Scissors effect with rectangular shape, or</li>
<li>Surface cut effect (provided by SegmentEditorExtraEffects extension), with smoothing disabled</li>
<li>Create a box model (e.g., using SlicerIGT extensions’s Create models module) and transform it using a transform interactively.</li>
</ul>

---

## Post #3 by @Aep93 (2021-02-19 21:45 UTC)

<p>Thanks for your response <a class="mention" href="/u/lassoan">@lassoan</a>. I have little experience with Python coding in the slicer, but I could solve my problem with the Scissors effect for now. Thanks a lot.</p>

---
