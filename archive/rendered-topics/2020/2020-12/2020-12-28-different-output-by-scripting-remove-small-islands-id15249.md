# Different output by scripting 'REMOVE_SMALL_ISLANDS'

**Topic ID**: 15249
**Date**: 2020-12-28
**URL**: https://discourse.slicer.org/t/different-output-by-scripting-remove-small-islands/15249

---

## Post #1 by @ond12 (2020-12-28 14:33 UTC)

<p>Hello 3Dslicer forum</p>
<p>I made a small Python script to start the “Islands”  -&gt; “REMOVE_SMALL_ISLANDS” effect.</p>
<pre><code>self.segmentEditorWidget.setActiveEffectByName("Islands")
effect = self.segmentEditorWidget.activeEffect()
effect.setParameter("Operation","REMOVE_SMALL_ISLANDS")
effect.setParameter("MinimumSize", 1000)
effect.self().onApply()
</code></pre>
<p>with the a parameters “1000”</p>
<p>so i did the same with the SegmentEditor GUI with the “1000” voxels parameters<br>
but the segmentation output is not the same and i don’t find why</p>
<p>do you have an ideas ?</p>
<p>Thanks a lot</p>

---
