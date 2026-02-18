# Converters -> Create a DICOM Series

**Topic ID**: 6708
**Date**: 2019-05-06
**URL**: https://discourse.slicer.org/t/converters-create-a-dicom-series/6708

---

## Post #1 by @gcsharp (2019-05-06 19:48 UTC)

<p>Is “Converters” -&gt; “Create a DICOM Series” supported?<br>
Is there any difference between using that feature compared with “Data” -&gt; “Export to DICOM”?<br>
Do we want/need both methods?</p>

---

## Post #2 by @lassoan (2019-05-06 20:02 UTC)

<p>DICOM export infrastructure (that you can launch from Data module) uses various modules to export various types of DICOM IODs. 3D volumes (CT, MRI, …) are exported using “Create DICOM Series” module.</p>

---
