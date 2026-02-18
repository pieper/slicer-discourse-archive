# Trying to make a STL from a NRRD

**Topic ID**: 7615
**Date**: 2019-07-16
**URL**: https://discourse.slicer.org/t/trying-to-make-a-stl-from-a-nrrd/7615

---

## Post #1 by @harsh (2019-07-16 16:17 UTC)

<p>I Imported a nrrd file and then used Segment Editor module to create a segment with the appropriate threseholds that I was looking for, upon this I recieve the error Traceback (most recent call last):<br>
File “C:\Program Files\Slicer 4.10.2\lib\Slicer-4.10\qt-scripted-modules\SegmentEditorEffects\SegmentEditorEffects\SegmentEditorThresholdEffect.py”, line 349, in onApply<br>
modifierLabelmap = self.scriptedEffect.defaultModifierLabelmap()<br>
MemoryError: std::bad_alloc: bad allocation</p>

---

## Post #2 by @lassoan (2019-07-16 16:23 UTC)

<p>You have run out of memory. Crop the master volume using Crop volume module to the relevant region, maybe also increase the voxel size if needed and/or increase virtual memory size on your computer.</p>

---

## Post #3 by @muratmaga (2019-07-16 16:31 UTC)

<p>Your computer ran out of memory during the task. How big is your dataset, and how much RAM do you have on it?</p>
<p>Typical suggestion for RAM is 6-10X of your dataset.</p>
<p>Mail](<a href="https://go.microsoft.com/fwlink/?LinkId=550986" rel="nofollow noopener">https://go.microsoft.com/fwlink/?LinkId=550986</a>) for Windows 10</p>

---

## Post #4 by @harsh (2019-07-16 21:44 UTC)

<p>data set is around 10gb file, my computer has 32gb ram and a 1060gtx</p>

---

## Post #5 by @muratmaga (2019-07-17 08:54 UTC)

<p>Yep, you need more memory. Follow <a class="mention" href="/u/lassoan">@lassoan</a> suggestions.</p>

---
