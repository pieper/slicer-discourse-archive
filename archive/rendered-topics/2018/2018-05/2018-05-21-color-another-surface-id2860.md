# Color another surface

**Topic ID**: 2860
**Date**: 2018-05-21
**URL**: https://discourse.slicer.org/t/color-another-surface/2860

---

## Post #1 by @Boyce_Doyle (2018-05-21 12:14 UTC)

<p>Operating system:Unbuntu16.04.3<br>
Slicer version:4.8.1-linux-amd64<br>
Expected behavior:I have two 3d-mri images(assume they are a and b) and  a segmentation from volume a.I want to using the gray intensity from b to make a color-show for the segmentation surface(using the vertex gray intensity). Thank you for a solution.<br>
Note:1. Only the surface will show. The body of the segmentation will be discarded.<br>
2. The vertex will be colored in outshow.–My biggest chanllenge.<br>
Actual behavior:</p>

---

## Post #2 by @pieper (2018-05-21 12:35 UTC)

<p>It sounds like you are looking for this:</p>
<p><a href="https://www.slicer.org/wiki/Documentation/4.8/Modules/ProbeVolumeWithModel" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/4.8/Modules/ProbeVolumeWithModel</a></p>

---

## Post #3 by @Boyce_Doyle (2018-05-22 00:33 UTC)

<p>Thank you for your patient solution. A bit more, can we use some features of segmentation or label classes to bypass the model using?<br>
I hope more automatic.</p>

---

## Post #4 by @lassoan (2018-05-22 02:58 UTC)

<p>You can export segmentation to models and run ProbeVolumeWithModel by writing a few lines of Python script.</p>
<p>These examples should help:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_model_nodes_from_segmentation_node" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/ScriptRepository#Export_model_nodes_from_segmentation_node</a><br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Developers/Python_scripting#Running_a_CLI_from_Python</a></p>

---

## Post #5 by @Boyce_Doyle (2018-05-29 03:12 UTC)

<p>Thanks a lot.I solved it.</p>

---
