# How to programmatically convert some of my segments into models and then get and store information from these models?

**Topic ID**: 17195
**Date**: 2021-04-20
**URL**: https://discourse.slicer.org/t/how-to-programmatically-convert-some-of-my-segments-into-models-and-then-get-and-store-information-from-these-models/17195

---

## Post #1 by @akshay_pillai (2021-04-20 06:02 UTC)

<p>Operating system: Windows 10<br>
Slicer version: 4.11</p>
<p>I want to (i)programmatically convert some of my segments into models and then (ii)get and store information from these models. Information like surface area, volume, etc. How can I do this programmatically? I would like to convert all the segments into models and store this information as an excel sheet or as data or graph. Is there any way to do this?</p>

---

## Post #2 by @cpinter (2021-04-20 11:09 UTC)

<p>For the first question see solution in the script repository:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_model_nodes_from_segmentation_node" class="onebox" target="_blank" rel="noopener">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_model_nodes_from_segmentation_node</a></p>
<p>However, for your second question there is no need for such conversion, because the Segment Statistics module can do it for you from the surface models representation within the segmentations (see explanation of the representations <a href="https://slicer.readthedocs.io/en/latest/user_guide/image_segmentation.html">here</a>). To programmatically drive a module you need to see <a href="https://github.com/Slicer/Slicer/blob/master/Modules/Scripted/SegmentStatistics/SegmentStatistics.py">its source code</a>, then simply set the proper inputs and call the necessary functions.</p>

---

## Post #3 by @akshay_pillai (2021-04-27 15:29 UTC)

<p>Thanks , Segment Statistics was perfect.</p>

---
