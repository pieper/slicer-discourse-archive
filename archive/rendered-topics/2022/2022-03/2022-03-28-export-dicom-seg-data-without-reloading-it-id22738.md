# Export DICOM-SEG data without reloading it

**Topic ID**: 22738
**Date**: 2022-03-28
**URL**: https://discourse.slicer.org/t/export-dicom-seg-data-without-reloading-it/22738

---

## Post #1 by @Johannes (2022-03-28 21:30 UTC)

<p><strong>Hi 3D Slicer forum,</strong></p>
<p>Unfortunately, as described in this <a href="https://discourse.slicer.org/t/export-dicom-seg-data/21636/2">post</a>, some DICOM files do not have correctly saved data on origin, spacing and axis directions.</p>
<p>Therefore, no DICOM-SEG object can be created.</p>
<p>As described in the post above, the error can be avoided by importing the DICOM object and then exporting it again. Then the missing data is added.</p>
<p>I have found that unfortunately almost all the sequences in my data pool do not correspond to the DICOM standard.</p>
<p><strong>I would like to know whether there is another option without reloading the data?</strong></p>
<p>The slicer console also shows an additional indication when trying to export the entire study. It works for individual sequences.</p>
<blockquote>
<p>TypeError: <strong>init</strong>() missing 1 required positional argument: ‘referenceFile’</p>
</blockquote>

---
