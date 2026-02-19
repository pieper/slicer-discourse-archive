---
topic_id: 24879
title: "Markups Distorted When Zoom Isnt Constant Along Different Ax"
date: 2022-08-23
url: https://discourse.slicer.org/t/24879
---

# Markups distorted when zoom isn't constant along different axes

**Topic ID**: 24879
**Date**: 2022-08-23
**URL**: https://discourse.slicer.org/t/markups-distorted-when-zoom-isnt-constant-along-different-axes/24879

---

## Post #1 by @keri (2022-08-23 08:24 UTC)

<p>Hi,</p>
<p>It is probably predictable that markups may work incorrectly with 3D view where zoom along different axes is different (in the animation Z-axis zoomed 8 times).<br>
Does somebody know where to find methods that are responsible for this?<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/8/9/8941fb3e9fdc893585ee2a5fc9956fc881a81354.gif" alt="markups_with_inequal_zoom" data-base62-sha1="jAeMeDsEgYomfFNwkwJx2yawoHG" width="690" height="431" class="animated"></p>

---

## Post #5 by @keri (2022-08-26 17:17 UTC)

<p>I created a draft <a href="https://github.com/Slicer/Slicer/pull/6515" rel="noopener nofollow ugc">pull request</a> but I need help to finilize it.</p>
<p><strong>The idea:</strong><br>
As markups orientation is updated everytime camera is modified, the same way compensate scaling. Introduce <code>vtkSmartPointer&lt;vtkDoubleArray&gt; GlyphScaleArray;</code> and set <code>this-&gt;GlyphMapper-&gt;SetScaleModeToScaleByVectorComponents();</code>.<br>
As orientation is updated in <code>UpdateControlPointGlyphOrientation</code>, I introduce <code>UpdateControlPointGlyphScale</code> function (in <code>vtkSlicerMarkupsWidgetRepresentation3D.cxx</code>).</p>
<p><strong>The problem:</strong><br>
Camera scaling is in global coordinate system.<br>
Markups points always oriented away from the camera: X-to the left, Y-up, Z-away from camera.<br>
To compensate camera scaling I need to correctly project scaling from global coordinate system to markups point coord system (I don’t have enough knowledge what is <code>quaternion</code> and it seems I do that incorrectly).<br>
<img src="https://us1.discourse-cdn.com/flex002/uploads/slicer/original/3X/b/f/bf16260c0d5c66e6c5d4f4e8f0d883d288e5bea0.gif" alt="markups_with_inequal_zoom_problem" data-base62-sha1="rgqEiP5qwrI2GsEl2kc8TTLzAOY" width="600" height="496" class="animated"></p>

---

## Post #6 by @lassoan (2022-08-26 20:49 UTC)

<p>To avoid parallel discussions, let’s talk about this in the pull request.</p>

---
