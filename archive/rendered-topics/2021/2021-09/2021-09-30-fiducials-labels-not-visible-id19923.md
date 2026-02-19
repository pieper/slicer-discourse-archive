---
topic_id: 19923
title: "Fiducials Labels Not Visible"
date: 2021-09-30
url: https://discourse.slicer.org/t/19923
---

# Fiducials labels not visible

**Topic ID**: 19923
**Date**: 2021-09-30
**URL**: https://discourse.slicer.org/t/fiducials-labels-not-visible/19923

---

## Post #1 by @Chintha_Siva_Prasad (2021-09-30 06:54 UTC)

<p>I had compiled slicer, but the labels of fiducials are not showing…</p>

---

## Post #2 by @cpinter (2021-09-30 08:50 UTC)

<p>This is very little information. What platform? Slicer revision? Build sucessful? What do you do exactly to show fiducials, what do you expect, and what happens instead?</p>

---

## Post #3 by @Chintha_Siva_Prasad (2021-09-30 08:55 UTC)

<p>On linux(ubuntu 20.04). Built successfully. When I am placing fiducials both through UI and script, I am not to see the labels of the fiducials. I am just getting the fiducial dot(not the name).<br>
And also while compilation I replaced the placement fiducial icon with custom one.</p>

---

## Post #4 by @lassoan (2021-09-30 13:33 UTC)

<p>Showing/hiding point labels is a flag in the display node. You also need to make sure the label size is not 0.</p>
<p>By default the point labels are displayed for fiducials, but maybe you loaded an old scene or saved a default label size = 0 in your application settings.</p>

---
