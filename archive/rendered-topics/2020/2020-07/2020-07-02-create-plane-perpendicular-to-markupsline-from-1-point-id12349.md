---
topic_id: 12349
title: "Create Plane Perpendicular To Markupsline From 1 Point"
date: 2020-07-02
url: https://discourse.slicer.org/t/12349
---

# Create plane perpendicular to MarkupsLine from 1º point

**Topic ID**: 12349
**Date**: 2020-07-02
**URL**: https://discourse.slicer.org/t/create-plane-perpendicular-to-markupsline-from-1-point/12349

---

## Post #1 by @apparrilla (2020-07-02 22:06 UTC)

<p>I have 2 points in a MarkupsLine and I want to align a model perpendicular to this line from 1º line point. i should like to have a slider to rotate model arround itself throw this custom axis and another slider to traslate model all over the line.<br>
Thanks on advance</p>

---

## Post #2 by @lassoan (2020-07-02 23:56 UTC)

<p>This <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rotate_a_node_around_a_specified_line">example in the script repository</a> shows how to create a transform that rotates any node around a markups line. With slight modifications you can make it do exactly what you need (e.g., position the object at the line endpoint, etc).</p>
<p>These <a href="https://www.slicer.org/wiki/Documentation/Nightly/Training#PerkLab.27s_Slicer_bootcamp_training_materials">programming tutorials</a> explain how to create a module with a GUI, such as node selectors for the line and model and a slider for controlling the rotation angle.</p>

---
