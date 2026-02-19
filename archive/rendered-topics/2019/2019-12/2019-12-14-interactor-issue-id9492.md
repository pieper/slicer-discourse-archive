---
topic_id: 9492
title: "Interactor Issue"
date: 2019-12-14
url: https://discourse.slicer.org/t/9492
---

# Interactor issue

**Topic ID**: 9492
**Date**: 2019-12-14
**URL**: https://discourse.slicer.org/t/interactor-issue/9492

---

## Post #1 by @fraca (2019-12-14 01:34 UTC)

<p>Hi, i’m trying to update this code (build for 3DSlicer 3.6) for 3DSlicer 4.10.2 but i have some issues with the interactor. I want to observe the “LeftButtonReleaseEvent” when i press only on the Red Slice Viewer (in 3DSlicer).</p>
<blockquote>
<p>self.RedSliceInteractor=slicer.ApplicationGUI.GetMainSliceGUI(“Red”).GetSliceViewer().GetRenderWidget().GetRenderWindowInteractor() self.RedSliceLeftButtonReleaseTag=self.RedSliceInteractor.AddObserver(“LeftButtonReleaseEvent”,self.HandleClickInRedSlice)</p>
</blockquote>
<p>This is the first part of the function that i call above:</p>
<blockquote>
<p>def HandleClickInRedSlice(self):<br>
if not self.Selecting:<br>
return<br>
coordinates = self.RedSliceInteractor.GetLastEventPosition()<br>
ctrlKey = self.RedSliceInteractor.GetControlKey()</p>
</blockquote>
<p>So i want to obatin also the coordinates of the point where i clicked and i i pressed the Ctrl key.<br>
Can you help me?</p>

---

## Post #2 by @lassoan (2019-12-15 06:05 UTC)

<p>A post was merged into an existing topic: <a href="/t/interactor-from-old-version-to-4-10-2/9493">Interactor from old version to 4.10.2</a></p>

---

## Post #3 by @lassoan (2019-12-15 06:05 UTC)



---
