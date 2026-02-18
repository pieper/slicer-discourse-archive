# Modify segment directly using Python

**Topic ID**: 7856
**Date**: 2019-08-03
**URL**: https://discourse.slicer.org/t/modify-segment-directly-using-python/7856

---

## Post #1 by @hherhold (2019-08-03 00:49 UTC)

<p>I’ve seen a lot of python scripts that use existing segment editor effects, but is there a way to directly access segment data and volume data from python to implement prototype segmentation algorithms? Or is that something that’s better done via C++?</p>
<p>I’m positive there are probably pointers to how to do this in the docs…</p>
<p>Thanks!</p>
<p>-Hollister</p>

---

## Post #2 by @lassoan (2019-08-03 02:17 UTC)

<p>Contribution of new Segment Editor effects would be very welcome! You can implement Segment Editor effects either in C++ or Python. There is a template for Python-scripted segment editor effect in the Extension wizard and you can use all the current Segment Editor effects as examples of how to implement your own effect - see in <a href="https://github.com/Slicer/Slicer/tree/master/Modules/Loadable/Segmentations/EditorEffects" rel="nofollow noopener">Slicer core</a> and in <a href="https://github.com/lassoan/SlicerSegmentEditorExtraEffects" rel="nofollow noopener">SegmentEditorExtraEffects extension</a>.</p>

---
