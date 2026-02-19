---
topic_id: 887
title: "Apply Reformat Reslicing"
date: 2017-08-17
url: https://discourse.slicer.org/t/887
---

# Apply reformat reslicing

**Topic ID**: 887
**Date**: 2017-08-17
**URL**: https://discourse.slicer.org/t/apply-reformat-reslicing/887

---

## Post #1 by @Prashant_Pandey (2017-08-17 05:02 UTC)

<p>What is the easiest way to resample a volume after applying the desired slice angle using the reformat widget?</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.6/FAQ#How_can_I_use_the_reformat_widget_view_to_resample_my_images.3F" rel="nofollow noopener">This page</a> recommends using the python console - is this still the best way?</p>

---

## Post #2 by @cpinter (2017-08-17 13:39 UTC)

<p>I’m afraid so. The slice node is a special node that does not have a parent transform as transformable nodes that you can use from the UI. It contains a matrix that you need to extract (inverted) into a transform node.</p>
<p>You can just copy-paste the code into the interactor, no changes required. Once you have the transform node you can set it as parent to your volume in the Transforms module or Data module.</p>

---
