---
topic_id: 19004
title: "Exporting The Thickness Bone Table From Bone Thickness Mappi"
date: 2021-07-31
url: https://discourse.slicer.org/t/19004
---

# Exporting the thickness bone table from Bone Thickness Mapping extension

**Topic ID**: 19004
**Date**: 2021-07-31
**URL**: https://discourse.slicer.org/t/exporting-the-thickness-bone-table-from-bone-thickness-mapping-extension/19004

---

## Post #1 by @M.Odaba (2021-07-31 18:39 UTC)

<p>Hi,<br>
I’ve been using Bone Thickness Mapping extension. It’s an amazing tool and the heatmap it creates is super useful. However, I need to have access to thickness values to do more statistical analyses. I assume for each pixel or coordinate, there is a thickness value. I’m new in scripting and still learning Python. From Line 921 to 924 of the provided script (BoneThicknessMapping.py), it says:</p>
<h1><a name="p-63999-thickness-table-1" class="anchor" href="#p-63999-thickness-table-1" aria-label="Heading link"></a>thickness table</h1>
<pre><code>    ix = [int(i) for i in [minmax_thickness[0]*gradient_scale_factor, (minmax_thickness[1])*gradient_scale_factor + 1]]
    thicknessTableNode = BoneThicknessMappingLogic.build_color_table_node('ThicknessColorMap', ix[-1])
    for i in range(ix[0], ix[-1]): calculate_and_set_colour(thicknessTableNode, i, hue=p(i, ix[-1], ix[0]) * 0.278, sat=0.9, val=0.9)
</code></pre>
<p>Does this mean that the data I’m after is called “thicknessTableNode”? If so, would you let me know how I can save the data in a table, text file or other formats?</p>
<p>Thanks,<br>
Mo</p>

---

## Post #2 by @pieper (2021-07-31 19:25 UTC)

<p>I haven’t used the module myself, but the thickness data is stored as a scalar field on a model node, so you can use <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html?highlight=arrayFromModelPointData#slicer.util.arrayFromModelPointData"><code>arrayFromModelPointData</code></a> to get a numpy array.  You can also <code>arrayFromModelPoints</code> to get the corresponding vertex coordinates in RAS space.</p>
<p>You could file an issue on <a href="https://github.com/Auditory-Biophysics-Lab/SlicerBoneThicknessMappingExtension/issues">the extension repository</a> to explain what you are trying to do and get more clues.</p>

---

## Post #3 by @M.Odaba (2021-08-05 00:57 UTC)

<aside class="quote no-group" data-username="pieper" data-post="2" data-topic="19004">
<div class="title">
<div class="quote-controls"></div>
<img loading="lazy" alt="" width="24" height="24" src="https://sea2.discourse-cdn.com/flex020/user_avatar/discourse.slicer.org/pieper/48/8_2.png" class="avatar"> pieper:</div>
<blockquote>
<p>arrayFromModelPoints</p>
</blockquote>
</aside>
<p>Thanks for your reply.<br>
Would you also make an example of how to export the thickness data and vortex coordinates in RAS space in a text or csv file? I need to export this file out of 3D Slicer.</p>
<p>Thanks a lot.</p>

---

## Post #4 by @lassoan (2021-08-07 16:41 UTC)

<p>You get all these values in numpy arrays, so you can easily save them in any format you need. There is nothing Slicer-specific in this, you can just use basic Python functions from packages like numpy, pandas, etc.</p>

---

## Post #5 by @Gonzalo_Rojas_Costa (2024-01-03 00:00 UTC)

<p>Or, is it possible to get thickness values using a ROI, or something similar function? Because, I want to compare the skull thickness in the frontal area, occipital, etc. in two different populations.</p>

---
