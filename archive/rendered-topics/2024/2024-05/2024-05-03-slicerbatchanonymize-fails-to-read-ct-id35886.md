# SlicerBatchAnonymize fails to read CT

**Topic ID**: 35886
**Date**: 2024-05-03
**URL**: https://discourse.slicer.org/t/slicerbatchanonymize-fails-to-read-ct/35886

---

## Post #1 by @Matteboo (2024-05-03 08:46 UTC)

<p>Hello,<br>
I’m anonymizing several CT using the <em>SlicerBatchAnonymize</em> extension. It works well except for one CT.<br>
I can load the CT manually using the DICOM data module without any issue.</p>
<p>I get the following errors :</p>
<pre><code class="lang-auto">[VTK] Size mismatch! The size of  C:/path/000000.dcm is [512, 512, 563] and does not match the required size [512, 512, 1] from file C:/path/000000.dcm
[VTK] Algorithm vtkITKArchetypeImageSeriesScalarReader (000002811EFFB0C0) returned failure for request: vtkInformation (000002810FAEC4C0)
[VTK]   Debug: Off
[VTK]   Modified Time: 242836
[VTK]   Reference Count: 1
[VTK]   Registered Events: (none)
[VTK]   Request: REQUEST_DATA
[VTK]   FORWARD_DIRECTION: 0
[VTK]   ALGORITHM_AFTER_FORWARD: 1
[VTK]   FROM_OUTPUT_PORT: 0
[Python] Could not read scalar volume using GDCM approach.  Error is: FileFormatError
[VTK] Size mismatch! The size of  C:/path/000000.dcm is [512, 512, 563] and does not match the required size [512, 512, 1] from file C:/path/000000.dcm
[VTK] Algorithm vtkITKArchetypeImageSeriesScalarReader (000002811EFF9CC0) returned failure for request: vtkInformation (000002817EB5AAD0)
[VTK]   Debug: Off
[VTK]   Modified Time: 243083
[VTK]   Reference Count: 1
[VTK]   Registered Events: (none)
[VTK]   Request: REQUEST_DATA
[VTK]   FORWARD_DIRECTION: 0
[VTK]   ALGORITHM_AFTER_FORWARD: 1
[VTK]   FROM_OUTPUT_PORT: 0
[Python] Could not read scalar volume using DCMTK approach.  Error is: FileFormatError
[Python] Error reading/writing file: C:\path
[Python] 'NoneType' object has no attribute 'GetImageData'
</code></pre>
<p>I don’t know if it’s relevant but when I load the CT throught the DICOM database, it get the mention <em>- imageType ORIGINAL-PRIMARY-AXIAL</em></p>

---
