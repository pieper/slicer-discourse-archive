# Update slice view positions and orientations using MarkupsFiducialNode interactions

**Topic ID**: 26651
**Date**: 2022-12-08
**URL**: https://discourse.slicer.org/t/update-slice-view-positions-and-orientations-using-markupsfiducialnode-interactions/26651

---

## Post #1 by @LaurennLam (2022-12-08 15:44 UTC)

<p>Hi every one,<br>
I add an interactive vtkMRMLMarkupsFiducialNode with a single point which allows me to update my 2D views orientations and positions.<br>
But here’s the thing, if I call <code>SetNthControlPointPosition</code>, then when I try to move it on the 3D view, then it only moves along Axial axis. I can’t translate it on other direction.<br>
Does anyone has any clue about this ?<br>
Thanks a lot.</p>

---

## Post #2 by @lassoan (2022-12-08 21:11 UTC)

<p>Depending on “Placement mode” setting (in Markups module / Display / Advanced / 3D Dsiplay) in 3D views markups either move in the camera plane or it snaps to the surface visible at the mouse pointer position. Do you experience a different behavior?</p>

---

## Post #3 by @LaurennLam (2022-12-09 09:15 UTC)

<p>Hi Andras,<br>
I tried to move from  ‘snap to visible surface’ and ‘unconstrained’ but I have the same.<br>
I forgot to mention that I did that in a custom python module.<br>
Here is the main goal. I want to update the red slice according to the markups position, but I also want to update the markups position if I move the 2D slices. So I first create the markups</p>
<pre><code class="lang-auto">orientationMarkupsNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")
orientationMarkupsNode.CreateDefaultDisplayNodes()
orientationMarkupsNode.SetUndoEnabled(True)
orientationMarkupsNode.GetDisplayNode().SetUndoEnabled(True)
orientationMarkupsNode.GetDisplayNode().SetHandlesInteractive(True)
orientationMarkupsNode.GetDisplayNode().SetInteractionHandleScale(HandleMarkerScale)
orientationMarkupsNode.GetDisplayNode().SetOpacity(0)
orientationMarkupsNode.AddObserver(slicer.vtkMRMLMarkupsNode.PointModifiedEvent,
                                 self._onPlaneMarkupChanged)

def _onPlaneMarkupChanged(self):
  # Update the red slice position
</code></pre>
<p>I also observe the 2D slices modified event</p>
<pre><code class="lang-auto">slicer.util.getNode("vtkMRMLSliceNodeRed").AddObserver(vtk.vtkCommand.ModifiedEvent, self._updateMarkupPosition)

def _updateMarkupPosition(self):
  # Update the markups position by setting it the correct position
  orientationMarkupsNode.SetNthControlPointPosition(0, correct_position)
</code></pre>
<p>If I call the <code>SetNthControlPointPosition</code> then my markup is blocked along the Z axis. But if I don’t call it, it works well except I cannot update it when I move 2D slices.</p>
<p>To be honest, I’m surprised that it doesn’t make a loop because as I understand, the <code>SetNthControlPointPosition</code> called <code>PointModifiedEvent</code> but maybe it’s an other issue…</p>
<p>Is it clearer <a class="mention" href="/u/lassoan">@lassoan</a> ?</p>

---

## Post #4 by @lassoan (2022-12-09 17:16 UTC)

<p>If you move the slice views wherever the markup point is then it is important to exclude the view that you are interacting with. You can use the <code>'Markups.MovingInSliceView</code> attribute of the markup node, which is set during moving a control point. See for example how it is done in <a href="https://github.com/SlicerHeart/SlicerHeart/blob/764184d5e4de1c0c0d60bf502e03da54b50a69f1/ValveAnnulusAnalysis/ValveAnnulusAnalysis.py#L753">SlicerHeart</a>.</p>

---

## Post #5 by @LaurennLam (2022-12-13 12:31 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a> ,<br>
Thanks for your answer. Finally, it seems that there was an error with the code which computes the intersection point between my three slices, and that’s why the markup was trapped in the Z axis…<br>
FYI, I took this code here <a href="https://github.com/SlicerHeart/SlicerHeart/blob/master/ValveView/ValveView.py#L213" class="inline-onebox" rel="noopener nofollow ugc">SlicerHeart/ValveView.py at master · SlicerHeart/SlicerHeart · GitHub</a><br>
It seems that the extracted normal aren’t correct.</p>

---

## Post #6 by @lassoan (2022-12-13 12:53 UTC)

<p>Since the slice rotation feature is now built into Slicer core and for defining the annulus curve we use a more comprehensive module, we don’t use this module or fix errors that occur for special cases.</p>
<p>We made the more robust (see <a href="https://github.com/Slicer/Slicer/blob/b29ab1d8053427eab77a80d1e4b074daa909cc38/Libs/MRML/DisplayableManager/vtkMRMLSliceIntersectionRepresentation2D.cxx#L584">here</a>) by making sure that only currently visible slices in the same view group are taken into account and slices that are nearly parallel are excluded from the computation (as the intersection line can be computed mathematically for nearly-parallel planes but the result is a random line position/orientation).</p>

---
