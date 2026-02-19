---
topic_id: 24424
title: "Nthmarkup Changed Into Nthcontrolpoint"
date: 2022-07-20
url: https://discourse.slicer.org/t/24424
---

# NthMarkup changed into NthControlPoint?

**Topic ID**: 24424
**Date**: 2022-07-20
**URL**: https://discourse.slicer.org/t/nthmarkup-changed-into-nthcontrolpoint/24424

---

## Post #1 by @mosenco (2022-07-20 22:06 UTC)

<p>As someone suggested me, i read the documentation about the Migration to Slicer 5.0<br>
I have this method called <code>SetNthMarkupDescription()</code> but i found no clue into the guide except for this line:<br>
<strong>vtkMRMLMarkupsNode::GetNthMarkupSelected() is replaced by GetNthControlPointSelected()</strong></p>
<p>It’s not SetNth and i’ve check if ControlPoint existed in the Slicer 4, but no. There is no method with ControlPoint in it.</p>
<p>I made a guess and i noticed that exist in Slicer 5.0 a method called SetNthControlPointDescription.</p>
<p>So i changed <code>SetNthMarkuptDescription</code> into <code>SetNthControlPointDescription</code>. Can someone confirm that i did right?</p>

---

## Post #2 by @lassoan (2022-07-20 22:07 UTC)

<p>Yes, all <code>Get/SetNthMarkup...</code> methods have been renamed to <code>Get/SetNthControlPoint...</code>.</p>

---
