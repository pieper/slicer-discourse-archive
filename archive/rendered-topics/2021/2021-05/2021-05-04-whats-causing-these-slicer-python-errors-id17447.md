# What's Causing These Slicer / Python Errors

**Topic ID**: 17447
**Date**: 2021-05-04
**URL**: https://discourse.slicer.org/t/whats-causing-these-slicer-python-errors/17447

---

## Post #1 by @spycolyf (2021-05-04 16:08 UTC)

<p><a class="mention" href="/u/pieper">@pieper</a> <a class="mention" href="/u/lassoan">@lassoan</a> <a class="mention" href="/u/jcfr">@jcfr</a> <a class="mention" href="/u/jamesobutler">@jamesobutler</a></p>
<p>My module works perfectly except if I push the “Set Thickness” button first. Then hardly anything works. If I push other buttons first, everything works perfectly.  We beta test next Monday, so HELP!!!</p>
<p>This issue is listed in tracker here: <a>https://github.com/KitwareMedical/SlicerQReads/issues/103</a></p>
<p>Here’s the deal. After I push the “Set Threshold” button I get this error…</p>
<pre><code>Traceback (most recent call last):
  File "/home/jcfr/Projects/SlicerQReads-Release/Slicer-build/lib/SlicerQReads-4.13/qt-scripted-modules/QReads.py", line 389, in updateGUIFromParameterNode
    QReadsLogic.slabThicknessInMmToNumberOfSlices(volumeNode, slabThicknessInMm))
  File "/home/jcfr/Projects/SlicerQReads-Release/Slicer-build/lib/SlicerQReads-4.13/qt-scripted-modules/QReads.py", line 612, in slabThicknessInMmToNumberOfSlices
    assert tichknessInMm &gt; 0
AssertionError
</code></pre>
<p>Here’s the code segments at 389 and 612</p>
<blockquote>
<pre><code> def updateGUIFromParameterNode(self, caller=None, event=None):
      QReadsLogic.setSlab(       (line 389)
          QReadsLogic.slabModeFromString(slabModeStr),
          QReadsLogic.slabThicknessInMmToNumberOfSlices(volumeNode, slabThicknessInMm))
</code></pre>
</blockquote>
<pre><code>@staticmethod
  def slabThicknessInMmToNumberOfSlices(volumeNode, tichknessInMm):
     if volumeNode is None:
      return 1
    assert tichknessInMm &gt; 0  (line 612)
    return int(tichknessInMm / max(volumeNode.GetSpacing()))
</code></pre>
<p>… and no jokes anout</p>

---

## Post #2 by @jcfr (2021-05-04 16:55 UTC)

<p>3 posts were merged into an existing topic: <a href="/t/slicerqr-development/15954">SlicerQR Development</a></p>

---

## Post #3 by @jcfr (2021-05-04 16:55 UTC)



---
