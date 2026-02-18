# Python Library for Local Threshold Effect

**Topic ID**: 12345
**Date**: 2020-07-02
**URL**: https://discourse.slicer.org/t/python-library-for-local-threshold-effect/12345

---

## Post #1 by @vertebra (2020-07-02 18:30 UTC)

<p>In Python through slicer, is there a way to run the local threshold effect like the following pseudocode?</p>
<p>set feature size to 6.000 mm<br>
set threshold range to 245.00 to 1003.00<br>
set type to grow cut<br>
segment = point.localThreshold()</p>
<p>Thank you!</p>

---

## Post #2 by @lassoan (2020-07-02 19:35 UTC)

<p>You need to set the effect parameters and then call <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects/blob/master/SegmentEditorLocalThreshold/SegmentEditorLocalThresholdLib/SegmentEditorEffect.py#L309"><code>apply(ijkPoints)</code></a>. These examples should help with the details: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#How_to_run_segment_editor_effects_from_a_script</a></p>

---
