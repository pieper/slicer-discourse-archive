---
topic_id: 9493
title: "Interactor From Old Version To 4 10 2"
date: 2019-12-14
url: https://discourse.slicer.org/t/9493
---

# Interactor from old version to 4.10.2

**Topic ID**: 9493
**Date**: 2019-12-14
**URL**: https://discourse.slicer.org/t/interactor-from-old-version-to-4-10-2/9493

---

## Post #1 by @fraca (2019-12-14 01:34 UTC)

<p>Hi, i’m try to convert this code that was build for 3DSlicer 3.6 to the newest 3DSlicer 4.10.2, but i have some issues to define the interactor.<br>
Can you help me?</p>
<blockquote>
<p>self.RedSliceInteractor=slicer.ApplicationGUI.GetMainSliceGUI(“Red”).GetSliceViewer().GetRenderWidget().GetRenderWindowInteractor()<br>
self.RedSliceLeftButtonReleaseTag=self.RedSliceInteractor.AddObserver(“LeftButtonReleaseEvent”,self.HandleClickInRedSlice)</p>
</blockquote>
<p>This is a part of the function that needs the interactor:</p>
<blockquote>
<p>def HandleClickInRedSlice(self):<br>
if not self.Selecting:<br>
return<br>
coordinates = self.RedSliceInteractor.GetLastEventPosition()<br>
ctrlKey = self.RedSliceInteractor.GetControlKey()</p>
</blockquote>
<p>I’m trying to observe the mouse left-click on the Red Slice of 3DSlicer, and i have also to check if Ctrl-key is pressed and to take the coordinates on the image of the point pressed</p>

---

## Post #2 by @fraca (2019-12-14 01:34 UTC)

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

## Post #3 by @lassoan (2019-12-15 06:08 UTC)

<p>Interactors are hard. I would not recommend to implement features at such low level but instead utilize Markups widgets to define point positions, lines, curves, etc. See examples in script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer</a></p>

---

## Post #4 by @fraca (2019-12-17 11:46 UTC)

<p>Thanks for your suggestion. There’s a way to run a function when i create only one markup node with mouse-click? I tried to do something with <code>AddObserver</code>, but i found some issues.</p>

---

## Post #5 by @lassoan (2019-12-17 13:07 UTC)

<p>See working examples in the script repository, for example: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Manipulating_objects_in_the_slice_viewer</a></p>

---
