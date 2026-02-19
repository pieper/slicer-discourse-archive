---
topic_id: 22754
title: "Using Json Files To Create Markups"
date: 2022-03-29
url: https://discourse.slicer.org/t/22754
---

# Using json files to create markups

**Topic ID**: 22754
**Date**: 2022-03-29
**URL**: https://discourse.slicer.org/t/using-json-files-to-create-markups/22754

---

## Post #1 by @Tulika_Nandi (2022-03-29 17:59 UTC)

<p>Hi, I’m trying to create a line markup by loading a json file. I am able to see the line in the 3D view but not in the slice views despite trying our various display and visibility options. Could you share an example json file for a line that works? Similar to the example for fiducials provided here - <a href="https://slicer.readthedocs.io/en/v4.11/user_guide/modules/markups.html" class="inline-onebox" rel="noopener nofollow ugc">Markups — 3D Slicer documentation</a>.</p>
<p>Also, for the schema, I am not able to use v1.0.3 - could you provide a correct link to use for this?</p>
<p>Tulika</p>

---

## Post #2 by @lassoan (2022-03-31 16:19 UTC)

<p>In recent Slicer versions we added <code>positionStatus</code> field, which seems to be initialized to <code>undefined</code> by default. I’ll change that to be set to <code>defined</code> by default when <code>position</code> is specified. The new behavior will be available in tomorrow’s Slicer Preview Release.</p>
<p>As a workaround, you can specify <code>"positionStatus": "defined"</code> for each control point.</p>

---

## Post #3 by @Tulika_Nandi (2022-04-01 15:08 UTC)

<p>That works - thank you!</p>

---

## Post #4 by @Tulika_Nandi (2022-04-01 15:31 UTC)

<p>One more question - when creating fiducials using a json file, is there a way to change the color of each fiducial individually?</p>

---

## Post #5 by @jamesobutler (2022-04-01 15:38 UTC)

<p>Control points in a Markups Point List can have unique label names for each control point, but the entire list has a single display which includes color. Therefore all control points in a single Point List must have the same color, but different Point Lists can have their own color.</p>

---

## Post #6 by @lassoan (2022-04-02 01:11 UTC)

<p>In one point list you can use two colors - selected and unselected.</p>
<p>In recent Slicer versions you can add any amount of additional metadata for each control point. That can be used for coloring curves, but not yet for coloring the control points. This control point coloring would not be hard to implement, but right now I don’t know about any project that will need this in the near future.</p>
<p>If you need this feature and you are somewhat familiar with C++ then you can help with the implementation. Alternatively, you can generate a colored model using vtkGlyph3D filter using a short (about 10-20 lines) Python script.</p>

---

## Post #7 by @Tulika_Nandi (2022-04-04 08:22 UTC)

<p>Thank you for the suggestions! Sorry I don’t have experience with C++ so can’t help with that. It’s not crucial for me at the moment - the workaround of using separate point lists should be enough for now.</p>

---
