---
topic_id: 47371
title: "Export Models as One STL after transformation"
date: 2026-06-17
url: https://discourse.slicer.org/t/47371
last_bumped: 2026-06-17T22:29:09.204Z
---

# Export Models as One STL after transformation

**Topic ID**: 47371
**Date**: 2026-06-17
**URL**: https://discourse.slicer.org/t/export-models-as-one-stl-after-transformation/47371

---

## Post #1 by @jawdoc (2026-06-17 20:01 UTC)

<p>Greetings. I am a facial surgeon and fairly familiar with 3D Slicer. I have a quick question. So my goal is to take a mandible fracture, segment the fracture, and move the segments to their anatomic positions, which allows me to print a 3D model for titanium plate bending prior to surgery. I have segmented the rendering for each fracture segment and converted them to a model so I can transform or move them to reduce the fractures. Now I want to export multiple ~4 segments as a single STL. Is there a way I can combine the segments into a single STL for export?</p>

---

## Post #2 by @pieper (2026-06-17 20:43 UTC)

<p>One option would be to make one new segmentation for each segment so you can move them independently, then harden them, then copy them back into a single segmentation and then merge them all with the logical operators and then export the result as a single stl.</p>

---

## Post #3 by @mikebind (2026-06-17 21:01 UTC)

<p>The “Dynamic Modeler” module’s “Append” tool should work perfectly for this.  Probably you would need to harden your transforms before appending the models into a merged model, but you can test if this is necessary.</p>

---

## Post #4 by @jawdoc (2026-06-17 21:48 UTC)

<p>Steve</p>
<p>I follow everything except how to copy the hardened segmentations into a new segment.<br>
Can you elaborate a little more on that?</p>

---

## Post #5 by @pieper (2026-06-17 22:29 UTC)

<p>In the Segmentations module there’s a Copy/Move segments option.</p>

---
