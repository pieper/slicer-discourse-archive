---
topic_id: 41886
title: "Way To Acess Eagag"
date: 2025-02-26
url: https://discourse.slicer.org/t/41886
---

# Way to acess eagag

**Topic ID**: 41886
**Date**: 2025-02-26
**URL**: https://discourse.slicer.org/t/way-to-acess-eagag/41886

---

## Post #1 by @Djonathan_Souza (2025-02-26 18:10 UTC)

<p>Hello, I need a way to access the segmentation node, as I need to save the segmentations.</p>
<p>However, I am using pythonSlicer to run the application and I cannot use MRML according to the documentation at <a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#module-slicer" class="inline-onebox" rel="noopener nofollow ugc">slicer — 3D Slicer documentation</a>.</p>
<p>Here is the code:</p>
<pre data-code-wrap="python"><code class="lang-python">segmentation_nodes = slicer.mrmlScene.GetNodesByClass("vtkMRMLSegmentationNode")
 

# I am receiving the following error when I call the function to save a segmentation:
{
  "error": "Failed to process the segmentations: module 'slicer' has no attribute 'mrmlScene'"
}

</code></pre>
<p>I am looking for a way to do this without using <code>mrml</code>. Thank you in advance!</p>

---

## Post #2 by @pieper (2025-02-26 18:46 UTC)

<p><a href="https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#module-slicer:~:text=Warning-,These%20attributes%20are%20only%20set%20in%20the%20Python%20environment%20embedded%20in%20the%20Slicer%20main%20application.,-Additionally%20for%20all" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/developer_guide/slicer.html#module-slicer:~:text=Warning-,These%20attributes%20are%20only%20set%20in%20the%20Python%20environment%20embedded%20in%20the%20Slicer%20main%20application.,-Additionally%20for%20all</a></p>

---
