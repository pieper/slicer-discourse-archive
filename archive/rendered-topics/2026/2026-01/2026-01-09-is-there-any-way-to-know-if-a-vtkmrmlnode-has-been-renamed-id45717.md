---
topic_id: 45717
title: "Is There Any Way To Know If A Vtkmrmlnode Has Been Renamed"
date: 2026-01-09
url: https://discourse.slicer.org/t/45717
---

# Is there any way to know if a vtkMRMLNode has been renamed?

**Topic ID**: 45717
**Date**: 2026-01-09
**URL**: https://discourse.slicer.org/t/is-there-any-way-to-know-if-a-vtkmrmlnode-has-been-renamed/45717

---

## Post #1 by @Suhaim (2026-01-09 10:34 UTC)

<p>Hi all,<br>
If you create a markup node(vtkMRMLMarkupsNode) and add control points to it, the control points are named using a default format(“%N-%d”) with respect to the current name of the markup node.</p>
<p>Renaming a markup node doesn’t modify the names of the existing control points of the respective markup. If there was any event in <a href="https://apidocs.slicer.org/main/classvtkMRMLMarkupsNode.html#a3b63d658dab9d501e4104fb6e3da24b0" rel="noopener nofollow ugc">vtkMRMLMarkupsNode</a> or its parents that fires when the node is renamed, I could react to it and update the labels.</p>
<p>I was able to achieve what I wanted using <strong><a href="https://vtk.org/doc/nightly/html/classvtkCommand.html#a59a8690330ebcb1af6b66b0f3121f8fea534a769a2e6b5cc199c2b40a78665896" rel="noopener nofollow ugc">vtkCommand::ModifiedEvent;</a></strong> however, this event also fires for several other cases. I just wanted to ask if there was an event I missed, so that my function is not called for every vtkCommand::ModifiedEvent and is more optimized.</p>
<p>Thanks!</p>

---

## Post #2 by @ebrahim (2026-01-09 13:33 UTC)

<p>I don’t see a name change event <a href="https://github.com/Slicer/Slicer/blob/963ef4e4c0bb277a33f6b0c610f5e481521ca9ec/Libs/MRML/Core/vtkMRMLMarkupsNode.h#L234">here</a> or elsewhere so I think I agree with the way you approached it.</p>

---

## Post #3 by @lassoan (2026-01-10 17:58 UTC)

<p>What would you like to achieve? Rename all the other control points if the user renames one control point (e.g., user specifies for one vertebra that it is T5 and you want to update the labels for all the others accordingly)?</p>

---

## Post #4 by @Suhaim (2026-01-12 04:14 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, what I wanted to achieve was :-</p>
<ol>
<li>Let’s say a line markup node name “L_1” has been created and two control points were added to it.</li>
<li>Programatically I rename these two control points as L_1-entry, L_1-target respectively when they get defined.</li>
<li>If the user renames the line as “L_2”, I want the control point’s names to change to L_2-entry and L_2-target.</li>
</ol>

---

## Post #5 by @lassoan (2026-01-12 17:31 UTC)

<p>Thanks for the additional information. There is no separate event for node rename, but you can easily fulfill your needs without it.</p>
<p>A simple option is to do a delayed update whenever a node is changed: add an observer to the <code>Modified</code> event of all the markup nodes you are interested and connect that to reset of a single-shot QTimer with a short timeout (500ms whenever). In the timer callback check if the markup control point names are up-to-date and update them if needed.</p>
<p>You can avoid this if you capture the node rename event in the GUI. For example, the <a href="https://apidocs.slicer.org/main/classqMRMLNodeComboBox.html">qMRMLNodeComboBox</a> widget emits a signal if the user rename the current node. You also get notified about a node rename if you add a dedicated button for it in your module GUI.</p>
<p>It would not be hard to implement auto-rename of control points that were named using the “default name format” whenever a node name changes; or add a node renamed event to vtkMRMLNode, but the need just has not come up frequently enough and there are alternative solutions.</p>

---

## Post #6 by @Suhaim (2026-01-13 03:55 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a> for the detailed explanation and the alternatives suggested, this helps a lot!</p>

---
