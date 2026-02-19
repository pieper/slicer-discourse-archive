---
topic_id: 37769
title: "Lighting In 3D Stereoscopic View"
date: 2024-08-08
url: https://discourse.slicer.org/t/37769
---

# Lighting in 3D stereoscopic view

**Topic ID**: 37769
**Date**: 2024-08-08
**URL**: https://discourse.slicer.org/t/lighting-in-3d-stereoscopic-view/37769

---

## Post #1 by @Laura_A (2024-08-08 09:37 UTC)

<p>I am trying to apply the lighting of the 3D view a the left and right eye 3D stereoscopic views, but the lighting is only applied to the view in the 3D Slicer UI.</p>
<p>Steps I follow:</p>
<ol>
<li>Load a model in 3D Slicer</li>
<li>Create 3D stereoscopic view (<a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html" class="inline-onebox" rel="noopener nofollow ugc">Script repository — 3D Slicer documentation</a>, “Show a 3D view outside the view layout” and <code>SetStereoType</code>) for both right and left eye</li>
<li>Open “Lights” module and apply e.g. Sunset lighting to All views (also individually)</li>
</ol>
<p>Only the lighting is applied to the view from the UI, but not in the pop-up left and right views.</p>
<p>How can apply the lighting to all the views?</p>

---

## Post #2 by @pieper (2024-08-08 12:46 UTC)

<p>I’m sure the Lights module could be improved to support multiple views with just a bit of programming.  You could look at the code and probably figure it out.</p>

---
