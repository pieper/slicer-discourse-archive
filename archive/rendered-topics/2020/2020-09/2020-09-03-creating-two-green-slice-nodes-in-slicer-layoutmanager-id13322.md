---
topic_id: 13322
title: "Creating Two Green Slice Nodes In Slicer Layoutmanager"
date: 2020-09-03
url: https://discourse.slicer.org/t/13322
---

# Creating two green slice nodes in slicer layoutmanager

**Topic ID**: 13322
**Date**: 2020-09-03
**URL**: https://discourse.slicer.org/t/creating-two-green-slice-nodes-in-slicer-layoutmanager/13322

---

## Post #1 by @Chintha_Siva_Prasad (2020-09-03 14:25 UTC)

<p>how can I insert two green slice nodes in a slicer layout manager?</p>

---

## Post #2 by @lassoan (2020-09-03 14:44 UTC)

<p>By “green” do you mean you want the view to be called green, color the border green, or use the coronal default orientation?</p>
<p>You can change the color of slice nodes to green for multiple views.</p>
<p>Slice names and labels are unique, so you can only have one of them be “G” / “Green”.</p>
<p>If you mean that you want to show multiple coronal views, then set its orientation by calling <code>sliceNode.SetOrientation</code> (see <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Change_default_slice_view_orientation">example</a>). You can set default orientation in the <code>orientation</code> property of your layout (see example of how to create custom layout <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_viewer_layout">here</a>).</p>

---

## Post #3 by @Chintha_Siva_Prasad (2020-09-04 06:26 UTC)

<p>Actually I want 4 slice nodes.A set of (green, red, yellow) slice nodes and a seperate slice node.Because I had already used the three nodes earlier, how can I create a new sliceNode.</p>

---

## Post #4 by @lassoan (2020-09-05 21:47 UTC)

<p>You can create your custom layout, with as many viewers you need, using any default orientations. See example in script repository: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_viewer_layout">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Customize_viewer_layout</a></p>

---
