# Place Fiducial Marker with EndPlacementEvent observer

**Topic ID**: 27797
**Date**: 2023-02-13
**URL**: https://discourse.slicer.org/t/place-fiducial-marker-with-endplacementevent-observer/27797

---

## Post #1 by @kleingeo (2023-02-13 19:47 UTC)

<p>I am trying to execute a function after a fiducial marker is placed. I was trying to implement it with this:</p>
<pre><code class="lang-python">def onMarkupEndInteraction(caller, event):
    # Do stuff
    pass

interactionNode = slicer.app.applicationLogic().GetInteractionNode()
selectionNode = slicer.app.applicationLogic().GetSelectionNode()
selectionNode.SetReferenceActivePlaceNodeClassName("vtkMRMLMarkupsFiducialNode")
pointListNode = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLMarkupsFiducialNode")

pointListNode.AddObserver(interactionNode.EndPlacementEvent, onMarkupEndInteraction)
selectionNode.SetActivePlaceNodeID(pointListNode.GetID())
interactionNode.SetCurrentInteractionMode(1)
</code></pre>
<p>however, it seems to be executing <code>onMarkupEndInteration</code> before the fiducial marker is placed. I have been trying many different methods (as there are many different ways to initialize and place fiducial markers), but none seem to properly execute the <code>observer</code> for the fiducial marker.</p>

---

## Post #2 by @lassoan (2023-02-15 05:39 UTC)

<p>You can observe events of the markups node, such as <a href="https://apidocs.slicer.org/master/classvtkMRMLMarkupsNode.html#aceeef8806df28e3807988c38510e56caaf1067cd7bcb1bd0992112b22daf219d5">slicer.vtkMRMLMarkupsNode.PointPositionDefinedEvent</a>.</p>

---
