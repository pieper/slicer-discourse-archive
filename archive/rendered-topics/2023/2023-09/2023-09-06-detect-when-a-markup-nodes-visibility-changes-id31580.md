---
topic_id: 31580
title: "Detect When A Markup Nodes Visibility Changes"
date: 2023-09-06
url: https://discourse.slicer.org/t/31580
---

# Detect when a markup node's visibility changes

**Topic ID**: 31580
**Date**: 2023-09-06
**URL**: https://discourse.slicer.org/t/detect-when-a-markup-nodes-visibility-changes/31580

---

## Post #1 by @bruce (2023-09-06 01:23 UTC)

<p>I have a Python loadable scriptable module that creates a custom workflow. The module contains tables of nodes (such as MarkupsROINodes and MarkupsLineNodes) and provides a checkbox for the user to change their visibiliity.</p>
<p>I am observing these nodes using node.AddObserver(vtk.vtkCommand.ModifiedEvent, myCallback) to detect if they have been deleted so they can be removed them from the module’s table. How do I observe their visibility status (in case it has been changed through another menu)? I tried node.AddObserver(vtk.vtkMRMLDisplayableNode.DisplayModifiedEvent, myCallback) but this didn’t seem to pick up any events.</p>

---

## Post #2 by @pieper (2023-09-06 19:01 UTC)

<p>Visibility is stored in the display node, so you need to add the observer to that node, not the markup node.</p>

---

## Post #3 by @bruce (2023-09-06 21:14 UTC)

<p>Thanks, that worked well.</p>
<blockquote>
<pre><code>    node.GetDisplayNode().AddObserver(vtk.vtkCommand.ModifiedEvent, myCallback)
</code></pre>
</blockquote>

---

## Post #4 by @cpinter (2023-09-07 11:15 UTC)

<p>Or<br>
<code>node.AddObserver(slicer.vtkMRMLDisplayableNode.DisplayModifiedEvent, myCallback)</code></p>

---
