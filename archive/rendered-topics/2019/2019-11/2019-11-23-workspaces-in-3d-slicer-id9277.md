---
topic_id: 9277
title: "Workspaces In 3D Slicer"
date: 2019-11-23
url: https://discourse.slicer.org/t/9277
---

# Workspaces in 3D Slicer

**Topic ID**: 9277
**Date**: 2019-11-23
**URL**: https://discourse.slicer.org/t/workspaces-in-3d-slicer/9277

---

## Post #1 by @Umesh_Persad (2019-11-23 11:35 UTC)

<p>Are there any plans to implement the concept of workspaces in 3D Slicer so that the user can create a custom layout with modules and save that as a workspace? There could also be discipline specific workspaces e.g. Orthopaedics, Cardiology, Neuroscience etc.</p>

---

## Post #2 by @pieper (2019-11-23 14:40 UTC)

<p>Yes, but it requires some programming to really change the UI.</p>
<p><a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Slicelets</a></p>
<p>We tend to have extensions that provide domain-specific functionality and sometimes they change the UI (see SlicerHeart, SlicerCMF, SlicerMorph, SlicerDMRI, etc)</p>

---

## Post #3 by @lassoan (2019-11-23 15:00 UTC)

<p>Slicer GUI and behavior is so efficiently customizable using Python scripting (see examples that Steve listed above) that I’m not sure if any further infrastructure for supporting “workspaces” would be useful. Such an infrastructure would be a lot of work to develop and maintain and would be much more limited compared to what can be done today.</p>

---

## Post #4 by @Umesh_Persad (2019-11-23 21:44 UTC)

<p>I understand, thanks.</p>

---
