# Can I transfer the RAS coordinate system back to LPS

**Topic ID**: 32394
**Date**: 2023-10-24
**URL**: https://discourse.slicer.org/t/can-i-transfer-the-ras-coordinate-system-back-to-lps/32394

---

## Post #1 by @Benjamin-JZ (2023-10-24 07:21 UTC)

<p>I know that patient data has been converted to values in the RAS coordinate system after being imported into 3Dslicer. For example, I have a DICOM metadata with Origin [-202, -33,100]. But the Origin obtained from the vtkMRMLVolumeNode and vtkMRMLSegmentationNode types is [202,33,100]. I would like to know if there is a method to convert or obtain the original Origin: [-202, -33,100].<br>
Thanks :–)</p>

---

## Post #2 by @cpinter (2023-10-24 12:21 UTC)

<p>Can you please describe why you need this conversion <em>within</em> Slicer? Normally all operations in Slicer happen in RAS, and then one can export the results in LPS. Would that work for you?</p>

---

## Post #3 by @lassoan (2023-10-24 13:07 UTC)

<p>I agree that it should not be necessary to convert the internal coordinate values when you are in Slicer, as all coordinate values are stored as RAS.</p>
<p>You can of course <em>display</em> coordinate values in any coordinate system; or use positive values and add the direction code (L/R, A/P, I/S) - as we do it in the Data Probe (in the lower-left corner). Conversion is trivial: invert the sign of the first two coordinates.</p>

---

## Post #4 by @Benjamin-JZ (2023-10-24 13:21 UTC)

<p>Thank you for your answer. I know that doing so in 3Dslicer looks a bit like taking off your pants and farting. It’s unnecessary. It’s a long story. The representation I encountered earlier can only store one context, which means that no matter how many segments I annotate on a SegmentationNode. These segments have their own attributes. But in the end, these attributes will only correspond to a large annotation area in the end. Similar to the feeling of many to one. So I made other attempts. In fact, after observing, I also found that the conversion between LPS and RAS only requires adjusting the xy axis.</p>
<p>That’s it. Thank you again</p>

---
