---
topic_id: 34852
title: "Generating Thickness Map"
date: 2024-03-12
url: https://discourse.slicer.org/t/34852
---

# Generating thickness map

**Topic ID**: 34852
**Date**: 2024-03-12
**URL**: https://discourse.slicer.org/t/generating-thickness-map/34852

---

## Post #1 by @Pol (2024-03-12 22:06 UTC)

<p>I used the following method to generate a thickness ma of the left ventricular myocardium:</p>
<ul>
<li>Compute medial surface using <strong>Simple Filters module - BinaryThinningImageFilter</strong>.</li>
<li>Compute distance map using <strong>Simple Filters module - DanielssonDistanceMapImageFilter</strong>. Input is binary: Yes; Use image spacing: Yes.</li>
<li>Copy distance values from the distance map to model node using <strong>Probe volume with model</strong> module.</li>
</ul>
<p>In the last step (probe volume with model) there is an error message asking for the input model. What is the correct input model?</p>
<p>Thank you!</p>

---

## Post #2 by @Jennifer_Ortiz (2024-03-13 18:09 UTC)

<p>Hey! I have also been making thickness maps and I found that for <strong>Probe Volume with Model in modules:</strong></p>
<p>the Input Volume: DanielsonDistanceMapImageFilter output<br>
the Input Model: Original model stl</p>
<p>This works for me and I hope that this helps!</p>

---
