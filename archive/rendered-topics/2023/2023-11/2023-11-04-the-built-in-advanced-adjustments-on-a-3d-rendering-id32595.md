---
topic_id: 32595
title: "The Built In Advanced Adjustments On A 3D Rendering"
date: 2023-11-04
url: https://discourse.slicer.org/t/32595
---

# The built-in "Advanced" adjustments on a 3D rendering

**Topic ID**: 32595
**Date**: 2023-11-04
**URL**: https://discourse.slicer.org/t/the-built-in-advanced-adjustments-on-a-3d-rendering/32595

---

## Post #1 by @MikeN (2023-11-04 05:10 UTC)

<p>Hi guys,</p>
<p>I’m new to 3D Slicer. I rendered a CT scan in 3D, using the various preset displays. I wanted to adjust the rendering, and I’m trying to understand the various adjustments.</p>
<p>On the panel to the left of the visualization are various adjustments, such as the sliders and movable discs below the “Advanced”/“Volume properties”/“Scalar Opacity Mapping” headings. There are more of course.</p>
<p>Are these adjustments sufficient to go from any given preset display to any other preset display?</p>
<p>This would give me the confidence to dive into the adjustments. Otherwise I suppose I might need to go down to the API level and learn how to start from scratch, which would be a huge undertaking.</p>
<p>Best, Mike</p>
<p>Slicer version: 5.4.0</p>

---

## Post #2 by @pieper (2023-11-05 15:18 UTC)

<aside class="quote no-group" data-username="MikeN" data-post="1" data-topic="32595">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://avatars.discourse-cdn.com/v4/letter/m/76d3ee/48.png" class="avatar"> MikeN:</div>
<blockquote>
<p>Are these adjustments sufficient to go from any given preset display to any other preset display?</p>
</blockquote>
</aside>
<p>Yes, but there are a lot of variables so it would be hard to manually recreate one preset from another.  For example they may have different numbers of control points in the color or opacity mappings.</p>

---

## Post #3 by @MikeN (2023-11-09 23:53 UTC)

<p>Thanks for your help.</p>
<p>I have a followup question about creating a custom preset for volume rendering. Is there a way of building (from scratch) and saving a new preset via the buttons, etc., in the panel? Or do you have to make a file, say “MyPresets.mrml”, that contains the values (opacity, etc.).?</p>

---

## Post #4 by @muratmaga (2023-11-10 02:38 UTC)

<p>No, currently there is no easy way to export your custom volume property and register it as a preset.  MyPresets.mrml requires Icons etc to be defined.</p>
<p>You can alternatively save your volume property (.vp file) and load it each time into your scene. it will immediately be available to you under the Volume Properties dropdown selector (not in presets).</p>

---
