# Avoid recenter during vtkMRMLSliceLogic::FitSliceToAll

**Topic ID**: 20496
**Date**: 2021-11-05
**URL**: https://discourse.slicer.org/t/avoid-recenter-during-vtkmrmlslicelogic-fitslicetoall/20496

---

## Post #1 by @riep (2021-11-05 09:46 UTC)

<p>Hi all,<br>
I am wondering if I could do a modification of vtkMRMLSliceLogic::FitSliceToVolume to add a Boolean to avoid recenter and only adjust de FOV. Would it sounds good to you?<br>
The final objective is to have it exposed in vtkMRMLSliceLogic::FitSliceToAll<br>
Pierre</p>

---

## Post #2 by @riep (2021-11-05 12:42 UTC)

<p>I do not plan to change the current slicer behavior, so this option would be by default activated.</p>

---

## Post #3 by @jamesobutler (2021-11-05 14:03 UTC)

<p>Isn’t FitSliceToVolume inherently a centering action because it is attempting to fit the extent of the volume into the current slice view? Fitting both width and height to the view is like centering FOV.</p>
<p>Or are you just trying to select the volume as the background volume to show in the slice views?</p>

---

## Post #4 by @riep (2021-11-05 14:21 UTC)

<p>We could also see it as an adjustment of the FOV without changing the origins of the slices.<br>
<strong>example</strong>: part of your image is hidden because of a zoom in. Now you want to see the full image at the exact same slice offset (without changing the origins) for now it is not possible except by zooming out manually.</p>

---

## Post #5 by @lassoan (2021-11-08 02:50 UTC)

<p>I’ve felt the need for this feature a few times, too (center the view but not change the slice offset). It would be nice if you could implement this extra flag in vtkMRMLSlicerLogic. An extra flag in vtkMRMLSliceLogic::Fit* methods would be suitable. The implementation is not completely trivial, as you would need to intersect the bounding box with the transformed volume node. I’m not sure how (if) I would expose this feature on the GUI.</p>

---

## Post #6 by @riep (2021-11-08 11:28 UTC)

<p>thanks, Andreas &amp; James, I will work on it and keep you posted.</p>

---
