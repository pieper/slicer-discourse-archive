---
topic_id: 8785
title: "Change Active Markup List Open Curve From Another Module And"
date: 2019-10-15
url: https://discourse.slicer.org/t/8785
---

# Change active markup list (open curve) from another module, and control-click to add new points

**Topic ID**: 8785
**Date**: 2019-10-15
**URL**: https://discourse.slicer.org/t/change-active-markup-list-open-curve-from-another-module-and-control-click-to-add-new-points/8785

---

## Post #1 by @mikebind (2019-10-15 21:37 UTC)

<p>Hello, I have several objects whose visualizations in Slicer are represented by the new Open Curve markups.  From my module, I would like to be able to select which Open Curve is currently active and click to add new points to that currently active curve by clicking on the slice views (or 3D view).  I can currently achieve this in a roundabout way by switching to the Markups module, selecting the curve node in the List selector at the top, then clicking the “Create and Place Open Curve” button along the top.  I want to be able achieve this without changing away from my module.   I found <code>slicer.modules.markups.logic().SetActiveListID()</code>, but I haven’t been able to make this work.  The corresponding <code>GetActiveListID()</code> function returns a MRML id string like ‘vtkMRMLMarkupsCurveNode24’ but supplying a string like that to <code>SetActiveListID</code> in the python interactor fails with error<br>
<code>Traceback (most recent call last):</code><br>
<code>  File "&lt;console&gt;", line 1, in &lt;module&gt;</code><br>
<code>TypeError: SetActiveListID argument 1: method requires a VTK object</code></p>
<p>Supplying a curve node as the argument does not throw an error, but also doesn’t seem to change the active list.</p>
<p>----- EDIT BELOW—</p>
<p>OK, I just discovered that actually supplying a curve node DOES seem to change the active list, but the change is not reflected in the GUI view. I suspect I need a call to something like updateGuiFromMRML() somewhere, but I can’t find how to do that call. I’ll keep looking, but if someone knows how to do that, I would be appreciative.</p>

---

## Post #3 by @lassoan (2019-10-17 04:56 UTC)

<p>These examples probably do what you need: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Switching_to_markup_fiducial_placement_mode" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Switching_to_markup_fiducial_placement_mode</a></p>

---

## Post #4 by @mikebind (2019-10-20 03:45 UTC)

<p>Thank you.  These are helpful references.  I am still not sure why the Markups module GUI view is not updated when I set the active list ID, but it’s not actually very important for my purposes, so I am no longer pursuing it.  I appreciate the help, thanks!</p>

---
