---
topic_id: 12193
title: "Shape Analysis Interpretation"
date: 2020-06-24
url: https://discourse.slicer.org/t/12193
---

# Shape analysis interpretation

**Topic ID**: 12193
**Date**: 2020-06-24
**URL**: https://discourse.slicer.org/t/shape-analysis-interpretation/12193

---

## Post #1 by @quentin_devignes (2020-06-24 09:23 UTC)

<p>Dear SlicerSALT team,</p>
<p>Currently using SPHARM-PDM analysis, I wonder what interpretation could be given when there are surface differences between two groups but no volume differences  (assessed with 2 different methods). It seems quite difficult to use the term “atrophy”… Moreover, the displacements are generally both inward and outward. What is the current physiopathological interpretation of this?</p>
<p>Best regards,</p>
<p>Quentin</p>

---

## Post #2 by @styner (2020-07-06 16:12 UTC)

<ul>
<li>
<p>Displacement differences locally can be due to local atrophy or growth, even if there is no global volume difference as small local size/volume differences may not rise to significant global size/volume differences.</p>
</li>
<li>
<p>Alternatively, there may be growth in one section and atrophy in another, thus you have local size differences that even out for a global analysis</p>
</li>
<li>
<p>Finally, you can also a local surface deformation differences without local volumetric differences, that usually then indicates that the surrounding of the structure is changing (e.g. a larger neighboring structure)</p>
</li>
</ul>
<p>The visualizations of shape differences should provide insight to which situation you have, though we are aware that we need better &amp; more intuitive visualizations</p>

---
