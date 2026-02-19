---
topic_id: 12783
title: "Zoom In Out Mouse Controls And Orientation Not Working In A"
date: 2020-07-30
url: https://discourse.slicer.org/t/12783
---

# Zoom in/out mouse controls and orientation not working in a a slice view outside the view layout

**Topic ID**: 12783
**Date**: 2020-07-30
**URL**: https://discourse.slicer.org/t/zoom-in-out-mouse-controls-and-orientation-not-working-in-a-a-slice-view-outside-the-view-layout/12783

---

## Post #1 by @apparrilla (2020-07-30 00:43 UTC)

<p>Hi everyone,</p>
<p>I follow the scrypt repository example for adding a slice view outside the view layout and it works straightforward but I have some trouble with volumes managing.<br>
1.- Mouse controls (zoom, move, scroll slices) don´t work<br>
2.- Orientation Presets ComboBox just show “Reformat”.<br>
3.- Volume ReSlice Driver Module let me change Orientation but it doesn´t update properly when I change “mode” or “rotation”, just when I change “driver”</p>
<p>Thanks on advance</p>

---

## Post #2 by @pieper (2020-07-30 12:15 UTC)

<p>Hi - Please provide a small reproducible example script.</p>

---

## Post #3 by @lassoan (2020-07-30 13:08 UTC)

<p>I was able to reproduce the problem using the example in the script repository.</p>
<p>The script has to be tuned a bit because initialization is slightly different since event handling is moved to widgets. I’ll post an update once I figured out what exactly need to be changed.</p>

---

## Post #4 by @lassoan (2020-07-30 14:52 UTC)

<p>I’ve updated the <a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Show_a_slice_view_outside_the_view_layout">example script</a> (slice logic had to be registered with the application), view interactions work now.</p>

---

## Post #5 by @apparrilla (2020-07-31 12:55 UTC)

<p>Thanks <a class="mention" href="/u/lassoan">@lassoan</a>, works like a charm.</p>

---
