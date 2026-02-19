---
topic_id: 31304
title: "Is It Possible To Make Crosshair Node Invisible In Yellow Sl"
date: 2023-08-23
url: https://discourse.slicer.org/t/31304
---

# Is it possible to make crosshair node invisible in yellow slice view window?

**Topic ID**: 31304
**Date**: 2023-08-23
**URL**: https://discourse.slicer.org/t/is-it-possible-to-make-crosshair-node-invisible-in-yellow-slice-view-window/31304

---

## Post #1 by @icedream (2023-08-23 03:03 UTC)

<p>i have found some code to make node with display node to be invisible in yellow slice view window like the code below</p>
<pre><code class="lang-python">pointListNode = getNode("F")
pointListDisplayNode = pointListNode.GetDisplayNode()
pointListDisplayNode.SetVisibility(False) # Hide all points
pointListDisplayNode.SetVisibility(True) # Show all points
pointListDisplayNode.SetSelectedColor(1,1,0) # Set color to yellow
pointListDisplayNode.SetViewNodeIDs(["vtkMRMLSliceNodeRed", "vtkMRMLViewNode1"]) # Only show in red slice view and first 3D view
</code></pre>
<p>but crosshair node don’t have display node ,is it possible to make crosshair node invisible in yellow slice view window?</p>

---

## Post #2 by @jay1987 (2023-08-24 00:56 UTC)

<p>may be you need to hard code into C++ code?</p>

---

## Post #3 by @jcfr (2023-08-24 05:16 UTC)

<p>I would indeed expect the following code to work:</p>
<pre><code class="lang-python">for viewerName in ["Red", "Green", "Yellow"]:

    sliceNode = slicer.util.getNode(f"vtkMRMLSliceNode{viewerName}")
    sliceLogic = slicer.app.applicationLogic().GetSliceLogic(sliceNode)

    # The vtkMRMLSliceDisplayNode controls appearance of slice intersections
    # in slice views and slices in 3D views.
    sliceDisplayNode = sliceLogic.GetSliceDisplayNode()

    # Display slice intersection on all views expect the "Yellow" one
    sliceDisplayNode.SetViewNodeIDs(["vtkMRMLViewNode1", "vtkMRMLSliceNodeRed", "vtkMRMLSliceNodeGreen"])
</code></pre>
<p>After a cursory check, this feature is missing, it could be added to the following functions:</p>
<ul>
<li><code>vtkMRMLSliceIntersectionInteractionRepresentation::UpdateFromMRML()</code></li>
<li><code>vtkMRMLSliceIntersectionInteractionRepresentation2D::UpdateFromMRML()</code></li>
</ul>
<p>Is it something you could help with ?</p>

---

## Post #4 by @icedream (2023-08-24 11:37 UTC)

<p>thank you <a class="mention" href="/u/jcfr">@jcfr</a> ,these code may work for intersection line , do you know how to make crosshair node invisible in the Yellow Slice Window?</p>

---
