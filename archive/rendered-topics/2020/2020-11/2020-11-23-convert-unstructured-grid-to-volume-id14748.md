---
topic_id: 14748
title: "Convert Unstructured Grid To Volume"
date: 2020-11-23
url: https://discourse.slicer.org/t/14748
---

# Convert Unstructured Grid to Volume

**Topic ID**: 14748
**Date**: 2020-11-23
**URL**: https://discourse.slicer.org/t/convert-unstructured-grid-to-volume/14748

---

## Post #1 by @Asees_Kaur (2020-11-23 20:51 UTC)

<p>Hi <a class="mention" href="/u/lassoan">@lassoan</a>, I am currently trying to convert my unstructured grid to a volume. So I can import it into Slicer and export it as DICOM images. The process I’m following is:</p>
<ol>
<li>Create my input file:</li>
</ol>
<ul>
<li>Convert UnstructuredGrid to Polydata with GeometryFilter</li>
<li>Convert PolyData to empty ImageData with PolyDataToImageStencil and ImageStencil</li>
<li>write input file</li>
</ul>
<ol start="2">
<li>Use the vtkProbeFilter</li>
</ol>
<ul>
<li>read input file</li>
<li>read original unstructured grid as source file</li>
<li>write to file.</li>
</ul>
<p>You have previously provided an example of how to do this, <a href="https://github.com/lassoan/SlicerNotebooks/blob/master/UnstructuredGridToVolume.ipynb" rel="noopener nofollow ugc">https://github.com/lassoan/SlicerNotebooks/blob/master/UnstructuredGridToVolume.ipynb</a>, however this is now unavailable.</p>
<p>I wanted to know if my method was correct, and if you could repost your example ?</p>

---
