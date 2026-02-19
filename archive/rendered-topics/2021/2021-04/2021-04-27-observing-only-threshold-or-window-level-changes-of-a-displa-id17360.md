---
topic_id: 17360
title: "Observing Only Threshold Or Window Level Changes Of A Displa"
date: 2021-04-27
url: https://discourse.slicer.org/t/17360
---

# Observing Only Threshold or Window/Level changes of a display node

**Topic ID**: 17360
**Date**: 2021-04-27
**URL**: https://discourse.slicer.org/t/observing-only-threshold-or-window-level-changes-of-a-display-node/17360

---

## Post #1 by @nathanbmnt (2021-04-27 18:59 UTC)

<p>Hello,<br>
I have a module where I want to do calculations every time a volume node’s window/level or threshold are changed. Right now my observation is just of the modified event of the display node which is very general:</p>
<p><code>volume.GetDisplayNode().AddObserver(vtk.vtkCommand.ModifiedEvent, self.onVolumeDisplayNodeModified)</code></p>
<p>Is there a way to only observe W/L or threshold changes?</p>

---

## Post #2 by @pieper (2021-04-27 19:00 UTC)

<p>You can check the source code, but no, I don’t think there’s a custom event for that.  We’d probably accept a PR to add that.</p>

---
