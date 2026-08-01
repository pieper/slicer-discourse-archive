---
topic_id: 47779
title: "Boundary Cut: Upper airway volume + Lower airway volume does not equal Total airway volume"
date: 2026-07-31
url: https://discourse.slicer.org/t/47779
last_bumped: 2026-07-31T13:37:46.874Z
---

# Boundary Cut: Upper airway volume + Lower airway volume does not equal Total airway volume

**Topic ID**: 47779
**Date**: 2026-07-31
**URL**: https://discourse.slicer.org/t/boundary-cut-upper-airway-volume-lower-airway-volume-does-not-equal-total-airway-volume/47779

---

## Post #1 by @valperrier1999 (2026-07-31 13:37 UTC)

<p>Hello,</p>
<p>I am working on a research project where I need to measure upper, lower and total airway volumes from CBCT scans using 3D Slicer (version 5.10.0).</p>
<p>My workflow is the following:</p>
<ol>
<li>Segment the complete upper airway in ITK-SNAP.</li>
<li>Import the segmentation into 3D Slicer.</li>
<li>Convert the segmentation to a model.</li>
<li>Create three anatomical planes using <strong>Markups Plane</strong>:
<ul>
<li>Superior plane (ENP-Ba)</li>
<li>Intermediate plane (C2)</li>
<li>Inferior plane (C4)</li>
</ul>
</li>
<li>Use <strong>Dynamic Modeler → Boundary Cut</strong> to create:
<ul>
<li>Upper airway (between ENP-Ba and C2)</li>
<li>Lower airway (between C2 and C4)</li>
</ul>
</li>
<li>Measure the volume of each model in <strong>Models → Information</strong>.</li>
</ol>
<p>The anatomical definition is:</p>
<ul>
<li><strong>Upper airway:</strong> between ENP-Ba and C2</li>
<li><strong>Lower airway:</strong> between C2 and C4</li>
<li><strong>Total airway:</strong> between ENP-Ba and C4</li>
</ul>
<p>Therefore, mathematically I would expect:</p>
<p><strong>Total airway volume = Upper airway volume + Lower airway volume</strong></p>
<p>However, I consistently obtain smaller summed volumes.</p>
<p>For example:</p>
<p><strong>Example 1</strong></p>
<ul>
<li>Total airway = <strong>14,084 mm³</strong></li>
<li>Upper airway = <strong>4,856 mm³</strong></li>
<li>Lower airway = <strong>2,789 mm³</strong></li>
<li>Sum = <strong>7,645 mm³</strong></li>
</ul>
<p><strong>Example 2</strong></p>
<ul>
<li>Total airway = <strong>16,622 mm³</strong></li>
<li>Upper airway = <strong>12,894 mm³</strong></li>
<li>Lower airway = <strong>3,039 mm³</strong></li>
<li>Sum = <strong>15,933 mm³</strong></li>
</ul>
<p>I also tried:</p>
<ul>
<li>using Seed Points,</li>
<li>recreating the models,</li>
<li>repeating the cuts,</li>
</ul>
<p>but the discrepancy remains.</p>
<p>My questions are:</p>
<ol>
<li>Is <strong>Boundary Cut</strong> intended to generate complementary sub-volumes?</li>
<li>Should I expect the sum of the upper and lower airway volumes to equal the total airway volume?</li>
<li>If not, what is the recommended workflow in Slicer to partition an airway model between anatomical planes while preserving volume?</li>
</ol>
<p>The goal is to obtain reproducible airway volume measurements for scientific research.</p>
<p>Thank you very much for your help.</p>

---
