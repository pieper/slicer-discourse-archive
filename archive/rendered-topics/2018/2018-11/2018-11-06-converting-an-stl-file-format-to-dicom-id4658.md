---
topic_id: 4658
title: "Converting An Stl File Format To Dicom"
date: 2018-11-06
url: https://discourse.slicer.org/t/4658
---

# Converting an STL file format to DICOM

**Topic ID**: 4658
**Date**: 2018-11-06
**URL**: https://discourse.slicer.org/t/converting-an-stl-file-format-to-dicom/4658

---

## Post #1 by @philipm (2018-11-06 17:54 UTC)

<p>Hello all,</p>
<p>I have an STL file used for 3D printing that originally came from a DICOM structure (RT structure set) that was contoured in Varian Eclipse software for radiation therapy treatment planning purposes. I was hoping to convert this STL back into a DICOM file that I can export back into Eclipse/velocity software from Varian.</p>
<p>The reason I am not using original DICOM is that there was some post processing that was done after conversion to STL so the DICOM is not actually representative of the final design used for 3D printing.</p>
<p>I originally used 3D slicer to convert from the DICOM to STL format so I am hoping there would be some capability to do the reverse.</p>
<p>Any insight would be greatly appreciated.</p>
<p>Kind Regards,</p>
<p>Phil</p>

---

## Post #2 by @cpinter (2018-11-06 18:16 UTC)

<p>Of course:<br>
<a href="https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export" class="onebox" target="_blank">https://www.slicer.org/wiki/Documentation/Nightly/Modules/DICOM#DICOM_export</a></p>

---

## Post #3 by @philipm (2018-11-07 16:02 UTC)

<p>Would this work even if it is not stored in the right hierarchy? I.e. the STL file is loaded into slicer as a “model”. And when I try and create the appropriate hierarchy (i.e. attach it to a fake/new patient and study - once I get to the export stage it does not generate the DICOM when export is selected however there are also no errors messages produced…</p>

---

## Post #4 by @cpinter (2018-11-07 16:09 UTC)

<p>It has to be a segmentation, not a model. You can do conversions in the Segmentations module (import/export section).</p>
<p>Can you add a screenshot about the export window after you clicked export and there were no errors?</p>
<p>Also can you check the log? About / Report an error</p>

---
