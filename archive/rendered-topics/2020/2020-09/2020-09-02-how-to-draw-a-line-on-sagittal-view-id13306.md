---
topic_id: 13306
title: "How To Draw A Line On Sagittal View"
date: 2020-09-02
url: https://discourse.slicer.org/t/13306
---

# How to draw a line on sagittal view

**Topic ID**: 13306
**Date**: 2020-09-02
**URL**: https://discourse.slicer.org/t/how-to-draw-a-line-on-sagittal-view/13306

---

## Post #1 by @DavidCai1246 (2020-09-02 20:54 UTC)

<p>For the application I am working on, I would like to draw horizontal lines in the sagittal view to mark specific slices that I am interested in. Is there code that can help me achieve this?</p>
<p>I know that in the Markups module I can use a button to draw a markup line, I would like something similar to that.</p>
<p>Thanks in advance!</p>

---

## Post #2 by @lassoan (2020-09-02 21:09 UTC)

<p>Markup lines or planes should work well for this. You can place them easily from Python script: add a markups line/plane node to the scene and set control point positions.</p>

---

## Post #3 by @DavidCai1246 (2020-09-02 21:25 UTC)

<p>For the python script do you mean:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rotate_a_node_around_a_specified_line" class="onebox" target="_blank" rel="nofollow noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Rotate_a_node_around_a_specified_line</a></p>

---

## Post #4 by @lassoan (2020-09-02 22:57 UTC)

<p>There are several relevant examples, see here: <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Markups">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Markups</a></p>

---

## Post #5 by @DavidCai1246 (2020-09-02 23:03 UTC)

<p>thank you very much!</p>

---
