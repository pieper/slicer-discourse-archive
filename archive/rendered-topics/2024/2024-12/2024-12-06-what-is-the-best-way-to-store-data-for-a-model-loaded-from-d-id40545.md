# What is the best way to store data for a model, loaded from DICOM-RT ion plan file?

**Topic ID**: 40545
**Date**: 2024-12-06
**URL**: https://discourse.slicer.org/t/what-is-the-best-way-to-store-data-for-a-model-loaded-from-dicom-rt-ion-plan-file/40545

---

## Post #1 by @Mik (2024-12-06 12:27 UTC)

<p>Currently i’m working on loading and visualization of ion range compensator,<br>
which data is loaded from <a href="https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.8.8.25.html" rel="noopener nofollow ugc">DICOM-RT ion plan file</a>. The compensator volume data taken from the dicom file are very similar to image parameters: rows, columns, pixel spacing, thickness data.</p>
<p>The compensator is going to be a square block or slab with a milled down center part of the block by a milling machine.</p>
<p>Typical amount of data isn’t very large, for rows=50 and columns=50, thickness data size is 2500 single precision digits.</p>
<p>What is best way to store the data for model visualization?</p>
<ol>
<li>A class derived from vtkMRMLModelNode, and thickness data is stored as std::vector&lt; float &gt;.</li>
<li>A class derived from vtkMRMLModelNode, and thickness data is stored as observed vtkMRMLTableNode.</li>
<li>A loader member function which takes the data and creates a compensator model.</li>
</ol>

---
