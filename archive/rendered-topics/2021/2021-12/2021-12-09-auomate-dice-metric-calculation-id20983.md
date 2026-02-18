# Auomate DICE metric calculation

**Topic ID**: 20983
**Date**: 2021-12-09
**URL**: https://discourse.slicer.org/t/auomate-dice-metric-calculation/20983

---

## Post #1 by @Sanghita_Nag (2021-12-09 21:23 UTC)

<p>Is there a way to automate DICE metric calculation for a bunch of studies?</p>

---

## Post #2 by @lassoan (2021-12-10 14:08 UTC)

<p>You can use Segment Comparison to compute Dice and Hausdorff similarity metrics. Note that while Dice metric might be somewhat usable as an optimization metric during segmentation training, it is generally not suitable as an absolute metric for evaluating segmentation, so I would recommend using Hausdorff distance instead. You can find more details in <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4533825/">Taha2015</a>, see for example Table 5, where the only recommended use for Dice is when there are outliers, and it is neutral or not recommended for everything else (in contrast, Hausdorff has only 2 contraindications, one of them is resolved by using 95th percentile instead of maximum of the Hausdorff distance; and the other is “General shape and alignment”, which is usually not the goal of medical segmentation evaluation).</p>
<p>You can use Python scripting to automate anything that you can do using the graphical user interface. Probably the best is to start from examples in the <a href="https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html">script repository</a>. If there is anything specific that you cannot figure out then you can ask here.</p>

---
