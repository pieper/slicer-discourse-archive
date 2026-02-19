---
topic_id: 8401
title: "How To Save 3D Slicer Model Into Step File"
date: 2019-09-12
url: https://discourse.slicer.org/t/8401
---

# How to save 3D slicer model into .step file

**Topic ID**: 8401
**Date**: 2019-09-12
**URL**: https://discourse.slicer.org/t/how-to-save-3d-slicer-model-into-step-file/8401

---

## Post #1 by @rahul (2019-09-12 12:58 UTC)

<p>Operating system:<br>
Slicer version:<br>
Expected behavior:<br>
Actual behavior:</p>

---

## Post #2 by @lassoan (2019-09-12 13:07 UTC)

<p>Slicer can read/write many file formats - see complete list <a href="https://www.slicer.org/wiki/Documentation/Nightly/SlicerApplication/SupportedDataFormat" rel="nofollow noopener">here</a>. You’ll have to use mesh converter to create a .step file from any of the supported file formats.</p>
<p>If you want this feature to be directly available in Slicer then you can implement VTK mesh to .step conversion using some library (and if you want the file format to be available in the Save data dialog then also add a custom node storage node).</p>

---

## Post #3 by @balakonvict (2022-09-27 10:55 UTC)

<p>can you elaborate in detail sir?</p>

---

## Post #4 by @pieper (2022-09-27 12:41 UTC)

<p>The updated link to the supported file formats is here:</p>
<p><a href="https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#models" class="onebox" target="_blank" rel="noopener">https://slicer.readthedocs.io/en/latest/user_guide/data_loading_and_saving.html#models</a></p>

---

## Post #5 by @balakonvict (2022-09-29 11:15 UTC)

<p>im getting stl as file format output and in need to import into solidwords for designing brackets and after that i will be importing it into ansys and now imhaving stl file as the final output</p>

---
